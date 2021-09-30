---
author: Benedikte Kallåk
description: This section describes the Event Ingest Api
---

# Ingest Alarms & Events to Veracity

Events and alerts are ingested into Veracity using API. 
- The api is accessible from [api-portal](https://api-portal.veracity.com/). 
- Select api: *Data Fabric IoT Event Ingest API*

Events are defined by templates and Veracity allows ingest of any event template. If the template used is not defined in Veracity, 
the ingested event will only be validated according to message size and 

A specialized event is the the equipment event that allows for topology inserts and updates as well as health messages.

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

- Url: https://api.veracity.com/veracity/ioteventsingest/api/v2/asset/{assetId}/event/equipment
- Authorization: Bearer token [click here]( authenticate-api.md)
- Ocp-Apim-Subscription-Key: from application client or B2C user


### query param
-assetId: asset imo nr or veracity guid
-assetIdSchema: imo/veracity  (the schema for the asset id)

### body
The body contains the JSON message in the following format

```json
{
  {
    "manufacturer": "string",
    "modelNo": "string",
    "serialNo": "string",
    "softwareVersion": "string",
    "timeStampUTC": "2021-09-29T10:15:00.269Z",
    "healthStatus": "string",
    "expiryDate": "2021-09-29T10:15:00.269Z",
    "equipmentId": [
      {
        "dataChannelId": "string",
        "namingRule": "string"       
      }
    ]
  }
}

```

* equipmentId:
	* dataChannelId: The identifier /code used by the codebook used for asset categorization ( Vis code, mc key, JSME id etc.)
	* namingRule: name of codebook: Vis, JSME
* healtStatus: can be null (omitted) if event is a topology event only.
* timeStampUtc: timestamp for event, UTC: format: "2021-04-06T14:22:48.950716+02:00"
* expiryDate: Optional, equipment such as charts have expiry date
* healtStatus: ok, notok
* softwareVersion: major.minor.patch

[see how to ingest health message]( health-message.md).

## Ingest event by template
This endpoint can be used to ingest any event a JSON object to Veracity with some paramerters in header. 

- Url: https://api.veracity.com/veracity/ioteventsingest/api/v2/asset/{assetId}/event
- Authorization: Bearer token [click here]( authenticate-api.md)
- Ocp-Apim-Subscription-Key: from application client or B2C user


### Header param
- assetId: asset imo nr or veracity guid
- assetIdSchema: imo/veracity  (the schema for the asset id)
- eventType: event template
- timeStampUtc: timestamp for event, UTC: format: "2021-04-06T14:22:48.950716+02:00"
- dataChannelId: The identifier /code used by the codebook used for asset categorization ( Vis code, mc key, JSME id etc.)
- namingRule: name of codebook: Vis, JSME
- eventId: optional. If not provided, a UUID will be generated

### Body

```json
{
  {
    any json object
  }
}

```

[see exampe of event of type bunker delivery note event]( generic-message.md).