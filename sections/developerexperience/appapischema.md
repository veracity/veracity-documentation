---
author: Veracity
description: Application or API schema.
---

# Veracity application

A Veracity application represents your app/api in Veracity Identity and allow you to connect to api's and/or expose api scopes|

## Schema

|Field path|Description|accepted values|
|----------|-----------|---------------|
|name|The name of the app registration||
|sku|specify type of registration|app/api/app;api|
|properties.isApi|Turn on if your registration publishes api scopes. If true at least 1 published scope must be defined|true/false|
|properties.clientType|the type of client application|None/Confidential/Public/Spa/ClientCredential/Native|
|properties.applicationUrl|The root url of your application||
|properties.redirectUrls|the return url for the authentication flows||
|properties.publishedScopes|List of scopes to publish for an api||
|properties.services|List of services the app registration can manage subscriptions for||
|properties.secretManagementOptions|Defines how the VRM is going to treate secret rotation|none/rollover/onlyIfEmpty|
|advanced.apiProductSubscriptions|the list of api products to create subscriptions for. Adding the veracity platform apis is not nessesary as this is added in the backend.||
|advanced.apiProductSubscriptions.productId|the product id that you will add (mandatory)||
|advanced.apiProductSubscriptions.productName|The name of the api product (optional)||
|advanced.apiAcceses|Set up access to api scopes (only for client applications)||
|advanced.apiAcceses.apiClientId|the app id of the api you want a grant for||
|advanced.apiAcceses.scopes|The scopes to get a grant for||
|advanced.clients|Give access to your api scope(s) to other external clients (only for apis)||
|advanced.clients.clientId|The app id of the clien you want to grant access to||
|advanced.clients.scopes|the scopes you will grant access to||

```json
{
      "sections": {
        "properties": {
          "isApi": false,
          "clientType": "Confidential",
          "redirectUrls": [
            "$parameter('appReplyUrl')"
          ],
          "applicationUrl": "$parameter('appUrl')",
          "allowImplicitGrantFlow": true,
          "publishedScopes": [],
          "services": [
            "$resources[?name== parameter('serviceName')].id"
          ],
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
              "scopes": [
                "user_impersonation"
              ]
            }
          ]
        }
      },
      "name": "$parameter('appName')",
      "sku": "app",
      "resourceType": "veracity.application"
    } 
```