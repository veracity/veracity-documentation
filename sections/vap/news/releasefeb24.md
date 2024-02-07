---
author: Veracity
description: This is the changelog for the release 4.12 of Veracity Adapter for Power BI (VAP).
---
# VAP 4.12 release PLACEHOLDER

**This is a placeholder for the 4.12 release. We will remove update this information and remove this disclaimer when we do the VAP 4.12 release.**

Read this page to learn what has changed in the Veracity Adapter for Power BI. 

This release brings quality improvements by redesigning **Manage File** and **Manage User** modules in the Admin Panel. Note that there are no changes in functionalities. However, VAP looks a bit different now, and you do some things in different places than before. The changes are based on the feedback from our users.

Note that this is a placeholder for the release, and we will update it when we make the release 4.12
## New Features
This section covers new features.

### New filters and sorting columns
On the 'Users' page (previously 'Manage Users') and on the 'Resources' page (previously 'Manage File'), we have enabled new filtering options for you and made some columns sortable.

**To filter**, in the right corner, select the magnifying glass icon, select a filter, select filter settings, and select the **Apply** button.

To hide filtering options, select the magnifying glass icon again.

<figure>
	<img src="../admin-tab/assets/users_filter.png"/>
</figure>

If you can sort a column, it has two arrows next to its name. The arrow in the dark blue colour shows the current sorting direction. For example, if the bottom arrow is dark blue, the column is sorted in the descending order. 

**To change the column's sorting order**, select the column's name.

<figure>
	<img src="assets/sort.png"/>
</figure>

For details on the Resource page, [see the updated documentation page](../admin-tab/resource.md).

For details on the Users page, [see the updated documentation page](../admin-tab/users.md).

## Changes in existing features
This section covers changes in existing features.

### Changed where you add objects
We have changed how you add the following:
* Add File.
* Add Web App.
* Add a user.
* Batch add users.

Now, you select the plus icon in the left sidebar and  select the object you want to add. You can do that from any page in the Admin Panel except the Home page.

<figure>
	<img src="assets/add.png"/>
</figure>

### Renamed Manage File to Resources
Now, the 'Manage File' page is called 'Resources'. For details, [see the updated documentation page](../admin-tab/resource.md).

### Merged Manage Web into Resources
Now, the 'Manage Web' page is a part of the 'Resources' page. For details, [see the updated documentation page](../admin-tab/resource.md).

### Renamed Manage Users to Users
Now, the 'Manage Users' page is called 'Users'.

### Changed filtering and actions in Users
We have changed how you filter users and how we show the actions that can give you statistics for the user or let you edit or delete the user. For details, [see the updated documentation page](../admin-tab/users.md).

### Changed filtering for Resources
We have changed how you filter resources. For details, [see the updated documentation page](../admin-tab/resource.md).

### Moved data location and workspace ID to Configure
Now, the information on the ID of your workspace and the location of your Power BI files is at the top of the 'Configure' page. For details, [see the updated documentation page](../admin-tab/configure.md).

## Security improvements
Before this release, we have done several releases focused on security improvements. Also, in October 2023, we had penetration tests and acted on all the findings in order of importance, finishing the improvement process in November 2023.