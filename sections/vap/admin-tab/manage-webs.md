---
author: Veracity
description: Overview of the Manage Webs tab in the admin tab.
---
## Manage Webs

To create a new web connection:
1. Select the **Create new web app connection** button.
2. In the **Root URL**, provide the full root URL to your web application.
3. To accept the legal terms of using the service, below the ***Root URL***, enable the toggle **I accept and understand...**
4. In the **Display name**, provide the name that the end users should see when they change between different reports or applications.
5. Optionally, in the **Description** field, describe your report for the end users. Note that currently the description is not shown to the users.
6. Below **Description**, you can enable the following toggles:

	Enable Dedicated Domain Name - if your web app requires a dedicated domain name, enable this to provide the domain name.
	
	Enable Service Worker - if your web app uses service workers, enable this and provide the full URL of the JS file where you register the service workers for your web app.
	
	Single page application (SPA) - if your web app is a single page application, enable this, and select your app's framework, and the full URL of the "App.js" file containing routing configuration for your SPA framework.
	
	Host In One Gateway - if your web app is hosted in One Gateway, enable this, and provide your app's Client ID for One Gateway. Then, go to your One Gateway, and allow access for the VAP Web App. Also, allow for VAP to control the authentication. After that, the configuration for your web app will disable URL direct access, making it only valid when interacting from VAP.
	
	Attach User Token - if you want to attach user token in the request header, enable this.

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
* Invoice Detail - add information for invoicing, for example, cost center, your project and task number, and so on. Note that currently this field is not shown.
* Invoice Contact Email - provide email for sending you invoices. Note that currently this field is not shown.
* Business Owner - provide the name of the service owner. Note that currently this field is not shown. However, it can be used for communication regarding your VAP service.
* Contact Email - provide an email for contacting you regarding your VAP service.
* Service Description - describe your VAP service.
* Send notification to all users - enable it to send notifications to users when their account is modified. This is a default setting, and you can override it for each user account.
* Notified Group - select to notify users with a certain role (for example, SystemAdmin) when a new user has successfully self-subscribed to the tenant or an entity in your tenant has turned on public view (access).
	
	Allow Self Subscribe - enable to allow users to self-register and access your web service.
	
	Enable manage filters - if you enable this default setting, a "Manage Filters" button will be shown under "Manage Reports", and you wil be able to configure reusable report filters for your users.
	
	Show dataset and report id - enable to show the ID of data sets and reports.
	
	Enable Power BI - enable Power BI in your VAP service.
	
	Enable Web Apps - enable connecting web applications to your VAP service.

* Background image - add a background image to your VAP service.

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
* Footer Header - provide the title for the middle section of the footer. 
* Support Contact Email - provide the support email contact for your service.
* Tenant Information - provide information about your service. If this field is empty, then it is not shown to the users.
* Tenant Information URL - if you want to have a clickable link or email under your "Tenant Information", provide it in this field.
* Copy Right - if you want to change the default copyright information shown in the footer, provide your custom text.

Note that to see the changes in footer properties, you need to refresh the page first.

### Report Release Note

Under "Report Release Note", you can download a JSON template file for release notes. You can use it for creating your release notes with the purpose of communicating changes to your end users.