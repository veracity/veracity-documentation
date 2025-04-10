---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Update assets
Instances of sites/assets can be ingested and updated using apis.

## API endpoints
To browse the api, [Asset Model Ingest](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/DataFabric-MMS-Ingest-API-swagger.json). 

**Example for Ingest**
https://api.veracity.com/veracity/mms/ingest/dnves/api/v1
(when tenantAlias in dnves and api version is v1)

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).

Each post/put request is within a tenant and tenant is hence part of query path. 
The tenant-alias to be used in query is given for the environment setup for you.  In these example "dnves" is used as example tenant.

## Access rights
Only users or service principles with access to an site can access the site; [for more details how to manage users](accesscontrol.md)

## Create Portfolio
A site needs to be added to a portfolio. A portfolio in AssetModel is a group of assets/sites that share access control. If portfolio already exist, use [query](assetmodelQuery.md) portfolio to get id.


`POST: {baseurl}/{tenantAlias}/api/v1/portfolios`

```json
{
  "portfolioId": "",
  "portfolioName": "Test"
}
```


## Create sites
Use POST method to create a new site and PUT method to update existing sites. 
For ingest new site there is one endpoint for asyc and one for sync operations, see descriptions below.
The synch method only allows you to ingest site level data and information about devices and hierachies need to be posted in seperate methods. Whereas, the async method all information can be ingested in the body.

## Ingest a new site  (async operation)
Site ID must be a unique string (does not have to be a guid). If site id is not given, a guid is created

**Note:** The technology needs to be specified in the body. Workspaceid needs to be provided and needs to be an exisiting workspace in Dataworkbench. 


`POST: {baseUrl}/{tenantAlias}/api/v1/portfolios/{portfolioId}/sites`

Minimum body when ingesting:

```json
{
  "siteId": "Test123",
  "name": "Test Asset",
  "modelType": "Site",
  "technology": "Solar",
  "dwWorkspaceId": "string",
  "metadata": [], 
  "timeseries": [],   
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

If siteId is null in body; the system will automatically generate an guid as a unique id

Since this is a async operation, the id returned is job-id and not site id


## Create site as synchronized operation

`POST: {baseUrl}/{tenantAlias}/api/v1/portfolios/{portfolioId}/sites/sync`

The technology for the site must be defined in the body.

## Update whole site

If you need to syncronize from source to Asset Model on regular basis, the endpoint for updating whole site should be used:

**Note**: When using this methods metadata and timeseries-tags not defined in the source body will be removed from the target:
-If metadata or timeseries-tags are is not listed, they will be removed
-If devices are not listed, they will be removed
-Hierarchies are not affected!!

`PUT: https://baseUrl/{tenantAlias}/api/v1/portfolios/{portdolioId}/sites/{siteId}`

Example request body:
```
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
  "timeseries": [
    {
      "name": "AirPressure",
      "timeseriesId": "",
      "alternativeId": "",
      "unit": "Pa"
    },
{
      "name": "Azimuth",
      "timeseriesId": "",
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
      "timeseries": [
        {
          "name": "CommStatus",
          "timeseriesId": "",
          "alternativeId": "",
          "unit": "string"
        }
      ]
    }
  ]
}
```

## Update set of metadata
In this example an array of two metadata are updated. Name is metadata-name according to standard. 
```
PUT: {baseUrl}/{tenantAlias}/api/v1/sites/{siteId}/metadata
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

**Example**
`https://api.veracity.com/veracity/mms/ingest/{tenantAlias}/api/v1/sites/{siteId}/metadata`

## Update single metata

`PUT: {baseUrl}/{tenantAlias}/api/v1/sites/{siteId}/metadata/{metadataName}`

**Example**
In this example metadata filed City is updated on site Site123 in tenant dnves

`PUT: {baseUrl}/dnves/api/v1/sites/Site123/metadata/City`

Request Body:
```json
{
  "unit": "",
  "value": "Boulder"
}
```

