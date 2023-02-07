# Event ingest
 Veracity supports ingesting events via two main channels:
- HTTP API
	* [How to authenticate](Authenticate.md)
	* [C# code example using http client](#c#-code-example-using-http-client)
	* [C# code example using Veracity IoT SDK](#c#-code-example-using-veracity-iot-sdk)
* IoT Hub
	- [Stream events to IoT Hub](#submit-events-to-iot-hub)
## Use api

The api is accessible from [api-portal](https://api-portal.veracity.com/).  Select api   [Data Fabric IoT Event Broker Ingest API](https://api-portal.veracity.com/docs/services/DataFabric-IoTEventBrokerIngestAPI)
You can call the api directly from your application using standard tooling in your platform. For .Net and Python we provide SDK and examples.  When invoking the api, the consumer needs a token for authentication.

* How to authenticate
* How to explore the api in the portal
* How to use Veracity IoT SDK

Any eventtype can be ingested by POSTing a JSON object to Veracity with some header paramerters.
```
Request url: POST  https://api.veracity.com/veracity/ioteventbrokeringest/api/v1/events?tenantId={tenantId}&assetIdIssuer={assetIdIssuer}&assetId={assetId}&eventType={eventType}&timeStampUtc={timeStampUtc}&topic={topic}
```
- Base url: https://api.veracity.com/veracity
- Authorization: [Bearer token](Authenticate.md)
- Ocp-Apim-Subscription-Key: from application client or B2C user

### Header parameters
* assetId: E.g. "123456". Used together with AssetIdIssuer to identify an asset
* assetIdIssuer: E.g. "IMO", "MMSI", "JSMEA".Used together with AssetId to identify an asset
* eventType: E.g: Voyagereport, Topologyreport  (name of template for event)
* timeStampUtc: timestamp for Event, UTC: format: "2021-04-06T14:22:48.950716+02:00" (yyyy-mm-ddTHH:
* topic: Messages are filtered on topic when subscribing to Events. Can be any keyword that is meaningful or useful for subscription purposes E.g: "Engines","Cylinders","Arrival","Delivery". See MC-topics.
* tenantId: optional. If the user or application is only registered to a single tenant it will be using this tenant on ingest

**Example**
```
POST https://api.veracity.com/veracity/ioteventbrokeringest/api/v1/events?eventType=Topology&topic=TopologyHealth&timeStampUTC=2023-01-01T12:00:00Z&assetId=123&assetIdIssuer=imo
```
### C# code example using http client
For C# you can use Veracity nuget package or alternatively using http client. Fetching bearer token and ingesting Event. Example is written in C#. This approach is transferable to other languages utilizing http clients.

```
//main program
{
var token = await GetToken();
var subscriptionKey = "[OCP APIM Subscription key]";

// Ingest Event using bearer token
string assetId = "123";
string assetIdIssuer = "imo";
var timestamp = (DateTime.UtcNow).ToString("yyyy-MM-ddTHH:mm:ssZ");
string topic = "MC/Cylinders";
string eventType = "HealthReport";
var tenantId = "[tenantId]";
var jsonPayload =
"{\"HealthStatus\":\"OK\",\"CylinderStatus\":{\"Temperature\":24.03,\"Pressure\":20.8}}";  

var httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", subscriptionKey);
httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
var baseUrl = "api.veracity.com/veracity";
var url = $"https://{baseUrl}/ioteventbrokeringest/api/v1/events?" +
    $"tenantId={tenantId}&eventType={eventType}&topic={topic}&" +
    $"timeStampUTC={timestamp}&assetId={assetId}&assetIdIssuer={assetIdIssuer}";
var httpContent = new StringContent(jsonPayload.ToString(), Encoding.UTF8, "application/json");
var result = await httpClient.PostAsync(url, httpContent);
var contentresult = result.Content.ReadAsStringAsync().Result;
}

async Task<string> GetToken()
{
    var url = "https://login.microsoftonline.com/dnvglb2cprod.onmicrosoft.com/oauth2/token";
    var client_id = "[client_id]";
    var client_secret = "[client_secret]";
    var grant_type = "client_credentials";
    var resource = "https://dnvglb2cprod.onmicrosoft.com/29a8760a-d13a-41ce-998e-0a00c3d948d5";

    var postData = new Dictionary<string, string>
       {
           {"grant_type", grant_type},
           {"client_id", client_id},
           {"client_secret", client_secret},
           {"resource", resource},
       };

    using HttpClient httpClient = new HttpClient();
    httpClient.BaseAddress = new Uri(url);
    HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Post, httpClient.BaseAddress);

    request.Content = new FormUrlEncodedContent(postData);
    HttpResponseMessage authResponse = httpClient.PostAsync(url, new FormUrlEncodedContent(postData)).Result;
    var result = await authResponse.Content.ReadAsStringAsync();
    var token = (string)JToken.Parse(result)["access_token"];
    return token;
}
```


### C# code example using Veracity IoT SDK

Use nuget package **Veracity.IoT.SDK.Client**
Client id, secret and subscription key must be provided

```
using Veracity.IoT.SDK.Client;


string clientId = "[clientId]"; 
string clientSecret = "[clientSecret]";
string subscriptionKey = "[subscriptionKey]";
string baseUrl = "https://api.veracity.com/veracity/";

var tokenProvider = new ClientCredentialsTokenProvider(clientId, clientSecret);
var eventsClient = new VeracityIoTTimeSeriesClient(tokenProvider, baseUrl, subscriptionKey);

string assetId = "123456";
string assetIdIssuer = "imo";
DateTime timeStampUtc = DateTime.UtcNow;
string topic = "MC/Cylinders";
string eventType = "HealthReport";
var jsonPayload =
"{\"HealthStatus\":\"OK\",\"CylinderStatus\":{\"Temperature\":24.03,\"Pressure\":20.8}}";

var ingestResult = await eventsClient.Events.IngestEvent(jsonPayload, eventType, topic, timeStampUtc, assetId, assetIdIssuer);
```

## Submit events to Iot Hub
You will need the following information to be able to publish events to the IoT Hub:
* IoT Hub connection string
* IoT Hub device ID   (this is part of the connection string)

### C# example
An event can be streamed to an Azure IoT hub by wrapping it into a Veracity-event-message format
```json
  {
 "TenantId": "tenant id",
 "AssetId": "i.e. imo no",
 "AssetIdIssuer": "imo or other issuer",
 "Topic": "topic for event",
 "EventType": "name of event - template",
 "TimeStampUtc": "time event happened"
 "Payload" : "the event content - JSON"
  }
```

Microsoft supports nuget pacakges for sending data to IOTHub by connection string. (Microsoft.Azure.Devices.Client).

```
  using Microsoft.Azure.Devices.Client;

 var connectionString = "must be provided";
 var device = DeviceClient.CreateFromConnectionString(connectionString);
 await device.OpenAsync();		
.. 
 var json = JsonConvert.SerializeObject(myObj);
 byte[] msgByteArray = Encoding.ASCII.GetBytes(json);
 var message = new Message(msgByteArray);
 //max payload size is 256KB for Azure IOT hub
 await device.SendEventAsync(message);
 await device.CloseAsync();
 
```


### Node.js example

We'll be writing a simple Node.js application that will publish events to the IoT Hub. 

1. Navigate to the `test` folder and create a new Node.js project:  
```
cd ../test
npm init -y
``` 
2. Install the `azure-iot-device` and the `azure-iot-device-mqtt` packages:
```
npm install azure-iot-device azure-iot-device-mqtt
```
Also install the `dotenv` package to be able to read the configuration values from a `.env` file and the `uuid` package to generate a unique device ID: 
```
npm install dotenv uuid
```
3. Create a new file named `.env` and add the following configuration values:  

```
IOTHUB_CONNECTION_STRIN="<iot-hub-connection-string>"
IOTHUB_DEVICE_ID="<YOUR_DEVICE_ID>"`` 

Replace the `<iot-hub-connection-string>` and `<YOUR_DEVICE_ID>` placeholders with the actual values. Make sure to add the `.env` file to the `.gitignore` file.  
```
4) Create a new file named `test_publisher.js` and add the following code:

```js
require('dotenv').config();
const { Mqtt } = require('azure-iot-device-mqtt');
const { Client, Message } = require('azure-iot-device');
const {v4: uuidv4} = require('uuid');  
const  ConnectionString = process.env.IOTHUB_CONNECTION_STRING;
const  DeviceId = process.env.IOTHUB_DEVICE_ID;
const  TestAssetId = '<YOUR_TEST_ASSETID>';
const  TestTopic = '<YOUR_TEST_TOPIC>';
const  TestAssetIdIssuer = '<YOUR_TEST_ASSETID_ISSUER>';
const  TestEventType = 'TestEvent';
const publishMessage = async (eventData) => {
let client; 
try {
client = Client.fromConnectionString(ConnectionString, Mqtt);
await client.open();
} catch (err) {
const error = new  Error(`Error connecting to the IoTHub: ${err.message}`);
throw error;
}
  
eventData.deviceId = DeviceId;
const data = JSON.stringify(eventData);
const message = new  Message(data);
return  new  Promise((resolve, reject) => {
// send the message
client.sendEvent(message, function(err, res) {
// close the connection
client.close(function() {
if (err) {
return reject(err);
}
resolve(res);
});
});
});
}

publishMessage({
AssetId: TestAssetId,
Topic: TestTopic,
AssetIdIssuer: TestAssetIdIssuer,
Payload: {
TestPayloadItem: 'test-value-1',
TestPayloadItem2: 'test-value-2'
},
EventType: TestEventType,
TimeStampUtc: new  Date().toISOString(),
id: uuidv4()
})
.then(() => console.log('Message was sent successfully.'))

.catch((err) => console.error('An error has occurred:'. err));
```
 
Replace the `<YOUR_TEST_ASSETID>`, `YOUR_TEST_ASSETID_ISSUER`, and `<YOUR_TEST_TOPIC>` placeholders with actual values from your application.  

5. Run the `test_publisher.js` script:
```
node test_publisher.js
``` 
If all is well, you should have an event published and ready to be consumed by the Azure Function.
 


