---
author: Benedikte Kallåk
description: This section describes the different endpoints of the IoT Api
---
# Veracity IoT Api
The api is accessible from [api-portal](https://api-portal.veracity.com/). To group the endpoints in api-portal, select the "group by tag" button.
- Select api: *Data Fabric Time Series API*
- Base url: *https://api.veracity.com/veracity/timeseries/api/*

## Security Model
Only users that has access to an asset can access data from this asset.


## Asset metadata

* [GET /v1/Assets](#get-v1assets)
* [GET /v1/Assets/{id}](##get-v1assetsid)
* [GET /v1/DataChannelList/{id}](#get-v1datachannellistid)

## Timeseries data
* [GET /v1/Assets/{id}/DataChannels/{dataChannelId}/TimeSeriesData/ .getRawData](#get-v1assetsiddatachannelsdatachannelidtimeseriesdatagetdownsampleddata)
* [GET /v1/Assets/{id}/DataChannels/{dataChannelId}/TimeSeriesData/ .getDownSampledData](#get-v1assetsiddatachannelsdatachannelidtimeseriesdatagetdownsampleddata)
* [POST /v1/TimeSeriesData/.getTimeSeriesData](#post-v1timeseriesdatagettimeseriesdata)
* [POST /v1/TimeSeriesData/.latest](#post-v1timeseriesdatalatest)
* [POST /v1/TimeSeriesData/.time_range](#post-v1timeseriesdatatime_range)
* [POST /v1/DataQuality/.timeseriesdata](#post-v1dataqualitytimeseriesdata)

## Data Quality
* [POST /v1/DataQuality/aggregate/.score](#post-v1dataqualityaggregatescore)
* [POST /v1/DataQuality/aggregate/.rulescore](#post-v1dataqualityaggregaterulescore)
* [POST /v1/DataQuality/aggregate/.channelscore](#post-v1dataqualityaggregatechannelscore)
* [POST /v1/DataQuality/trend/.score](#post-v1dataqualitytrendscore)
* [POST /v1/DataQuality/trend/.rulescore](#post-v1dataqualitytrendrulescore)

## Workspace
* [GET /v1/Workspaces](#get-v1workspaces)
* [GET /v1/Workspaces/{workspaceid}](#get-v1workspacesworkspaceid)
  	
## Asset metadata
## GET /v1/Assets
Returns all of the assets you have access to, for which timeseries data is available
Request url:  https://api.veracity.com/veracity/timeseries/api/v1/Assets

## GET /v1/Assets/{id}
Returns the asset with specified assetguid if user has access to it and timeseries data is available
* id: asset guid

## GET DataChannelList
#### GET /v1/DataChannelList/{id}
List all metadata for data-channels registered for this asset that the user has access to.  Inaccessible channels, based on permissions, are filtered out.
* id: asset guid

## TimeSeriesData

### GET /v1/Assets/{id}/DataChannels/{dataChannelId}/TimeSeriesData/.getRawData
Returns raw data for given data-channel for given time period defined by before or after the offset. Response data is listed as EventData.
 * id: asset guid
 * dataChannelId: shortId of DataChannelUuid of datachannel.
 * offset: Relative point in time to either start from or end at the requested timeseries data. Date format using ISO8601 format YYYY-MM-DDThh:mm:ss.  For example, "2007-04-05T14:30Z"
 * before: logical (true/false), if true then the timeseries will end at the offset, if false the timeseries will start from the offset.
 * includeOffsetBoundary: True/False. Include offset in query. Default is true
 * limit: Max datapoints to return. System limit is 200,000
 * header: true/false. Set to true if metadata is to be returned together with datapoints. Default is false.

### GET /v1/Assets/{id}/DataChannels/{dataChannelId}/TimeSeriesData/.getDownSampledData
If high resolution of data is not required or can be traded off for less dense data (and performance benefits) this is the recommended way of getting timeseries.
Essentially the timeseries is binned by the duration specified in the parameter and the min/max/average of the data per bin is returned.
Returns downsampled datapoints for given datachannel for given time period defined by before or after offset. The interval to downsample, is given in request payload. Response data is listed as TabularData.
* id: asset guid
* dataChannelId: shortId of DataChannelUuid of datachannel.
* offset: Relative point in time to either start from or end at the requested timeseries data. Date format using ISO8601 format YYYY-MM-DDThh:mm:ss.  For example, "2007-04-05T14:30Z"
* before: logical (true/false), if true then the timeseries will end at the offset, if false the timeseries will start from the offset. Default is true
* includeOffsetBoundary: True/False. Include offset in query. Default is true
* limit: Max datapoints to return. System limit is 200,000
* header: true/false. Set to true if metadata is to be returned together with datapoints. Default is false.
* downScaleInterval: specify downscaling interval. Set to null if no downscaling. ISO8601 duration format. I.e. PT30S, PT1H, PT10M, PT60S

### POST /v1/TimeSeriesData/.getTimeSeriesData
Returns timeseries data for a set of datachannels on an asset (or set of assets) by specifying request payload. 
Response data will be provided as TabularData with max, min and average if downscaling is used. If not; rawdata is listed as EventData.

* downScaleInt: specify downscaling interval,  Set to null if no downscaling.ISO8601 duration format. I.e. PT30S, PT1H, PT10M, PT60S
* start, end: date format using ISO8601 format YYYY-MM-DDThh:mm:ss.  For example, "2007-04-05T14:30Z"
* dimension: set null if not used in ingest. 
* dataChannelIdType: Are you requesting channels by ShortId or DataChannelUuid 
* dataChannelIds: Array of channel ids. Use type specified in dataChannelIdType.  I.e. "AI030206", "AI030207", "AI030701"			 
* includeStartBoundary/includeEndBoundary: Set true/false depending of whether timestamps for boundaries should be included
* assetIds: array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
* limit: Max number of datapoints to be returned. System max limit is 200 000. 
* typeOption: sddData/Data. sddData returns datapoints and metadata, Data returns datapoints only. 


### POST /v1/TimeSeriesData/.latest
Get the latest n-received values for given channels. Datapoints in the response are listed as EventData.

* assetIds: array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
* dimension: set null if not used in ingest. 
* dataChannelIdType: Are you requesting channels by ShortId or DataChannelUuid 
* dataChannelIds: Array of channel ids. Use type specified in dataChannelIdType.  I.e. "AI030206", "AI030207", "AI030701" 


### POST /v1/TimeSeriesData/.time_range
Returns min date and max date for received datapoints for selected channels

* assetIds: array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
* dimension: set null if not used in ingest. 
* dataChannelIdType: Are you requesting channels by ShortId or DataChannelUuid 
* dataChannelIds: Array of channel ids. Use type specified in dataChannelIdType.  I.e. "AI030206", "AI030207", "AI030701" 


## Data quality

### /v1/DataQuality/.timeseriesdata
Returns data quality measures for channels for selected time period.

* downScaleInt: specify downscaling interval. Default is 1H (i.e. PT1H). ISO8601 duration format.I.e. PT30S, PT1H, PT10M, PT60S
* start, end: date format using ISO8601 format YYYY-MM-DDThh:mm:ss.  For example, "2007-04-05T14:30Z"
* rules: name of rules to check
* dataChannelIdType: Are you requesting channels by ShortId or DataChannelUuid 
* dataChannelIds: Array of channel ids. Use type specified in dataChannelIdType.  I.e. "AI030206", "AI030207", "AI030701"			 
* includeStartBoundary/includeEndBoundary: Set true/false depending on whether timestamps for boundaries should be included
* assetIds: array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
* limit: Max number of datapoints to be returned. System max limit is 200 000. 
* typeOption: sddData/Data. sddData returns datapoints and metadata, Data returns datapoints only


### POST /v1/DataQuality/aggregate/.score
Returns aggregated dataquality score for assets for given time period

* start: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
* end: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
* assetIds: arrays of asset guids
* includePreviousPeriod: returns rulescore for previous period (period with same length as specified by start and end)


### POST /v1/DataQuality/aggregate/.rulescore
Returns aggregated dataquality score per data quality metric for selected period

* start: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
* end: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
* assetIds: arrays of asset guids
* includePreviousPeriod: returns rulescore for previous period (period with same length as specified by start and end)

### POST /v1/DataQuality/aggregate/.channelscore</td>                            
Returns aggregated data quality score per channel per data quality metric for selected period

* start: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
* end: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
* assetIds: arrays of asset guids
* includePreviousPeriod: returns rulescore for previous period (period with same length as specified by start and end)

### POST /v1/DataQuality/trend/.score</td>            
Returns aggregations per week for data quality score in selected period

* start: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
* end: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
* assetIds: arrays of asset guids
* includePreviousPeriod: returns rulescore for previous period (period with same length as specified by start and end)

### POST /v1/DataQuality/trend/.rulescore</td>                                 
 Returns aggregations per week for each data quality metric in selected period.        
 
* start: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
* end: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
* assetIds: arrays of asset guids
* includePreviousPeriod: returns rulescore for previous period (period with same length as specified by start and end)
                            
## Workspaces
Returns Asset Connect workspaces user has access to

### GET /v1/Workspaces
Returns workspaces user has access to

### GET /v1/Workspaces/{workspaceid}
Returns the workspace by id, and the assets (if any) in the workspace which have IoT Data enabled.

## GET StoredProcedure
### /v1/StoredProcedure/{name}		
Stored procedures can be used for custom queries. Must be managed by Veracity administrators.


