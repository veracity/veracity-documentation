---
author: Veracity
description: Veracity Api Spec schema
---

# Veracity Api Spec

A Veracity API spec is the representation of your application within Veracity API Management. The API Spec resource allows you to publish your API Specifications into Veracity API Management and perform updates. 

## Schema

|Field path|Description|accepted values|
|----------|-----------|---------------|
|name|The name of the API specification, shown in the Veracity navigation menu|string  <br /> Character limit: 4-200 <br />Valid characters: Alphanumerics, underscores, commas, whitespaces, and hyphens|
|resourceType|schema used by veracity|veracity.apiSpec|
|locked|Locked state will determine if the user can edit the apiSpec through the user interface in developer. Manual override is still possible. VRM ignores this field and will make chages regardless |true/false|
|sku|Not used in the current release|standard|
|properties.description|A description of the apiSpec (optional)|||

## Examples

A basic Veracity apiSpec 
```json
{
  "resourceGroup": {
    "name": "$parameter('rgName')",
    "isProduction": false,
    "description": "Spec and Product",
    "tags": [
      "Test",
      "Product and Spec"
    ],
    "locked": true
  },
  "resources": [
    {
      "name": "$parameter('specName')",
      "sku": "standard",
      "resourceType": "veracity.apiSpec",
      "locked": true,
      "sections": {
        "properties": {
          "description": "$parameter('description')",
          "uploadType": "swagger-link-json",
          "apiSpec": "$parameter('apiBackendSwaggerUrl')",
          "apiSuffix": "$parameter('apiSuffix')",
          "version": null,
          "products": [
            "$parameter('apiProductId')"
          ],
          "requireSubscription": true,
          "backendUrl": "$parameter('apiBackendUrl')",
          "versionSetId": null
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
  },
  {
    "name": "apiBackendSwaggerUrl",
    "type": "string",
    "value": "https://petstore.swagger.io/v2/swagger.json"
  },
  {
    "name": "apiSuffix",
    "type": "string",
    "value": "myapispec"
  },
  {
    "name": "apiProductId",
    "type": "string",
    "value": "ppazdc58ef53-e16d-4fe8-b3ac-375690dfdd21"
  },
  {
    "name": "apiBackendUrl",
    "type": "string",
    "value": "https://petstore.swagger.io/v2"
  }
]
```


