---
author: Benedikte Kallåk
description: Description of quick start section
---

# Veracity IoT Api

Only users that has access to an asset can access data from this asset.

The api is accessible from api-portal: https://api-portal.veracity.com/

https://api-portal.veracity.com/docs/services/DataFabric-TimeSeriesAPI/



## Api endpoints

Base url: https://api.veracity.com/veracity/timeseries/api

To sort the endpoints in similar matter as the table below, select the "group by tag" button.

<table border="1" width="100">
    <thead>
      <tr>	  
	    <th>GET/POST</th>
        <th>Asset endpoint</th>        
      </tr>
    </thead>
    <tbody>      
        <tr>
		    <td>GET</td>
            <td>/v1/Assets</td>                   
        </tr>
		  <tr>
		    <td>GET</td>
            <td>/v1/Assets</td>                  
        </tr>
		 <tr>           
            <td colspan=2>Returns the assets with assetguid specified if user has access to it and timeseries data is available.</td>                 
        </tr>
		  </tbody>
  </table>
  
  <table border="1" width="100">
    <thead>
      <tr>	  
	    <th>GET/POST</th>
        <th>DataChannelList endpoint</th>        
      </tr>
    </thead>
    <tbody>      
        <tr>
		    <td>GET</td>
            <td>/v1/DataChannelList{id}</td>                       
        </tr>		 
		 <tr>           
            <td colspan=2>List all metadata for all channels registered for this asset. When requesting timeseries data for selected datachannles use either shortid or UUID. </td>                 
        </tr>
		  </tbody>
  </table>
  
  
  <table border="1" width="100">
    <thead>
      <tr>	  
	    <th>GET/POST</th>
        <th>DataQuality endpoint</th>        
      </tr>
    </thead>
    <tbody>      
       		 <tr>
            <td>POST</td>
            <td>/v1/DataQuality/.timeseriesdata</td>                                        
        </tr>
		 <tr>           
            <td colspan=2>Returns dataquality measures for channels for selected time periode</td>                 
        </tr>
        <tr>
            <td>POST</td>
            <td>/v1/DataQuality/aggregate/.score</td>                          
        </tr>
		 <tr>           
            <td colspan=2>Returns aggregated dataquality score for assets for given time period</td>                 
        </tr>
		
		  <tr>
            <td>POST</td>
            <td>/v1/DataQuality/aggregate/.rulescore</td>          
        </tr>
		 <tr>           
            <td colspan=2>Returns aggregated dataquality score per data quality metric for selected period</td>                        
        </tr>
		
		  <tr>
            <td>POST</td>
            <td>/v1/DataQuality/aggregate/.channelscore</td>
                            
        </tr>
		 <tr>           
            <td colspan=2>Returns aggregated dataquality score per channel per data quality metric for selected period</td>                    
        </tr>
		
		  <tr>
            <td>POST</td>
            <td>/v1/DataQuality/trend/.score</td>
            
        </tr>
		 <tr>           
            <td colspan=2>Returns aggregations per week for data quality score in selected periode</td>                 
        </tr>
		
		
		  <tr>
            <td>POST</td>
            <td>/v1/DataQuality/trend/.rulescore</td>
                                 
        </tr>
		 <tr>           
            <td colspan=2><pre>Returns aggregations per week for
			each dataquality metric in selected period.</pre></td>             
        </tr>
		
		 <tr>
           <td colspan=2><pre>
			Start: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
			End: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
			Assetid: arrays of asset guids
			IncludePrevisousPeriod: returns rulescore for previous period (period with same length as specified)
			</pre></td>                          
        </tr>
  </tbody>
  </table>
  
  
