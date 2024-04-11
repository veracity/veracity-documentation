---
author: Veracity
description: This is the changelog for the second April 2024 release of Data Workbench.
---

# April 2024 second release
Release date: 11 April 2024

Read this page to learn what has changed in Veracity Data Workbench with the April 2024 second release. Now, we enable you to check through API who has shared data sets with you so that you know where they come from and can easily identify their context. We also give you access to more API endpoints for tenant and workspace so that you can automate your work with APIs.
## New features
This section covers new features.

### Query share owners by data set ID list
You can query who shared the data sets with you so that you understand the data set context by using the POST method and calling the following endpoint.

`https://api.veracity.com/veracity/dw/gateway/api/v1/{workspaceId:guid}/shares/sharedBy/Query`

Request payload

```json
{
"datasetIds": [
    "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  ]
}
```

Sample response

```json
[ {
        "datasetId": "f80b0de1-3b1d-4a64-aa4d-88d6073ff1cd",    // ID of the data set
        "sharedBy": {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",   // ID of the shared user
            "sharedByType": "User",
            "name": "User Name"  // Name of the shared user
        }
    },
    {
        "datasetId": "6113fcaa-a29e-4804-b9a9-dac331676ee8",    // ID of the data set
        "sharedBy": {
            "id": "a1d9ef10-39c3-4d3a-8c33-241a0b1138a1",   // ID of the shared workspace
            "sharedByType": "Workspace",
            "name": "Workspace Name"  // Name of the shared workspace
        }
    }]
```

Note that:
* If the data sets were shared with a person, you must be this person or the person who initiated the share. 
* If the data sets were shared with a workspace, you must be a member of this workspace.

### Create a workspace in a tenant
You can create a workspace belonging to a specified tenant by using the POST method and calling the following endpoint.

`https://api.veracity.com/veracity/dw/gateway/api/v1/tenants/{tenantId:guid}/workspaces`

Request payload

```json
{
     "name": "string",
     "description": "string"
}
```

Sample response

```json
{
  "id": "196a8ff4-dfbc-4ee7-ae08-4f38b84d9c86",
  "name": "SHANGHAI",
  "description": "WS SHANGHAI"
}
```

### Get workspace by its ID
You can retrieve a workspace through its ID by using the GET method and calling the following endpoint.
`https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId:guid}`

Sample response

```json
{
    "id": "6113fcaa-a29e-4804-b9a9-dac331676008",
    "name": "Workspace Name1",
    "description": "Workspace created by test1"
}
```


### Get all workspaces in a tenant
You can get all workspaces that belong to a specified tenant by using the GET method and calling the following endpoint.

`https://api.veracity.com/veracity/dw/gateway/api/v1/tenants/{tenantId:guid}/workspaces`

Sample response

```json
[
    {
        "id": "6113fcaa-a29e-4804-b9a9-dac331676008",
        "name": "Workspace Name1",
        "description": "Workspace created by test1"
    },
    {
        "id": "89a1fcaa-D43e-9802-c879-cad886785129",
        "name": "Workspace Name2",
        "description": "Workspace created by test2"
    }
]
```

### Get all users and role scopes in a tenant
You can get all users and their assigned role scopes in a specified tenant by using the GET method and calling the following endpoint.

`https://api.veracity.com/veracity/dw/gateway/api/v1/tenants/{tenantId:guid}/users/roles`

Sample response

```json
{
    "result": [
        {
            "userId": "ddbf7526-abc3-45e2-bfd9-a2223a431a12",
            "email": "name.surname@dnv.com",
            "name": "Name Surname",
            "isServicePrincipal": false,
            "roleScope": {
                "role": "administrator",
                "scopeType": "Tenant",
                "scopeRef": "c39867d7-a4c0-4ae2-8281-7d45936a3bec"
            }
        },
        {
            "userId": "e574383d-994e-4a3d-9a7d-5d76755552e1",
            "email": "Name.Surname@dnv.com",
            "name": "Name Surname",
            "isServicePrincipal": false,
            "roleScope": {
                "role": "reader",
                "scopeType": "Tenant",
                "scopeRef": "c39867d7-a4c0-4ae2-8281-7d45936a3bec"
            }
        }
    ],
    "pageIndex": 1,
    "pageSize": 2,
    "totalCount": 65,
    "totalPages": 33
}
```

### Get all users and role scopes in a workspace
You can get all users and their assigned role scopes in a specified workspace by using the GET method and calling the following endpoint.

`https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId:guid}/users/roles`

Sample response

```json
{
    "result": [
        {
            "userId": "ddbf7526-abc3-45e2-bfd9-a2223a431a12",
            "email": "name.surname@dnv.com",
            "name": "Name Surname",
            "isServicePrincipal": false,
            "roleScope": {
                "role": "administrator",
                "scopeType": "Workspace",
                "scopeRef": "c39867d7-a4c0-4ae2-8281-7d45936a3bec"
            }
        },
        {
            "userId": "e574383d-994e-4a3d-9a7d-5d76755552e1",
            "email": "Name.Surname@dnv.com",
            "name": "Name Surname",
            "isServicePrincipal": false,
            "roleScope": {
                "role": "reader",
                "scopeType": "Workspace",
                "scopeRef": "c39867d7-a4c0-4ae2-8281-7d45936a3bec"
            }
        }
    ],
    "pageIndex": 1,
    "pageSize": 2,
    "totalCount": 65,
    "totalPages": 33
}
```