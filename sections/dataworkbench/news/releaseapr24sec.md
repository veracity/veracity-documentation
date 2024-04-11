---
author: Veracity
description: This is the changelog for the April 2024 release of Data Workbench.
---

# April 2024 second release
Release date: 11 April 2024

Read this page to learn what has changed in Veracity Data Workbench with the April 2024 second release. Now, we enable you to check through API who has shared data sets with you so that you know where they come from and can indentify their context easily. We also give you access to more API endpoints for tenant and workspace so that you can automate your work with APIs.

## New features
This section covers new features.

### Query share owners by data set ID list
You can query who shared the data sets with you so that you understand the data set context. To do so, use the POST method and call the following endpoint.

`/gateway/api/v{v:apiVersion}/workspaces/{workspaceId:guid}/shares/sharedBy/Query`

Payload
`{
datasetIds: guid[]
}`

Response
` [{
datasetId: guid,
sharedBy { .... }
}]`

Note that:
* If the data sets were shared with a person, you must be this person or the person who initiated the share. 
* If the data sets were shared with a workspace, you must be a member of this workspace.

### Create a workspace in a tenant
You can create a workspace belonging to a specified tenant. To do so, use the POST method and call the following endpoint.

`/gateway/api/v{v:apiVersion}/tenants/{tenantId:guid}/workspaces`

Request
`{
     Name,
     Description}
     `
Response
`{
  id: string,
  name:  string,
  description:  string
}`

### Get workspace by its ID
You can retrieve a workspace through its ID. To do so, use the GET method and call the following endpoint.
`/gateway/api/v{v:apiVersion}/workspaces/{workspaceId:guid}`

Response
`{
    id: string,
    name: string,
    description: string
}`

### Get all users and role scopes in a tenant
You can get all users and their assigned role scopes in a specified tenant. To do so, use the GET method and call the following endpoint.

`/gateway/api/v{v:apiVersion}/tenants/{tenantId:guid}/users/roles`

Response
`{
    "result": [
        {
            "userId": "ddbf7526-abc3-45e2-bfd9-a2223a431a12",
            "email": "Jane.Yao@dnv.com",
            "name": "Jane Yao",
            "isServicePrincipal": false,
            "roleScope": {
                "role": "administrator",
                "scopeType": "Tenant",
                "scopeRef": "c39867d7-a4c0-4ae2-8281-7d45936a3bec"
            }
        },
        {
            "userId": "e574383d-994e-4a3d-9a7d-5d76755552e1",
            "email": "Jork.Cao@dnv.com",
            "name": "Jork Cao",
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
}`

### Get all users and role scopes in a workspace
You can get all users and their assigned role scopes in a specified workspace. To do so, use the GET method and call the following endpoint.

`/gateway/api/v{v:apiVersion}/workspaces/{workspaceId:guid}/users/roles`

Response
` {
    "result": [
        {
            "userId": "3e4d0494-0bad-41fb-aa1f-0c2e53516171",
            "email": "Nana.Ouyang@dnv.com",
            "name": "Nana Ouyang",
            "isServicePrincipal": false,
            "roleScope": {
                "role": "administrator",
                "scopeType": "Workspace",
                "scopeRef": "961a8ff4-dfbc-4ee7-ae08-4f38b84d9c86"
            }
        },
        {
            "userId": "cc4c079a-5411-6899-8dd4-b8783f9417a8",
            "email": "Ina.Zhang@dnv.com",
            "name": "Ina Zhang",
            "isServicePrincipal": false,
            "roleScope": {
                "role": "reader",
                "scopeType": "Workspace",
                "scopeRef": "961a8ff4-dfbc-4ee7-ae08-4f38b84d9c86"
            }
        }
    ],
    "pageIndex": 1,
    "pageSize": 2,
    "totalCount": 53,
    "totalPages": 27
}`