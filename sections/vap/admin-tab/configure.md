---
author: Veracity
description: Overview of the Configure tab in the admin tab.
---

# Configure

## Header Icon

Under "Header Icon", you can edit the favicon (header) icon for your VAP service or reset it to the default. To upload your own icon, select the **Edit Head Icon** button. To reset the icon to the default, select the **Reset to default icon**. If this a DNV or Veracity-owned service, leave the default logo.


## Statistics Report

Under "Statistics Report", you can see the statistics for your VAP service including VAP usage, historical data, who is using your tenant, and the information on key fields.

## Entity types

Under "Entity types", you can add entity types, see what types are already created, edit or delete them.

## Tenant Properties

Under "Tenant Properties", you can see tenant properties and edit them.

To edit tenant properties, select the **Edit** button and edit the fields you need to change. You can edit the following fields:
* Invoice Detail - add information for invoicing, for example, cost center, your project and task number, and so on. Note that currently this field is not shown.
* Invoice Contact Email - provide email for sending you invoices. Note that currently this field is not shown.
* Business Owner - provide the name of the service owner. Note that currently this field is not shown. However, it can be used for communication regarding your VAP service.
* Contact Email - provide an email for contacting you regarding your VAP service.
* Service Description - describe your VAP service.
* Send notification to all users - enable it to send notifications to users when their account is modified. This is a default setting, and you can override it for each user account.
* Notified Group - select to notify users with a certain role (for example, UserAdmin) when a new user has successfully self-subscribed to the tenant or an entity in your tenant has turned on public view (access).
	
	Allow Self Subscribe - enable to allow users to self-register and access your web service. 
	
	Enable manage filters - if you enable this default setting, a "Manage Filters" button will be shown under "Manage Reports", and you wil be able to configure reusable report filters for your users.
	
	Show dataset and report id - enable to show the ID of data sets and reports on Power BI reports in "Manage File".
	
	Enable Power BI - enable Power BI in your VAP service.
	
	Enable Web Apps - enable connecting web applications to your VAP service.
	

* Background image - add a background image to your VAP service.

## Tenant Documents

Under "Tenant Documents", you can define what documents should be avaliable for all users from the "Home" menu. You can see the documents added to your tenant. To sort them by column, select the column's name. In the right corner of each row, you can:
* Edit the document.
* Delete the document.

To add a document:
1. Select the **Add** button.
2. In the **Report title** dropdown, select the name of the document (PDF, image).
3. In the **Display name**, add the name for the document that should be shown to users.
4. Select the **Save** button.

## Refresh Schedule Plan

Under "Refresh Schedule Plan", you can schedule when the reports in your VAP service should refresh data. The table shows all the schedled refreshes. To sort them by column, select the column's name. In the right corner of each row, you can:
* Edit the scheduled refresh.
* Delete the scheduled refresh.

To add a scheduled refresh:
1. Select the **Add** button.
2. In the **Title**, provide a name for the refresh plan. This is only shown to Report and System Admin users.
3. In the time zone, select a time zone for the refresh, the start time, the intervals, and the number of daily refreshes (maximum 48 per day which means a refresh every 30 minutes). Note that scheduled refresh is a memory intensive background task and may be postponed during high memory usage by Power BI. Because of that, set the refreshes only in the necessary intervals.
4. Optionally, select the **Generate refresh times** to set the time for each refresh. To add another scheduled refresh, select the **Add another time** button.
5. Under **Weekdays**, select the days on which report data should be refreshed.
6. In the **Apply to PBI reports**, select which Power BI files should use this refresh plan. Note that the files need to be stored in a cloud.
7. Select the **Save & Apply** button.

If you want to apply a refresh plan or change it to another, you can do so for each report under "Manage file" or in the "Configure" tab.

## Footer Properties

Under "Footer Properties", you can see what is shown in the footer of your VAP service. To edit this, select the icon in the right corner of the row.

You can set the following properties for the footer:
* Footer Header - provide the title for the middle section of the footer. 
* Support Contact Email - provide the support email contact for your service.
* Tenant Information - provide information about your service. If this field is empty, then it is not shown to the users.
* Tenant Information URL - if you want to have a clickable link or email under your "Tenant Information", provide it in this field.
* Copy Right - if you want to change the default copyright information shown in the footer, provide your custom text.

Note that to see the changes in footer, entity types or tenant properties, you need to refresh the page first.

## Report Release Note

Under "Report Release Note", you can download a JSON template file for release notes. You can use it for creating your release notes with the purpose of communicating changes to your end users. After modifying the template, ipload it in [the "Manage Files" tab](manage-files.md)  and connect it to the report in [the "Manage Reports" tab](manage-reports.md).
