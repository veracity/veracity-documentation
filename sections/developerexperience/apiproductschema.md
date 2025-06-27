---
author: Veracity
description: Veracity Api Product schema
---

# Veracity Api Spec

A Veracity API product is the product you add your one or more APIs in Veracity API Management. The API Product resource allows you to publish your API Products into Veracity API Management and perform updates. 

## Schema

|Field path|Description|accepted values|
|----------|-----------|---------------|
|name|The name of the API product, shown in the Veracity navigation menu|string  <br /> Character limit: 4-200 <br />Valid characters: Alphanumerics, underscores, commas, whitespaces, and hyphens|
|resourceType|schema used by veracity|veracity.apiProduct|
|locked|Locked state will determine if the user can edit the apiProduct through the user interface in developer. Manual override is still possible. VRM ignores this field and will make chages regardless |true/false|
|sku|Not used in the current release|standard|
|sections.advanced.throttling.cors| Cross-Origin Resource Sharing configuration for the product|
|sections.advanced.throttling.enableThrottling|Enables throttling options for the product|
|sections.advanced.throttling.counterKey|throttling option for the product|
|sections.advanced.throttling.calls|throttling option for the product|
|sections.advanced.throttling.renewal|throttling option for the product|
|sections.advanced.throttling.incrementCondition|throttling option for the product|
|properties.requireSubscriptionApproval|Specifies of a new subscription requires approval before becomes active|
|properties.requireSubscription|Specifies if Product requires subscription to consume APIs registered for the Product|
|properties.apis|List of apiSpec Ids|
|properties.description|A description of the apiSpec (optional)|||

## Examples

A basic Veracity apiProduct
```json
{
  "resourceGroup": {
    "name": "$parameter('rgName')",
    "isProduction": false,
    "description": "Spec and Product",
    "tags": ["Test", "Product and Spec"],
    "locked": true
  },
  "resources": [
    {
      "name": "$parameter('productName')",
      "sku": "standard",
      "resourceType": "veracity.apiProduct",
      "sections": {
        "advanced": {
          "throttling": {
            "enableThrottling": false,
            "counterKey": "ipAddress",
            "calls": 20,
            "renewal": 60,
            "incrementCondition": "any"
          },
          "cors": null
        },
        "widget": { "enabledWidget": false },
        "properties": {
          "description": "$parameter('description')",
          "requireSubscriptionApproval": false,
          "requireSubscription": true,
          "state": "Published",
          "apis": [],
          "groups": [
              {
                  "id": "administrators",
                  "value": "Administrators"
              }
          ],
          "terms": null,
          "isPublic": false
      }
      }
    }
  ]
}
```



Example of parameter file


```json
[
  {
    "name": "rgName",
    "type": "string",
    "value": "MyResourceGroupName"
  },
  {
    "name": "specName",
    "type": "string",
    "value": "MyApiSpecName"
  },
  {
    "name": "description",
    "type": "string",
    "value": "Here is the description for my apiSpec"
  }
]
```


