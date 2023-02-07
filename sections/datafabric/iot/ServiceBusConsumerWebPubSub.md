# Service Bus consumer using Azure Functions and WebPubSub

This tutorial will guide you through the process of creating a single page application (SPA) that connects to an Azure ServiceBus queue and consumes messages in real-time via a WebSocket connection. 
The connection from the browser to the ServiceBus queue is established via a [WebPubSub](https://azure.microsoft.com/en-us/products/web-pubsub) service. WebPubSub is a recently released managed Azure service that enabled building real-time applications using a publish-subscribe architecture.

## 1. Create WebPubSub service
### From the Portal:
Create a WebPubSub service in Azure portal. You can find the quickstart [here](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/howto-develop-create-instance).

### From the CLI:
You can also create a WebPubSub service from the Azure CLI. We'll just list the commands here, but you can find the full instructions in this [Azure docs page](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/quickstart-cli-create).
Create a Web PubSub instance with the following command:
```bash
az webpubsub create --name "<your-unique-name>" --resource-group "myResourceGroup" --location "WestEurope" --sku Free_F1
```
## 2. Create the Azure functions
With the WebPubSub service created, we can now create the Azure functions. We'll use the [Azure Functions Core Tools](https://github.com/Azure/azure-functions-core-tools#installing) to create the functions, so make sure you have this installed.

### 2.1 Initialize the project
Create a new directory for the project and initialize it with the following command:
```bash
func init --worker-runtime javascript
```
Update `host.json`'s extensionBundle to version `3.3.0` or later to get Web PubSub support.
    
```json
{
    "version": "2.0",
    "extensionBundle": {
        "id": "Microsoft.Azure.Functions.ExtensionBundle",
        "version": "[3.3.0, 4.0.0)"
    }
}
```
There are 3 functions in the project, `notify`, `negotiate`, and `web_index`:
1. `notify` receive messages from the ServiceBus queue and forward them to the WebPubSub service (via an output binding)
2. `negotiate` is used to get service connection url with access token
3. `web_index` is used to render the web page index (as a single page application)

### 2.2 Create the `notify` function
Create the `notify` function with the following command:

```bash
func new -n notify -t "Azure Service Bus Queue trigger"
```
Next we'll configure the function to connect to our ServiceBus queue. 
Open `local.settings.json` and add a `ServiceBusConnectionString` property to the `Values` section, as shown below (replace the `<your-servicebus-connection-string>` string with your own ServiceBus connection string for the Veracity IoT platform):

```json
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "node",
    "AzureWebJobsStorage": "",
    "ServiceBusConnectionString": "<your-servicebus-connection-string>"
  }
}
```
Then open `notify/function.json` and set the `connection` property to the name of the ServiceBus connection string you created earlier. Also make sure to set the `queueName` property to the name of your own queue. 
```json
{
  "bindings": [
    {
      "type": "serviceBusTrigger",
      "name": "message",
      "direction": "in",
      "connection": "ServiceBusConnectionString",
      "queueName": "<your-servicebus-queue-name>"
    }
  ]
}
```
Finally, in `notify/index.js` make sure second parameter matches the value of the `name` property in `function.json`:

```javascript
module.exports = function(context, message) {
  context.log('ServiceBus queue trigger function processed message', message);
};
```
You can test the function locally with:
```bash
npm start
```
If all is well, you will see a message like this in the terminal:
```bash
Azure Functions Core Tools
Core Tools Version:       4.0.4915 Commit hash: N/A  (64-bit)
Function Runtime Version: 4.14.0.19631

[2022-12-20T08:51:15.558Z] Worker process started and initialized.

Functions:
	notify: serviceBusTrigger
For detailed output, run func with --verbose flag.
[2022-12-20T08:51:20.253Z] Host lock lease acquired by instance ID '00000000000000000000000034C39F08'.
```
You can also test the function by sending a message to the topic for which this queue is subscribe. You can find more info on publishing messages to the Veracity IoT Platform on our [developer documentation](https://developer.veracity.com/docs/section/datafabric/overview).
### 2.3 Create the `negotiate` function
The `negoiate` function is used to create a WebSocket connection to the WebPubSub service. It uses a `httpTrigger` binding to create a WebSocket endpoint that can be called from the client (in this case, a browser). 
At the moment of writing this guide, the [Azure Function Core Tools v4.0](https://github.com/Azure/azure-functions-core-tools) library doesn't yet contain a template for the WebPubSub service. So we'll use the `HTTPTrigger` instead. 
Create the `negotiate` function with the following command:

```bash
func new -n notify
```
Choose `HTTPTrigger` as the template (or choose something like "WebPubSub negotiate HTTP trigger" if you see it in the list).

Then update the `negotiate/function.json` file to add the `webPubSub` binding. 

```json
{
  "bindings": [
    {
      "type": "httpTrigger",
      "direction": "in",
      "name": "req",
      "authLevel": "anonymous"
    },
    {
      "type": "http",
      "direction": "out",
      "name": "res"
    },
    {
      "type": "webPubSubConnection",
      "name": "connection",
      "direction": "in",
      "hub": "<your-webpubsub-hub-name>"
    }
  ]
}
```
Also edit the `negotiate/index.js` file to add the following code:

```js
module.exports = function (context, req, connection) {
  context.res = { body: connection };
  context.done();
};
```
We also need to update the previous `notify` function to add the `webPubSub` output binding.
Edit `notify/function.json` and add the `webPubSub` binding, like so (use the same `hub` name as in the `negotiate` function):
```json
{
  "bindings": [
    {
      "type": "serviceBusTrigger",
      "name": "message",
      "direction": "in",
      "connection": "ServiceBusConnectionString",
      "queueName": "<your-servicebus-queue-name>"
    },
    {
      "type": "webPubSub",
      "name": "actions",
      "hub": "<your-webpubsub-hub-name>",
      "direction": "out"
    }
  ]
}
```
Now, update the `notify/index.js` file to forward the message to the WebPubSub service:
```js
module.exports = function (context, message) {
  context.log('JavaScript ServiceBus queue trigger function processed message', message);

  context.bindings.actions = {
    actionName: 'sendToAll',
    data: JSON.stringify(message),
    dataType: "text"
  }
  context.done();
};
```
Finally, we need to update the `local.settings.json` file to add the WebPubSub connection string. You can retrieve this from navigating to your WebPubSub service in the Azure portal, and then clicking on the "Keys" tab. 
Copy the "Connection string" and add it in your `local.settings.json`, as below:
```json
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "node",
    "AzureWebJobsStorage": "",
    "ServiceBusConnectionString": "<your-servicebus-connection-string>",
    "WebPubSubConnectionString": "<your-webpubsub-connection-string>"
  }
}
```
### 2.4 Add the web_index function
Before we can test the function, we need to add a simple web page that will connect to the WebPubSub service. This is done by adding a new function called `web_index` that will serve the `index.html` file.
In this function, we'll use the `httpTrigger` binding to create a HTTP endpoint that will serve the `index.html` file. From the UI we'll connect to the WebPubSub service using a WebSocket connection, which is exposed automatically in the `negotiate` function we created earlier.
Create the `web_index` function with the following command:
```bash
func new -n web_index -t "HTTP trigger
```
Add the `index.html` and `index.js` files located in the `web_index` folder. The UI was built on top of the Bootstrap framework and includes a basic chart, table, and a map, all of which are updated in real-time as new data is received from the Veracity IoT EventBroker.
## 3. Run the example end-to-end
### 3.1 Update the notify function
Before we can run the example end-to-end, we need to update the `notify` function send the data according to the Veracity IoT Message. By default, the `notify` function sends only the message body, but we will need to add a few properties as well, such as `eventType` and `topic`.

Update the `notify/index.js` file to match the following code:

```js
module.exports = function(context, message) {
  context.log('JavaScript ServiceBus queue trigger function processed message', message);

  // properties are available on the bindingData object
  const {applicationProperties} = context.bindingData;

  context.bindings.actions = {
    actionName: 'sendToAll',
    data: JSON.stringify({
      value: message,
      properties: {
        topic: applicationProperties.topic,
        eventType: applicationProperties.eventType
      }
    }),
    dataType: 'text'
  }
  context.done();
};
```
### 3.2 Run the functions locally
Now that we have the Azure Functions set up, we can run them locally and test the example end-to-end.
Start the Azure Functions runtime by running the following command:
```bash
npm start
```
You should see the following output:

```bash
Azure Functions Core Tools
Core Tools Version:       4.0.4915 Commit hash: N/A  (64-bit)
Function Runtime Version: 4.14.0.19631

[2022-12-21T10:44:58.549Z] Worker process started and initialized.
Functions:

	negociate:  http://localhost:7071/api/negociate

	web_index: [GET,POST] http://localhost:7071/api/web_index

	notify: serviceBusTrigger
```
Open the `http://localhost:7071/api/web_index` URL in your browser and inspect the console. You should see the following lines:
```bash 
Connecting to http://localhost:7071/api/negociate...
Connected to WebPubSub service
```

This means that the `web_index` function was able to connect to the `negotiate` function and retrieve the WebPubSub connection string.
### 3.3 Publish messages to the Veracity IoT Platform
The `web_index` function is now ready to receive messages from the Veracity IoT EventBroker. To do so, we need to publish some messages to the Veracity IoT Platform. The UI will display the messages in real-time, and you should see the chart, table, and map being updated.
The UI expects messages to be received in the following format:

```json
{
  "value": "{\"message\": \"body\"}",
  "properties": {
    "topic": "topic name",
    "eventType": "event type"
  }
}
```

Here's an example of a message that can be published to the Veracity IoT Platform:

```json
{"Payload":{"Temperature":7.845451070281867,"Pressure":-0.4986194983223189,"Humidity":25.0,"Latitude":58.49814652167727,"Longitude":10.078944402815145,"TimeStampUtc":"2022-12-21T10:30:46.435457Z"},"TenantId":"0cbb4396-ef53-4ff7-a1df-ff4c50dda75e","AssetId":"223344","AssetIdIssuer":"imo","Topic":"MC/Engines/2","EventType":"EquipmentStatus","TimeStampUtc":"2022-12-21T10:30:46.435457Z"}
```
Refer to the Developer documentation for more information on how to publish messages to the Veracity IoT Platform.

## 4. Deploy the example to Azure
The last step is to deploy the Azure Functions to Azure. This can be done by [creating a new function app service](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-function-app-portal) in the Azure portal.
Once the function app service is created, run the following command and replace the `<function-app-name>` with the name of your function app service:

```bash
func azure functionapp publish <your-function-app-name>
```



