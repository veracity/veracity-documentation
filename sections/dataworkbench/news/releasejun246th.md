---
author: Veracity
description: This is the changelog for the June 2024 sixth release of Data Workbench.
---

# June 2024 sixth release

Read this page to learn what has changed in Veracity Data Workbench with the June 2024 sixth release.

## New features
This section covers new features.

### Check what workspaces you can access
Now, using Data Workbench API, you can check what workspaces you can access within a tenant. To do so, use the GET method and call the following endpoint.

https://api.veracity.com/veracity/dw/gateway/api/v1/tenants/{tenantId}/workspaces

### New Contributor role
We have added a new role called Contributor that API users can use. It has been assigned to all the existing service accounts with workspace-level access that previously had the Reader role.