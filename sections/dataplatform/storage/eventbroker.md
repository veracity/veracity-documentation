---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Events
Events are json objects with a topic that can be published to a database and subscribers can subscribe to events or request events from database. 

## API endpoints
To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/DataFabric-IoTEventBrokerIngestAPI-swagger.json).

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).

*NOTE:* When authenticating for event data use resource
var resource = "https://dnvglb2cprod.onmicrosoft.com/29a8760a-d13a-41ce-998e-0a00c3d948d5";


### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)

## Event ingest
 Veracity supports ingesting events via two main channels:
- HTTP API	
	* [C# code example using http client](#c#-code-example-using-http-client)
	* [C# code example using Veracity IoT SDK](#c#-code-example-using-veracity-iot-sdk)

Any eventtype can be ingested by POSTing a JSON object to Veracity with some header paramerters.
```
Request url: POST  {baseurl}/api/v1/events?tenantId={tenantId}&workspaceId={workspaceId}&assetIdIssuer={assetIdIssuer}&assetId={assetId}&eventType={eventType}&timeStampUtc={timeStampUtc}&topic={topic}
```


### Header parameters
- tenantId: tenant id (guid)
- workspaceid: workspace is (guid)
- assetId: E.g. "123456". Used together with AssetIdIssuer to identify an asset
- assetIdIssuer: E.g. "IMO", "MMSI", "JSMEA".Used together with AssetId to identify an asset
- eventType: E.g: Voyagereport, Topologyreport  (name of template for event)
- timeStampUtc: timestamp for when event occured, UTC: format: "2021-04-06T14:22:48.950716+02:00" (yyyy-mm-ddTHH:
- topic: Messages are filtered on topic when subscribing to Events. Can be any keyword that is meaningful or useful for subscription purposes E.g: "Engines","Cylinders","Arrival","Delivery". See MC-topics.
- tenantId: optional. If the user or application is only registered to a single tenant it will be using this tenant on ingest

**Example**
```
POST {baseUrl}/api/v1/events?eventType=Topology&topic=TopologyHealth&timeStampUTC=2023-01-01T12:00:00Z&assetId=123&assetIdIssuer=imo
```
### C# code example using http client
For C# you can use Veracity nuget package or alternatively using http client. Fetching bearer token and ingesting Event. Example is written in C#. This approach is transferable to other languages utilizing http clients.

```cs
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

```cs
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
- IoT Hub connection string
- IoT Hub device ID   (this is part of the connection string)

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

Microsoft supports nuget pacakges for sending data to IOTHub by connection string. (Microsoft.Azure.Devices.Client)
```cs
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