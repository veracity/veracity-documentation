---
author: Veracity
description: This is the changelog for the January 2025 release of Data Workbench.
---

# January 2025 second release
Read this page to learn what has changed in Veracity Data Workbench with the second release in January 2025.

## New features
This section covers new features.

### Improved UI scaling for smaller screens
We have improved scaling in the UI for smaller screens to make it easier to use Data Workbench on devices with screen size below 1280 pixels.

### Workspace details page
We have added a page with workspace details. To find it, open the Workspace page and then select the **Details** tab.

On this tab, you can see the following:
* Workspace name
* Region
* Workspace description

If you are a workspace admin, you can also edit this information. However, you cannot change workspace's region.


### Add or edit workspace description
Now, workspace admins can add workspace descriptions when creating or editing a workspace. They can use this description to provide helpful information on the workspace; for example, what kind of data sets are shared inside it, who's using it, and for what.

As a workspace admin, to edit workspace description, go to Workspace > Details and, on the **Workspace details** tile, select the editing icon.

### See user's tenant access level
Now, in Workspace > Members, you can see user's tenant access level and workspace access level. If your role allows it, you can also change user's access level.

Users can have the following access levels in a tenant.

Tenant Admin:
* This level has the highest level of access.
* They can fully manage the account and all workspaces within it.
* This includes managing users, data, and all other aspects of the account.

Tenant Contributor:
* This level has access to all workspaces within the account.
* They can manage the data within these workspaces.
* However, they cannot manage users.

Tenant Reader:
* This level has the lowest level of access.
* They can only view all workspaces within the account.
* This is useful for oversight or auditing purposes.

Important Notes:
* Unless explicitly changed, users have the same role in each workspace within the tenant.
* User roles can only be upgraded within a workspace, not downgraded.
* Users cannot be removed from a workspace.

Users can have the following access levels in a workspace.

Workspace Admin:
* Has full control over the workspace.
* This includes managing users and all workspace functions.

Workspace Contributor:
* Has access to all workspace functions.
* However, they cannot manage users or the workspace itself.

Workspace Reader:
* Has limited access to the workspace.
* They can view content, share data, and download data within the workspace.

### Data set schema information
You can now view the schema description for each dataset in the datasets list. This provides additional context and understanding of the data within the dataset. The `schemaDescription` field is now included in the response of the `/workspaces/{workspaceId}/datasets/query` endpoint.

### Get workspace details via API
You can now retrieve detailed information about a workspace calling the following endpoint `/tenants/{tenantIdOrAlias}/workspaces/{workspaceId}`. This API returns the workspace ID, name, description, and region.

### Update workspace details via API
You can now update the name and description of a workspace calling the following endpoint `/tenants/{tenantIdOrAlias}/workspaces/{workspaceId}`.

## Changes in existing features

### Updated text in the tick box allowing resharing
We have updated the text in the tick box that you can select when sharing a data set, file, or folder. If you select it, it allows the recipient to share the data set, file, or folder with other people.

