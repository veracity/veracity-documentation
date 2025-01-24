---
author: Veracity
description: This page explains user management for a workspace in Data Workbench.
---
# User management

## User list
To see the user list, go to **Workspace** > **Members**. Users are listed in two tables, one containing only workspace members, and another containing only tenant members.

Each table:
* Shows user count in the top right corner.
* Shows the name, email, and role of each member.
* Becomes paginated if there are more than 20 members.

## Tenant versus workspace
**Tenant:** Represents an organization or company. A single tenant can have multiple workspaces.

**Workspace:** Represents a specific area or project within a tenant. Workspaces can be used to isolate data, teams, and permissions within an organization. For example, a company might have a separate workspace for each department, each geographical region, or each project.

## Tenant user roles
There are three roles for tenant users:
* Tenant Admin: This level has the highest level of access. They can fully manage the account and all workspaces within it. This includes managing users, data, and all other aspects of the account.
* Tenant Contributor: This level has access to all workspaces within the account. They can manage the data within these workspaces. However, they cannot manage users.
* Tenant Reader: This level has the lowest level of access. They can only view all workspaces within the account. This is useful for oversight or auditing purposes.

Note that:
* Tenant users have the same role in each workspace within a tenant unless explicitly changed on the workspace level.
* User roles can only be upgraded within a workspace, not downgraded.
* Users cannot be removed from a workspace.

## Workspace user roles
There are three roles for workspace users:
* Workspace Admin: Has full control over the workspace. This includes managing users and all workspace functions.
* Workspace Contributor: Has access to all workspace functions except user and workspace management.
* Workspace Reader: Has limited access to the workspace. They can view content, share data, and download data within the workspace.

A user can only have one role. There must be at least one admin per workspace.

## To add users
To add one or more users to the workspace:
1. In the workspace, go the **Workspace** tab.
2. In the left corner, go to the **Members** tab. Then, in the right corner, select "+ Invite members".
3. Enter the user's email address and select the user's role ("Reader" or "Admin").
If the user is not registered in Veracity, you will be prompted to invite them to Veracity.
4. Select the **Add** button. It will add the user to the workspace. You can add more than one user.
5. Select the **Invite** button. It will send the user a message informing they were added to the workspace.


## To change user's role
To change a user's role:
1. In the workspace, go the **Workspace** tab.
2. In the left corner, go to the **Members** tab. You will see a list of all users in the workspace.
3. Find the user in the list. You can see their role in the right corner of the row. 
4. Select the user's role. It will open a dropdown. 
5. From the dropdown, select a new role for the user.

## To remove a user
To remove a user from the workspace:
1. In the workspace, go the **Workspace** tab.
2. In the left corner, go to the **Members** tab.
3. Find the user in the list.
4. In the row with the user's name, select ***⋯*** (three dots). It will open a dropdown.
5. From the dropdown, select **Delete**.
