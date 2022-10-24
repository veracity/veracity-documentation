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
Data sets are saved with some query filters. Now, users with read access who are not members of a workspace can deselect the saved filters, for example, to filter by a smaller number of vessels or a shorter time range. 
Note that they cannot query data that is out of the scope of the saved data set. This means that they cannot filter by new vessels, time ranges that exceed the saved time range, and so on.

However, workspace admins and members can query data sets with all the available filters.

### Saving shared data sets
For users with read access, saving shared data sets is disabled, and the save button is hidden. However, they can copy the data set and save it as a new one.

 For admin users, the save button is enabled. For shared data sets, admin can copy a data set and save it as a new data set. For data sets that are not shared, admin can choose to "Save" a data set or "Save as new" to create a copy.

### Members display
Now, in the **Members** tab ("Workspace" > "Members"), there are two tables with members: "Workspace members" and "Tenant members", so that  you can see who is a workspace member, and who is a tenant member.

Each table:
* Displays user count in the top right corner.
* Shows the name, email, and role of each member.
* Becomes paginated if there are more than 20 members.

### Smaller banner in Connections
In the Connections tab, the banner "New conections coming soon" was made smaller.

## Bugs fixed

This section covers bugs that have been fixed:

* Fixed the 400 Bad Request error when sharing data set in the user interface.
* Fixed the 500 Internal Server Error for operations on service accounts.
* Fixed data synchronization issues for SoC (State of Compliance) data sets.
* Fixed redirecting to the Home page after trying to access a deleted data set by URL. Now, the redirect is to an error page.
* In data set lists, fixed display issues for data classification tooltip. Previously, it was cropped on small screens or when the list was displaying only a few data sets.
* In Data Catalogue, fixed display issues with the column picker. Previously, the column tags were cropped when they did not fit into the browser window. Now, they fade out.
* Corrected typos in the window telling with whom you have shared a data set.
* For the window for inviting users, fixed display issue ocurring when you tried to invite to the workspace existing users.
* Now, public access to storage accounts is disallowed.
* Previously, sharing data sets was logged in the Activity log even if the sharing has failed. Now, it is fixed.