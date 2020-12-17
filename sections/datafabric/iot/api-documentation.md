---
author: Benedikte Kallåk
description: This section describes the different endpoints of the IoT Api
---

# Veracity IoT Api

Only users that has access to an asset can access data from this asset.

The api is accessible from api-portal: https://api-portal.veracity.com/

https://api-portal.veracity.com/docs/services/DataFabric-TimeSeriesAPI/



## Api endpoints

Base url: https://api.veracity.com/veracity/timeseries/api

To sort the endpoints in similar matter as the table below, select the "group by tag" button.

<table border="1" width="100%">
    <thead>
      <tr>	  
	    <th>GET/POST</th>
        <th>Endpoint</th>        
      </tr>
    </thead>
    <tbody>      
        <tr>		   
            <td colspan=2>Assets</td>                   
        </tr>
		<tr>
		    <td>GET</td>
            <td>/v1/Assets</td>                  
        </tr>
		 <tr>           
            <td colspan=2>Returns all of the assets you have access to, for which timeseries data is available</td>                 
        </tr>		
		<tr>
		    <td>GET</td>
            <td>/v1/Assets/{id}</td>                  
        </tr>
		 <tr>           
            <td colspan=2>Returns the asset with specified assetguid if user has access to it and timeseries data is available.</td>                 
        </tr>		
		<tr >           
            <td colspan=2>DataChannelList</td>                 
        </tr>		
        <tr>
		    <td>GET</td>
            <td>/v1/DataChannelList{id}</td>                       
        </tr>		 
		 <tr>           
            <td colspan=2><pre>List all metadata for all channels registered for this asset.
When requesting timeseries data for selected datachannles use either shortid or UUID. </pre></td>                 
        </tr>		
		<tr >           
            <td colspan=2>TimeSeriesData</td>                 
        </tr>
		 <tr>
            <td>GET</td>
            <td>/v1/Assets/{id}/DataChannels/{dataChannelId}/TimeSeriesData/.getRawData</td>
	     </tr>
         <tr>
		     <td colspan=2><pre>Returns raw data for given datachannel for given time periode defined by before or after offset.
Data is listed as EventData.
-<var>id</var>: asset guid
-<var>dataChannelId</var>: shortId of DataChannelUuid of datachannel.
-<var>offset</var>: date format using ISO8601 format YYYY-MM-DDThh:mm:ss.  For example, "2007-04-05T14:30Z"
-<var>before</var>: true/false. Are you requesting data before or after the offset. Default is true
-<var>includeOffsetBoundary</var>: True/False. Include offset in query. Default is true
-<var>limit</var>: Max datapoints to retun. System limit is 200,000
-<var>header</var>: true/false. Set to true if metadata is to be returned together with datapoins. Default is false.</pre></td>
	      </tr>   
		   <tr>
            <td>GET</td>
            <td>/v1/Assets/{id}/DataChannels/{dataChannelId}/TimeSeriesData/.getDownSampledData</td>
			</tr>
		 <tr>           
            <td colspan=2><pre>Returns downsampled datapoints for given datachannel for given time periode defined by before or after offset. 
-<var>id</var>: asset guid
-<var>dataChannelId</var>: shortId of DataChannelUuid of datachannel.
-<var>offset</var>: date format using ISO8601 format YYYY-MM-DDThh:mm:ss.  For example, "2007-04-05T14:30Z"
-<var>before</var>: true/false. Are you requesting data before or after the offset. Default is true
-<var>includeOffsetBoundary</var>: True/False. Include offset in query. Default is true
-<var>limit</var>: Max datapoints to retun. System limit is 200,000
-<var>header</var>: true/false. Set to true if metadata is to be returned together with datapoins. Default is false.
-<var>downScaleInterval</var>: specify downscaling interval,  Set to null if no downscaling.ISO8601 duration format.I.e. PT30S, PT1H, PT10M, PT60S</pre></td>
	      </tr>   
		  <tr>
            <td>POST</td>
            <td>/v1/TimeSeriesData/.getTimeSeriesData</td>
	     </tr>
		 <tr>
            <td colspan=2><pre>Returns timeseries data for a vessel or set of vessels by spesifying channel ids. 
