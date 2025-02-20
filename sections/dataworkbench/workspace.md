---
author: Veracity
description: This page explains activity logging in Data Workbench.
---
# Workspace
The workspace page has three tabs:
* Members: Workspace member management.
* Details: Workspace name, region, and description.
* Activity log: Logs of all activity in a workspace.

## Members and access levels
Under **Workspace members**, you can use the search bar to find a workspace member by their name or email.
For each member, you see the following data:
* Name
* Email
* Tenant access level
* Workspace access level

Regarding **Tenant access level**:
* User can belong to a tenant containing this workspace and have a Tenant Admin or Tenant Reader role in this tenant.
* Tenant Admin can fully manage the account (tenant) and all workspaces.
* Tenant Reader can only view all workspaces and read data in them.
* By deafult, user's tenant role gives them the same permissions in each workspace in this tenant.
* A Tenant Admin or Tenant Reader cannot be removed from a workspace in this tenant.
* You can upgrade Tenant Reader's permission in a workspace to Workspace Admin.

Regarding **Workspace access level**:
* Workspace Admin has full control over the workspace, including managing users (add, change role, remove) and all functions.
* Workspace Reader has limited access to view content, share data, and download data within the workspace.

### To add workspace members
To add one or more members to the workspace:
1. In the top right corner, select **Invite workspace members**.
3. Enter the member's email address and select the member's role ("Reader" or "Admin").
If the member is not registered in Veracity, you will be prompted to invite them to Veracity.
4. Select the **Add** button. It will add the member to the workspace. You can add more than one member.
5. Select the **Invite** button. It will send the member a message informing they were added to the workspace.

<figure>
	<img src="assets/invite.png"/>
</figure>

### To change member's role
To change a member's role:
1. Find the member in the list.
2. In the row with the member, locate the **Tenant access level** or **Workspace access level** column.
3. In the column, select the member's current role and, in the dropdown that shows, select another role for the member.

Note that:
* To change tenant access level for a member, you need to be Tenant Admin.
* To change workspace access level for a member, you need to be Tenant Admin or Workspace Admin.

### To remove member
To remove a member from the workspace:
1. Find the member in the list.
2. In the row with the member's name, select ***⋯*** (three dots). It will open a dropdown.
3. From the dropdown, select **Delete**.

To remove multiple members from the workspace:
1. Next to the members you want to remove, tick the tickbox.
1. In the top right corner, select the garbage can icon.

<figure>
	<img src="assets/removemany.png"/>
</figure>

## Details
The details tab shows:
* Workspace name: The display name for this workspace.
* Region: Where this workspace's data is stored (EU or USA). Note that after you select a Region, you cannot change it.
* Description: Workspace description.

## Activity log
Data Workbench logs the following events with the information who did the action and when (in UTC time format):
* Adding new member to Data Workbench.
* Changes to tenant (created, role added, role deleted).
* Changes to tenant members (invited member, member role updated, member deleted).
* Changes to workspaces (created, changed workspace description, role added, role deleted).
* Changes to workspace members (invited member, member role updated, member deleted).
* Changes to schemas (added, updated).
* Changes to schema versions (add schema version to schema, change default schema version of schema).
* Changes to data sets (created, modified, deleted) and access to them (including granting and revoking SAS access keys).
* Downloading a data set.
* Changes to data integrations (created, modified, deleted).
* Changes to service accounts for API sharing (created, updated, regenerate service account secret, deleted).