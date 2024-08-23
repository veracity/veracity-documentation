---
author: Veracity
description: This section describes event query api
---

# Event query api

You can call the api directly from your application using standard tooling in your platform. For .Net and Python we provide SDK and examples.  When invoking the api, the consumer needs a token for authentication.

- [How to authenticate](authenticate.md)
- [How to explore the api in the portal](ApiPortal.md)
- [Query events](#query-events)
	- [How to use Veracity IoT SDK](#c#-code-example-using-veracity-iot-sdk)
	- [C# code example using Http client](#c#-code-example-using-http-client)

## Security Model
Users or applications can only access data for assets, tenants and respective topics they have access to.

## Querying Events using API
[Browse api definition](apiendpoints.md)
This endpoint can be used to fetch Events with various parameters for filtering.

-   Base url:  [https://api.veracity.com/veracity/](https://api.veracity.com/veracity/)
-   Authorization: Bearer token  [click here](Authenticate.md)
-   Ocp-Apim-Subscription-Key: from application client or B2C user

### Get Events
Relative url: 
```
ioteventbrokerquery/api/v1/events?tenantId={tenantId}&eventType={eventType}&topic={topic}&fromUtcDate={fromUtcDate}&toUtcDate={toUtcDate}&assetId={assetId}&assetIdIssuer={assetIdIssuer}&maxNumberOfItems={maxNumberOfItems}&offset={offset}
```
-   assetId: E.g. "123456". Used together with AssetIdIssuer to identify an asset
-   assetIdIssuer: E.g. "IMO", "MMSI", "JSMEA".Used together with AssetId to identify an asset
-   eventType: E.g: Voyagereport, Topologyreport
-   fromUtcDate: Date time start range, UTC: format: "2021-04-06T14:22:48.950716+02:00"
-   toUtcDate: Date time end range, UTC: format: "2021-04-06T14:22:48.950716+02:00"
-   maxNumberOfItems: Number of events to return
-   offset: You can specify an offset from where to start returning data
-   topic: Messages are filtered on topic when subscribing to Events. Can be any keyword that is meaningful or useful for subscription purposes E.g: "Engines","Cylinders","Arrival","Delivery"
-   tenantId: optional. If the user or application is only registered to a single tenant it will be using this tenant on ingest

### C# code example using Veracity IoT SDK
Use latest nuget package **Veracity.IoT.SDK.Client**
Client id, secret and subscription key must be given

```cs
using Veracity.IoT.SDK.Client; 
 
string clientId = "[clientId]";
string clientSecret = "[clientSecret]";
string subscriptionKey = "[subscriptionKey]";
string baseUrl = "https://api.veracity.com/veracity/";
 
var tokenProvider = new ClientCredentialsTokenProvider(clientId, clientSecret);
var eventsClient = new VeracityIoTTimeSeriesClient(tokenProvider, baseUrl, subscriptionKey);  
 
//Replace as needed
var assetId = "555";
var assetIdIssuer = "imo";
var topic = "MC/Engines";
var eventType = "eventtype";
DateTime fromUtcDate = new DateTime(2000, 1, 1);
DateTime toUtcDate = DateTime.UtcNow;
var maxNumberOfItems = 10;
var offset = 0;
var result = await eventClient.Events.GetEvents(_tenantId,
assetId, assetIdIssuer, topic, eventType, fromUtcDate, toUtcDate, maxNumberOfItems, offset);
```

### C# code example using Http client
Alternatively, using http client. Fetching bearer token and querying Events. Example is written in C#. This approach is portable to other languages using http clients.

```cs
var token = await GetToken(); 
var subscriptionKey = "[OCP APIM Subscription key]";  
 
// Query Event using bearer token
string assetId = "123";
string assetIdIssuer = "imo";
DateTime fromUtcDate = DateTime.UtcNow;
DateTime toUtcDate = DateTime.UtcNow;
string topic = "MC/Cylinders";
string eventType = "HealthReport";
var tenantId = "[tenantId]";
var maxNumberOfItems = 1000;
var offset = 0;
 
var httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", subscriptionKey);
httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
var baseUrl = "api.veracity.com/veracity";
var url = $"https://{baseUrl}/ioteventbrokerquery/api/v1/events?" +
    $"tenantId={tenantId}" +
    $"&eventType={eventType}&topic={topic}" +
    $"&assetId={assetId}&assetIdIssuer={assetIdIssuer}" +
    $"&fromUtcDate={fromUtcDate}&toUtcDate={toUtcDate}" +
    $"&maxNumberOfItems={maxNumberOfItems}&offset={offset}";
 
var result = await httpClient.GetAsync(url);
var contentresult = result.Content.ReadAsStringAsync().Result;

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
