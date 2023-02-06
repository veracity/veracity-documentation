---
author: Benedikte Kallåk
description: Description of quick start section
---

# Data provider
A data-provider ingests sensor-data or events to Veracity using different protocols and data-formats. 
- Sensor data is streamed to Veracity IoT Hub 
- Events are sent to Veracity using rest-api or streamed using IoT Hub

When using IoT Hub, data provider needs a private connection string and when using rest-api, B2C authentication is required.

## Protocols

- HTTPS
- AMQP, AMQP over WebSockets
- MQTT, MQTT over WebSockets


## Data format for sensordata

High frequency data is streamed into Veracity IOT hub from edge solution or from another data platform. 
The data format supported are:
 - [ISO 19848](#iso19848-message-format)
 - [Veracity ](#veracity-message)
 - [Trisense](#trisense-message)
 - CSV: Veracity IOT also support CSV uploads to data container.

## Data format for events
The payload of the event can be any data structure in JSON format. Each data-structure is defined as a event-type (template). Each event require some meta-data such as asset, topic and timestamp and event-type.


## Ingest events using rest-api
Any eventtype can be ingested by POSTing a JSON object to Veracity with some header paramerters.

Base url: https://api.veracity.com/veracity
Request url: POST  https://api.veracity.com/veracity/ioteventbrokeringest/api/v1/events?tenantId={tenantId}&assetIdIssuer={assetIdIssuer}&assetId={assetId}&eventType={eventType}&timeStampUtc={timeStampUtc}&topic={topic}
Authorization: Bearer token click here
Ocp-Apim-Subscription-Key: from application client or B2C user

### Header parameters
- assetId: E.g. "123456". Used together with AssetIdIssuer to identify an asset
- assetIdIssuer: E.g. "IMO", "MMSI", "JSMEA".Used together with AssetId to identify an asset
- eventType: E.g: Voyagereport, Topologyreport  (name of tempalte for event)
- timeStampUtc: timestamp for Event, UTC: format: "2021-04-06T14:22:48.950716+02:00"
- topic: Messages are filtered on topic when subscribing to Events. Can be any keyword that is meaningful or useful for subscription purposes E.g: "Engines","Cylinders","Arrival","Delivery"
- tenantId: optional. If the user or application is only registered to a single tenant it will be using this tenant on ingest

Example
POST https://api.veracity.com/veracity/ioteventbrokeringest/api/v1/events?eventType=Topology&topic=TopologyHealth&timeStampUTC=2023-01-01T12:00:00Z&assetId=123&assetIdIssuer=imo

### Body examples
```json
  {
    any valid JSON object
  }

```

```json
  {
    "manufacturer": "string",
    "modelNo": "string",
    "serialNo": "string",
    "softwareVersion": "string",
    "type": "string",
    "dataChannelId": "string",
    "name": "string",
    "timeStampUTC": "string",
    "healthStatus": "string",
    "expiryDate": "string"
  }

```

### C# code example using IoT SDK
Client id, secret and subscription key must be provided
Use nugt package 

```c#
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

### C# code example using http client
Alternatively using http client. Fetching bearer token and ingesting Event. Example is written in C#. This approach is transferable to other languages utilizing http clients.

```c#

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
## Ingest event using IoT hub
An event can be streamed to an Azure IoT hub by wrapping it into a Veracity-event-message format



## Setup
Before data can be ingested to Veracity the following must be done:
1.	Vessel must be registered by Veracity administrator
2.	Channel list must be imported by Veracity administrator
3.	You must receive connection string for connection to Veracity IOT hub for streaming data. If data is to be uploaded as CSV files to data fabric container you will receive access to such container.

[Submit JSON message to IOT hub](#submit-json--to-iot-hub)

## Data channel list

A channel list is an overview of all the tags/datachannels with its metadata. 
An excel template consists of the following columns:

<table border="1" width="100%">
    <thead>
      <tr>	  
	    <th>Excel column</th>
        <th>Description</th>        
      </tr>
    </thead>
    <tbody>             
		<tr>
		    <td>ShortId</td>
            <td>Tag id used by system on asset. Tag used to identify datapoint at ingest </td>
        </tr>
		<tr>
		    <td>Name</td>
            <td>name of channel</td>
        </tr>
		<tr>
		    <td>Remarks</td>
            <td>Description of channel</td>                  
        </tr>
		<tr>
		    <td>Path</td>
            <td>Path to breakdownstructure used for asset. I.e. VIS path according to ISO 19848. Can be mapped using ML </td>                  
        </tr>
		<tr>
		    <td>LowerLimit</td>
            <td>Boundaries</td>                  
        </tr>
		<tr>
		    <td>UpperLimit</td>
            <td>Boundaries</td>                  
        </tr>
		<tr>
		    <td>Quantity</td>
            <td>I.e celsius, kilo</td>                  
        </tr>
		<tr>
		    <td>UnitSymbol</td>
            <td>Displayed in charts (e.g. kg, m, C)</td>                  
        </tr>	
		<tr>
		    <td>DataFormat</td>
            <td>Format of data received; String, Decimal,Boolean</td>                  
        </tr>	
		<tr>
		    <td>Alias</td>
            <td>Alias for shortId (tag id) if exist. This is optional</td>                  
        </tr>	
 	</tbody>
 </table>


## ISO19848 Message format

The Veracity Ingest SDK contains utility classes for how to generate ISO19848-format messages.
Veracity SDK is available as Nuget package:

https://www.nuget.org/packages/Veracity.IoT.SDK.Models/


Note: ShipId is only necessary when sending data for several assets (platform to platform integration).
ShipId is IMO nr or DNVGL unique asset identifier.

When sending from an edge device on asset, the Header section can be removed. Hence, the connection string is unique per asset.

The ISO Message allows for either EventData or TabularData format. The difference between the two is that EventData allows for datapoints not occurring regularly. 
This means that EventData can report values on different timestamps for different channels, whereas TabularData reports values using same timestamp for all datapoints in requested dataset. 

### Example of EventData

```json
{
   "Header":
      {"ShipId":"12345"},
    "TimeSeriesData":
	{
	    "EventData":
		{
		   "DataSet":[
		     {
			  "TimeStamp":"2020-12-18T11:17:46.202505Z",
			  "DataChannelId":"tag1",
			  "Value":12.21
			 },
			 {
			  "TimeStamp":"2020-12-18T11:19:44.2026323Z",
			  "DataChannelId":"tagy",
			  "Value":13.4
			 }
			 ]
		}
	}
}
```

### Example of tabular data
You can send several datapoints with minimal overhead.  A data channel id is the tag id. You can add as many datasets as you want in “a package”. A dateset is a timestamp with values for all datachannels defined in set DataChannelId.
For the TabularData format, the index of each value in the Value list must correspond to same index associated with the given value in the DataChannelId list. 
```json
{
"Header":
  {"ShipId":"12345"},
   "TimeSeriesData":
    {
	   "TabularData":
	     {		
		  "DataChannelId":["Tag1","TagY","TagX"],
		   "DataSet": [
		      {
			   "TimeStamp":"2020-12-18T11:24:12Z",
			   "Value":[12.21,13.4,534.3]
			  },
			  {
			   "TimeStamp":"2020-12-18T11:24:12Z",
			   "Value":[13.21,13.344,114.3]
			  },
              {
			   "TimeStamp":"2020-12-18T11:27:16Z",
			   "Value":[12.24,11.4,574.753]
			  }			  
		   ]
		 }
	}
}	
```	   
	   
## Veracity Message
In a Veracity message several datapoints can be sent in same message.
	
```json
{  
  "MessageId": "1234",
  "sentTimestamp": "2020-12-18T11:24:12Z",
  "messages": [
  {
      "id":"1234454",
	  "assetId":"345",
	  "tagId":"Tag1",
	  "value":"12.21",
      "timestamp":"2020-12-18T11:24:12Z",	  
	  "dimension":"C12"    
  }
  {
      "id":"1234454",
	  "assetId":"345",
	  "tagId":"TagY",
	  "value":"13.4"    
	   "timestamp":"2020-12-18T11:24:12Z"	  
  }
  ]
}
```	   
*Id: can be used to group tags together in a serie
*assetId: guid of asset or IMO nr
*tagId: shortid of channel
*value: value of datapoint
*dimension: Optional - can be used to relate datapoint to component
*sentTimestamp: Timestamp, UTC, 

## Combine events and tabular


## Submit JSON to IoT Hub

Once the JSON is obtained, the MS SDK provides an easy way of sending the JSON to the IOT Hub using Microsoft.Azure.Devices.Client; as demonstrated in the code example below:

Connection string to IOT hub is received by Encrypted email.

This code snippet shows how to use Microsoft.Azure.Devices.Client to send messages to IOT hub

```cs
  using Microsoft.Azure.Devices.Client;
  using Newtonsoft.Json;
  using Veracity.IoT.SDK.Models.Input.ISO;

....

 var connectionString = configuration.GetConnectionString("IoTHubConnectionString");
 var device = DeviceClient.CreateFromConnectionString(connectionString);
 await device.OpenAsync();
			
 IsoMessage isoMessage = new IsoMessage();  //add shipId if required and timeseruesdata
 
 var json = JsonConvert.SerializeObject(isoMessage);
 byte[] msgByteArray = Encoding.ASCII.GetBytes(json);
 var message = new Message(msgByteArray);
 //max payload size is 256KB for Azure IOT hub
 await device.SendEventAsync(message);
 await device.CloseAsync();
 
```

## Protocols
IoT Hub and the device SDKs support the following protocols for connecting devices:

If your solution cannot use the device libraries, devices can use the MQTT v3.1.1, HTTPS 1.1, or AMQP 1.0 protocols to connect natively to your hub.
- SDK: https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-sdks
- Communicate with your IoT hub using the MQTT protocol: https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-mqtt-support
