---
author: Benedikte Kallåk
description: This section describes the different endpoints of the Event Query Api
---
# Data Fabric IoT Event Query API
The api is accessible from [api-portal](https://api-portal.veracity.com/).
Select api: Data Fabric IoT Event Query API

To group the endpoints in api-portal, select the "group by tag" button.

## Authentication
Authorization: Use bearer-token
See how to authenticate for the api [click here]( authenticate-api.md).

## Security Model
Only users that has access to an asset can access data from this asset.

## Api endpoints

Base url: https://api.veracity.com/veracity/iotevents/api/v1

### Equipment and Topology for asset
[Get equipmentlist for a given asset](#getequipmentlistforasset)
[Get current topology for an equipment](#getcurrenttopologyforanequipmentforasset)
Get latest topology report for an asset
Get values for a given equipment code

### Health reports 
Get latest health report for an asset

### Events on asset
Get topic list for a given asset
Get all events for a given asset

### Events based on topic or id (across vessels)
Get all events for a specific topic
Get event based on eventId


#### Get equipmentlist for asset
- Relative url: /GetEquipmentByAsset?schema={schema}&id={id}
- Schema: schema for asset identider - i.e. IMO, 
- Id: asset identifier for given schema
- Response: List of unique equipment codes (id)

#### Get current topology for an equipment for asset
- Relative url: /GetCurrentTopologyByEquipmentCode?schema={schema}&code={code}&id={id}
- Schema: schema for asset identider - i.e. IMO, 
- Id: asset identifier for given schema
- Code: equipment code
- Response: Systemdata for 

#### Get latest topology report for asset
/GetCurrentTopologyByEquipmentCode?schema={schema}&code={code}&id={id}

#### Get values for a given equipment code

#### Get latest health report for asset

#### Get topic list for a given asset

#### Get all events for asset

#### Get all events for a specific topic

#### Get event based on eventId

