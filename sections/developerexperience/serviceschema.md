---
author: Veracity
description: Veracity Service schema
---

# Veracity Service

A veracity service is the representation of your application within Veracity. The service is where we connect user subscriptions and Service spesific terms to. 

## Schema

|Field path|Description|accepted values|
|----------|-----------|---------------|
|name|The name of the service, shown in the veracity navigation menu|string  <br /> Character limit: 4-200 <br />Valid characters: Alphanumerics, underscores, commas, whitespaces, and hyphens|
|resourceType|schema used by veracity|veracity.service|
|locked|Locked state will determine if the user can edit the service through the user interface in developer. Manual override is still possible. VRM ignores this field and will make chages regardless |true/false|
|sku|Not used in the current release|standard|
|properties.serviceUrl|The url to the frontpage of the application  |must be https|
|properties.visible|Sets if the service should be visible in the veracity MyServices and in the novigation menu. Will not take full effect for non production environments|true/false|
|properties.openInNewTab|Open in new tab when cliking the tile in myServices|true/false|
|properties.shortName|Legacy property (optional)|||
|properties.description|A description of the service (optional)|||
|properties.businessOwnerId|The veracity id of the business owner (optional)|||
|properties.technicalContactEmail|Email address for the technical contact (optional)|||
|properties.providerCompanyName|Company name of the service provider (optional)|||
|properties.tags|tagging of the service in myServices (optional)|||
|advanced.passwordPolicy|Used if your usecase require a password policy to meet regulatory demands. Please refrain from setting th policy as a global veracity policy|||
|advanced.passwordPolicy.enforcePasswordPolicy|Turn the policy on and off. setting this a false is the same as not specifing a policy. |true/false|
|advanced.passwordPolicy.scope|Does the policy apply for the service only or for all of Veracity if the user has a subscription to the service|service=0 <br/>veracity=1|
|advanced.passwordPolicy.intervalType|Set the unit type for the interval|days=0 <br/> months=1 <br/>years=2|
|advanced.passwordPolicy.interval|The max age for the password|numeric <br/> supported ranges:<br/>for days 30,60,90,180,365,730 <br/> for months 1,2,3,6,12,24<br/>for years 1,2 |
|advanced.accessLevels|Define access levels for your service. This is the simplest form of access control, only suited for simple applications. If any applications have started using access levels, this feature must not be turned off. Deleting or renaming an access level that has subscribers is not supported and will not have an effect.||
|advanced.accessLevels.useAccessLevels|Turns the support on or off|true/false|
|advanced.accessLevels.accessLevels|Define the levels with name|string <br/>Character limit: 2-50 <br/>Valid characters: Alphanumerics, underscores, hyphen, periods|

## Examples

A basic veracity service 
```json
{
  "name": "$parameter('serviceName')",
  "sku": "standard",
  "resourceType": "veracity.service",
  "locked": true,
  "sections": {
    "properties": {
      "description": "A test service",
      "shortName": "DemoService",
      "openInNewTab": false,
      "visible": false,
      "serviceUrl": "$parameter('appUrl')",
      "shortDescription": "a test service",
    },
    "advanced": {
      "passwordPolicy": null,
      "accessLevels": {
        "useAccessLevels": false,
        "accessLevels": null
      }
    }
  }
}
```

A veracity service with access levels and password policy correctly configured

```json
{
  "name": "$parameter('serviceName')",
  "sku": "standard",
  "resourceType": "veracity.service",
  "locked": true,
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
      "passwordPolicy": {
        "enforcePasswordPolicy": true,
	"interval": 180,
        "intervalType": 0,
        "scope": 0
      },
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

Examples of connecting a service to an app/api is show in the VRM application/API schema page
