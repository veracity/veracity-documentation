---
author: Benedikte Kallåk
description: Description of quick start section
---

# Veracity IoT Api

Only users that has access to an asset can access data from this asset.

The api is accessible from api-portal: https://api-portal.veracity.com/

https://api-portal.veracity.com/docs/services/DataFabric-TimeSeriesAPI/



## Api endpoints

Base url: https://api.veracity.com/veracity/timeseries/

To sort the endpoints in similar matter as the table below, select the "group by tag" button.

<table>
    <thead>
      <tr>	  
	    <th>GET/POST</th>
        <th>Endpoint</th>
        <th>Comment</th>       
      </tr>
    </thead>
    <tbody>
        <tr >
		    <td colspan=3>"Asset"</td>               
        </tr>
        <tr>
		    <td>GET</td>
            <td>..api/v1/Assets</td>
            <td>Returns all of the assets you have access to, for which timeseries data is available. The response contains an id; use this id in asset specific requests</td>            
        </tr>
		 <tr>
            <td>GET</td>
            <td>..api/v1/Assets{id}</td>
            <td>Returns the assets with assetguid specified if user has access to it and timeseries data is available.</td>                 
        </tr>
		 <tr >
		    <td colspan=3>"DataChannelList"</td>               
        </tr>
        <tr>
           <td>GET</td>
            <td>..api/v1/DataChannelList{id}</td>
            <td>List all metadata for all channels registered for this asset. When requesting timeseries data for selected datachannles use either shortid or UUID. </td>                               
        </tr>
		 <tr>
		    <td colspan=3>"DataQuality"</td>               
        </tr>
		 <tr>
            <td>POST</td>
            <td>..api/v1/dataquality</td>
            <td>Returns aggregated dataquality calculations for requested assets</td>                               
        </tr>
        <tr>
            <td>POST</td>
            <td>..api/v1/dataquality</td>
            <td>Returns all of the assets you have access to, for which timeseries data is available. The response contians an id; use this id in asset specific requests</td>                          
        </tr>
		  <tr>
            <td>POST</td>
            <td>..api/v1/dataquality</td>
            <td>Returns all of the assets you have access to, for which timeseries data is available. The response contians an id; use this id in asset specific requests</td>                          
        </tr>
		  <tr>
            <td>POST</td>
            <td>..api/v1/dataquality</td>
            <td>Returns all of the assets you have access to, for which timeseries data is available. The response contians an id; use this id in asset specific requests</td>                          
        </tr>
		  <tr>
            <td>POST</td>
            <td>..api/v1/dataquality</td>
            <td>Returns all of the assets you have access to, for which timeseries data is available. The response contians an id; use this id in asset specific requests</td>                          
        </tr>
		  <tr>
            <td>POST</td>
            <td>..api/v1/dataquality</td>
            <td>Returns all of the assets you have access to, for which timeseries data is available. The response contians an id; use this id in asset specific requests</td>                          
        </tr>
		 <tr>
		    <td colspan=3>"TimeSeriesData"</td>               
        </tr>
		  <tr>
            <td>POST</td>
            <td>..api/v1/TimeSeriesData/.getTimeSeriesData</td>
            <td>Returns timeseries data for a vessel or set of vessels
			payload: {
  "downScaleInt": "PT30S",
  "start": "2020-06-29T14:34:00.000Z",
  "end": "2020-06-30T17:10:00.000Z",
  "dimension": null,
  "limit": 5000,
  "dataChannelIdType": "ShortId",
  "includeStartBoundary": true,
  "includeEndBoundary": true,
  "assetIds": [
    "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724"
  ],
  "dataChannelIds": [
    "AI030206", "AI030207", "AI030701"
  ],
  "typeOption": "SddData"
}</td>               
</tr>           
        
		<tr>
            <td>POST</td>
            <td>..api/v1/TimeSeriesData/.latest</td>
            <td>Get the latest n-received values for given channels</td>
	</tr>
    </tbody>
  </table>
  
  
  

Returns timeseries data for a vessel or set of vessels
Data is downscaled to interval specified in Post message

•	downScaleInt: Use  ISO8601 timespan for downscale interval
•	start: from date
•	end: to date
•	dimensions: Only to be used when this is configured in ingest. Default “” (empty string)
•	limit: max nr of datarows to get
•	dataChannelIdType: Are you requesting channels by ShortId or DataChannelUuid
•	includeStartBoundary: from and including start date
•	includeEndBoundary: Until and including end date
•	assetsIds: If more than one use , (“1212”, “3243”)
•	dataChannelIds: shortId or Uuid
•	typeOption: 
Sdd: metadataonly
sddData: metadata and data
Data: data only

POST
https://api.veracity.com/veracity/timeseries/api/v1/TimeSeriesData/.latest

{
  "dimension": "",
  "latestNValues": 50,
  "dataChannelIdType": "ShortId",
  "assetIds": [
    "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724"
  ],
  "dataChannelIds": [
    "AI030206"
  ],
  "typeOption": "Data"
}	Get the latest received values for given channels

•	dimensions: Only to be used when this is configured in ingest. Default “” (empty string)
•	latestNValues: no of latest values
•	dataChannelIdType: Are you requesting channels by ShortId or DataChannelUuid
•	assetsIds: If more than one use , (“1212”, “3243”)
•	dataChannelIds: shortId or Uuid
•	typeOption: 
Sdd: metadataonly
sddData: metadata and data
Data: data only

POST
v1/TimeSeriesData/.time_range	Returns min date and max date for received data for a channel
Currently only to be used when dimensions is used in ingest
Stored Procedures	
Can be used to set up special queries	Custom by Veracity administrators
	


## Subscribe to API

Our API is managed by Azure API management and hence you need 
1.	Ingested data can be accessed using Veracity IOT api.
2.	Go to Veracity api portal: https://api-portal.veracity.com/
3.	Sign in
4.	Select Product
5.	Select Veracity Platform API. This api contains all the Veracity platform APIs which allow you to integrate with platform and enjoy the platform features by calling related API, it contains all the legacy "My service API" and "Data fabric API".
6.	Select Subscribe
7.	After subscription, your access keys are available from
 
 
## Test api from portal.	

1.  Go to https://api-portal.veracity.com/
2.	Sign in
3.	Select API
4.	Select Data Fabric Time Series API
5.	Select Group  by Tag
6.	Select an endpoint – i.e https://api.veracity.com/veracity/timeseries/api/v1/Assets
7.	Select Try It
8.	If you are  signed in Ocp-Apim keys are filled out.  This is the key you can get from subscription key described above
9.	Select Authorization code from Authorization 






