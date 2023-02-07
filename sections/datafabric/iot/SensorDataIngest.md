# Ingest sensor data

## Content
* [Channel list /taglist](#channellist)
* [Stream sensor data using Iot Hub](#iot-hub)
* [Data format](#data-format)
* [Use CSV upload](#csv-upload)

## Channellist 
Before sensor data can be streamed to Veracity, channel-list needs to be registered for the asset. A channel list is an overview of all the tags/datachannels with its metadata.  An Excel template consists of the following columns can be provided or JSON. 

The data channel properties  is based on ISO19848 standard for meta-data.
|Column	 |Description  |
|--|--|
|ShortId  |	Tag id used by system on asset. Tag used to identify datapoint at ingest |  
|Name| Name of channel	|
|Remarks| Description of channel|
|Path| used to group channels for visualization in IOT Explorer|
|LowerLimit |Boundaries |
|UpperLimit |Boundaries |
|QuantityName| I.e celsius, kilo|
|UnitSymbol| displayed in chart|
|DataFormat|  String, Decimal,Boolean|
|Alias|  Alias of tag, groups|
|DataChannelType| Inst, calc etc|
|Update Cycle| represents the cycle of updating measurement value, in unit seconds|
|Calculation Period|When a value of Data Channel is a result of calculation that uses measurement value of specific time periods, Calculation Period shall be used to describe the said period, in unit seconds|

In addition several identifiers can be modeled for the channels such as: 
* Universal ID
* Local ID
* Short ID

## IOT Hub
Sensor-data (datapoints) are sent as JSON to veracity IOT hub using different protocols.
Microsoft supports nuget pacakges for sending data to IOTHub by connection string. (Microsoft.Azure.Devices.Client)
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
````

## Data format
The data format for ingesting raw datapoints (sensor data) are:
 * [ISO 19848](#iso19848-message-format)
 * [Veracity ](#veracity-message-format)
 * Wits: Used by oil-rigs to send drilling data
 * [Trisense](#trisense-message)

### Iso19848 message format

The ISO 19848 Message allows EventData and/or TabularData format. The difference between the two is that EventData allows for datapoints not occurring regularly. This means that EventData can report values on different timestamps for different channels, whereas TabularData reports values using same timestamp for all datapoints in requested dataset. 
Using tabular data-foramt, you can send several datapoints with minimal overhead.  A data channel id is the tag id. You can add as many datasets as you want in “a package”. A dateset is a timestamp with values for all datachannels defined in set DataChannelId. For the TabularData format, the index of each value in the Value list must correspond to same index associated with the given value in the DataChannelId list. 

Note: ShipId is only necessary when sending data for several assets (platform to platform integration). ShipId is IMO nr or DNV unique asset identifier. DataQuality is optional.
**Example of ISO19848**
```json
{
	"Package": {
		"Header": {
			"ShipID": "1234567"			
		},
		"TimeSeriesData": [
			{				
				"TabularData": [
					{
						"NumberOfDataSet": "2",
						"NumberOfDataChannel": "2",
						"DataChannelID": ["A230","0020"],
						"DataSet": [
							{
								"TimeStamp": "2023-01-01T12:00:00Z",
								"Value": ["100.0","200.0"],
								"Quality": ["0","1"	]
							},
							{
								"TimeStamp": "2023-01-02T12:00:00Z",
								"Value": ["100.5","205.0"],
								"Quality": ["0","0"	]
							}
						]
					},
					{
						"NumberOfDataSet": "3",
						"NumberOfDataChannel": "1",
						"DataChannelID": ["0130"],
						"DataSet": [
							{
								"TimeStamp": "2023-01-01T12:00:00Z",
								"Value": ["100.0"],
								"Quality": ["0"]
							},
							{
								"TimeStamp": "2023-01-02T00:00:00Z",
								"Value": ["100.2"],
								"Quality": ["0"]
							},
							{
								"TimeStamp": "2023-01-02T12:00:00Z",
								"Value": ["100.3"],
								"Quality": ["0"	]
							}
						]
					}
				],
				"EventData": {
					"NumberOfDataSet": "3",
					"DataSet": [
						{
							"TimeStamp": "2023-01-01T12:00:01Z",
							"DataChannelID": "0011",
							"Value": "HIGH",
							"Quality": "0"
						},
						{
							"TimeStamp": "2023-01-01T12:00:01Z",
							"DataChannelID": "X021",
							"Value": "HIGH",
							"Quality": "0"
						},
						{
							"TimeStamp": "2023-01-01T12:00:23Z",
							"DataChannelID": "0011",
							"Value": "NORMAL",
							"Quality": "0"
						}
					]
				}
			}			
		]
	}
}
```
TimeSeriesData can contain a combination of tabular and event format or only one of the formats.

#### Nuget package 
The C# classes supporting ISO model is found in nuget package Veracity.IOT.SDK.Models

### Veracity message format
The C# classes supporting this format is found in nuget package Veracity.IOT.SDK.Models
```
{
	"messageId": "1234",
	"messages": [
		{
			"timestamp": "2023-01-01T12:00:23Z",
			"tagId": "0011",
			"value": "NORMAL",
			"quality": "0"
		},
		{
			"timestamp": "2023-01-02T12:00:00Z",
			"tagId": "0013",
			"value": "100.3",
			"quality": "0"
		}
	]
}

```
- messageId is optional if you want to tag all datapoints with same package-id
- quality is optional

#### Trisense
```
{
  "deviceId": "db:62:f9:6f:7d:b7",
  "TMP": 8,
  "HUM": 69,
  "CHRG": 5865,
  "WAP": 421
}
```

## CSV upload
CSV files can be uploaded to a data container in  Veracity. The CSV files are automatically read and ingested into correct ingest pipeline. Data can be accesses through apis.
The container needs to be managed by Veracity.
