---
author: Veracity
description: This is the changelog for the December 2025 release of Data Workbench.
---

# December 2025 release
Read this page to learn what has changed in Veracity Data Workbench with the December 2025 release.

## New features  
This section covers new features.

### Programmatic sharing of datasets and storage  
You can now create shares for datasets and file storage via API. This includes:
- Sharing a dataset with a user or workspace.
- Sharing file storage with a user or workspace, including specifying a subfolder path and access level (`ReadAndWrite` or `ReadOnly`).
- Re-sharing shared datasets, subject to access permissions.
- Sharing a dataset with modifications (for example, filtered columns or queries), creating a new derived dataset for the recipient.

Only workspace administrators can share with `ReadAndWrite` access or apply modifications during sharing.

**New endpoints:**
- `POST /workspaces/{workspaceId}/storages/shares` – Share file storage with a user or workspace.
- `POST /workspaces/{workspaceId}/datasets/{datasetId}/shares` – Share a dataset with a user or workspace.
- `POST /workspaces/{workspaceId}/datasets/{datasetId}/shareasnew` – Share a dataset with modifications (e.g., filtered columns or queries).

Full details on these endpoints, including request payloads and responses, are available in the [**API Explorer**](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json).

### Revoke shares programmatically  
You can now revoke a share programmatically, enabling automated access management when collaborators no longer need access.

**New endpoint:**
- `POST /workspaces/{workspaceId}/shares/{shareId}/revoke` – Revoke a share (owner or workspace admin only).

See the **API Explorer** for full specifications.

### Retrieve and query shares via API  
Gain better visibility into data sharing with two new read operations.

**New endpoints:**
- `GET /workspaces/{workspaceId}/shares/{shareId}` – Get details of a specific share.
- `POST /workspaces/{workspaceId}/shares/query` – Query shares using filters such as dataset ID, receiver type, status, and creator.

These support auditability and integration with external tools. Refer to the [API Explorer](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json) for full request and response schemas.

### Event routing for updated datasets  
The platform now routes `DatasetUpdated` events to the Share service. This enables automatic updates to shared datasets when their source datasets change, ensuring consistency across shared data.

**Configuration change:**
- The `dataworkbench.dataset.updated` event is now routed to the `shareservice` subscription in the `sbt-dataset` event topic.

## Changes in existing features  
This section covers changes in existing features.

### Improved event handling for analytics  
The Share event listeners have been updated to ensure only necessary permissions are granted or revoked in response to sharing actions. This improves security and compliance in event-driven workflows.

### Controlled dataset and user synchronization  
A new configuration option allows control over synchronization during workspace onboarding:
- `IsSyncDatasets`: Determines whether tables/views are synced to Unity Catalog.
- `IsSyncUsers`: Controls whether users are synced.

This provides greater flexibility in managing analytics integrations.

### Unified storage for Unity Catalog  
For newly onboarded workspaces, managed tables in Unity Catalog now use the metastore’s storage account as the default location. This simplifies storage management and improves consistency.