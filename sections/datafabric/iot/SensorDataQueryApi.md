---
author: Benedikte Kallåk
description: This section describes Sensor Query API.
---

# Sensor Query Api
You can call the api directly from your application using a RestClient.  An SDK is provided for .Net and for Python.
When invoking the api, the consumer needs a token for authentication.
Explore the api in the portal: [Data Fabric IoT Time Series Query API V2](https://api-portal.veracity.com/docs/services/DataFabric-IoT-TimeSeriesAPI-V2) . Select group by tag.  Note: [you must be signed in](ApiPortal.md).

* [How to authenticate](authenticate.md)
* [How to explore the api in the portal](ApiPortal.md)
*  [Get timeseries data](#get-timeseries-data)
	* [C# code using Http client](#c#-code-using-http-client)
	* [C# code using Veracity SDK for C#](#c#-code-example-using-veracity-iot-sdk)
	* [Python example](SensorDataPython.md)
* [Query for calculated data quality](#query-for-calculated-data-quality)
## Security Model
Only users that has access to an asset can access sensor-data from this asset on the channels user has subscribed. 

## Get timeseries data
Returns timeseries data for a set of datachannels on an asset (or set of assets) by specifying request payload. 
* Base URL: *https://api.veracity.com/veracity/*
#### Flat response
```
POST https://api.veracity.com/veracity/timeseries2/api/v2/timeSeries
```
#### ISO 19848 response
```
POST https://api.veracity.com/veracity/timeseries2/api/v2/iso19848/timeSeries
```
**Request Payload**
```json
{
  "assetIds": [
    "1234"
  ],
  "dataChannelIds": [
    "string"  //Array of channel ids. Use type specified in dataChannelIdType. I
  ],
  "typeOption": "Data",//sddData/Data. sddData returns datapoints and metadata, Data returns datapoints only. (applies ISO 19848 only)
  "downScaleInt": "null", //specify downscaling interval,  Set to null if no downscaling.ISO8601 duration format. I.e. PT30S, PT1H, PT10M, PT60S
  "start": "2021-04-05T14:30Z", //using ISO8601 format YYYY-MM-DDThh:mm:ss
  "end": "2021-06-05T14:30Z",   // using ISO8601 format YYYY-MM-DDThh:mm:ss
  "limit": 1000, //Max number of datapoints to be returned. System max limit is 200 000.
  "dataChannelIdType": "ShortId", //Are you requesting channels by ShortId or DataChannelUuid or LocalId
  "includeStartBoundary": true,
  "includeEndBoundary": true
}
```
#### Downsized datapoints
If high resolution of data is not required or can be traded off for less dense data (and performance benefits) this is the recommended way of getting timeseries. Essentially the timeseries is binned by the duration specified in the parameter and the min/max/average of the data per bin is returned.
Set downScaleInt in request payload to  specify downscaling interval. Set to null if no downscaling. ISO8601 duration format. I.e. PT30S for 30 sec, PT1H, for 1 hour, PT10M for 10 minutes, PT60S 

### C# code example using Veracity IoT SDK
Use latest nuget package **Veracity.IoT.SDK.Client**
```
using Veracity.IoT.SDK.Client;
using Veracity.IoT.SDK.Models.Query;

string clientId = "[clientid]";
string clientSecret = "[secret]";
var subscriptionKey = "[subscription key]";
string baseUrl = "https://api.veracity.com/veracity/";

var tokenProvider = new ClientCredentialsTokenProvider(clientId, clientSecret);
var veracityIoTclient = new VeracityIoTTimeSeriesClient(tokenProvider, baseUrl, subscriptionKey);

var allAssets = await veracityIoTclient.Assets.MyAssets();
//get asset id
var assetGuid = allAssets[0].Id;

//Replace as needed
DateTime fromUtcDate = DateTime.UtcNow.AddDays(-7);
DateTime toUtcDate = DateTime.UtcNow;
string shortId = "wind_speed";
var maxNumberOfItems = 1000;
DefaultQueryPayload payload = new DefaultQueryPayload()
{
    AssetIds = new List<Guid> { assetGuid },
    DataChannelIds = new List<string> { shortId },
    IncludeStartBoundary = true,
    DownScaleInt = "PT60S",  //set null if raw-data
    Start = fromUtcDate,
    End = toUtcDate,
    Limit = maxNumberOfItems,
    DataChannelIdType = DataChannelIdTypeEnum.ShortId};
    
var result = await veracityIoTclient.TimeSeries.Veracity.GetTimeseries(payload);
```

### C# code using Http client
Alternatively using http client. Fetching bearer token and querying Events. Example is written in C#. This approach is portable to other languages using http clients.

```
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

// Query iot using bearer token
var token = await GetToken();
var subscriptionKey = "[Subscription key]";

var httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", subscriptionKey);
httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
var baseUrl = "api.veracity.com/veracity";

//get all assets you have access to
var url = $"https://{baseUrl}/timeseries2/api/v2/assets";
var result = await httpClient.GetAsync(url);
var contentresult = result.Content.ReadAsStringAsync().Result;

//retrive asset id from collection
string assetId = "38c0c0bc-ef5c-4d20-ab73-d06ff9ece405";

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
    downScaleInt = "PT60S",  //set null if raw-data
    typeOption = "Data",
    dataChannelIdType = "ShortId",
    includeStartBoundary= true
};

url = $"https://{baseUrl}/timeseries2/api/v2/timeSeries";
string json = JsonConvert.SerializeObject(payload);
var content = new StringContent(json, Encoding.UTF8, "application/json");
content.Headers.ContentType = new MediaTypeHeaderValue("application/json");

result = httpClient.PostAsync(url, content).Result;
contentresult = result.Content.ReadAsStringAsync().Result;


public class RequestPayload
{
    public string[] assetIds { get; set; }
    public string[] dataChannelIds { get; set; }
    public string typeOption { get; set; }
    public string downScaleInt { get; set; }
    public DateTime start { get; set; }
    public DateTime end { get; set; }
    public int limit { get; set; }
    public string dataChannelIdType { get; set; }
    public bool includeStartBoundary { get; set; }
    public bool includeEndBoundary { get; set; }

}
```

### Get Channellist for asset
List all metadata for data-channels registered for this asset that the user has access to.  Inaccessible channels, based on permissions, are filtered out.
```
GET https://api.veracity.com/veracity/timeseries2/api/v2/DataChannelList/{assetId}
```
* assetId: asset guid


### Get latest datapoints
Get the latest n-received values for given channels. Datapoints in the response are listed as EventData.
#### Flat response
```
https://api.veracity.com/veracity/timeseries2/api/v2/timeSeries/latest
```
#### ISO 19848 response
```
https://api.veracity.com/veracity/timeseries2/api/v2/iso19848/timeSeries/latest
```
#### Request payload
Receive last 100 datapoints for channel A101 and A202 on asset 1234
```json
{
  "assetIds": [
    "1234"
  ],
  "dataChannelIds": ["A101", "A202"], 
  "typeOption": "Data",
  "latestNValues": 100,
  "dataChannelIdType": "ShortId"
}
```

## Query for calculated data quality
Receive calculated data quality on ingested sensor data based on defined metrics.

Returns aggregated dataquality score for assets for given time period
```
https://api.veracity.com/veracity/timeseries2/api/v2/DataQuality/aggregate/.score
```
Returns aggregations per week for each dataquality metric in selected periode

```
https://api.veracity.com/veracity/timeseries2/api/v2/DataQuality/trend/.rulescore
```
