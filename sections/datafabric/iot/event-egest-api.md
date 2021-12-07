---
author: Benedikte Kallåk
description: This section describes the different endpoints of the Event Query Api
---
# Data Fabric IoT Event Query API
- The api is accessible from [api-portal](https://api-portal.veracity.com/).
- Select api: Data Fabric IoT Event Query API V2
- To group the endpoints in api-portal, select the "group by tag" button.

## Authentication
Authorization: Use bearer-token
See how to authenticate for the api [click here](authenticate-api.md).

## Security Model
Only users that has access to an asset can access data from this asset.

## Equipment topology and Health
Base url: *https://api.veracity.com/veracity/


### Get current equipment topology on asset
Get latest (current) topology on asset
Relative url: iotevents2/api/v2/assets/{assetId}/events/equipment/topology/latest?assetIdSchema={assetIdSchema}

- assetId: asset imo nr or veracity guid
- assetIdSchema: imo/veracity  (the schema for the asset id)

### Get current topology on equipment
Get latest (current) topology on asset
Relative url: iotevents2/api/v2/assets/{assetId}/events/equipment/topology/dataChannel/latest?assetIdSchema={assetIdSchema}&dataChannelId={dataChannelId}&namingRule={namingRule}

- assetId: asset imo nr or veracity guid
- assetIdSchema: imo/veracity  (the schema for the asset id)
- dataChannelId: The identifier /code used by the codebook used for asset categorization ( Vis code, mc key, JSME id etc.)
- namingRule: name of codebook: DNV-VIS, JSME, MC, etc.

### Get historical topology events on dataChannel
Get a list of equipment topology events registered on given data channels
Relative url: iotevents2/api/v2/assets/{assetId}/events/equipment/topology?assetIdSchema={assetIdSchema}&dataChannelId={dataChannelId}&namingRule={namingRule}[&fromUtcDate][&toUtcDate]

- assetId: asset imo nr or veracity guid
- assetIdSchema: imo/veracity  (the schema for the asset id)
- dataChannelId: The identifier /code used by the codebook used for asset categorization ( Vis code, mc key, JSME id etc.)
- namingRule: name of codebook: DNV-VIS, JSME, MC, etc.
- fromUtcDate: optional - select events from this timestamp. UTC-format: "2021-04-06T14:22:48.950716+02:00"
- toUtcDate: optional - select events until and including this timestamp. UTC-format: "2021-04-06T14:22:48.950716+02:00"


## Events
Base url: *https://api.veracity.com/veracity/

### Get events for the provided start. end date, template type, naming rule and data channel Id
Relative url: /iotevents2/api/v2/assets/{assetId}/events?assetIdSchema={assetIdSchema}&dataChannelId={dataChannelId}&namingRule={namingRule}[&fromUtcDate][&toUtcDate][&eventType]

- assetId: asset imo nr or veracity guid
- assetIdSchema: imo/veracity  (the schema for the asset id)
- dataChannelId: The identifier /code used by the codebook used for asset categorization ( Vis code, mc key, JSME id etc.)
- namingRule: name of codebook: DNV-VIS, JSME, MC, etc.
- fromUtcDate: optional - select events from this timestamp. UTC-format: "2021-04-06T14:22:48.950716+02:00"
- eventType: event type (template/topic)

### Get an event based on EventId
Relative url: iotevents2/api/v2/assets/{assetId}/events/eventId/{eventId}?assetIdSchema={assetIdSchema}

### Events by type
Get event by event type
Relative url: iotevents2/api/v2/assets/{assetId}​/events/eventType/{eventType}?assetIdSchema={assetIdSchema}[&fromUtcDate][&toUtcDate]

- assetId: asset imo nr or veracity guid
- eventType: event type (template/topic)
- assetIdSchema: imo/veracity  (the schema for the asset id)
- fromUtcDate: optional - select events from this timestamp. UTC-format: "2021-04-06T14:22:48.950716+02:00"
- toUtcDate: optional - select events until and including this timestamp. UTC-format: "2021-04-06T14:22:48.950716+02:00"

### Get n-latest Events

Relative url: iotevents2/api/v2/assets/{assetId}/events​/latest?assetIdSchema={assetIdSchema}[&dataChannelId][&namingRule][&eventType][&nLatest]
- assetId: asset imo nr or veracity guid
- assetIdSchema: imo/veracity  (the schema for the asset id)
- dataChannelId: The identifier /code used by the codebook used for asset categorization ( Vis code, mc key, JSME id etc.)
- namingRule: name of codebook: DNV-VIS, JSME, MC, etc.
- eventType: event type (template/topic)
- nLatest: no of latest events to fetch
