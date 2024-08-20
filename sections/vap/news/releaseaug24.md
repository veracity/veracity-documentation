---
author: Veracity
description: This is the changelog for the release 4.16 of Veracity Adapter for Power BI (VAP).
---
# VAP 4.16 release

Read this page to learn what has changed in the Veracity Adapter for Power BI. 

## New Features

This section covers new features.

### Edit report or entity from Home

As a Data Admin, you can now edit a report or entity from the **Home** page. When you view a report or entity, in the top right corner of the page, select **Edit** and then choose either **Edit Entity** or **Edit Report**. This will open the current entity or report and you can make changes.

### New Tenant Properties for invoicing automation

On the **Config** page, in **Tenant Properties**, we have added the following properties: 
* Project Number
* Task Number
* Legal Entity
* Cost Center
 
These properties are used to automate invoices.

### Enable download of Power BI files

As a System Admin, you can enable the download of Power BI files. To do it, on the **Config** page, in the **Tenant Properties**, select **Edit**. Then, toggle on **Allow download Pbix**. Note that this feature is toggled off by default. 

### Download Power BI files

Now, you can download Power BI files from **Resources**. To do it, on the **Resources** page, in the **Actions** column, select the **Download pbix File** icon. The download will start automatically and you will be notified when it is completed.

Note that:
* Downloading .PBIX file types is only possible if a System Admin enabled it.
* The download icon is not available for other file types.

### Upgrade or downgrade of user role

Now, you can see who upgraded or downgraded a user role.

To do it, on the **Users** page, in the **Actions** column, select the **View History** icon. Then, go to the **Admin Operate History** tab. Here, you can view the following information.
* Under **Operate user**, who upgraded or downgraded a user role.
* Under **Description**, the names of new and old user roles.
* Under **Date time**, when the user role was changed.

### New Page View Distribution chart

Now, on the **Activity Statistics** page, in the **Report Statistics** tab, you can view a new **Page View Distribution** pie chart. The chart shows report page views in a percentage format. 

To see the number of interactions with a report page, select the chart. This will open a pop-up window with the number of the report page views and the time of the last view.

### Security improvements
We have enhanced the security and stability of VAP services.

### Improved response speed for resources
We have improved the response speed for resources from VAP to user clients.

### Paginated report support
For demo purposes, we have prepared a PoC of paginated reports.


## Changes in existing features

This section covers changes in existing features.

### Updated fields in Tenant Properties

We have changed the type of the **Business Owner** and **Contact Email** fields to e-mail.

### Veracity migrates Veracity Data Fabric/My data to Veracity Data Workbench
If you built a report using Data Fabric, we now recommend you to start using Data Workbench File storage for new reports which require client data.
