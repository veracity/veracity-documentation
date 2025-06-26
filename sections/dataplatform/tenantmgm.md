---
author: Veracity
description: This page lists available nuget packages
---

# Managing tenants and workspaces

## API endpoints
To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json).
See section Tenants

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)
(data workbench api)

## To check what workspaces you can access within a tenant
Call the `{baseurl}/tenants/{tenantId}/workspaces` endpoint with a GET method.


## To create a workspace in a tenant
You can create a workspace belonging to a specified tenant by using the POST method and calling the following endpoint.
This require user to be tenant admin.

`{baseUrl}/tenants/{tenantId:guid}/workspaces`

Below you can see a sample request payload.

```json
{
     "name": "string",
     "description": "string",
      "region": "string"
}

```
Region should be "EU" or "US" depending on which region the data should be located in (data residency)

Below you can see a sample response.

```json
{
  "id": "196a8ff4-dfbc-4ee7-ae08-4f38b84d9c86",
  "name": "SHANGHAI",
  "description": "WS SHANGHAI",
  "region": "EU"
}
```

## To get workspace by its ID
You can retrieve a workspace through its ID by using the GET method and calling the following endpoint.
`{baseUrl}/workspaces/{workspaceId:guid}`

## To query activity logs for a workspace
Call the endpoint {baseurl}/workspaces/{workspaceId}/ledger providing the ID of the workspace.

You can add to the request a page size and page index, for example `PageSize=1&PageIndex=5`.


## Users and roles

### To get all users and role scopes in a tenant
You can get all users and their assigned role scopes in a specified tenant by using the GET method and calling the following endpoint.

`{baseUrl}/tenants/{tenantId:guid}/users/roles`


### To get all users and role scopes in a workspace
You can get all users and their assigned role scopes in a specified workspace by using the GET method and calling the following endpoint.

`{baseUrl}/workspaces/{workspaceId:guid}/users/roles`

