---
author: Benedikte Kallåk
description: This section describes the Event Ingest Api
---

# Ingest Alarms & Events to Veracity

Events and alerts are ingested into Veracity using API. 
- The api is accessible from [api-portal](https://api-portal.veracity.com/). 
- Select api: *Data Fabric IoT Event Ingest API*

Events are defined by event-types (templates) and Veracity allows ingest of any eventtype. If the eventtype used is not defined in Veracity, 
the ingested event will only be validated according to basic JSON validation.

A specialized event is the the equipment event that allows for topology inserts and updates as well as health status.

## Authentication
Authorization: Use bearer-token
See how to authenticate for the api [click here]( authenticate-api.md).

## Security Model
Only users (incl. application credentials) that has access to an asset can ingest data to an asset.

## Setup
Before data can be ingested to Veracity the following must be done:
1.	Vessel must be registered by Veracity administrator
2.	You must have access to the assets you are ingesting data for


## Ingest equipment event
This endpoint is used for adding new equipment, updating endpoint and update health status
- Base url: https://api.veracity.com/veracity
- Request url: https://api.veracity.com/veracity/ioteventsingest2/api/v2/assets/{assetId}/event/equipment?assetIdSchema={assetIdSchema}

- Authorization: Bearer token [click here]( authenticate-api.md)
- Ocp-Apim-Subscription-Key: from application client or B2C user

### query param
-assetId: asset imo nr or veracity guid
-assetIdSchema: imo/veracity  (the schema for the asset id)

### body
The body contains the JSON message in the following format

```json

  {
    "manufacturer": "string",
    "modelNo": "string",
    "serialNo": "string",
    "softwareVersion": "string",
    "type": "string",
    "dataChannelId": "string",
    "name": "string",
    "timeStampUTC": "string",
    "healthStatus": "string",
    "expiryDate": "string"
  }


```

* dataChannelId: The equipment identifier /code used by the namingstandard used for asset categorization ( Vis code, mc key, JSME id etc.). This is the local id (ISO 19848) containing the namingrule
* name:Equipment name
* healtStatus: ok, notok - can be null (omitted) if event is a topology event 
* timeStampUtc: timestamp for event, UTC: format: "2021-04-06T14:22:48.950716+02:00"
* expiryDate: Optional, equipment such as charts have expiry date
* softwareVersion: major.minor.patch


## Ingest health status
Use same endpoint as for equipment: '
```json
{
  {
   
    "healthStatus": "string",    
    "equipmentId": [
      {
       "dataChannelId": "string",
       "dataChannelId": "string",
       "name": "string",
      }
    ]
  }
}

```

## Ingest event by eventtype
This endpoint can be used to ingest any eventtype as a JSON object to Veracity with some paramerters in header. 
- Base url: https://api.veracity.com/veracity
- Request url: https://api.veracity.com/veracity/ioteventsingest2/api/v2/assets/{assetId}/event?assetIdSchema={assetIdSchema}&eventType={eventType}&dataChannelID={dataChannelID}[&eventId][&timeStampUtc]
- Authorization: Bearer token [click here]( authenticate-api.md)
- Ocp-Apim-Subscription-Key: from application client or B2C user


### Header param
- assetId: asset imo nr or veracity guid
- assetIdSchema: imo/veracity  (the schema for the asset id)
- eventType: event type (template/topic)
- timeStampUtc: timestamp for event, UTC: format: "2021-04-06T14:22:48.950716+02:00"
- dataChannelId: The equipment identifier /code used by the namingstandard used for asset categorization ( Vis code, mc key, JSME id etc.). This is the local id (ISO 19848) containing the namingrule
- eventId: optional. If not provided, a UUID will be generated
- timeStampUTC: option. If not provided, UTC.now will be used

### Body

Payload
```json
{
  
    any json object
  
}
```

Example:
```json
{
	"equipment": {
		"customFields": null,
		"key": "Propulsion/Engine_1/CylinderHead_1",
		"title": "Propulsion Engine 1 Cylinder Head 1"
	},
	"eventData": {
		"id": "4b2161e8-efd3-408a-8090-2359a4e84f78",
		"mcKey": "Propulsion/Engine_1/CylinderHead_1/ExhaustGas/Outlet/Temperature",
		"eventType": "EquipmentReading",
		"discipline": "Machinery",
		"timestampUTC": "2021-11-01T12:36:01.9860000Z",
		"timestampLocal": "2021-11-01T12:36:01.0000000Z"
	},
	"equipmentReading": {
		"customFields": null,
		"unit": "?C",
		"value": 104,
		"content": "ExhaustGas",
		"measure": "Temp",
		"position": "Outlet",
		"readingTime": "2021-11-01T12:36:01.1990000Z"
	}
}
```