---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Service bus consumer using Azure functions
Azure Service Bus is a fully managed enterprise message broker which is used to build applications and services that use an event-driven architecture. It provides message queues and publish-subscribe topics with at-least-once delivery guarantees. It also supports sessions, transactions, and dead-letter queues. 
This guide will walk you through the process of creating a new Azure Function that uses a Service Bus trigger to consume messages in real-time.

## Pre-requisites
To get started, the following are needed to be installed on your machine:
- [dotnet 6.0](https://dotnet.microsoft.com/download/dotnet/6.0)
- [Node.js](https://nodejs.org/en/download/)
- An [Azure subscription](https://azure.microsoft.com/free/) is required to deploy the Azure Function. The rest of the tools we'll install them as we go along. Some familiarity with Azure Functions and Service Bus is beneficial but not essential.
 
## Code example on GitHub
[Link missing]()
## Create an Azure Function with Service Bus trigger  
Azure Functions integrates with Azure Service Bus via triggers and bindings. For this article, we'll be using the Service Bus trigger to consume messages from a queue. If you're looking for a guide on how to use the output bindings, please refer to the [Azure Service Bus output binding for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-output) article on the Azure docs.
An Azure Function can be written in several programming languages using official SDK: C#, Java, JavaScript, and Python. For this article, we'll be using C# in an isolated worker process. You can read more about the benefits of using an isolated process on this [article](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide).  

The easiest way to create a new Azure Function is to use the [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local) (v4).
 
If you're using VS code, you can also install these extensions to make it easier to create and manage Azure Functions:

- [Azure Functions extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)

- [Azure Account extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azure-account)

### Step 0. Create a new file directory

Create a new directory for your project and navigate to it using the terminal:
```js
mkdir servicebus-consumer-example
cd servicebus-consumer-example
```
Inside the directory, create 2 new subfolders to hold the source code and the tests: 
```js
mkdir src test
``` 

### Step 1. Install the Azure Functions Core Tools  

The functions core tools is a Node.js library and can be installed using the `npm` tool that's distributed with Node.js.  
The `-g` flag installs the library globally so that it can be used from any directory.

```js
npm install -g azure-functions-core-tools@4
```
For alternative ways to install the Azure Functions Core Tools, please refer to the [installation guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local) on the Azure docs.

### Step 2. Create a new Azure Function project
Navigate to the `src` folder and run the `func init` command to create a new Azure Function project:
 ```js
cd src
func init
```
 
The `func init` command will prompt you to select a language and a worker runtime. For this article, we'll be using C# and the isolated worker runtime.
 
Select option `2.` at the below prompt:

```js
Select a number for worker runtime:
1. dotnet
2. dotnet (isolated process)
3. node
4. python
5. powershell
6. custom
```
Then select option `1.`:

```js
Select a number for language:
1. c#-isolated
2. f#-isolated
```
 Run the `ls` command to verify that the project was created successfully:

```
ls
``` 
The output should look like this:
```js
Program.cs Properties host.json local.settings.json src.csproj
```
### Step 3. Create a new Azure Function with Service Bus trigger

Run the `func new` command to create a new Azure Function with a Service Bus trigger:
```js
func new
``` 
The `func new` command will prompt you to select a template. Select option `6. ServiceBusQueueTrigger` at the below prompt:
```js
Select a number for template:
1. QueueTrigger
2. HttpTrigger
3. BlobTrigger
4. TimerTrigger
5. EventHubTrigger
6. ServiceBusQueueTrigger
7. ServiceBusTopicTrigger
8. EventGridTrigger
9. CosmosDBTrigger
``` 
Then enter a function name:
```js
Choose option: 6
Function name: ServiceBusConsumer
```
If all is well, you should see something like the following:
```js
The function "ServiceBusConsumer" was created successfully from the "ServiceBusQueueTrigger" template.
```
### Step 4. Run the Azure Function locally
Before we are able to run the function locally, we need to configure it. To be able to consume events using the Veracity IoT Platform, the following information is needed:
- ServiceBus Connection string
- ServiceBus queue name
 
#### Step 4.1
Edit the `local.settings.json` file and add the following configuration values: 
```json
{
"IsEncrypted": false,
"Values": {
"AzureWebJobsStorage": "UseDevelopmentStorage=true",
"FUNCTIONS_WORKER_RUNTIME": "dotnet-isolated",
"ServiceBusConnectionString": "<servicebus-connection-string>",
"ServiceBusQueueName": "<servicebus-queue-name>"
}
}
```
 Replace the `<servicebus-connection-string>` and `<servicebus-queue-name>` placeholders with the actual values.  

#### Step 4.2
We also need to edit the `ServiceBusConsumer.cs` file to edit the `ServiceBusTrigger` attribute:

 ```cs
[Function("ServiceBusConsumer")]
public  void Run(
[ServiceBusTrigger("%ServiceBusQueueName%", Connection = "ServiceBusConnectionString")]
string eventMsg,FunctionContext context)
{
_logger.LogInformation($"C# ServiceBus queue trigger function processed message: {eventMsg}");
}
```
 
Run the `func start` command to start the Azure Function locally:
 
```cs
func start
```
If all is well, you should see something like the following:
```cs
Functions:
ServiceBusConsumer: serviceBusTrigger  
For detailed output, run func with --verbose flag.
[2022-11-30T12:24:13.873Z] Worker process started and initialized.
```
Now you are ready to consume events from the Veracity IoT Platform using Azure Service Bus.
 
### Step 5. Consume events in the Azure Function
In order to test the ServiceBus consumer function, we'll be sending some test events to the Veracity IoT Platform. See [ingest event](EventIngest.md)

Now that we have published an event to the IoT Hub, it should be routed to the Service Bus queue and ready to be consumed by the Azure Function.  

We can test this by runing the `func start` command again:
```json
func start
``` 
If all is well, you should see something like the following:
```cs
Functions: 
ServiceBusConsumer: serviceBusTrigger 
For detailed output, run func with --verbose flag.
[2022-11-30T16:17:07.781Z] Worker process started and initialized.
[2022-11-30T16:17:08.107Z] Executing 'Functions.ServiceBusConsumer' (Reason='(null)', Id=492ef31a-769a-409a-9980-2baba8ab9451)

[2022-11-30T16:17:08.107Z] Trigger Details: MessageId: a40fa9c6e4c64862860ea035176a49ab, SequenceNumber: 200, DeliveryCount: 1, EnqueuedTimeUtc: 2022-11-30T16:17:01.1810000Z, LockedUntilUtc: 2022-11-30T16:17:38.0400000Z, SessionId: (null)

[2022-11-30T16:17:08.170Z] C# ServiceBus queue trigger function processed message: {

[2022-11-30T16:17:08.170Z] "TestPayloadItem": "test-value-1",
[2022-11-30T16:17:08.170Z] "TestPayloadItem2": "test-value-2"
[2022-11-30T16:17:08.170Z] }
[2022-11-30T16:17:08.179Z] Executed 'Functions.ServiceBusConsumer' (Succeeded, Id=492ef31a-769a-409a-9980-2baba8ab9451, Duration=87ms)

```
As you can see, the Azure Function has consumed the event and printed the payload to the console.
 

#### Read the message properties in the Azure Function
The Azure Function has consumed the event and printed the payload to the console. However, you may need to read the message properties as well, such as the `AssetId`, `Topic`, and `EventType`.

In the current implementation of Azure Functions (v4) for dotnet isolated process, the message properties are not directly available in the function arguments. Instead, we have to read them via the function `context` object, like so:  
```cs
// ServiceBusConsumer.cs 
using System.Text.Json;
using System.Text.Json.Serialization;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging; 
namespace src; 

public  class ServiceBusConsumer
{
private  readonly ILogger _logger;  
public ServiceBusConsumer(ILoggerFactory loggerFactory)
{
_logger = loggerFactory.CreateLogger<ServiceBusConsumer>();
}
 
[Function("ServiceBusConsumer")]
public  void Run(
[ServiceBusTrigger("%ServiceBusQueueName%", Connection = "ServiceBusConnectionString")]
string eventMsg,FunctionContext context)
{
_logger.LogInformation($"C# ServiceBus queue trigger function processed message: {eventMsg}");
IReadOnlyDictionary<string, object?> bindingData = context.BindingContext.BindingData;
var userProperties = bindingData["UserProperties"]?.ToString();
  
_logger.LogInformation($"userProperties: {userProperties}");
if (userProperties == null)
{
return;
}
var message = JsonSerializer.Deserialize<MessageProperties>(userProperties);
_logger.LogInformation($"Message topic: {message?.Topic}");
_logger.LogInformation($"Event type: {message?.EventType}");
_logger.LogInformation($"AssetId: {message?.AssetId}");
}  

public  class MessageProperties
{
[JsonPropertyName("eventType")]
public  string? EventType { get; set; }
[JsonPropertyName("topic")]
public  string? Topic { get; set; }
[JsonPropertyName("assetId")]
public  string? AssetId { get; set; }
}
}
```
### Step 6. Deploy the Azure Function to Azure

  Now that we have a working Azure Function, we can deploy it to Azure. First, you'll need to create a new function app service in Azure if you don't have one already. You can do this in a few ways:

- in the [Azure portal](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-function-app-portal)

- from the [command line](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-csharp?tabs=azure-cli%2Cin-process)

Once you have a function app service created, you can deploy the function to it using:
 
```json
func azure functionapp publish <YOUR_FUNCTION_APP_NAME>
``` 
Replace the `<YOUR_FUNCTION_APP_NAME>` placeholder with the actual name of your function app service.
Now if you go to the Azure portal and navigate to your function app service, you should see a `ServiceBusConsumer` function under the Functions section.
 

### Further reading
- [Azure Functions documentation](https://docs.microsoft.com/en-us/azure/azure-functions/)
- [Azure Functions for .NET isolated process](https://docs.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-rocess-guide)
- [Azure Service Bus documentation](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview)

