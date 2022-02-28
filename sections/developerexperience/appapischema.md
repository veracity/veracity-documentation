---
author: Veracity
description: Application or API schema.
---

# Veracity application

A Veracity application represents your app/api in Veracity Identity and allow you to connect to api's and/or expose api scopes

## Schema

|Name|Description|Accepted values|
|----|-----------|---------------|
|name|The name of the app registration. Resource names are unique per project. Setting a new name will result in a new resource, while using an exsisting name will result in an update.|string<br/>Character limit: 4-200<br/>Valid characters: Alphanumerics, underscores, commas, whitespaces, and hyphens|
|sku|App registration type code|[SKU](#sku)|
|resourceType|Type of resource|string, e.g veracity.service, veracity.application|
|locked|Locks changes from the developer UI. Can be manually unlocked. VRM ignores this lock. Best used to avoid overwritting manual changes on next deploy|true/false|
|sections|Configuration sections|[Sections](#sections)|

### SKU
|Value|Description|
|-----|-----------|
|app|Client application|
|api|API|
|app;api|An API that is also a client application

### Sections
|Property|Description|Accepted value|
|--------|-----------|--------------|
|properties|Basic properties|[Properties](#properties)|
|advanced|Advanced properties|[Advanced](#advanced)|

### Properties
|Property|Description|Accepted value|
|--------|-----------|--------------|
|isApi|Turn on if your registration publishes api scopes. If true at least 1 published scope must be defined|true/false|
|clientType|the type of client application|[ClientType](#clienttype)|
|applicationUrl|The root url of your application|must be https, localhost is excempt from this rule|
|redirectUrls|the return url for the authentication flows|must be https, localhost is excempt from this rule|
|publishedScopes|List of scopes to publish for an api||
|services|List of services the app registration can manage subscriptions for||
|secretManagementOptions|Defines how the VRM is going to treat secret rotation|none = no secret created <br/><br/> rollover = creates up to two secrets, the oldest secret is then replaced<br/><br/>onlyIfEmpty = Only creates if no secret is present|

### ClientType
|Value|Description|
|-----|-----------|
|None||
|Confidential| Confidential client application (e.g web server)|
|Public| Public client application|
|Spa| Single page appliation, public client using Authorization code flow with PKCE|
|ClientCredential|App using client credentials|
|Native|Mobile or desktop application|
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
|clients.clientId|The app id of the client you want to grant access to|Test = a4a8e726-c1cc-407c-83a0-4ce37f1ce130 <br/><br/>Stag = 28b7ec7b-db04-40bb-a042-b7ac5a8b36be<br/><br/>Prod = 83054ebf-1d7b-43f5-82ad-b2bde84d7b75 |
|clients.scopes|the scopes you will grant access to||

## Examples
Example of an API with no client application. The same configuration can be used in combination with other client application types, sku then needs to be set as app;api
```json
{
  "name": "$parameter('appName')",
  "sku": "api",
  "resourceType": "veracity.application",
  "locked":true,
  "sections": {
    "properties": {
      "isApi": true,
      "clientType": "None",
      "redirectUrls": [],
      "applicationUrl": null,
      "publishedScopes": [
        {
          "description": "Short description of scope",
          "scopeName": "user_impersonation"
        },
        {
          "description": "Short description of scope",
          "scopeName": "user_management"
        }
      ],
      "services": [],
      "secretManagementOptions": null
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
          "apiClientId": "$parameter('apiClientId')",
          "scopes": ["user_impersonation"]
        }
      ]
    }
  }
}
```

Example of a confidential client application

```json
{
  "name": "$parameter('appName')",
  "sku": "app",
  "resourceType": "veracity.application",
  "locked":true,
  "sections": {
    "properties": {
      "isApi": false,
      "clientType": "Confidential",
      "redirectUrls": ["$parameter('appReplyUrl')"],
      "applicationUrl": "$parameter('appUrl')",
      "allowImplicitGrantFlow": true,
      "publishedScopes": [],
      "services": [],
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
          "apiClientId": "$parameter('apiClientId')",
          "scopes": ["user_impersonation"]
        }
      ]
    }
  }
}
```
Example of a public client application
```json
{
  "name": "$parameter('appName')",
  "sku": "app",
  "resourceType": "veracity.application",
  "locked":true,
  "sections": {
    "properties": {
      "isApi": false,
      "clientType": "Public",
      "redirectUrls": ["$parameter('appReplyUrl')"],
      "applicationUrl": "$parameter('appUrl')",
      "publishedScopes": [],
      "services": [],
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
          "apiClientId": "$parameter('apiClientId')",
          "scopes": ["user_impersonation"]
        }
      ]
    }
  }
}
```
Example of a native client application
```json
{
  "name": "$parameter('appName')",
  "sku": "app",
  "resourceType": "veracity.application",
  "locked": true,
  "sections": {
    "properties": {
      "isApi": false,
      "clientType": "Native",
      "redirectUrls": ["$parameter('nativeReply')"],
      "publishedScopes": [],
      "services": [],
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
         "apiClientId": "$parameter('apiClientId')",
         "scopes": ["user_impersonation"]
       }
      ]
    }
  }
}
```
Example of a client credential client application
```json
{
  "name": "$parameter('appName')",
  "sku": "app",
  "resourceType": "veracity.application",
  "locked": true,
  "sections": {
    "properties": {
      "isApi": false,
      "clientType": "ClientCredentials",
      "redirectUrls": [],
      "applicationUrl": null,
      "publishedScopes": [],
      "services": [],
      "secretManagementOptions": "none",
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
         "apiClientId": "$parameter('apiClientId')",
         "scopes": ["user_impersonation"]
       }
      ]
    }
  }
}
```
Example of a spa client application
```json
{
  "name": "$parameter('appName')",
  "sku": "app",
  "resourceType": "veracity.application",
  "locked": true,
  "sections": {
    "properties": {
      "isApi": false,
      "clientType": "Spa",
      "redirectUrls": ["$parameter('appReplyUrl')"],
      "applicationUrl": null,
      "publishedScopes": [],
      "services": [],
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
         "apiClientId": "$parameter('apiClientId')",
         "scopes": ["user_impersonation"]
       }
      ]
    }
  }
}
```
