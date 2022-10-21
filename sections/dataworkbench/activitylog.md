---
author: Veracity
description: This page explains activity logging in Data Workbench.
---
# Activity logs
Data Workbench logs the following events:
* Adding new user to Data Workbench.
* Changes to tenant (created, role added, role deleted).
* Changes to tenant members (invited member, member role updated, member deleted).
* Changes to workspaces (created, changed workspace description, role added, role deleted).
* Changes to workspace members (invited member, member role updated, member deleted).
* Changes to schemas (added, updated).
* Changes to schema versions (add schema version to schema, change default schema version of schema).
* Changes to data sets (created, modified, deleted, shared or revoked access).
* Changes to connections (created, modified, deleted).
* Changes to connector (created, modified, deleted).
* Changes to service accounts for API sharing (created, updated, regenerate service account secret, deleted).

To see the activity log for a workspace, go to the **Workspace** tab. Then, under the bar with an arrow, go to the **Activity log** tab.

## Filters
Under the **Activity log** tab, you can select one or more filters. You can filter the logs by:
* The time range of the changes.
* The actions performed.
* The entities that were changed.
* The users who have performed an action (text search).

To select a filter:
1. Select the name of a filter. A dropdown window will appear. 
2. In the window,  check the values you want to filter by.
3. At the bottom of the window, select the **Apply** button.

To change the values you are filtering by:
1. Select the name of a filter. A dropdown window will appear. 
2. In the window,  uncheck the values you do not want to filter by.
3. At the bottom of the window, select the **Apply** button.

To deselect a filter with all its values:
1. Select the name of a filter you have applied. A dropdown window will appear. 
2. At the bottom of the window, select the **Clear filter** button.

To deselect all the filters, in the right corner of the window and above the logs, select the **Clear all filters** button.
