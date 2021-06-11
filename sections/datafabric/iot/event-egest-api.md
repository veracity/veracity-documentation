---
author: Benedikte Kallåk
description: This section describes the different endpoints of the Event Query Api
---
# Veracity IoT Api
The api is accessible from [api-portal](https://api-portal.veracity.com/).
Select api: Data Fabric IoT Event Query API
To group the endpoints in api-portal, select the "group by tag" button.

## Security Model
Only users that has access to an asset can access data from this asset.

## Api endpoints

Base url: https://api.veracity.com/veracity/iotevents/api/v1

# Equipment and Topology for asset
* [GET Event/GetCurrentTopologyByEquipmentCode?schema={schema}&code={code}&id={id}](#get-v1datachannellistid)
Fetches current topology for an equipment

* [GET /Event/GetEquipmentByAsset?schema={schema}&id={id}(#get-v1assetsiddatachannelsdatachannelidtimeseriesdatagetdownsampleddata)
Fetches equipment for a given asset Schema and Id

* [GET /Event/GetEquipmentByAsset?schema={schema}&id={id}(#get-v1assetsiddatachannelsdatachannelidtimeseriesdatagetdownsampleddata)
Fetches equipment for a given asset Schema and Id

* [GET /Event/GetLatestTopologyEventByAsset?schema={schema}&id={id}(#get-v1assetsiddatachannelsdatachannelidtimeseriesdatagetdownsampleddata)
Fetches latest topology event for an asset

* [GET /Event/GetEventsByEquipmentCode?code={code}(#get-v1assetsiddatachannelsdatachannelidtimeseriesdatagetdownsampleddata)
Fetches values for a given equipment code

* [GET /Event/GetEventsByEquipmentStatus?schema={schema}&key={key}&value={value}(#get-v1assetsiddatachannelsdatachannelidtimeseriesdatagetdownsampleddata)
Fetches values for a given equipment data value, dataset schema and name


# Health

* [GET /Event/GetLatestHealthEventByAsset?schema={schema}&id={id}(#get-v1assetsiddatachannelsdatachannelidtimeseriesdatagetdownsampleddata)
Fetches latest health event for an asset

# Events on asset
* [GET /Event/GetTopicsByAsset?schema={schema}&id={id}(#get-v1assetsiddatachannelsdatachannelidtimeseriesdatagetdownsampleddata)
Fetches topics for a given asset Schema and Id

* [GET /Event/GetEventsByAsset?schema={schema}&id={id}(#get-v1assetsiddatachannelsdatachannelidtimeseriesdatagetdownsampleddata)
Fetches values for a given asset id (Schema and Id)



# Events based on topic or id (across vessels)

Fetches all events for a specific topic
* [GET /Event/GetEventsByTopic?topic={topic}](#get-v1assets)
Fetches all events for a specific topic

* [GET /Event/{id}](##get-v1assetsid)
Fetches an event based on EventId



