---
author: Veracity
description: This is a migration guide for VAP reports from Data Fabric to Data Workbench File storage.
---

# Migration Guide for VAP Users: Data Fabric to Data Workbench File Storage
**This is a draft and may not be fully accurate**. We will update this document soon.

## Introduction
- **Purpose**: This guide aims to assist VAP report developers in making their Power BI report work after migrating their data storage from Data Fabric to Data Workbench File Storage.
  
	For your Power BI report to read from a new location (File Storage), you need to change it in the Power BI Desktop. Then, upload it to VAP and switch the file connection in Reports to the newly updated report. 
- **Audience**: VAP users with existing reports using Data Fabric.

## Prerequisites
- Access to the original Power BI files.
- Access to VAP and Data Workbench File Storage.
- Follow the migration guide from Veracity Data Workbench File Storage. See the following documentation:
	- [Veracity Data Workbench migration](https://developer.veracity.com/docs/section/datafabric/datafabric-migration)
	- [Migration from Data Fabric](https://developer.veracity.com/docs/section/dataworkbench/filestorage/migrating)
	- [File storage](https://developer.veracity.com/docs/section/dataworkbench/filestorage/filestorage)
- Necessary permissions to upload and manage reports in VAP.

## Steps for VAP report developers to migrate an old Power BI report 

### Step 1: Locate and download the original Power BI file
If you cannot find the original Power BI file, download it from your service:
1. Go to the VAP Admin tab and navigate to the Resources section.
2. Use the filter to locate the .PBIX file by name.
3. Select the file and click the download icon to save it to your local machine.

**Note that** if download is not enabled in your service, you need to go to the **Config** page. Then, in **Tenant Properties**, select **Edit**, and enable **Allow Download Pbix**.

### Step 2: Change your Power BI report to read from a new location (File Storage)
1. Open the report in Power BI Desktop.
2. Go to Data Workbench and select the **Data Catalogue** tab (1).
3. Select **File storage** (2).
4. In the **File storage** row, select the three dots menu (3). This will open a dropdown menu with more options.
5. From the dropdown menu, select **Generate keys** (4). This will open a pop-up window where you can generate your key.

<figure>
	<img src="file-storage-as-data-source/assets/2.png"/>
</figure>

6. Under **Set access level**, select **Read** (1).
7. Under **Set access end**, set a date far in the future (2). It is important because the report can refresh the data if the access key is inside the 'Set access end' period.
8. Select **Generate key** (3). 

<figure>
	<img src="file-storage-as-data-source/assets/3.png"/>
</figure>

9. Select **Copy key** (1) and go to Power BI Desktop.
	**Make sure to save this access key**. You will need it later.

<figure>
	<img src="file-storage-as-data-source/assets/4.png"/>
</figure>

### Step 3: Open your old Power BI file with Power BI Desktop
1. In Power BI Desktop, in the **Home** tab (1), select **Transform data** (2). This will open a dropdown. Select **Transform data** (3).

<figure>
	<img src="file-storage-as-data-source/assets/8.png"/>
</figure>

2. Find the query which uses Data Fabric and select it (1).
3. Then, under **Applied Steps**, next to **Source**, double-click the gear icon (2).
4. Under URL parts (3 & 4), paste the access key you just generated in Data Workbench in the following way:
	* In the upper part (3), paste the part of the access key which is before **?** symbol. Do not include the **?** symbol here.
	* In the lower part (4), paste the part of the URL which begins with the **?** symbol, including the **?** symbol.
5. Select **Ok** (5).

<figure>
	<img src="file-storage-as-data-source/assets/14.png"/>
</figure>

### Step 4: Upload the downloaded report in your VAP service
To upload the file you downloaded in step 1:
1. In the left navigation sidebar, select the plus icon.
1. Select **Add Resource File**.
1. Under **File Name**, name the file. In the name, include a version number or date for easy identification.
1. Then, drag and drop the file from your local machine onto **Drop file here or click to upload** or select **Drop file here or click to upload** to add the file from your local machine.
1. In the bottom right corner, select **Save**.

#### Scheduled Refresh
If the report needs to be refreshed with new data, follow [the scheduled refresh steps](admin-tab/resource.md).

Then, test the on-demand refresh from VAP by clicking the **Refresh Report** icon. It might take some time, so wait, or you come back to this point later.

### Step 5: Change the file name to the newly uploaded file in Reports
1. Go to **Resources** and locate the old report name.
1. Then, hover over the **Used in Reports** column for that report to view the report title connected to the old Data Fabric file.
1. Note down this report title.

Then, go to **Reports** to change the file connection to the latest file version. 

**Note that you need to repeat the steps below for all the report titles you noted down in the step above.**

1. In **Reports**, search for the report title using the Filter option.
1. Edit the report by changing the file name to the newly uploaded file (latest version or today’s date).
1. Select **Save**.
1. Hover over the **Used in Entities** column for that report to view the entities where the report is used.
1. Make sure you have access to these entities.
1. Run the reports from **Home** to ensure they work correctly.

Go to **Resources** to delete the old file connected to Data Fabric. To do it:
1. Find the old Power BI report File Name.
1. Make sure the **Used in reports** column displays *0 Reports*.
1. In the **Actions** column, select **Delete** to delete the old Power BI file that used datasource from Data Fabric.

### Step 6: Repeat the steps for all Power BI file names you need to migrate 
For all Power BI file names that you need to migrate, follow all the above steps starting with [step 1](#step-1:-locate-and-download-the-original-Power-BI-file).

## Conclusion
- Now you should have migrated all your Power BI reports to be connected to Data Workbench File Storage. Your reports will run as expected and should refresh data from File Storage if set up.
- Need Support? If you need any support, contact the [support team](mailto:support@veracity.com).

## Summary of Key Points
- **Download and upload**: Download the original Power BI files if you do not have them in your source control repository.
- **Prepare for migration**: Familiarize yourself with File Storage and upload your data from Data Fabric to File Storage.
- **Connect and update**: Change the old reports. Connect your reports to the new data source. Obtain access keys for your data in File Storage and change the Power BI reports using these keys.
- **Upload**: Upload in VAP, and ensure they are correctly configured.
- **Test and repeat**: Test the reports to ensure they work correctly and repeat the process for all necessary reports.