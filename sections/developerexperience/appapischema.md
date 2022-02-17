---
author: Veracity
description: Application or API schema.
---

# Veracity application

A Veracity application represents your app/api in Veracity Identity and allow you to connect to api's and/or expose api scopes|

## Schema

|Name|Description|Accepted values|
|----|-----------|---------------|
|name|The name of the app registration. Resource names are unique per project. Setting a new name will result in a new resource, while using an exsisting name will result in an update.||
|sku|App registration type code|[SKU](#SKU)|
|resourceType|Type of resource||
|sections|Configuration sections|[Sections](#Sections)|

### SKU
|Property|Description|
|--------|-----------|
|app|Client application|
|api|API|
|app:api|An API that is allso a client application

### Sections
|Property|Description|Accepted value|
|--------|-----------|--------------|
|properties|Basic properties|[Properties](#Properties)|
|advanced|Advanced properties|[Advanced](#Advanced)|

### Properties
|Property|Description|Accepted value|
|--------|-----------|--------------|
|isApi|Turn on if your registration publishes api scopes. If true at least 1 published scope must be defined|true/false|
|clientType|the type of client application|None/Confidential/Public/Spa/ClientCredential/Native|
|applicationUrl|The root url of your application||
|redirectUrls|the return url for the authentication flows||
|publishedScopes|List of scopes to publish for an api||
|services|List of services the app registration can manage subscriptions for||
|secretManagementOptions|Defines how the VRM is going to treat secret rotation|none/rollover/onlyIfEmpty|

### Advanced
|Property|Description|Accepted value|
|--------|-----------|--------------|
|apiProductSubscriptions|the list of api products to create subscriptions for. Adding the veracity platform apis is not nessesary as this is added in the backend.||
|apiProductSubscriptions.productId|the product id that you will add (mandatory)||
|apiProductSubscriptions.productName|The name of the api product (optional)||
|apiAcceses|Set up access to api scopes (only for client applications)||
|apiAcceses.apiClientId|the app id of the api you want a grant for||
|apiAcceses.scopes|The scopes to get a grant for||
|clients|Give access to your api scope(s) to other external clients (only for apis)||
|clients.clientId|The app id of the clien you want to grant access to||
|clients.scopes|the scopes you will grant access to||

## Example

```json
{
  "name": "$parameter('appName')",
  "sku": "app",
  "resourceType": "veracity.application",
  "sections": {
    "properties": {
      "isApi": false,
      "clientType": "Confidential",
      "redirectUrls": ["$parameter('appReplyUrl')"],
      "applicationUrl": "$parameter('appUrl')",
      "allowImplicitGrantFlow": true,
      "publishedScopes": [],
      "services": ["$resources[?name== parameter('serviceName')].id"],
      "secretManagementOptions": "rollover"
    },
    "advanced": {
      "apiProductSubscriptions": [
        {
          "productId": "veracity-platfrom-api",
          "productName": "Veracity Platform API"
        }
      ],
      "clients": [],
      "apiAcceses": [
        {
          "apiClientId": "a4a8e726-c1cc-407c-83a0-4ce37f1ce130",
          "scopes": ["user_impersonation"]
        }
      ]
    }
  }
}
```