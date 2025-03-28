---
author: Veracity
description: Overview of the Resource tab in the admin tab.
---

# Resources
The 'Resources' tab consists of the **File** subtab (that opens by default) and the <a href="#webapp">**Web App** subtab</a>.

Resources are shown in a table and each resource is presented in one row. Some columns are sortable, which is indicated by arrow symbols next to the column name. To sort the column, select its name.

In the **Actions** column, you can:
* See the history of the changes done to the resource (1).
* Edit the resource (2).
* Delete the resource (3).
* Download the resource, which file type is .PBIX (4). 

Note that:
* Due to limitations set by Microsoft, you cannot download a large .pbix. It may time out after 4 minutes. If it happens, send a support ticket to get help downloading the report. For more information, go [here](https://learn.microsoft.com/en-us/power-bi/create-reports/service-export-to-pbix#limitations-when-downloading-a-report-pbix-file).
* Downloading .PBIX file types is only possible if a System Admin enabled it. To enable the download of Power BI files, on the **Config** page, in the **Tenant Properties**, select **Edit** and toggle on **Allow download Pbix**.

<figure>
    <img src="assets/resource_actions.png"/>
</figure>

## Configure Data Workbench Service Account
If your reports use Data Workbench data sets, configuring your Data Workbench Service Account allows the necessary connection details to be automatically filled in whenever needed. This saves you from manually entering them each time you access your data sets.

### Where to find it
On the **Resources** page, in the top right corner, an icon has been added to access **Data Workbench Service Account** (DWB Service Account).  
When you open it, you can add your Data Workbench Dataset Service Account by providing the following information:

- **Data Workbench workspace ID**: [Check here how to find it](https://developer.veracity.com/docs/section/dataworkbench/apiendpoints#workspace-id).
- **Data Workbench workspace name**: You can find it in your Data Workbench > Workspace > [Details tab](https://developer.veracity.com/docs/section/dataworkbench/workspace#details).
- **[Data Workbench Service Account ID](../../dataworkbench/apimanagement.md)**: Note that you can only add an account with "Grant all workspace data" enabled.
- **[Account Secret](../../dataworkbench/apimanagement.md)**.

## Auto-renew SAS token for Data Workbench structured uploaded data sets

You can now automatically renew SAS tokens for Data Workbench structured uploaded data sets. This ensures your data connections remain active without manual intervention.

If you want to learn more about structured uploaded data sets, [go here](../../dataplatform/concepts/structdata.md).

### To enable auto-renewal for a SAS token:
1. Edit your report in the **Resource** section.
2. Click the **Load Data Source** button.
3. For Data Source "Azure Data Lake Storage", under **Data Source Sub Type**, select **DWB Structured Dataset**.
4. Tick the **Auto Renew SAS Token** box.  
   The token will renew automatically once a day at CET midnight.

## Improved resource UI and data source management
We have enhanced the user interface for data source management after uploading a report or clicking **Load Data Source**. The changes make it easier to understand data source status and identify issues.

### Key improvements:
- Users can now select the auto-renew option for Data Workbench structured uploaded data sets and provide necessary renewal information.
- The data source type is now clearly defined, which is crucial for background processes like token renewal.
- Detailed error information for loading data sources and performing data source actions (update data source, credentials, SAS token, bind gateway).
- Users can independently reload each data source without reopening the "Edit File" page.
- A new status bar displays the connection and action status of the data source, making it easier to monitor progress.

## API management link added in resource file dialog
In the **Edit Resource file** dialog, a link has been added to the [API Management documentation](../../dataworkbench/apimanagement.md), where you can learn how to manage service accounts, including granting "all workspace data" permissions.

