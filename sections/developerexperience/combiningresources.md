---
author: Veracity
description: Combining resources
---

# Combining resources

Examples of how to connect resources together

## Already exsisting resources

Add your service, app, or api id to the template

### Services
Services are added to apps or API, they must be under the same resource group.

To add an exsisting service to an app or API, simply add the service id in the services array in the app/api json schema.

examples: 

```json
"services":["00000000-0000-0000-0000-000000000000"]
```
```json
"services":[
  "00000000-0000-0000-0000-000000000000",
  "00000000-0000-0000-0000-000000000000"
]
```
### App or API
Adding an authorized client application:
```json
"clients":[
            {
              "clientId": "00000000-0000-0000-0000-000000000000",
              "scopes": [ "user_impersonation"] 
            }
          ],
```
### Adding API access:
APIs and scopes the application is authorized to use. Only APIs in the same project can be added.
```json
"clients":[
             {
               "apiClientId":"00000000-0000-0000-0000-000000000000",
               "apiName":"TestApi",
               "scopes":["user_impersonation"]
             }
          ],
```
## Resources created during runtime
Resources that are added to another resource in the same call as they are created must follow be processed first. This goes from top to bottom based on the provided template.
Best practice is to create services before apps or API.

### Example: A service, an app and an API created and connected together at runtime
Use a JMESPath query to get the id from the resourcesthat have been created

In this example the service is created first, then as the Confidential app is created, a query for the serviceid is executed:
```json
  "$resources[?name== parameter('serviceName')].id"
```
As the API is created the process is repeated to add the client to the api with provided scopes
```json
"clients": [
             {
               "clientId": "$resources[?name== parameter('appName')].id",
               "scopes": [ "user_impersonation", "user_management" ] 
             }
           ]
```
Full example
```json
{
  "resourceGroup": {
  "name": "$parameter('rgName')",
  "description": "testing",
  "tags": [ "test" ],
  "isProduction": false,
  "locked":false,
 },
 "resources": [
    { 
      "name": "$parameter('serviceName')",
      "sku": "standard",
      "resourceType": "veracity.service",
      "locked": true,
      "sections": {
        "properties": {
          "businessOwnerId": null,
          "description": "",
          "category": null,
          "shortName": "NP_service",
          "openInNewTab": true,
          "visible": false,
          "serviceUrl": "$parameter('serviceUrl')",
          "shortDescription": "",
        },
        "advanced": {
          "passwordPolicy": null,
          "accessLevels": {
            "useAccessLevels": false,
            "accessLevels": null
          }
        }
      }
    },
    { 
      "name": "$parameter('appName')",
      "sku": "app",
      "resourceType": "veracity.application",
      "locked": true,
      "sections": {
        "properties": {
          "isApi": false,
          "clientType": "Confidential",
          "redirectUrls": ["$parameter('appReplyUrl')"],
          "applicationUrl": "$parameter('appUrl')",
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
              "apiClientId": "$parameter('apiClientId')",
              "scopes": ["user_impersonation"]
            }
          ]
        }
      }
    },
    {
      "name": "$parameter('apiName')",
      "sku": "api",
      "resourceType": "veracity.application",
      "locked": true
      "sections": {
        "properties": {
          "isApi": true,
          "clientType": "None",
          "redirectUrls": [],
          "applicationUrl": null,
          "publishedScopes": [
            {
              "scopeName": "user_management",
              "description": "user_management"
            },
	         {
              "scopeName": "user_impersonation",
	            "description": "test av scopes"
            }
          ],
          "services": []
        },
        "advanced": {
          "apiProductSubscriptions": [
            {
              "productId": "veracity-platfrom-api",
              "productName": "Veracity Platform API"
            }
          ],
          "clients": [
            {
              "clientId": "$resources[?name== parameter('appName')].id",
              "scopes": [ "user_impersonation", "user_management" ] 
            }
          ],
          "apiAcceses": [
            {
              "apiClientId": "$parameter('apiClientId')",
              "scopes": ["user_impersonation"]
            }
          ]
        }
      }
    }
  ],
  "outputs": [
    {
      "name": "serviceId",
      "value": "$resources[?name== parameter('serviceName')].id",
      "type": "string"
    },
    {
      "name": "appId",
      "value": "$resources[?name== parameter('appName')].id",
      "type": "string"
    },
    {
      "name": "apiId",
      "value": "$resources[?name== parameter('apiName')].id",
      "type": "string"
    }
  ]
}
```
