---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Schema management 
You can manage your workspace's schema with API calls. You can do CRUD operations for the following endpoints.

## Schema API endpoints
To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json).
(see subsection Scehma)

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](auth.md).


### To get a list of workspace schemas for a specific workspace
Call the {baseurl}/workspaces/{workspaceId}/schemas endpoint. 

To get the schema, add to the request `includeDefaultSchemaVersion=true`.

Below you can see an example of a successful response (code 200).

```json
    "result": [
        {
            "id": "7c312976-3d3d-4te3-9234-12f238f71234",
        "workspaceId": "00000000-0000-0000-0000-000000000000",
        "name": "DCS Period Summary",
        "description": "Aggregated emissions per DCS period including verification status, grouped by owner and flag",
        "industry": "Maritime",
        "isPredefined": true,
        "avatarColor": 55,
        "createdBy": "c44e1e55-fa3a-4553-b974-87eb50e41234",
        "createdOn": "2022-05-23T11:42:34.9558871Z",
        "lastModifiedBy": "c44e1e55-1232-4553-b974-87eb50e41234",
        "lastModifiedOn": "2022-05-23T11:42:34.9558871Z"
    },
 {
        "id": "2a0b9aa7-b7d5-4fbb-9a59-850459cd1234",
        "workspaceId": "e03c005e-1adf-456a-9d84-3f8694831234",
        "name": "TEST Name",
        "description": "TEST DESCRIPTION",
        "industry": "",
        "isPredefined": false,
        "avatarColor": 60,
        "createdBy": "2f3t7ee2-1234-4d25-af86-f5364fcb1234",
        "createdOn": "2022-06-07T06:49:35.5587386Z",
        "lastModifiedBy": "2f2e7ae3-1234-4d25-af86-f5364fcb1234",
        "lastModifiedOn": "2022-06-17T08:55:25.063984Z"
    }
```

### To get a schema by its ID
Call the following endpoint with the GET method.
`{baseUrl}/workspaces/{workspaceId}/Schemas/{schemaId}`

### To get schema version ID
Call the following endpoint with the GET method.

`{baseUrl}/workspaces/{workspaceId}/Schemas/schemaversions/{schemaVersionId}`

### To create a new schema
Call the `{baseUrl}/workspaces/{workspaceId}/Schemas/add` endpoint with the POST method.

Note that only a workspace admin can do this.

### To patch a schema (change name, short name, or description)
Call the following  endpoint with the PATCH method.
`{baseUrl}/workspaces/{workspaceId}/Schemas/{schemaId}`

Note that only a workspace admin can do this.

### To add schema version
Call the following endpoint with the POST method.
`{baseUrl}/workspaces/{workspaceId}/Schemas/schemaversions/add`

Note that only a workspace admin can do this.

### To make schema version default
Call the following endpoint with the PATCH method.
`{baseUrl}/workspaces/{workspaceId}/Schemas/{schemaId}/schemaversions/{schemaVersionId}`

Note that only a workspace admin can do this.