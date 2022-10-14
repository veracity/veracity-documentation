---
author: Veracity
description: This is a tutorial how to query data with Data Workbench.
---
# How to query for data?
If you want to query data, follow this tutorial for step-by-step instructions.

To query data:
1. Authenticate and authorize your API calls. See how to [here](authentication.md).
2. Find your workspace ID. To do so, see the URL of your workspace in a browser. The part after ```ws/```is the ID of your workspace.
3. Find the ID of a data set you want to query from. See how to do that [here](https://developer.veracity.com/docs/section/dataworkbench/apiendpoints#data-sets-endpoints).
4. Once you have the ID of a workspace and a data set, you can query for data by workspace ID, data set ID, and some additional properties. To do so, call the https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId}/datasets/{datasetId}/query endpoint.
You must provide the `{workspaceId}` (string, $UUID) and the {datasetId} (string, $UUID). You can use additional properties in your query. 

Below you can see a sample request body.

```json
{
  "pageIndex": 0,
  "pageSize": 0,
  "columnFilter": [
    "string"
  ],
  "queryFilters": {
    "additionalProp1": [
      "string"
    ],
    "additionalProp2": [
      "string"
    ],
    "additionalProp3": [
      "string"
    ]
  }
}
```

Below you can see an example of a successful request (code 200).

```json
{
  "data": [
    "string"
  ],
  "pagination": {
    "pageIndex": 0,
    "pageSize": 0,
    "totalPages": 0,
    "totalCount": 0
  }
}
```