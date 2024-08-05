---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Access Control
Access control is defined within the security bounday of a Workspace.

## Tenant
A tenant can contain one or several workspaces.

## Workspace
Each workspace has a dedicated data container.

A portfolio in asset model (group of assets/sites) is represented as workspace. The users given access to the workspace has access to the assets in this workspace/portfolio.

## Roles in workspace
Currently the following roles are available:
* Admin: can upload data, execute analytics
* Reader: can only view information
* Tenant administrator: can add new workspaces, has admin access to all workspaces in tenant

## Apis