## Update set of timeseries 
Timeseries are the same as signals/data channels and represents the name of a monitored value typically coming from sensors. The names of the timeseries must exist in the standard.

`PUT: {baseUrl}/{tenantAlias}/api/v1/sites/{siteId}/timeseries`

When parameterId is not given, a unique signal id is created. 
**Example request payload**
```
{
  "timeseries": [
    {
      "name": "AirPressure",
      "timeseriesId": "",
      "alternativeId": "",
      "unit": "Pa"
    },
{
      "name": "Azimuth",
      "timeseriesId": "",
      "alternativeId": "A123",
      "unit": "Deg"
    }
  ]
}
```

## Devices
Devices are created and updated much the same way as site using
- POST for new devices
- PUT for updating. Parameters and metadata can be updated in batch on a single device or one by one

### Add devices
Use POST method
If deviceId is not given, a guid is created

DeviceType should be the asset model of the device you are creating such as Meter, Inverter etc. The device TYpe needs to be defined in the standard
The technology for the device is inherited from the site.  

`POST {baseUrl}/{tenantAlias}/api/v1/sites/{siteId}/devices/dev123/metadata`

Request body:
```json
{
  "deviceId": "string",
  "name": "string",
  "deviceType": "Device",
  "metadata": [
    {
      "name": "string",
      "unit": "string",
      "value": "string"
    }
  ],
  "timeseries": [
    {
      "name": "string",
      "timeseriesId": "string",
      "alternativeId": "string",
      "unit": "string"
    }
  ]
```

### Change metadata on device
`PUT {baseUrl}/{tenantAlias}/api/v1/sites/{siteId}/devices/{deviceId}}/metadata`

Request body is array of metadata to change
```json
{
  "metadata": [
    {
      "name": "string",
      "unit": "string",
      "value": {}
    }
  ]
}
```
### Set signal on device
`PUT {baseUrl}/{tenantAlias}/api/v1/sites/{siteId}/devices/{deviceId}}/timeseries`

When signalId is not given, a unique signal id is created. 
**Request payload**
```
{
  "timeseries": [
    {
      "name": "string",
      "timeseriesId": "string",
      "alternativeId": "string",
      "unit": "string"
    }
  ]
}
```


## Set internal status on site
Internal status is a list of different status with name and value. The status shown in UI is named status and has the following values: draft, production

Internal status can be set with 

`POST:   {baseurl}/{tenantAlias}/api/v1/sites/{siteId}/status`

```
{
  "name": "status",
  "severity": 0,
  "value": "production"
}
```

You can still create your own internal statuses - and read these using the query api


## Update multiple versions of metadata
Some of the metadata describing an asset (a site) needs to exist with several values in order to support "what-if" scenarios. The assessment feature of Asset Model allows for several versions of same metadata. 

Assessment types are defined as part of the [standard](standard.md). When creating an Assessment type, it is given a name and a list of metadata that belongs to this assessment.

An assessment of a selected type can be added to a site and values for its defined metadata fields can be edited. This can be done from Web tool as well as APIs.

### Create new assessment on site

`POST:   {baseurl}/{tenantAlias}/api/v1/sites/{siteId}/assessments`

```
{
  "name": "string",
  "assessmentType": "string",
  "metadata": [
    {
      "name": "string",
      "unit": "string",
      "value": "string"
    }
  ]
}
```

assessmentType is the name of assessment type defined in Standard.
name: needs to be unique within the site

For metadata do one of the following;

- can be empty array. Then query the assessment of the site and use PUT to change the values
- Read the assessment from schema, and add all metadata with its new values

**Example**

Get assessment model name Irras-v2
`{baseurl}/{tenantAlias}/api/v1/assessment-models/Irrad-v2`

Use the response, and build an array of metadata to modify for the site

### Update assessment on site

`PUT:   {baseurl}/{tenantAlias}/api/v1/sites/{siteId}/assessments/{assessmentName}`

assessmentName is the name of the assessment to edit (not the assessment type)
