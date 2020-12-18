---
author: Benedikte Kallåk
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


## Data chanel list

A channel list is an overview of all the tags/meassure poits that will provide data togehter with its metadata. 
Download excel template 

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
            <td>Tag id used by system on asset </td>
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
            <td>Path to breakdownstructure used fo rasset. I.e VIS path according to ISO 19848. Can be mapped using ML (specify /Unm</td>                  
        </tr>
		<tr>
		    <td>LowerLimit</td>
            <td>/v1/Assets</td>                  
        </tr>
		<tr>
		    <td>UpperLimit</td>
            <td>Boundariess</td>                  
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
            <td>format of data received; String, Descimal,Boolean</td>                  
        </tr>	
		<tr>
		    <td>Alias</td>
            <td>Alias for shortId (tag id) if exist. This is optional</td>                  
        </tr>			
		
 </tbody>    		
 </table>


## ISO19848 Message format

The Veracity Ingest SDK contains utility classes for how to generate ISO19848-format messages.
Veracity SDK is available as nuget package:

https://www.nuget.org/packages/Veracity.IoT.SDK.Models/


Note: ShipId is only necessary when sending data for several assets (platform to platform integration).
ShipId is IMO nr or DNVGL unique asset identifier.

When sending from an edge device on asset, the Header section can be removed. Hence, the connection string is unique per asset.

The ISO Message allows for either EventData or TabularData format. The difference between the two is that EventData allows for datapoints not occurring regularly. This means that EventData can report values on different timestamps for different tag id’s, whereas TabularData only reports values on the same timestamp for all tag id’s. 

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
You can send several datapoints with minimal overhead.  A data channel id is the tag id. You can add as many datasets as you want in “a package”. 
For the TabularData format ,the index of each value in the Value list must correspond to same index associated with the given value in the DataChannelId list. 
```json
{
"Header":
  {"ShipId":"12345"},
   "TimeSeriesData":
    {
	   "TabularData":
	     {		
		  "DataChannelId":["Tag1","Tagy","Tagx"],
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
	   
	

## Submit JSON  to IoT Hub

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
- HTTPS
- AMQP
- AMQP over WebSockets
- MQTT
- MQTT over WebSockets

If your solution cannot use the device libraries, devices can use the MQTT v3.1.1, HTTPS 1.1, or AMQP 1.0 protocols to connect natively to your hub.
- SDK: https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-sdks
- Communicate with your IoT hub using the MQTT protocol: https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-mqtt-support
