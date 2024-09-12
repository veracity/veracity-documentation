---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Datasharing
Datasets can be shared to users and businesses.

## Schema API endpoints
To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json).
(see subsection Shares)

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](auth.md).

## Get share owner info

```
POST {baseurl}/workspaces/{workspaceId}/schemas endpoint. 
```
BODY

```json
{
  "datasetIds": [
    "string"
  ]
}
```

The response lists xxx