Datapoits will be provided as tabularData with max, min and average if downscaling is used. If not; rawdata is listed as EventData.
-<var>downScaleInt</var>: specify downscaling interval,  Set to null if no downscaling.ISO8601 duration format.I.e. PT30S, PT1H, PT10M, PT60S
-<var>start, end</var>: date format using ISO8601 format YYYY-MM-DDThh:mm:ss.  For example, "2007-04-05T14:30Z"
-<var>dimension</var>: set null if not used in ingest. 
-<var>dataChannelIdType</var>: Are you requesting channels by ShortId or DataChannelUuid 
-<var>dataChannelIds</var>: Array of channel ids. Use type specified in dataChannelIdType.  I.e. "AI030206", "AI030207", "AI030701"			 
-<var>includeStartBoundary/includeEndBoundary</var>: Set true/false depending of whether timestamps for boundaries should be included
-<var>assetIds</var>: array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
-<var>limit</var>: Max number of datapoints to be returned. System max limit is 200 000. 
-<var>typeOption</var>: sddData/Data. sddData returns datapoints and metadata, Data returs datapoints only </pre></td>               
          </tr>                   
		  <tr>
            <td>POST</td>
            <td>/v1/TimeSeriesData/.latest</td>           
	     </tr>
		  <tr>         
            <td colspan=2><pre>Get the latest n-received values for given channels. Data is listed as EventData.
-<var>dimension</var> set null if not used in ingest. 
-<var>dataChannelIdType</var>: Are you requesting channels by ShortId or DataChannelUuid
-<var>dataChannelIds</var>: Array of channel ids. Use type specified in dataChannelIdType. I.e. "AI030206", "AI030207", "AI030701"			 			
-<var>assetIds</var>: array of guid of asset, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
-<var>latestNValues</var>: Max number of datapoints to be returned. 
-<var>typeOption</var> sddData or Data. sddData returns datapoints and metadata, Data returs datapoints only </pre></td>               
          </tr>          
           <tr>
            <td>POST</td>
            <td>..api/v1/TimeSeriesData/.time_range</td>           
	     </tr>		  
		 <tr>
		  <td colspan = 2><pre>Returns min date and max date for received datapoints for selected channels
-<var>assetIds</var>: array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
-<var>dimension</var>: set null if not used in ingest. 
-<var>dataChannelIdType</var>: Are you requesting channels by ShortId or DataChannelUuid 
-<var>dataChannelIds</var>: Array of channel ids. Use type specified in dataChannelIdType.  I.e. "AI030206", "AI030207", "AI030701" </pre></td>
		 </tr>		 
		 <tr>           
            <td colspan=2>DataQuality endpoint </td>                 
        </tr>	  
  		 <tr>
            <td>POST</td>
            <td>/v1/DataQuality/.timeseriesdata</td>                                        
        </tr>
		 <tr>           
            <td colspan=2><pre>Returns dataquality measures for channels for selected time periode
-<var>downScaleInt</var>: specify downscaling interval. Default is 1H, PT1H, ISO8601 duration format.I.e. PT30S, PT1H, PT10M, PT60S
-<var>start, end</var>: date format using ISO8601 format YYYY-MM-DDThh:mm:ss.  For example, "2007-04-05T14:30Z"
-<var>rules</var>: name of rules to check
-<var>dataChannelIdType</var>: Are you requesting channels by ShortId or DataChannelUuid 
-<var>dataChannelIds</var>: Array of channel ids. Use type specified in dataChannelIdType.  I.e. "AI030206", "AI030207", "AI030701"			 
-<var>includeStartBoundary/includeEndBoundary</var>: Set true/false depending of whether timestamps for boundaries should be included
-<var>assetIds</var>: array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
-<var>limit</var>: Max number of datapoints to be returned. System max limit is 200 000. 
-<var>typeOption</var>: sddData/Data. sddData returns datapoints and metadata, Data returs datapoints only</pre></td>                 
        </tr>
        <tr>
            <td>POST</td>
            <td>/v1/DataQuality/aggregate/.score</td>                          
        </tr>
		 <tr>           
            <td colspan=2><pre>Returns aggregated dataquality score for assets for given time period
