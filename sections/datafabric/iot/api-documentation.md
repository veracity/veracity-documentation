---
author: Benedikte Kallåk
description: This section describes the different endpoints of the IoT Api
---
# Veracity IoT Api
The api is accessible from [api-portal](https://api-portal.veracity.com/)
To group the endpoints, select the "group by tag" button.

## Security Model
Only users that has access to an asset can access data from this asset.

## Api endpoints

Base url: https://api.veracity.com/veracity/timeseries/api

* [GET /v1/Assets](#get-v1assets)
* [GET /v1/Assets/{id}](#get-get-v1assetsid)
* [GET /v1/DataChannelList/{id}](#get-v1datachannellistid)
* [GET /v1/Assets/{id}/DataChannels/{dataChannelId}/TimeSeriesData/.getRawData](#v1assetsiddatachannelsdatachannelidtimeseriesdatagetdownsampleddata)
* [GET /v1/Assets/{id}/DataChannels/{dataChannelId}/TimeSeriesData/.getDownSampledData]()
* [POST /v1/TimeSeriesData/.getTimeSeriesData](#v1timeseriesdatagettimeseriesdata)
* [POST /v1/TimeSeriesData/.latest](#v1timeseriesdatalatest)
* [POST /v1/TimeSeriesData/.time_range](#v1timeseriesdatatime_range)
* [POST /v1/DataQuality/.timeseriesdata]#v1dataqualitytimeseriesdata)
* [POST /v1/DataQuality/aggregate/.score](#v1dataqualityaggregatescore)
* [POST /v1/DataQuality/aggregate/.rulescore](#v1dataqualityaggregaterulescore)
* [POST /v1/DataQuality/aggregate/.channelscore](#v1dataqualityaggregatechannelscore)
* [POST /v1/DataQuality/trend/.score](#v1dataqualitytrendscore)
* [POST /v1/DataQuality/trend/.rulescore](#v1dataqualitytrendrulescore)
* [GET /v1/Workspaces](#v1workspacesworkspaces)
* [GET /v1/Workspaces/{workspaceid}](#v1workspacesworkspaceid)
  	
### Assets

#### GET /v1/Assets
Returns all of the assets you have access to, for which timeseries data is available

#### GET /v1/Assets/{id}
Returns the asset with specified assetguid if user has access to it and timeseries data is available
* assetIds: asset guid

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
 * before: true/false. Are you requesting data before or after the offset. Default is true
 * includeOffsetBoundary: True/False. Include offset in query. Default is true
 * limit: Max datapoints to retun. System limit is 200,000
 * header: true/false. Set to true if metadata is to be returned together with datapoins. Default is false.

#### /v1/Assets/{id}/DataChannels/{dataChannelId}/TimeSeriesData/.getDownSampledData
Returns downsampled datapoints for given datachannel for given time periode defined by before or after offset. The interval to downsample, is given as parameter.
* id: asset guid
* dataChannelId: shortId of DataChannelUuid of datachannel.
* offset: date format using ISO8601 format YYYY-MM-DDThh:mm:ss.  For example, "2007-04-05T14:30Z"
* before: true/false. Are you requesting data before or after the offset. Default is true
* includeOffsetBoundary: True/False. Include offset in query. Default is true
* limit: Max datapoints to retun. System limit is 200,000
* header: true/false. Set to true if metadata is to be returned together with datapoins. Default is false.
* downScaleInterval: specify downscaling interval,  Set to null if no downscaling. ISO8601 duration format. I.e. PT30S, PT1H, PT10M, PT60S

#### /v1/TimeSeriesData/.getTimeSeriesData
Returns timeseries data for a vessel or set of vessels by spesifying specifying paramters in a payload. 
Datapoits will be provided as tabularData with max, min and average if downscaling is used. If not; rawdata is listed as EventData.

* downScaleInt: specify downscaling interval,  Set to null if no downscaling.ISO8601 duration format.I.e. PT30S, PT1H, PT10M, PT60S
* start, end: date format using ISO8601 format YYYY-MM-DDThh:mm:ss.  For example, "2007-04-05T14:30Z"
* dimension: set null if not used in ingest. 
* dataChannelIdType: Are you requesting channels by ShortId or DataChannelUuid 
* dataChannelIds: Array of channel ids. Use type specified in dataChannelIdType.  I.e. "AI030206", "AI030207", "AI030701"			 
* includeStartBoundary/includeEndBoundary: Set true/false depending of whether timestamps for boundaries should be included
* assetIds: array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
* limit: Max number of datapoints to be returned. System max limit is 200 000. 
* typeOption: sddData/Data. sddData returns datapoints and metadata, Data returs datapoints only 


#### /v1/TimeSeriesData/.latest
Get the latest n-received values for given channels. datapoints in the response are listed as EventData.

* assetIds: array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
* dimension: set null if not used in ingest. 
* dataChannelIdType: Are you requesting channels by ShortId or DataChannelUuid 
* dataChannelIds: Array of channel ids. Use type specified in dataChannelIdType.  I.e. "AI030206", "AI030207", "AI030701" 


#### /v1/TimeSeriesData/.time_range
Returns min date and max date for received datapoints for selected channels

* assetIds: array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
* dimension: set null if not used in ingest. 
* dataChannelIdType: Are you requesting channels by ShortId or DataChannelUuid 
* dataChannelIds: Array of channel ids. Use type specified in dataChannelIdType.  I.e. "AI030206", "AI030207", "AI030701" 


### Data quality
#### /v1/DataQuality/.timeseriesdata
Returns dataquality measures for channels for selected time periode

* downScaleInt: specify downscaling interval. Default is 1H (i.e. PT1H). ISO8601 duration format.I.e. PT30S, PT1H, PT10M, PT60S
* start, end: date format using ISO8601 format YYYY-MM-DDThh:mm:ss.  For example, "2007-04-05T14:30Z"
* rules: name of rules to check
* dataChannelIdType: Are you requesting channels by ShortId or DataChannelUuid 
* dataChannelIds: Array of channel ids. Use type specified in dataChannelIdType.  I.e. "AI030206", "AI030207", "AI030701"			 
* includeStartBoundary/includeEndBoundary: Set true/false depending of whether timestamps for boundaries should be included
* assetIds: array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
* limit: Max number of datapoints to be returned. System max limit is 200 000. 
* typeOption: sddData/Data. sddData returns datapoints and metadata, Data returs datapoints only


#### /v1/DataQuality/aggregate/.score
Returns aggregated dataquality score for assets for given time period

* start: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
* end: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
* assetIds: arrays of asset guids
* includePreviousPeriod: returns rulescore for previous period (period with same length as specified by start and end)


#### /v1/DataQuality/aggregate/.rulescore
Returns aggregated dataquality score per data quality metric for selected period

* start: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
* end: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
* assetIds: arrays of asset guids
* includePreviousPeriod: returns rulescore for previous period (period with same length as specified by start and end)

#### /v1/DataQuality/aggregate/.channelscore</td>                            
Returns aggregated dataquality score per channel per data quality metric for selected period

* start: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
* end: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
* assetIds: arrays of asset guids
* includePreviousPeriod: returns rulescore for previous period (period with same length as specified by start and end)

#### /v1/DataQuality/trend/.score</td>            
Returns aggregations per week for data quality score in selected periode

* start: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
* end: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
* assetIds: arrays of asset guids
* includePreviousPeriod: returns rulescore for previous period (period with same length as specified by start and end)
    			
#### /v1/DataQuality/trend/.rulescore</td>                                 
 Returns aggregations per week for each dataquality metric in selected period.        
 
* start: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
* end: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
* assetIds: arrays of asset guids
* includePreviousPeriod: returns rulescore for previous period (period with same length as specified by start and end)
                            
### Workspaces
Returns Asset Connect workspaces user has access to

#### /v1/Workspaces
Returns workspaces user has access to

#### /v1/Workspaces/{workspaceid}
Returns the workspace by id, and the assets (if any) in the workspace which have IoT Data enabled.</td>

### StoredProcedure
#### /v1/StoredProcedure/{name}		
Stored procedures can be used for custom queries. Must me managed by Veracity administrators


