---
author: Veracity
description: This page explains how to utilize the analytics capabilities
---

# Execute analytics
Analytics scripts can be executed from UI in Data Workbench or by using APIs.

## API endpoints
To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json).

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)

## Execute analytics from API

```
POST: {base url}/workspaces/{workspaceId}/Analysis/execution 
```
Body
```
{
  "datasetIds": [
    "string"
  ],
  "provider": "string",
  "script": "string",
  "outputDatasetName": "string"
}
```
- Provider: Name of script provider
- Script: Name of analytic script to run
- OutputdatasetName: Name of the result dataset that will be uploaded to same workspace as the input dataset(s)


## How to debug
At the moment this is not possible. We are planning to support an IDE environment-

How to define input
How to store output
How to visualize
Transform data
Scheduler 
