---
author: Benedikte Kallåk
description: This section describes the different endpoints of the IoT Api
---

# Veracity IoT Api

Only users that has access to an asset can access data from this asset.

The api is accessible from [api-portal](https://api-portal.veracity.com/)

[/v1/Assets](#get-v1assets)



## Api endpoints

Base url: https://api.veracity.com/veracity/timeseries/api
To sort the endpoints in similar matter as the table below, select the "group by tag" button.

<div style="overflow-x: scroll;">
<table border="1" width="100%">
    <thead>
      <tr>	  
	    <th>GET/POST</th>
        <th>Endpoint</th>        
      </tr>
    </thead>
    <tbody>            
		<tr>
		    <td>GET</td>
            <td>[/v1/Assets](#get-v1assets)</td>                  
        </tr>
		<tr>
		    <td>GET</td>
            <td>[/v1/Assets/{id}](#get-/v1/assets)</td>                  
        </tr>
		<tr>
		    <td>GET</td>
            <td>/v1/DataChannelList/{id}</td>                  
        </tr>
		<tr>
		    <td>GET</td>
            <td>/v1/Assets/{id}/DataChannels/{dataChannelId}/TimeSeriesData/.getRawData</td>                  
        </tr>
		<tr>
		    <td>GET</td>
            <td>/v1/Assets/{id}/DataChannels/{dataChannelId}/TimeSeriesData/.getDownSampledData</td>                  
        </tr>
		<tr>
		    <td>POST</td>
            <td>/v1/TimeSeriesData/.getTimeSeriesData</td>                  
        </tr>
		<tr>
		    <td>POST</td>
            <td>/v1/TimeSeriesData/.getTimeSeriesData</td>                  
        </tr>
		 <tr>
            <td>POST</td>
            <td>/v1/TimeSeriesData/.latest</td>           
	     </tr>
		   <tr>
            <td>POST</td>
            <td>/v1/TimeSeriesData/.time_range</td>           
	     </tr>		  
		 <tr>
            <td>POST</td>
            <td>/v1/DataQuality/.timeseriesdata</td>                                        
        </tr>
		 <tr>
            <td>POST</td>
            <td>/v1/DataQuality/aggregate/.score</td>                          
        </tr>
		<tr>
            <td>POST</td>
            <td>/v1/DataQuality/aggregate/.rulescore</td>          
        </tr>
		<tr>
            <td>POST</td>
            <td>/v1/DataQuality/aggregate/.channelscore</td>                            
        </tr>
		<tr>
            <td>POST</td>
            <td>/v1/DataQuality/trend/.score</td>            
        </tr>
		 <tr>
            <td>POST</td>
            <td>/v1/DataQuality/trend/.rulescore</td>                                 
        </tr>
		 <tr>
            <td>GET</td>			 
            <td>/v1/Workspaces</td>
	    </tr>
        <tr>
            <td>GET</td>
            <td>/v1/Workspaces/{workspaceid}</td>
		 </tr>    		
    </tbody>
  </table>   
  </div>
		

### Assets

#### GET /v1/Assets
Returns all of the assets you have access to, for which timeseries data is available

#### GET /v1/Assets/{id}
Returns the asset with specified assetguid if user has access to it and timeseries data is available

### DataChannelList
#### GET /v1/DataChannelList/{id}
List all metadata for all channels registered for this asset.
When requesting timeseries data for selected datachannles use either shortid or UUID.

### TimeSeriesData

#### /v1/Assets/{id}/DataChannels/{dataChannelId}/TimeSeriesData/.getRawData
Returns raw data for given datachannel for given time periode defined by before or after offset. Response data is listed as EventData.
 * id: asset guid
 * dataChannelId: shortId of DataChannelUuid of datachannel.
 * offset: date format using ISO8601 format YYYY-MM-DDThh:mm:ss.  For example, "2007-04-05T14:30Z"
 ' before: true/false. Are you requesting data before or after the offset. Default is true
-<var>includeOffsetBoundary</var>: True/False. Include offset in query. Default is true
-<var>limit</var>: Max datapoints to retun. System limit is 200,000
-<var>header</var>: true/false. Set to true if metadata is to be returned together with datapoins. Default is false.


#### /v1/Assets/{id}/DataChannels/{dataChannelId}/TimeSeriesData/.getDownSampledData
Returns downsampled datapoints for given datachannel for given time periode defined by before or after offset. The interval to downsample, is given as parameter.
-<var>id</var>: asset guid
-<var>dataChannelId</var>: shortId of DataChannelUuid of datachannel.
-<var>offset</var>: date format using ISO8601 format YYYY-MM-DDThh:mm:ss.  For example, "2007-04-05T14:30Z"
-<var>before</var>: true/false. Are you requesting data before or after the offset. Default is true
-<var>includeOffsetBoundary</var>: True/False. Include offset in query. Default is true
-<var>limit</var>: Max datapoints to retun. System limit is 200,000
-<var>header</var>: true/false. Set to true if metadata is to be returned together with datapoins. Default is false.
-<var>downScaleInterval</var>: specify downscaling interval,  Set to null if no downscaling.
ISO8601 duration format. I.e. PT30S, PT1H, PT10M, PT60S


#### /v1/TimeSeriesData/.getTimeSeriesData
Returns timeseries data for a vessel or set of vessels by spesifying specifying paramters in a payload. 
Datapoits will be provided as tabularData with max, min and average if downscaling is used. If not; rawdata is listed as EventData.
<pre>
-<var>downScaleInt</var>: specify downscaling interval,  Set to null if no downscaling.ISO8601 duration format.I.e. PT30S, PT1H, PT10M, PT60S
-<var>start, end</var>: date format using ISO8601 format YYYY-MM-DDThh:mm:ss.  For example, "2007-04-05T14:30Z"
-<var>dimension</var>: set null if not used in ingest. 
-<var>dataChannelIdType</var>: Are you requesting channels by ShortId or DataChannelUuid 
-<var>dataChannelIds</var>: Array of channel ids. Use type specified in dataChannelIdType.  I.e. "AI030206", "AI030207", "AI030701"			 
-<var>includeStartBoundary/includeEndBoundary</var>: Set true/false depending of whether timestamps for boundaries should be included
-<var>assetIds</var>: array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
-<var>limit</var>: Max number of datapoints to be returned. System max limit is 200 000. 
-<var>typeOption</var>: sddData/Data. sddData returns datapoints and metadata, Data returs datapoints only 
</pre>

#### /v1/TimeSeriesData/.latest
Get the latest n-received values for given channels. datapoints in the response are listed as EventData.
<pre>
-<var>assetIds</var>: array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
-<var>dimension</var>: set null if not used in ingest. 
-<var>dataChannelIdType</var>: Are you requesting channels by ShortId or DataChannelUuid 
-<var>dataChannelIds</var>: Array of channel ids. Use type specified in dataChannelIdType.  I.e. "AI030206", "AI030207", "AI030701" 
</pre>

#### /v1/TimeSeriesData/.time_range
Returns min date and max date for received datapoints for selected channels
<pre>
-<var>assetIds</var>: array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
-<var>dimension</var>: set null if not used in ingest. 
-<var>dataChannelIdType</var>: Are you requesting channels by ShortId or DataChannelUuid 
-<var>dataChannelIds</var>: Array of channel ids. Use type specified in dataChannelIdType.  I.e. "AI030206", "AI030207", "AI030701" 
</pre>

### Data quality
#### /v1/DataQuality/.timeseriesdata
Returns dataquality measures for channels for selected time periode
<pre>
-<var>downScaleInt</var>: specify downscaling interval. Default is 1H, PT1H, ISO8601 duration format.I.e. PT30S, PT1H, PT10M, PT60S
-<var>start, end</var>: date format using ISO8601 format YYYY-MM-DDThh:mm:ss.  For example, "2007-04-05T14:30Z"
-<var>rules</var>: name of rules to check
-<var>dataChannelIdType</var>: Are you requesting channels by ShortId or DataChannelUuid 
-<var>dataChannelIds</var>: Array of channel ids. Use type specified in dataChannelIdType.  I.e. "AI030206", "AI030207", "AI030701"			 
-<var>includeStartBoundary/includeEndBoundary</var>: Set true/false depending of whether timestamps for boundaries should be included
-<var>assetIds</var>: array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
-<var>limit</var>: Max number of datapoints to be returned. System max limit is 200 000. 
-<var>typeOption</var>: sddData/Data. sddData returns datapoints and metadata, Data returs datapoints only
</pre>

#### /v1/DataQuality/aggregate/.score
Returns aggregated dataquality score for assets for given time period
<pre>
-<var>start</var>: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
-<var>end</var>: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
-<var>assetIds</var>: arrays of asset guids
-<var>includePreviousPeriod</var>: returns rulescore for previous period (period with same length as specified by start and end)
</pre>

#### /v1/DataQuality/aggregate/.rulescore
Returns aggregated dataquality score per data quality metric for selected period
<pre>
-<var>start</var>: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
-<var>end</var>: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
-<var>assetIds</var>: arrays of asset guids
-<var>includePreviousPeriod</var>: returns rulescore for previous period (period with same length as specified by start and end)</pre>

#### /v1/DataQuality/aggregate/.channelscore</td>                            
Returns aggregated dataquality score per channel per data quality metric for selected period
<pre>
-<var>start</var>: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
-<var>end</var>: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
-<var>assetIds</var>: arrays of asset guids
-<var>includePreviousPeriod</var>: returns rulescore for previous period (period with same length as specified by start and end)
</pre>


#### /v1/DataQuality/trend/.score</td>            
Returns aggregations per week for data quality score in selected periode
<pre>
-<var>start</var>: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
-<var>end</var>: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
-<var>assetIds</var>: arrays of asset guids
-<var>includePreviousPeriod</var>: returns rulescore for previous period (period with same length as specified by start and end)
</pre>    			


#### /v1/DataQuality/trend/.rulescore</td>                                 
 Returns aggregations per week for each dataquality metric in selected period.        
 <pre>
-<var>start</var>: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
-<var>end</var>: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
-<var>assetIds</var>: arrays of asset guids
-<var>includePreviousPeriod</var>: returns rulescore for previous period (period with same length as specified by start and end)
</pre>                              


### Workspaces
Returns Asset Connect workspaces user has access to

#### /v1/Workspaces/{workspaceid}
Returns the workspace by id, and the assets (if any) in the workspace which have IoT Data enabled.</td>

### StoredProcedure
#### /v1/StoredProcedure/{name}		
Stored procedures can be used for custom queries. Must me managed by Veracity administrators


