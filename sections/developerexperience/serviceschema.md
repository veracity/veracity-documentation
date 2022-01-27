---
author: Veracity
description: Veracity Service schema
---

# Veracity Service

A veracity service is the representation of your application within Veracity. The service is where we connect user subscriptions and Service spesific terms to. 

## Schema

|Field path|Description|accepted values|
|----------|-----------|---------------|
|name|The name of the service, shown in the veracity navigation menu||
|sku|Not used in the current release|standard|
|properties.serviceUrl|the url to the frontpage of the application||
|properties.visible|sets if the service should be visible in the veracity MyServices and in the novigation menu. Will not take full effect for non production environments|true/false|
|properties.openInNewTab|open in new tab when cliking the tile in myServices|true/false|
|properties.shortName|legacy property (optional)|||
|properties.description|A description of the service (optional)|||
|properties.businessOwnerId|The veracity id of the business owner (optional)|||
|properties.technicalContactEmail|Email address for the technical contact (optional)|||
|properties.providerCompanyName|Company name of the service provider (optional)|||
|properties.tags|tagging of the service in myServices (optional)|||
|advanced.passwordPolicy|Used if your usecase require a password policy to meet regulatory demands. Please refrain from setting th policy as a global veracity policy|||
|advanced.passwordPolicy.enforcePasswordPolicy|Turn the policy on and off. setting this a false is the same as not specifing a policy|true/false|
|advanced.passwordPolicy.scope|Does the policy apply for the service only or for all of Veracity if the user has a subscription to the service|service/veracity|
|advanced.passwordPolicy.intervalType|Set the unit type for the interval|days/months/years|
|advanced.passwordPolicy.interval|the max age for th password|numeric|
|advanced.accessLevels|Define access levels for your service. This is the simplest form of access control, only siuted for simple applications||
|advanced.accessLevels.useAccessLevels|Turns the support on or off||
|advanced.accessLevels.accessLevels|Define the levels with name||

```json
{
      "name": "$parameter('serviceName')",
      "sku": "standard",
      "resourceType": "veracity.service",
      "sections": {
        "properties": {
          "businessOwnerId": null,
          "description": "",
          "shortName": "NP_Dev_DemoService",
          "openInNewTab": true,
          "visible": true,
          "serviceUrl": "$parameter('appUrl')",
          "technicalContactEmail": "",
          "providerCompanyName": null,
          "tags": [ "Sample", "Dev" ] 
        },
        "advanced": {
          "passwordPolicy": null,
          "accessLevels": {
            "useAccessLevels": true,
            "accessLevels": [
              {
                "accessLevelName": "reader"
              },
              {
                "accessLevelName": "contributor"
              },
              {
                "accessLevelName": "owner"
              }
            ]
          }
        }
      }
    }
```