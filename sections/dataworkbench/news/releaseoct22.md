---
author: Veracity
description: This is the changelog for the October 2022 release of Data Workbench.
---

# October 2022 release

Release date: October 2022

Read this page to learn what has changed in Veracity Data Workbench with the October 2022 release.

## New features

This section covers new features.

### API endpoints for querying activity logs
Now, you can query activity logs (ledgers) on the workspace or data set level. 

To query activity logs for a workspace, call the endpoint https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId}/ledger[?PageSize][&PageIndex] providing the ID of the workspace.

To query activity logs (ledgers) for a data set, call the endpoint https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId}/datasets/{datasetId}/ledger[?PageSize][&PageIndex] providing the ID of the workspace and the data set.

## Changes in existing features

This section covers changes in existing features:
* [Home page changes](#home-page-changes)
* [Infinite scroll for Activity log](#infinite-scroll-for-activity-log)
* [Query filters for saved data sets](#query-filters-for-saved-data-sets)
* [Saving shared data sets](#saving-shared-data-sets)
* [Members display](#members-display)
* [Smaller banner in Connections](#smaller-banner-in-connections)

### Home page changes
The navigation tabs ("Home", "Data Catalogue", "Connections", "Members") were moved to the top of the page. Now, they are in the same line as the workspace picker.
The templates ("Poseidon Principles", "Sea Cargo Charter") were moved to the Home page from Data Catalogue, and they are placed below the navigation tabs.

Previously, the Home page was displaying "Connections" and below them, "Recent data sets". Now, "Recent data sets" are displayed on the top, and the "Connections" section is below them. Now, to the right of the "Recent data sets" section title, there is a "See all data sets" button. Also, to the right of the "Connections" section title, there is a "See all connections" button.

### Infinite scroll for Activity log
Previously, Activity log was paginated. Now, the data loads as you scroll down.

### Query filters for saved data sets
Data sets are saved with some query filters. Now, users with read access can deselect the saved filters, for example, to filter by a smaller number of vessels or a shorter time range. 

### Saving shared data sets
Data sets can be shared with stakeholders for a specified time after which the access expires. If a data set has been shared and at least one of the stakeholders still has access to it, no changes can be saved to this data set. However, admin users can use the "Save as new" button to copy the data set and save it as a new data set.

Note that users with read access cannot save data sets.

### Members display
Now, in the **Members** tab ("Workspace" > "Members"), there are two tables with members: "Workspace members" and "Tenant members", so that  you can see who is a workspace member, and who is a tenant member.

Each table:
* Displays user count in the top right corner.
* Shows the name, email, and role of each member.
* Becomes paginated if there are more than 20 members.

### Smaller banner in Connections
In the Connections tab, the banner "New conections coming soon" was made smaller.

## Bugs fixed

This release has brought some security improvements and some corrections in what is logged and when. Apart from that, the following issues have been fixed:

* In data set lists, fixed display issues for data classification tooltip. Previously, it was cropped on small screens or when the list was displaying only a few data sets.
* In Data Catalogue, fixed display issues with the column picker. Previously, the column tags were cropped when they did not fit into the browser window. Now, they fade out.
* Corrected typos in the window telling with whom you have shared a data set.
* For the window for inviting users, fixed display issue ocurring when you tried to invite to the workspace existing users.
