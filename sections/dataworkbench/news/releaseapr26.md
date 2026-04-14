This release adds a new endpoint and an optional parameter to another endpoint in Data Workbench API.


## New endpoint to get tenants and workspaces for current user
We have added a new endpoint `me/tenants` that gets a list of all tenants and their associated workspaces for the current user.

This endpoint has two parameters:
- `tenantIdOrAlias` (string, optional): returns a specific tenant by its ID or alias
- `includeRoleName` (boolean): if `true`, returns current user roles in tenants and workspaces

For details on this endpoint, check [API specification](https://docs.veracity.com/apis/platform/dataworkbenchv2) under section **Tenants V2**.

## Added parameter to get schema version for shared dataset
Previously, you could not read schema definition for a dataset that was shared to your workspace from another workspace.

Now, the endpoint `workspaces/{workspaceId}/datasets/{datasetID}` has an optional parameter (boolean) `includeSchemaVersion=true/false`. When you set this parameter to `true`, the response to your API calls will include full schema version details inside `schemaInfo`.

For details on this endpoint, check [API specification](https://docs.veracity.com/apis/platform/dataworkbenchv2) under section **Datasets V2**.
