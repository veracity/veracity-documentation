---
author: Veracity
description: Overview of the admin tab.
---

# Admin tab overview

To do administrator tasks in Veracity Adapter for Power BI (VAP), sign in to your VAP service, and select the **Admin tab** to see the administrator tasks you can do. Note that your user role might not give you access to all the tasks.

If you are a SystemAdministrator, you can see the full list of tasks:
* Manage Files — upload and delete files. Supported formats are PBIX, PDF, PNG, JPEG, GIF.
* Manage Reports — select reports and connect them to files or web applications.
* Manage Entities — create entities and connect them to reports, documents, and web applications.
* Manage Users — create, edit, and delete users. Assign and revoke user roles.
* Manage Webs — set up web applications.
* Configure — configure scaffolding and other properties.

## Manage Files

Once you have built your report in Power BI, you can upload it into VAP and share access to it with your clients. By default, the report data sources would be used in VAP, but you can override and update them. For details on data sources and security, go [here](vap.md#data-sources-and-security)

Below the "Manage Files" heading (top centre), you can see if your Power BI files are stored in the EU or USA.

Supported file formats are PBIX, PDF, PNG, JPEG, GIF, JSON. If you want to add release notes, upload a JSON file that follows the [Report Release Note template](#report-release-note).

To upload a file:
1. Select the **Upload a file** button.
2. Select the **Choose File** button and select the file from your local machine.
3. In the **Name** field, provide the name for the file. If you are uploading a report for a particular client, Veracity recommends including the client's name and the report's date in the file name.
4. In the right corner, select the **Upload** button.

If you get warnings when VAP checks your report's 'data sources, read the warnings and follow the troubleshooting they recommend. 

The "Manage Files" page shows all uploaded files in a table. To sort them by a specific column, select the column. 

In the right corner of each row you can:
* Refresh data (for [refreshable data sources](vap.md#data-sources-and-security)).
* Schedule a data refresh (for [refreshable data sources](vap.md#data-sources-and-security)).
* See history.
* Edit the file, see report ID and dataset ID or file name.
* Delete the file.

The actions above are listed from the first to the last icon from the left.



## Manage Reports

To create a new Power BI or Blob report:
1. Select the **Create new report** button. It will open a pop up window in the "PBI report/Blob report tab".
2. In the **Title**, provide the internal name of the report. It will be shown only to admin users.
3. In the **Display name**, provide the name of the report that will be visible to everyone.
4. Optionally, deselect the toggle **Use Display Name as Report URL Name**, and below in the field **Report URL name** provide your custom URL for the report. The URL name must be unique and cannot contain spaces or special characters. You can use alphanumeric values, underscore, and hyphen.
5. Optionally, in the **Description** field, describe your report for the end users. Note that currently the description is not shown to the users.
6. From the **File title** dropdown, select what PBI file you want your report to connect to.
7. Below **File title**, you can enable the following toggles:

	Printable — allows printing the report.
	
	Able to export data — allows exporting data.
	
	Show filter panel — if your reports uses filter pane, disable this option to show the filter.
	
	Hide custom report title — if you deselect this box, three options to choose from appear, so that you can customize the title of your report shown at the top of your Power BI report.
	
	Show bookmark icon — enables users to bookmark parts of the report, so that they can use them to go back to the bookmarked parts of the reports or share them as links with other people. Only user personal bookmarks will be shown.
		
	Show based on report file bookmarks — enables user personal bookmarks and report bookmarks. Use it for reports that will have some bookmarks created by the report author, but also will allow users to create their own.

8. In the **Role name**, if you have enabled Row Level Security (RLS), provide the role name as defined in your PBI report (Manage roles > Roles).
9. In the **Row level security parameter**, if you have enabled RLS, provide filter key and from the dropdown, select its type. To add another filter key, select the plus button next to the dropdown.
10. In the **Connect Tutorial**, you can select which tutorial for your report should be shown to the users. You can use tutorials to present new features, teach users how to read your reports, and so on.
11. In the right corner, select the **Add** button.

To create a new Web app report:
1. Select the **Create new report** button. It will open a pop up window in the "PBI report/Blob report tab".
2. Select the **Web app report** tab.
3. In the **Display name**, provide the name of the report that will be visible to everyone.
4. Optionally, deselect the toggle **Use Display Name as Report URL Name**, and below in the field **Report URL name** provide your custom URL for the report. The URL name must be unique and cannot contain spaces or special characters. You can use alphanumeric values, underscore, and hyphen.
5. Optionally, in the **Description** field, describe your report for the end users. Note that currently the description is not shown to the users.
6. From the **File title** dropdown, select what PBI file you want your report to connect to.
7. In the **Row level security parameter**, if you have enabled RLS, provide filter key and from the dropdown, select its type. To add another filter key, select the plus button next to the dropdown.
8. In the **Connect Tutorial**, you can select which tutorial to your report should be shown to your users. You can use tutorials to present new features, teach users how to read your reports, and so on.
9. In the right corner, select the **Add** button.

If your report contains imported data and you want to show its newer version with the fresh data, follow the steps below.
1. Upload the new report.
2. In the **File title** field, select the report you have just uploaded.
3. Select the **Save** button.

## Manage Entities

An entity:
* Can contain one or more reports.
* You share access to end users to one or more entities.
* Is a way of groping and structuring your reports.
* Represents the top-level concepts such as company, projects or assets.

To add an entity:
1. Select the **Add** button.
2. In the **Title**, provide the internal name of the entity. It will be shown only to admin users. By default, the title will be used to create the URL for the entity.
3. Optionally, deselect the toggle **Use Title as Entity URL Name** and then in the **Entity URL name** field provide a custom URL for the entity. The URL name must be unique and cannot contain spaces or special characters. You can use alphanumeric values, underscore, and hyphen.
4. In the **Type** dropdown, select the type of the entity you want to create. If you want users to be able to add themselves to the entity, select **Allow Self Subscribe**; this might be suitable for a demo. If you want users to access the entity wihout login to Veracity, select **Public View**; this might be suitable for a freemium model.
5. In the **Reports** dropdown, select one or more reports that should be available to the users who are part of the entity you are creating.
6. In the right corner, select the **Add** button.

The "Manage Entities" page shows all entities created in your VAP service. To sort them by a specific column, select the column. 

In the right corner of each row, you can:
* Add an icon for the entity.
* See history.
* Edit the entity and see its ID.
* Delete the entity.

The actions above are listed from the first to the last icon from the left.

## Manage Users

You can only add Veracity users to a VAP entity. However, if you try to add a non-Veracity user, you will be offered an option to invite them to Veracity. To get access to the VAP entity, this person needs to accept the invitation and create their Veracity account.

To add a user to an entity:
1. Select the **Add User** button.
2. Provide the user's email address, and select the **Check Email / User ID** button.
3. In the **Grant access to** dropdown, select the entity to which the user should be added.
4. In the **Roles** dropdown, assign a [role](userroles.md) to the user.
5. Optionally, deselect "Send notification to this user" if you do not want to notify the user that they have been added to an entity in VAP.

To batch add users to an entity:
1. Select the **Batch Add Users** button.
2. In the **Grant access to** dropdown, select the entity to which the users should be added.
3. In the **Roles** dropdown, assign a [role](userroles.md) to the users.
4. Select the **Choose File** button and choose a CSV file from your local machine to batch import users.

If you need a template for batch importing users, you can find it below the **Choose File** button.

The "Manage Users" page shows all users in your VAP service. You can:
* Filter each column providing the text to filter by or choosing an option from a dropdown. To clear all the filters, select the **Clear** button in the right corner of the row with the filters.
* Sort the "Name" and "Email" columns by selecting them.

## Manage Webs

To create a new web connection:
1. Select the **Create new web app connection** button.
2. In the **Root URL**, provide the full root URL to your web application.
3. To accept the legal terms of using the service, below the ***Root URL***, enable the toggle **I accept and understand...**
4. In the **Display name**, provide the name that the end users should see when they change between different reports or applications.
5. Optionally, in the **Description** field, describe your report for the end users. Note that currently the description is not shown to the users.
6. Below **Description**, you can enable the following toggles:

	Enable Dedicated Domain Name — if your web app requires a dedicated domain name, enable this to provide the domain name.
	
	Enable Service Worker — if your web app uses service workers, enable this and provide the full URL of the JS file where you register the service workers for your web app.
	
	Single page application (SPA) — if your web app is a single page application, enable this, and select your app's framework, and the full URL of the "App.js" file containing routing configuration for your SPA framework.
	
	Host In One Gateway — if your web app is hosted in One Gateway, enable this, and provide your app's Client ID for One Gateway. Then, go to your One Gateway, and allow access for the VAP Web App. Also, allow for VAP to control the authentication. After that, the configuration for your web app will disable URL direct access, making it only valid when interacting from VAP.
	
	Attach User Token — if you want to attach user token in the request header, enable this.

7. Select the **Check connection** button to verify if your web application can connect to your VAP service.
8. After establishing a connection, select the **Add** button to add the connection.

After you have added a new web connection, go to [Manage Entities](#manage-entities) to add your web application to a new or existing entity.

For help with connecting your web app to VAP, go to [Veracity Community](https://community.veracity.com/t/how-to-plug-the-web-apps-into-vap/145/3).

The "Manage Webs" page shows all connections created in your VAP service. To sort them by a specific column, select the column. 

In the right corner of each row, you can:
* See history.
* Edit and check the connection.
* Delete the connection.

The actions above are listed from the first to the last icon from the left.


## Configure

### Header Icon

Under "Header Icon", you can edit the favicon (header) icon for your VAP service or reset it to the default. To upload your own icon, select the **Edit Head Icon** button. To reset the icon to the default, select the **Reset to default icon**.


### Statistics Report

Under "Statistics Report", you can see the statistics for your VAP service including VAP usage, historical data, who is using your tenant, and the information on key fields.

### Entity types

Under "Entity types", you can add entity types, see what types are already created, edit or delete them.

### Tenant Properties

Under **Tenant Properties**, you can see tenant properties and edit them.
To edit tenant properties, select the **Edit** button and edit the fields you need to change. You can edit the following fields:
* Invoice Detail — add information for invoicing, for example, cost center, your project and task number, and so on. Note that currently this field is not shown.
* Invoice Contact Email — provide email for sending you invoices. Note that currently this field is not shown.
* Business Owner — provide the name of the service owner. Note that currently this field is not shown. However, it can be used for communication regarding your VAP service.
* Contact Email — provide an email for contacting you regarding your VAP service.
* Service Description — describe your VAP service.
* Send notification to all users — enable it to send notifications to users when their account is modified. This is a default setting, and you can override it for each user account.
* Notified Group — select to notify users with a certain role (for example, SystemAdmin) when a new user has successfully self-subscribed to the tenant or an entity in your tenant has turned on public view (access).
	
	Allow Self Subscribe — enable to allow users to self-register and access your web service.
	
	Enable manage filters — if you enable this default setting, a "Manage Filters" button will be shown under "Manage Reports", and you wil be able to configure reusable report filters for your users.
	
	Show dataset and report id — enable to show the ID of data sets and reports.
	
	Enable Power BI — enable Power BI in your VAP service.
	
	Enable Web Apps — enable connecting web applications to your VAP service.

* Background image — add a background image to your VAP service.

### Tenant Documents

Under "Tenant Documents", you can see the documents added to your tenant. To sort them by column, select the column's name. In the right corner of each row, you can:
* Edit the document.
* Delete the document.

To add a document:
1. Select the **Add** button.
2. In the **Report title** dropdown, select the name of the report.
3. In the **Display name**, add the name for the document that should be shown to users.
4. Select the **Save** button.

### Refresh Schedule Plan

Under "Refresh Schedule Plan", you can schedule when the reports in your VAP service should refresh data. The table shows all the schedled refreshes. To sort them by column, select the column's name. In the right corner of each row, you can:
* Edit the scheduled refresh.
* Delete the scheduled refresh.

To add a scheduled refresh:
1. Select the **Add** button.
2. In the **Title**, provide a name for the refresh plan. This is only shown to Report and System Admin users.
3. In the time zone, select a time zone for the refresh, the start time, the intervals, and the number of daily refreshes (maximum 48 per day which means a refresh every 30 minutes).
4. Optionally, select the **Generate refresh times** to set the time for each refresh. To add another scheduled refresh, select the **Add another time** button.
5. Under **Weekdays**, select the days on which report data should be refreshed.
6. In the **Apply to PBI reports**, select which Power BI files should use this refresh plan. Note that the files need to be stored in a cloud.
7. Select the **Save & Apply** button.

If you want to apply a refresh plan or change it to another, you can do so for each report under "Manage file".

### Footer Properties

Under "Footer Properties", you can see what is shown in the footer of your VAP service. To edit this, select the icon in the right corner of the row.

You can set the following properties for the footer:
* Footer Header — provide the title for the middle section of the footer. 
* Support Contact Email — provide the support email contact for your service.
* Tenant Information — provide information about your service. If this field is empty, then it is not shown to the users.
* Tenant Information URL — if you want to have a clickable link or email under your "Tenant Information", provide it in this field.
* Copy Right — if you want to change the default copyright information shown in the footer, provide your custom text.

Note that to see the changes in footer properties, you need to refresh the page first.

### Report Release Note

Under "Report Release Note", you can download a JSON template file for release notes. You can use it for creating your release notes with the purpose of communicating changes to your end users.