<table border="1" width="100">
    <thead>
      <tr>	  
	    <th>GET/POST</th>
        <th>TimeSeriesData endpoint</th>   
  <th>div</th>   		
      </tr>
    </thead>
    <tbody>      
		
		 <tr>
            <td>GET</td>
            <td>/v1/Assets/{id}/DataChannels/{dataChannelId}/TimeSeriesData/.getRawData</td>
            <td>Returns raw data for given datachannel for given time periode defined by before or after offset (ISO-8601 date format: YYYY-MM-DDTHH:mm:ss.SSSZ) Include header if metadata is to be returned together with datapoins</td>
	      </tr>   
		   <tr>
            <td>GET</td>
            <td>/v1/Assets/{id}/DataChannels/{dataChannelId}/TimeSeriesData/.getDownSampledData</td>
            <td>Returns downsampled datapoints for given datachannel for given time periode defined by before or after offset (ISO-8601 date format: YYYY-MM-DDTHH:mm:ss.SSSZ). Use downScaleInterval to specify the interval. Include header if metadata is to be returned together with datapoints</td>
	      </tr>   
		  <tr>
            <td>POST</td>
            <td>/v1/TimeSeriesData/.getTimeSeriesData</td>
            <td>Returns timeseries data for a vessel or set of vessels</td>
	      </tr>   
		  <tr>
            <td></td>
            <td>Payload description:</td>
            <td><pre><var>downScaleInt:</var> specify downscaling interval. 
			Set to null if no downscaling.
			ISO8601 duration format.
			I.e. PT30S, PT1H, PT10M, PT60S
			  -<var>start, end:</var> date format using ISO8601 format YYYY-MM-DDThh:mm:ss.
			  For example, "2007-04-05T14:30Z"
		      -<var>Dimension:</var> set null if not used in ingest. 
			  -<var>dataChannelIdType:</var> Are you requesting channels by ShortId or DataChannelUuid 
			  -<var>dataChannelIds:</var> Array of channel ids. Use type specified in dataChannelIdType.
			  I.e. "AI030206", "AI030207", "AI030701"			 
			  -<var>includeStartBoundary/includeEndBoundary:</var> Set true/false depending of whether timestamps for boundaries should be included
			  -<var>assetIds</var> array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
			  -<var>limit</var> Max number of datapoints to be returned. System max limit is 200 000. 
			  -<var>typeOption</var> sddData/Data. 
			  sddData returns datapoints and metadata.
			  Data returs datapoints only </pre>
            </td>               
          </tr>                   
		  <tr>
            <td>POST</td>
            <td>/v1/TimeSeriesData/.latest</td>
            <td>Get the latest n-received values for given channels</td>
	     </tr>
		  <tr>
            <td></td>
            <td>Payload description:</td>
            <td><pre><var>Dimension</var> set null if not used in ingest. 
			  <var>dataChannelIdType</var>Are you requesting channels by ShortId or DataChannelUuid </pre>
			  <var>dataChannelIds</var> Array of channel ids. Use type specified in dataChannelIdType. I.e. "AI030206", "AI030207", "AI030701"			 			
			  <var>assetIds</var> array of guid of asset, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
			  <var>latestNValues</var> Max number of datapoints to be returned. 
			  <var>typeOption</var> sddData or Data. sddData returns datapoints and metadata, Data returs datapoints only </pre>
            </td>               
          </tr>          
           <tr>
            <td>POST</td>
            <td>..api/v1/TimeSeriesData/.time_range</td>
            <td>Returns min date and max date for received datapoints for selected channels</td>
	     </tr>		  
		   </tbody>
  </table>
  
   <table border="1" width="100">
    <thead>
      <tr>	  
	    <th>GET/POST</th>
        <th>Workspaces endpoint</th>    	
      </tr>
    </thead>
    <tbody>      		 
		 
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
    </tbody>
  </table>
  
  <table border="1" width="100">
    <thead>
      <tr>	  
	    <th>GET/POST</th>
        <th>Stored procedure endpoint</th>   
  <th>div</th>   		
      </tr>
    </thead>
    <tbody>      
		 
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







