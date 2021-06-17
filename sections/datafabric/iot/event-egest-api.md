---
author: Benedikte Kallåk
description: This section describes the different endpoints of the Event Query Api
---
# Data Fabric IoT Event Query API
- The api is accessible from [api-portal](https://api-portal.veracity.com/).
- Select api: Data Fabric IoT Event Query API
- To group the endpoints in api-portal, select the "group by tag" button.

## Authentication
Authorization: Use bearer-token
See how to authenticate for the api [click here](authenticate-api.md).

## Security Model
Only users that has access to an asset can access data from this asset.

## Api endpoints

Base url: *https://api.veracity.com/veracity/iotevents/api/v1*

### Equipment and Topology for asset
[Get equipmentlist for a given asset](#get-equipmentlist-for-asset)
[Get latest topology report for an asset](#get-latest-topology-report-for-asset) 
[Get current topology for an equipment](#get-current-topology-for-an-equipment-for-asset)

### Health reports 
[Get latest health report for an asset](#get-latest-health-report-for-asset)

### Events on asset
[Get topic list for a given asset](#get-topic-list-for-asset)

### Events based on topic or id (across vessels)
[Get all events for a specific topic](#get-all-events-for-topic)
[Get event based on eventId](#get-event-by-eventid)


#### Get equipmentlist for asset
- Relative url: /Event/GetEquipmentByAsset?schema={schema}&id={id}
- Schema: schema for asset identider - i.e. IMO, 
- Id: asset identifier for given schema
- Response: List of unique equipment codes (id)

#### Get current topology for an equipment for asset
- Relative url: /Event/GetCurrentTopologyByEquipmentCode?schema={schema}&code={code}&id={id}
- Schema: schema for asset identider - i.e. IMO, 
- Id: asset identifier for given schema
- Code: equipment code
- Response: Current systemdata for equipment

#### Get latest topology report for asset
- Relative url: /Event/GetLatestTopologyEventByAsset?schema={schema}&id={id}
- Schema: schema for asset identider - i.e. IMO, 
- Id: asset identifier for given schema

This could respond in a report not containing all equipment if last report was incomplete.


#### Get latest health report for asset
- Relative url: /Event/GetLatestHealthEventByAsset?schema={schema}&id={id}
- Schema: schema for asset identider - i.e. IMO, 
- Id: asset identifier for given schema

This could respond in a report not containing health on all equipment if last report was incomplete.

#### Get topic list for asset
- Relative url: /Event/GetTopicsByAsset?schema={schema}&id={id}
- Schema: schema for asset identider - i.e. IMO, 
- Id: asset identifier for given schema
- Response: Array of unique topics

#### Get all events for asset
- Relative url: /Event/GetEventsByAsset?schema={schema}&id={id}
- Schema: schema for asset identider - i.e. IMO, 
- Id: asset identifier for given schema

This api-endpoint will change shortly to limit the response

#### Get all events for topic
- Relative url: /Event/GetEventsByTopic?topic={topic}
- Topic: topic name, i.e. "Communication/EquipmentStatus/HealthReport"
- Response: all event with this topic across vessels you have access to

#### Get event by eventId
- Relative url: /Event/{id}
- id: unique id of event ingested

[obsolete]
These endpoints will be re-implemented based on needs:
- Get values for a given equipment code
- Fetches values for a given equipment data value, dataset schema and name