-<var>start</var>: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
-<var>end</var>: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
-<var>assetIds</var>: arrays of asset guids
-<var>includePreviousPeriod</var>: returns rulescore for previous period (period with same length as specified by start and end)</pre></td>                 
        </tr>		
		<tr>
            <td>POST</td>
            <td>/v1/DataQuality/aggregate/.rulescore</td>          
        </tr>
		 <tr>           
            <td colspan=2><pre>Returns aggregated dataquality score per data quality metric for selected period
-<var>start</var>: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
-<var>end</var>: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
-<var>assetIds</var>: arrays of asset guids
-<var>includePreviousPeriod</var>: returns rulescore for previous period (period with same length as specified by start and end)</pre></td>                            
        </tr>		
		<tr>
            <td>POST</td>
            <td>/v1/DataQuality/aggregate/.channelscore</td>                            
        </tr>
		 <tr>           
            <td colspan=2><pre>Returns aggregated dataquality score per channel per data quality metric for selected period
-<var>start</var>: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
-<var>end</var>: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
-<var>assetIds</var>: arrays of asset guids
-<var>includePreviousPeriod</var>: returns rulescore for previous period (period with same length as specified by start and end)</pre></td>    			
        </tr>
		<tr>
            <td>POST</td>
            <td>/v1/DataQuality/trend/.score</td>            
        </tr>
		 <tr>           
            <td colspan=2><pre>Returns aggregations per week for data quality score in selected periode
-<var>start</var>: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
-<var>end</var>: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
-<var>assetIds</var>: arrays of asset guids
-<var>includePreviousPeriod</var>: returns rulescore for previous period (period with same length as specified by start and end)</pre></td>    			
        </tr>	
		 <tr>
            <td>POST</td>
            <td>/v1/DataQuality/trend/.rulescore</td>                                 
        </tr>
		 <tr>           
            <td colspan=2><pre>Returns aggregations per week for each dataquality metric in selected period.        
-<var>start</var>: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
-<var>end</var>: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
-<var>assetIds</var>: arrays of asset guids
-<var>includePreviousPeriod</var>: returns rulescore for previous period (period with same length as specified by start and end)</pre></td>                              
        </tr>      	
	<tr>           
            <td colspan=2>Workspaces</td>                 
        </tr> 
		  <tr>
            <td>GET</td>			 
            <td>/v1/Workspaces</td>
	    </tr>     
		 <tr>
		    <td colspan=2>Returns Asset Connect workspaces user has access to</td>
	     </tr>
		  <tr>
            <td>GET</td>
            <td>/v1/Workspaces/{workspaceid}</td>
		 </tr>     
		 <tr>
		    <td colspan=2>Returns the workspace by id, and the assets (if any) in the workspace which have IoT Data enabled.</td>
	     </tr>		 
     	<tr>           
            <td colspan=2 style="background-color:orange">StoredProcedure</td>                 
        </tr> 
		  <tr>
            <td>GET</td>
            <td>/v1/StoredProcedure/{name}</td>         
	     </tr>
		  <tr>
		    <td colspan=2>Stored procedures can be used for custom queries.</td>               
        </tr>
		   </tbody>
  </table>   
  

Stored Procedures	
Can be used to set up special queries	Custom by Veracity administrators
	


## Subscribe to API

data can be accessed uoing veracity IoT api. The API is managed by Azure API management and hence you need a subscription. 
1.	Go to Veracity api portal: https://api-portal.veracity.com/
2.	Sign in
3.	Select Product
4.	Select Veracity Platform API. This api contains all the Veracity platform APIs which allow you to integrate with platform and enjoy the platform features by calling related API, it contains all the legacy "My service API" and "Data fabric API".
5.	Select Subscribe
6.	After subscription, your access keys are available from Products
 
 
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
10. Fill in required parameters in payload and select SEND

## Use api from application

You need client credentials from Veracity for this.

### C# SDK
Our SDK 

### Python SDK







