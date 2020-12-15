---
author: Veracity
description: Description of quick start section
---

# Ingest IoT data to Veracity

Data is ingested into Veracity IOT hub from edge solution or from another data platform. 
The data format supoorted are:
 - ISO 19848
 - Veracity 
 - Trisense 

## Setup
Before data can be ingested to Veracity the following must be done:
1.	Vessel must be registered by Veracity IOT administrator
2.	Channel list must be imported by Veracity administrator
3.	You must receive connection string for connection to Veracity IOT hub for streaming data


##Data chanel list

A channel list is an overview of all the tags/meassure poits that will provide data togehter with its metadata. 
Download excel template 

ShortId	Tag id
Name	User friendly channel (tag) name
Remarks	Description of channel
Path 	Mapping to breakdown structure (ie. VIS). Can be set to /unmapped and can be mapped later without affecting the ingest of data
LowerLimit	Boundaries
UpperLimit	
Quantity Name	I.e celsius, kilo
UnitSymbol	Displayed in charts (e.g. kg, m, C)
DataFormat	String, Descimal,Boolean
Alias	Alias for shortId (tag id) if exist and not required
Quantity
Location

##ISO19848 Message format

The Veracity Ingest SDK contains utility classes for how to generate ISO19848-format messages.
Veracity SDK is available form GitHub.


https://www.nuget.org/packages/Veracity.IoT.SDK.Models/


Note: ShipId is only necessary when sending data for several assets (platform to platform integration).
ShipId is IMO nr or DNVGL unique asset identifier.

When sending from an edge device on asset, the Header section can be removed. Hence, the connection string is unique per asset.

The ISO Message allows for either EventData or TabularData format. The difference between the two is that EventData allows for datapoints not occurring regularly. This means that EventData can report values on different timestamps for different tag id’s, whereas TabularData only reports values on the same timestamp for all tag id’s. 

Example of EventData

Example of tabular data
You can send several datapoints with minimal overhead.  A data channel id is the tag id. You can add as many datasets as you want in “a package”. 
For the TabularData format ,the index of each value in the Value list must correspond to same index associated with the given value in the DataChannelId list. 

##Submit to IoT Hub

Once the JSON is obtained, the MS SDK provides an easy way of sending the JSON to the IOT Hub using Microsoft.Azure.Devices.Client; as demonstrated in the code example below:

Connection string to IOT hub is received by Encrypted email.

var device = DeviceClient.CreateFromConnectionString(connectionString);
await device.OpenAsync();
//max payload size is 256KB for Azure IOT hub
byte[] msgByteArray = Encoding.ASCII.GetBytes(json);
var message = new Message(msgByteArray);
await device.SendEventAsync(message);
await device.CloseAsync();

IoT Hub and the device SDKs support the following protocols for connecting devices:
•	HTTPS
•	AMQP
•	AMQP over WebSockets
•	MQTT
•	MQTT over WebSockets
If your solution cannot use the device libraries, devices can use the MQTT v3.1.1, HTTPS 1.1, or AMQP 1.0 protocols to connect natively to your hub.
1.	SDK: https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-sdks
2.	Communicate with your IoT hub using the MQTT protocol: https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-mqtt-support
