---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Update assets
Instances of sites/assets can be ingested and updated using apis.

## API endpoints
To browse the api, [Asset Model Ingest](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/DataFabric-MMS-Ingest-API-swagger.json). 

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).


Each post/put request is within a tenant and tenant is hence part of query path. 
The tenant-alias to be used in query is given for the environment setup for you.  In these example "dnves" is used as example tenant.



## Access rights
Only users or service principles with access to an site can access the site; [for more details how to manage users](accesscontrol.md)

##Portfolio
A site needs to be added to a portfolio. A portfolio in AssetModel is a group of assets/sites that share access control. If portfolio already exist, use [query](assetmodelQuery.md) portfolio to get id.

When creating a new portfolio; a workspace in Data workbench is automatically created.
Only users with admin access on tenant level can create portfolios.

```
POST: https://baseurl/dnves/api/v1/portfolios

{
  "portfolioId": "",
  "portfolioName": "Test"
}
```

**Note:** If a workspace already exist in Data Workbench, and you want to create a portfolio that corresponds, use workspace id as portfolio Id.


##Ingest a new site with a given id
Site ID must be a unique string (does not have to be a guid). If site id is not given, 

Minimum body when ingesting:
```
POST: https:/baseUrl/dnves/api/v1/portfolios/8de4a677-eff8-4142-9d1c-635c94b24155/sites 

{
  "siteId": "Test123",
  "name": "Test Asset",
  "modelType": "Site",
  "metadata": [], 
  "parameters": [],   
  "devices": [],         
  "hierarchies": [],    
  "internalStatus": [
    {
      "timestamp": "2024-08-01T12:02:31.782Z",
      "severity": 0,
      "name": "status",
      "value": "Draft"
    }
  ]
}

```
- If siteId is null in body; the system will automatically generate an guid as a unique id

Since this is a async operation, the id returned is job-id and not site id

** Create site synchronized**
```
POST: https:/baseUrl/dnves/api/v1/portfolios/8de4a677-eff8-4142-9d1c-635c94b24155/sites/sync 

Same body as async
```

## Update set of metadata
In this example an array of two metadata are updated. Name is metadata name according to standard. 
```
PUT: https://baseUrl/dnves/api/v1/sites/Test123
Body:
{
  "metadata": [
    {
      "name": "City",
      "unit": "string",
      "value": "Boulder"
    },
   {
      "name": "AllowStuck",
      "unit": "MM",
      "value": 44
    }
  ]
}
```

##Update single metata
```
PUT: https://we1dnvtwappvcvingest.azurewebsites.net/dnves/api/v1/sites/test123/metadata/City
Body:
{
  "unit": "string",
  "value": "Boulder"
}
```
##Update set of parameters
Parameters are the same as signals/data channels and represents the name of a monitored value typically coming from sensors. The names of the parameter must exist in the standard.

When parameterId is not given, a unique signal id is created. 
```
{
  "parameters": [
    {
      "name": "AirPressure",
      "parameterId": "",
      "alternativeId": "",
      "unit": "Pa"
    },
{
      "name": "Azimuth",
      "parameterId": "",
      "alternativeId": "",
      "unit": "Deg"
    }
  ]
}
```

## Devices
Devices are created and updated much the same way as site using
POST for new devices
PUT for updating. Parameters and metadata can be updated in batch on a single device or one by one

```
https://baseUrl/dnves/api/v1/sites/Test123/devices/dev123/metadata
```

##Upsert whole site
The whole site can be updated with all content. 
**Note**: When using this methods metadata and parameters not listed will be removed:
-If metadata or parameters are is not listed, they will be removed
-If devices are not listed, they will be removed

Hierarchies are not affected!!
```
PUT: https://baseUrl/dnves/api/v1/portfolios/8de4a677-eff8-4142-9d1c-635c94b24155/sites/Test123

body:
{
  "name": "Test-Asset",
  "modelType": "Site",
  "metadata": [
     {
      "name": "City",
      "unit": "string",
      "value": "Boulder"
    },
   {
      "name": "AllowStuck",
      "unit": "",
      "value": 44
    }
  ],
  "parameters": [
    {
      "name": "AirPressure",
      "parameterId": "",
      "alternativeId": "",
      "unit": "Pa"
    },
{
      "name": "Azimuth",
      "parameterId": "",
      "alternativeId": "",
      "unit": "Deg"
    }
  ],
  "devices": [
    {
      "deviceId": "",
      "name": "Inv_1",
      "deviceType": "Inverter",
      "metadata": [
        {
          "name": "CapacityAC",
          "unit": "kW",
          "value": "1.0"
        }
      ],
      "parameters": [
        {
          "name": "CommStatus",
          "parameterId": "",
          "alternativeId": "",
          "unit": "string"
        }
      ]
    }
  ]
}
```



## Set internal status on site
Internal status is a list of different status with name and value. The status shown in UI is named status and has the following values: draft, production

Internal status can be set with 
```
POST:   https://baseurl/dnves/api/v1/sites/Test123/status

{
  "name": "status",
  "severity": 0,
  "value": "production"
}
```

You can still create your own internal statuses - and read these using the query api


## Update multiple versions of metadata
The assessment feature of Asset Model allows for several versions of same metadata.
Assessment types are defined as part of the [standard](standard.md). An assessment of a selectred type can be added to a site and values for its defined metadata fields can be specified.

Feature is under work.