---
author: Veracity
description: Overview of the Manage Reports tab in the admin tab.
---

# Manage Reports
This page describes administrator tasks you can do in "Manage Reports".

## To create a new Power BI report
To create a new Power BI or Blob report:
1. Select the **Create new report** button. It will open a pop up window in the "PBI report/Blob report tab".
2. In the **Title**, provide the internal name of the report. It will be shown only to admin users.
3. In the **Display name**, provide the name of the report that will be visible to everyone.
4. Optionally, deselect the toggle **Use Display Name as Report URL Name**, and below in the field **Report URL name** provide your custom URL for the report. The URL name must be unique and cannot contain spaces or special characters. You can use alphanumeric values, underscore, and hyphen.
5. Optionally, in the **Description** field, describe your report for the end users. Note that currently the description is not shown to the users.
6. From the **File title** dropdown, select what PBI file you want your report to connect to.
7. Below **File title**, you can enable the following toggles:

	Printable - allows printing the report.
	
	Able to export data - allows exporting data.
	
	Show filter panel - if your reports uses filter pane, disable this option to show the filter.
	
	Hide custom report title - if you deselect this box, three options to choose from appear, so that you can customize the title of your report shown at the top of your Power BI report.
	
	Show bookmark icon - enables users to bookmark parts of the report, so that they can use them to go back to the bookmarked parts of the reports or share them as links with other people. Only user personal bookmarks will be shown.
		
	Show based on report file bookmarks - enables user personal bookmarks and report bookmarks. Use it for reports that will have some bookmarks created by the report author, but also will allow users to create their own.

8. In the **Role name**, if you have enabled [Row Level Security (RLS)](../data.md), provide the role name as defined in your PBI report (Manage roles > Roles).
9. In the **Row level security parameter**, if you have enabled [RLS](../data.md), provide filter key and from the dropdown, select its type. To add another filter key, select the plus button next to the dropdown.
10. In the **Connect Tutorial**, you can select which tutorial for your report should be shown to the users. You can use tutorials to present new features, teach users how to read your reports, and so on.
11. In the right corner, select the **Add** button.

## To create a new Web app report

To create a new Web app report:
1. Select the **Create new report** button. It will open a pop up window in the "PBI report/Blob report tab".
2. Select the **Web app report** tab.
3. In the **Display name**, provide the name of the report that will be visible to everyone.
4. Optionally, deselect the toggle **Use Display Name as Report URL Name**, and below in the field **Report URL name** provide your custom URL for the report. The URL name must be unique and cannot contain spaces or special characters. You can use alphanumeric values, underscore, and hyphen.
5. Optionally, in the **Description** field, describe your report for the end users. Note that currently the description is not shown to the users.
6. From the **File title** dropdown, select what PBI file you want your report to connect to.
7. In the **Row level security parameter**, if you have enabled [RLS](../data.md), provide filter key and from the dropdown, select its type. To add another filter key, select the plus button next to the dropdown.
8. In the **Connect Tutorial**, you can select which tutorial to your report should be shown to your users. You can use tutorials to present new features, teach users how to read your reports, and so on.
9. In the right corner, select the **Add** button.

## To refresh a report with imported data

If your report contains imported data and you want to show its newer version with the fresh data, follow the steps below.
1. Upload the new report.
2. In the **File title** field, select the report you have just uploaded.
3. Select the **Save** button.

## To enable bookmarks

You can enable or disable personal and report bookmarks. Bookmarks work like links and allow users to navigate to the parts of the report they were created on. For details, go [here](../reading-reports/bookmarks.md).

To enable only personal bookmarks:
1. Choose a report and in the right corner of the row, select the editing icon (the second one from the left). A pop-up window will appear.
2. In the pop-up window, under **File title**, select the **"Show bookmark icon"** toggle.
3. In the right corner of the window, select the **Save** button.

To enable personal and report bookmarks:
1. Choose a report and in the right corner of the row, select the editing icon (the second one from the left). A pop-up window will appear.
2. In the pop-up window, under **File title**, select the **"Show bookmark icon"** toggle.
3. Under the previous toggle, select the **"Show based on report file bookmarks"** toggle.
4. In the right corner of the window, select the **Save** button.

## To disable bookmarks

To disable personal and report bookmarks:
1. Choose a report and in the right corner of the row, select the editing icon (the second one from the left). A pop-up window will appear.
2. In the pop-up window, under **File title**, deselect the "Show bookmark icon" toggle.
3. In the right corner of the window, select the **Save** button.

To disable report bookmarks:
1. Choose a report and in the right corner of the row, select the editing icon (the second one from the left). A pop-up window will appear.
2. In the pop-up window, under **File title**, deselect the **"Show based on report file bookmarks"** toggle.
3. In the right corner of the window, select the **Save** button.

## Deleting user bookmarks

A personal bookmark is associated with the User GUID, Entity ID, and Report ID. If you do one of the actions below, it will be deleted.
* Delete any of the elements the bookmark is associated with.
* Remove the entity, report or the report object on which the bookmark was saved.


If you are updating the report in the "Manage Reports" tab by changing the reference for the report file from one PBIX file to another, VAP will ask if you want to preserve users' personal bookmarks. If you have done major changes to the report, preserving the bookmarks is not recommended.