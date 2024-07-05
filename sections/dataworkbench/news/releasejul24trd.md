---
author: Veracity
description: This is the changelog for the July 2024 third release of Data Workbench.
---

# July 2024 third release

Read this page to learn what has changed in Veracity Data Workbench with the July 2024 third release.

## New features
This section covers new features.

### Manage schemas with API
Now, as a workspace admin, you can manage your workspace's schema with API calls.

You can do CRUD operations for the following endpoints.

**To create a new schema**

Call the `https://api.veracity.com/veracity/dw//gateway/api/v1/workspaces/{workspaceId}/Schemas/add` endpoint with the POST method.

**To get a schema by its ID**

Call the `https://api.veracity.com/veracity/dw//gateway/api/v1/workspaces//{workspaceId}/Schemas/{schemaId}` endpoint with the GET method.

**To patch a schema (change name or description)**

Call the `https://api.veracity.com/veracity/dw//gateway/api/v1/workspaces/{workspaceId}/Schemas/{schemaId}` endpoint with the PATCH method.

**To add schema version**

Call the `https://api.veracity.com/veracity/dw//gateway/api/v1/workspaces/{workspaceId}/Schemas/Versions/add` endpoint with the POST method.

**To get schema version ID**

Call the `https://api.veracity.com/veracity/dw//gateway/api/v1/workspaces/{workspaceId}/Schemas/Versions/{schemaVersionId}` endpoint with the GET method.

**To make schema version default**

Call the `https://api.veracity.com/veracity/dw//gateway/api/v1/workspaces/{workspaceId}/Schemas/{schemaId}/Versions/{schemaVersionId}` endpoint with the PATCH method.

You might want to see [Data Workbench endpoints documentation](../apiendpoints.md) and [how to integrate APIs with Data Workbench](../apimanagement.md).