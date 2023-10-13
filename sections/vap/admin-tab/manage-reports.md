---
author: Veracity
description: Overview of the Manage Reports tab in the admin tab.
---

# Manage Reports
This page describes administrator tasks you can do in "Manage Reports".

## To create a new report property object and connect it to your file or web app
To create a new report object:
1. Select the **Create new report** button. It will open a pop up window in the "PBI report/Blob report tab".
2. In the **Title**, provide the internal name of the report. It will be shown only to admin users.
3. In the **Display name**, provide the name that will be visible to everyone with access.
4. Optionally, deselect the toggle **Use Display Name as Report URL Name**, and below in the field **Report URL name** provide your custom URL for the report. The URL name must be unique and cannot contain spaces or special characters. You can use alphanumeric values, underscore, and hyphen.
5. Optionally, in the **Description** field, describe your report for the end users. Note that currently the description is not shown to the users.
6. From the **File title** dropdown, select what file you want your report to connect to. If you do not see the file, go to [Manage Files to upload it](manage-files.md).	
7. Below **File title**, you can enable the following toggles:

	Printable - allows printing the report.
	
	Able to export data - allows exporting data from visuals in the report.
	
	Able to export as PDF  - allows exporting your entire report to a PDF document which gives users a snapshot of the current data and the state of the report. This uses Microsoft Power BI APIs so it may be a time-consuming process and some features and visualizations are not supported or shown properly in the exported file. For details on issues and limitations, see [Microsoft documentation](https://learn.microsoft.com/en-us/power-bi/collaborate-share/end-user-pdf?tabs=powerbi-service#visuals-that-arent-supported).
	
	Able to export as PPT - allows exporting your report to Power Point  which gives users a snapshot of the current data and the state of the report. This uses Microsoft Power BI APIs so it may be a time-consuming process and some features and visualizations are not supported or shown properly in the exported file. For details on issues and limitations, see [Microsoft documentation](https://learn.microsoft.com/en-us/power-bi/collaborate-share/end-user-powerpoint#visuals-that-arent-supported).
	
	Show filter panel - if your reports uses filter pane, disable this option to show the filter.
	
	Hide custom report title - if you deselect this box, three options to choose from appear, so that you can customize the title of your report shown at the top of your Power BI report.
	
	Show bookmark icon - enables users to bookmark parts of the report, so that they can use them to go back to the bookmarked parts of the reports or share them as links with other people. Only user personal bookmarks will be shown.
		
	Show based on report file bookmarks - enables user personal bookmarks and report bookmarks. Use it for reports that will have some bookmarks created by the report author, but also will allow users to create their own. Note that, when it is disabled, VAP will show only personal bookmarks.

8. In the **Role name**, if you have enabled [Row Level Security (RLS)](../data.md), provide the role name as defined in your PBI report (Manage roles > Roles).
9. In the **Row level security parameter**, if you have enabled [RLS](../data.md), provide filter key and from the dropdown, select its type. To add another filter key, select the plus button next to the dropdown.
10. In the **Connect Tutorial**, you can select which tutorial for your report should be shown to the users. You can use tutorials to present new features, teach users how to read your reports, and so on. If you do not see the file, go to [Manage Files to upload it](manage-files.md). In the "Configure" tab under "Report release note", you can find a tutorial template.
11. In the right corner, select the **Add** button.

## To create a new Web app report

To create a new Web app report:
1. Select the **Create new report** button. It will open a pop up window in the "PBI report/Blob report tab".
2. Select the **Web app report** tab.
3.  In the **Title**, provide the internal name of the web app. It will be shown only to admin users.
4.  In the **Display name**, provide the name that will be visible to everyone.
5. Optionally, deselect the toggle **Use Display Name as Report URL Name**, and below in the field **Report URL name** provide your custom URL for the report. The URL name must be unique and cannot contain spaces or special characters. You can use alphanumeric values, underscore, and hyphen.
6. Optionally, in the **Description** field, describe your report for the end users. Note that currently the description is not shown to the users.
7. From the **File title** dropdown, select what web app you want to connect to. The one you defined in Manage Webs.
8. In the **Row level security parameter**, if you want you web app to change content of diable features based on criteria, provide filter key and from the dropdown, select its type. To add another filter key, select the plus button next to the dropdown.
9. In the **Connect Tutorial**, you can select which tutorial to your report should be shown to your users. You can use tutorials to present new features, teach users how to interact with your web apps, and so on. Note that a report tutorial needs to be added in Manage File before it can be selected here. In the "Configure" tab under "Report release note", you can find a tutorial template.
10. In the right corner, select the **Add** button.


## To refresh a report with new content 

If your Power BI report contains imported data and you want to show its newer version with the fresh data, or if you need to replace an image or a PDF file with its newer version, follow the steps below.
1. In **Manage File**, upload the new file or report.
2. In the **File title** field, select the file you have uploaded.
3. Select the **Save** button.


## To enable bookmarks in a Power BI report

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

## To disable bookmarks in a Power BI report

To disable personal and report bookmarks:
1. Choose a report and in the right corner of the row, select the editing icon (the second one from the left). A pop-up window will appear.
2. In the pop-up window, under **File title**, deselect the "Show bookmark icon" toggle.
3. In the right corner of the window, select the **Save** button.

To disable report bookmarks:
1. Choose a report and in the right corner of the row, select the editing icon (the second one from the left). A pop-up window will appear.
2. In the pop-up window, under **File title**, deselect the **"Show based on report file bookmarks"** toggle.
3. In the right corner of the window, select the **Save** button.

## Deleting user bookmarks in a Power BI report

A personal bookmark is associated with the User GUID, Entity ID, and Report ID. If you do one of the actions below, it will be deleted.
* Delete any of the elements the bookmark is associated with.
* Remove the entity, report or the report object on which the bookmark was saved.


If you are updating the report in the "Manage Reports" tab by changing the reference for the report file from one PBIX file to another, VAP will ask if you want to preserve users' personal bookmarks. If you have done major changes to the report, preserving the bookmarks is not recommended.
