---
author: Benedikte Kallåk
description: Description of quick start section
---

# Event type

Different event types can be defined where the paramters in the body will vary. 

## Header

- assetId: 1234
- assetIdSchema: imo
- eventType: BunkerDeliveryNote
- timeStampUtc: timestamp for event, UTC: format: "2021-04-06T14:22:48.950716+02:00"
- dataChannelId: Consumables/BunkerDeliveryNote/IntermediteFuelOil
- namingRule: mc


## Body
```json
{
  
  "assets": {
    "globalId": "string",
    "name": "string",
    "type": "string"
  },
  "eventData": {
    "mcKey": "Consumables/BunkerDeliveryNote/IntermediteFuelOil",
    "discipline": "Consumables",
    "eventType": "BunkerDeliveryNote",
    "timestampUTC": "string",
    "timestampLocal": "string",
    "id": "string"
  },
  "bdnData": {
    "bdnNr": "string",
    "deliveryPort": {
      "name": "string",
      "unLoCode": "string"
    },
    "timeReport": {
      "hoseConnected": "string",
      "commencedPumping": "string",
      "completedPumping": "string",
      "hoseDisconnected": "string"
    },
    "bunkerData": {
      "fuelType": "string",
      "grade": "string",
      "kinematicViscosity": {
        "temperature": {
          "value": 0,
          "unit": "string"
        },
        "viscosity": {
          "value": 0,
          "unit": "string"
        }
      },
      "volumeAtLoadingTemp": {
        "value": 0,
        "unit": "string"
      },
      "volumeAt15dg": {
        "value": 0,
        "unit": "string"
      },
      "mass": {
        "value": 0,
        "unit": "string"
      },
      "loadingTemp": {
        "value": 0,
        "unit": "string"
      },
      "sulphurContent": {
        "value": 0,
        "unit": "string"
      },
      "densityAt15dg": {
        "value": 0,
        "unit": "string"
      },
      "waterContent": {
        "value": 0,
        "unit": "string"
      },
      "lowerHeatingValue": {
        "value": 0,
        "unit": "string"
      },
      "higherHeatingValue": {
        "value": 0,
        "unit": "string"
      }
    },
    "supplier": {
      "name": "string",
      "id": "string"
    }
  }
}


```
