---
author: Veracity
description: This page explains how to utilize the analytics capabilities
---

# Execute analytics
Analytics scripts can be executed from [UI in Data Workbench](https://developer.veracity.com/docs/section/dataworkbench/analytics) or by using APIs.

## API endpoints
To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json).

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).

### Baseurl
Check Data Workbench API in the page [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)

## Execute analytics from API

```
POST: {base url}/workspaces/{workspaceId}/analysis/executions 
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
- DatasetIds: Array of input dataset(s)' id. Depending on the script, it can be empty array [] or one item or more itmes.
- Provider: Name of script provider, Like workspaceId or "GPM"
- Script: Name of analytic script to run
- OutputdatasetName: Name of the result dataset that will be uploaded to same workspace as the input dataset(s), it is optional.


## How to debug
At the moment this is not possible. We are planning to support an IDE environment-

How to define input
How to store output
How to visualize
Transform data
Scheduler 
