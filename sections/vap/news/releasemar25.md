---
author: Veracity
description: This is the changelog for the release 4.22 of Veracity Adapter for Power BI (VAP).
---

# VAP 4.22 release
Read this page to learn what has changed in the Veracity Adapter for Power BI.

## New features
This section covers new features.

### Configure Data Workbench Service Account
If your reports use Data Workbench data sets, configuring your Data Workbench Service Account allows the necessary connection details to be automatically filled in whenever needed. This saves you from manually entering them each time you access your data sets.

#### Where to find it
On the **Resources** page, in the top right corner, we have added an icon to access **Data Workbench Service Account** (DWB Service Account). 
When you open it, you can add your Data Workbench Dataset Service Account providing the following information:
- Data Workbench workspace ID: [Check here how to find it](https://developer.veracity.com/docs/section/dataworkbench/apiendpoints#workspace-id).
- Data Workbench workspace name: You can find it in your Data Workbench > Workspace > [Details tab](https://developer.veracity.com/docs/section/dataworkbench/workspace#details).
- [Data Workbench Service Account ID](../../dataworkbench/apimanagement.md): Note you can only add an account with "Grant all workspace data" enabled.
- [Account Secret](../../dataworkbench/apimanagement.md).

### Auto-renew SAS token for Data Workbench structured uploaded data sets
Now, you can automatically renew SAS tokens for Data Workbench structured uploaded data sets. This ensures your data connections remain active without manual intervention.

If you want to learn more about structured uploaded data sets, [go here](../../dataplatform/concepts/structdata.md).

**To enable auto-renewal for a SAS token**, follow these steps:
1. Edit your report in the **Resource** section.
2. Click the **Load Data Source** button.
3. For Data Source "Azure Data Lake Storage", under **Data Source Sub Type**, select **DWB Structured Dataset**.
4. Tick the **Auto Renew SAS Token** box. 
The token will renew automatically once a day at CET midnight.

### Improved resource UI and data source management
We have enhanced the user interface for data source management after uploading a report or clicking **Load Data Source**. The changes make it easier to understand data source status and identify issues.

Below are key improvements:
- Users can now select the auto-renew option for Data Workbench structured uploaded data sets and provide necessary renewal information.
- The data source type is now clearly defined, which is crucial for background processes like token renewal.
- Detailed error information for loading data sources and data source actions (update data source, credentials, SAS token, bind gateway)
- Users can independently reload each data source without reopening the "Edit File" page.
- A new status bar displays the connection and action status of the data source, making it easier to monitor progress.

## Changes in existing features
This section covers changes in existing features.

### API management link added in resource file dialog
In the **Edit Resource file** dialog, we have linked to [API Management documentation](../../dataworkbench/apimanagement.md) where you can learn how to manage service accounts, including granting "all workspace data" permissions.