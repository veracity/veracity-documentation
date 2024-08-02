---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Update assets
Instances of sites/assets can be ingested and updated using apis.

Explore the api [Asset Model Ingest](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/DataFabric-MMS-Ingest-API-swagger.json). 

## Ingest Rest api
Base url: https://api.veracity.com/veracity/mms/ingest/

Each post/put request is within a tenant and tenant is hence part of query path. 
The tenant-alias to be used in query is given for the environment setup for you.

## Authentication
Use bearer token and subscription key [for more details how to acquire a token](..authentication.md)

## Access rights
Only users or service principles with access to an site can access the site; [for more details how to manage users](accesscontrol.md)


##Ingest a new site with a given id
Site ID must be a unique string (does not have to be a guid)
Minimum body when ingesting:
```
POST: 
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