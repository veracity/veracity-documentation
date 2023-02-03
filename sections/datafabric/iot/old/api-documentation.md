---
author: Benedikte Kallåk
description: This section describes the different endpoints of the IoT Api
---
# Veracity IoT Api
The api is accessible from [api-portal](https://api-portal.veracity.com/). To group the endpoints in api-portal, select the "group by tag" button.
- Select api: *Data Fabric Time Series API V2*
- Base url: *https://api.veracity.com/veracity/

## Security Model
Only users that has access to an asset can access data from this asset.

## Assets
- Base url: https://api.veracity.com/veracity/

### GET Assets 
Returns all of the assets you have access to, for which timeseries data is available
- Relative url:  timeseries2/api/v2/assets

### GET asset by id
Returns the asset with specified assetguid if user has access to it and timeseries data is available
* assetId: asset guid
- Relative url: imeseries2/api/v2/assets/{assetId}

### GET DataChannelList
List all metadata for data-channels registered for this asset that the user has access to.  Inaccessible channels, based on permissions, are filtered out.
* assetId: asset guid
- Relative url: timeseries2/api/v2/DataChannelList/{assetId}

## TimeSeriesData Queries

- Base url: https://api.veracity.com/veracity/

### GET RawData - single channel
Returns raw data for given data-channel for given time period defined by before or after the offset. 
 * assetId: asset guid
 * dataChannelId: shortId of DataChannelUuid of datachannel.
 * offset: Relative point in time to either start from or end at the requested timeseries data. Date format using ISO8601 format YYYY-MM-DDThh:mm:ss.  For example, "2007-04-05T14:30Z"
 * before: logical (true/false), if true then the timeseries will end at the offset, if false the timeseries will start from the offset.
 * includeOffsetBoundary: True/False. Include offset in query. Default is true
 * limit: Max datapoints to return. System limit is 200,000
 * header: true/false. Set to true if metadata is to be returned together with datapoints. Default is false.

#### Response as ISO 19848
- Relative url: timeseries2/api/v2/assets/{assetId}/dataChannels/{dataChannelId}/iso19848/timeSeries[?offset][&before][&includeOffsetBoundary][&limit][&header]
Response data is listed as EventData.

#### Response as flat structure
- Relative url: timeseries2/api/v2/assets/{assetId}/dataChannels/{dataChannelId}/timeSeries[?offset][&before][&includeOffsetBoundary][&limit]

### GET DownSampledData - single channel
If high resolution of data is not required or can be traded off for less dense data (and performance benefits) this is the recommended way of getting timeseries.
Essentially the timeseries is binned by the duration specified in the parameter and the min/max/average of the data per bin is returned.
Returns downsampled datapoints for given datachannel for given time period defined by before or after offset. The interval to downsample, is given in request payload. 
* id: asset guid
* dataChannelId: shortId of DataChannelUuid of datachannel.
* offset: Relative point in time to either start from or end at the requested timeseries data. Date format using ISO8601 format YYYY-MM-DDThh:mm:ss.  For example, "2007-04-05T14:30Z"
* before: logical (true/false), if true then the timeseries will end at the offset, if false the timeseries will start from the offset. Default is true
* includeOffsetBoundary: True/False. Include offset in query. Default is true
* limit: Max datapoints to return. System limit is 200,000
* header: true/false. Set to true if metadata is to be returned together with datapoints. Default is false.
* downScaleInterval: specify downscaling interval. Set to null if no downscaling. ISO8601 duration format. I.e. PT30S, PT1H, PT10M, PT60S

#### Response as ISO 19848
Response data is listed as TabularData.
- Relative url: timeseries2/api/v2/assets/{assetId}/dataChannels/{dataChannelId}/iso19848/timeSeries/downSampled[?offset][&before][&includeOffsetBoundary][&limit][&header][&downScaleInterval]

#### Response as flat structure
- Relative url: timeseries2/api/v2/assets/{assetId}/dataChannels/{dataChannelId}/timeSeries/downSampled[?offset][&before][&includeOffsetBoundary][&limit][&downScaleInterval]

### POST TimeSeriesData 
Returns timeseries data for a set of datachannels on an asset (or set of assets) by specifying request payload. 
* downScaleInt: specify downscaling interval,  Set to null if no downscaling.ISO8601 duration format. I.e. PT30S, PT1H, PT10M, PT60S
* start, end: date format using ISO8601 format YYYY-MM-DDThh:mm:ss.  For example, "2007-04-05T14:30Z"
* dimension: set null (or remove) if not used in ingest. 
* dataChannelIdType: Are you requesting channels by ShortId or DataChannelUuid 
* dataChannelIds: Array of channel ids. Use type specified in dataChannelIdType.  I.e. "AI030206", "AI030207", "AI030701"			 
* includeStartBoundary/includeEndBoundary: Set true/false depending of whether timestamps for boundaries should be included
* assetIds: array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
* limit: Max number of datapoints to be returned. System max limit is 200 000. 
* typeOption: sddData/Data. sddData returns datapoints and metadata, Data returns datapoints only. (ISO 19848 only)

Payload
```json
{
  "assetIds": [
    "string"
  ],
  "dataChannelIds": [
    "string"
  ],
  "typeOption": "Data",
  "downScaleInt": "string",
  "start": "string",
  "end": "string",
  "dimensions": [
    "string"
  ],
  "packageIds": [
    "string"
  ],
  "limit": 0,
  "dataChannelIdType": "DataChannelUuid",
  "includeStartBoundary": true,
  "includeEndBoundary": true
}
```

#### Response as ISO 19848
Response data will be provided as TabularData with max, min and average if downscaling is used. If not; rawdata is listed as EventData.
- Relative Url: timeseries2/api/v2/iso19848/timeSeries

#### Response as flat structure of datapoint
- Relative Url: timeseries2/api/v2/timeSeries

### GET Latest - single channel
Get the latest n-received values for given channel
* data-channels can be local Id, shortId or DataChannelUuid

#### Response as flat structure of datapoints
- Relative Url: timeseries2/api/v2/assets/{assetId}/dataChannels/{dataChannelId}/timeSeries/latest[?nLatest]

### POST Latest
Get the latest n-received values for given channels. Datapoints in the response are listed as EventData.

* assetIds: array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
* dimension: set null (or remove) if not used in ingest. 
* latestNValues: no of last values to read
* dataChannelIdType: Are you requesting channels by ShortId or DataChannelUuid 
* dataChannelIds: Array of channel ids. Use type specified in dataChannelIdType.  I.e. "AI030206", "AI030207", "AI030701" 
* typeOption: sddData/Data. sddData returns datapoints and metadata, Data returns datapoints only (relevant for ISO format only)

Payload
```json
{
  "assetIds": [
    "string"
  ],
  "dataChannelIds": [
    "string"
  ], 
  "typeOption": "Data",
  "dimensions": [
    "string"
  ],
  "latestNValues": 0,
  "dataChannelIdType": "DataChannelUuid"
}
```
#### as ISO 19848
- Relative url: timeseries2/api/v2/iso19848/timeSeries/latest

#### Response as flat structure of datapoints
- Relative url: timeseries2/api/v2/timeSeries/latest

### Time range
Returns min date and max date for received datapoints for selected channels
Relative url: timeseries2/api/v2/timeSeries/timeRange

* assetIds: array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
* dimension: set null if not used in ingest. 
* dataChannelIdType: Are you requesting channels by ShortId or DataChannelUuid 
* dataChannelIds: Array of channel ids. Use type specified in dataChannelIdType.  I.e. "AI030206", "AI030207", "AI030701" 

```json
{
  "assetIds": [
    "string"
  ],
  "dimensions": [
    "string"
  ],
  "dataChannelIds": [
    "string"
  ],
  "dataChannelIdType": "DataChannelUuid"
}
```

### Get datapoint based on packageIds
- Relative Url: timeseries2/api/v2/assets/{assetId}/timeSeries/packageId/{packageId}


## Data quality
Calculated data quality on ingested sensor data based on defined metrics.
Base url: https://api.veracity.com/veracity

### POST Data quality on selected data channels
Returns data quality measures for channels for selected time period.
. Relative url: timeseries2/api/v2/DataQuality/.timeseriesdata

* downScaleInt: specify downscaling interval. Default is 1H (i.e. PT1H). ISO8601 duration format.I.e. PT30S, PT1H, PT10M, PT60S
* start, end: date format using ISO8601 format YYYY-MM-DDThh:mm:ss.  For example, "2007-04-05T14:30Z"
* rules: name of rules to check
* dataChannelIdType: Are you requesting channels by ShortId or DataChannelUuid 
* dataChannelIds: Array of channel ids. Use type specified in dataChannelIdType.  I.e. "AI030206", "AI030207", "AI030701"			 
* includeStartBoundary/includeEndBoundary: Set true/false depending on whether timestamps for boundaries should be included
* assetIds: array asset guids, ie. "2d37a463-xxxx-yyyy-zzzz-33c6f21f1724" 
* limit: Max number of datapoints to be returned. System max limit is 200 000. 
* typeOption: sddData/Data. sddData returns datapoints and metadata, Data returns datapoints only

Payload

```json
{
  "downScaleInt" : "string"
  "start": "string",
  "end": "string",
  "rules": [
    "string"
  ],
  "limit": 0,
  "dataChannelIdType": "DataChannelUuid",
  "includeStartBoundary": true,
  "includeEndBoundary": true,
  "assetIds": [
    "string"
  ],
  "dataChannelIds": [
    "string"
  ],
  "typeOption": "Data"
}

```

### Aggregated scores
Returns aggregated dataquality score for assets for given time period

* start: Start of period using format YYYY-MM-DDTHH:mm:ss.SSSZ (ISO-8601)
* end: End of period using format YYYY-MM-DDTHH:mm:ss.SSSZ
* assetIds: arrays of asset guids
* includePreviousPeriod: returns rulescore for previous period (period with same length as specified by start and end)

```json
{
  "start": "string",
  "end": "string",
  "assetIds": [
    "string"
  ],
  "includePreviousPeriod": true
}
```
#### POST Aggregated score per asset
Returns aggregated dataquality score for assets for given time period
- Relative url: timeseries2/api/v2/DataQuality/aggregate/.score

#### POST Aggregated score per metric 
Returns aggregated dataquality score for assets for given time period
- Relative url: timeseries2/api/v2/DataQuality/aggregate/.rulescore

#### POST Aggregated score per channel per metric 
Returns aggregated data quality score per channel per data quality metric for selected period     
- Relative url: timeseries2/api/v2/DataQuality/aggregate/.channelscore

#### POST Get trend per week per asset
Returns aggregations per week for data quality score in selected period
- Relative url: timeseries2/api/v2/DataQuality/trend/.score

#### POST Get trend per week per metric per asset
Returns aggregations per week for each dataquality metric in selected periode
- Relative url: timeseries2/api/v2/DataQuality/trend/.rulescore


## Workspaces
Returns Asset Connect workspaces user has access to

### GET /v1/Workspaces
Returns workspaces user has access to

### GET /v1/Workspaces/{workspaceid}
Returns the workspace by id, and the assets (if any) in the workspace which have IoT Data enabled.

## GET StoredProcedure
### /v1/StoredProcedure/{name}
Stored procedures can be used for custom queries. Must be managed by Veracity administrators.


