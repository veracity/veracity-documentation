---
author: Benedikte Kallåk
description: This section describes how to query for sensor data using api
---

# Sensor Query Api
This REST api function as a proxy on top of dataplatform query api.

## Get timeseries data
Returns timeseries data for a set of datachannels on an asset (or set of assets) by specifying request payload. 
- Base URL: *https://api.veracity.com/veracity/*

```
POST https://api.veracity.com/veracity/timeseries3/api/v3/timeSeries
```
Note:	add in the header of the api call: x-tenant-id = tenantAlias 

**Request Payload**
```json
{
  "assetIds": [
    "1234"
  ],
  "dataChannelIds": [
    "string"  //Array of channel ids (guid or tag ids)
  ], 
  "start": "2021-04-05T14:30Z", //using ISO8601 format YYYY-MM-DDThh:mm:ss
  "end": "2021-06-05T14:30Z",   // using ISO8601 format YYYY-MM-DDThh:mm:ss
  "limit": 1000, //Max number of datapoints to be returned. System max limit is 200 000.  
  "includeStartBoundary": true,
  "includeEndBoundary": true
}
```
## GET timeseries using offset

```
https://api.veracity.com/veracity/timeseries3/api/v3/assets/{assetid}/dataChannels/
{datachannel id}/timeSeries?offset=2024-05-01&before=False
```

Note:	add in the header of the api call: x-tenant-id = tenantAlias 

Datachannels ids can be tagId or guid

## GET timeseries using n latest

```
https://api.veracity.com/veracity/timeseries3/api/v3/assets/{assetid}/dataChannels/
{datachannelId}/timeSeries/latest?nLatest=50```

Note:	add in the header of the api call: x-tenant-id = tenantAlias 

Datachannels ids can be tagId or guid

### C Sharp code using Http client
Alternatively using http client. Fetching bearer token and querying Events. Example is written in C#. This approach is portable to other languages using http clients.

```cs
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System.Net.Http.Headers;
using System.Text;

async Task<string> GetToken()
{
    var url = "https://login.microsoftonline.com/dnvglb2cprod.onmicrosoft.com/oauth2/token";
    var client_id = "[client id]";
    var client_secret = "[secret]";
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

// Query IoT using bearer token
var token = await GetToken();
var subscriptionKey = "[Subscription key]";

var httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", subscriptionKey);
httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
var baseUrl = "api.veracity.com/veracity";


DateTime fromUtcDate = DateTime.UtcNow.AddDays(-7);
DateTime toUtcDate = DateTime.UtcNow;
string shortId = "wind_speed";
var maxNumberOfItems = 1000;

var payload = new RequestPayload()
{
    assetIds = new string[] { assetId },
    start = fromUtcDate,
    end = toUtcDate, 
    dataChannelIds = new string[] { shortId },
    limit = maxNumberOfItems,   
    includeStartBoundary= true
};

url = $"https://{baseUrl}/timeseries3/api/v3/timeSeries";
string json = JsonConvert.SerializeObject(payload);
var content = new StringContent(json, Encoding.UTF8, "application/json");
content.Headers.ContentType = new MediaTypeHeaderValue("application/json");

result = httpClient.PostAsync(url, content).Result;
contentresult = result.Content.ReadAsStringAsync().Result;


public class RequestPayload
{
    public string[] assetIds { get; set; }
    public string[] dataChannelIds { get; set; }   
    public DateTime start { get; set; }
    public DateTime end { get; set; }
    public int limit { get; set; }   
    public bool includeStartBoundary { get; set; }
    public bool includeEndBoundary { get; set; }

}
```

### Get Channel list for asset
Use Veracity Asset model to model channel list with metadata.

