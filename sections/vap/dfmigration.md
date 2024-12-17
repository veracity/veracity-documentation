---
author: Veracity
description: This is a migration guide for VAP reports from Data Fabric to Data Workbench File storage.
---

# Migration Guide for VAP Users: Data Fabric to Data Workbench File Storage
**This is a draft and may not be fully accurate**. We will update this document soon.

## Introduction
- **Purpose**:This guide aims to assist VAP report developers in making their Power BI report work after migrating their data storage from Data Fabric to Data Workbench File Storage. 


For your Power BI report to read from a new location (File Storage), it must be changed in the Power BI Desktop. Then, upload it to VAP and switch the file connection in Report to the newly updated report. 
- **Audience**: VAP users with existing reports using Data Fabric.

## Prerequisites
- Access to the original Power BI files.
- Access to VAP and Data Workbench File Storage.
- Follow the migration guide from Veracity Data Workbench File Storage. See the following documentation: [Veracity Data Workbench migration](https://developer.veracity.com/docs/section/datafabric/datafabric-migration) , [Migration from Data Fabric](https://developer.veracity.com/docs/section/dataworkbench/filestorage/migrating), and [File storage](https://developer.veracity.com/docs/section/dataworkbench/filestorage/filestorage).
- Necessary permissions to upload and manage reports in VAP.

## Steps for VAP report developers to migrate an old Power BI report 

### Step 1: Locate and Download Original Power BI File
   - If you struggle to find the original Power BI file, download it from your service:
     1. Go to the VAP Admin tab and navigate to the Resources section.
     2. Use the filter to locate the .PBIX file by name.
     3. Select the file and click on the download icon to save it to your local machine.
     **Note that** if download is not enabled in your service, go to the **Config** page. Then, in **Tenant Properties**, select **Edit**, and enable **Allow Download Pbix**.

### Step 2: Change your Power BI report to read from new location (File Storage)
1. Open the report in Power BI Desktop 
2. Go to Data Workbench and select the **Data Catalogue** tab (1).
3. Select **File storage** (2).
4. In the **File storage** row, select the three dots menu (3). This will open a dropdown menu with more options.
5. From the dropdown menu, select **Generate keys** (4). This will open a pop-up window where you can generate your key.


<figure>
	<img src="../file-storage-as-data-source/assets/2.png"/>
</figure>

6. Under **Set access level**, select **Read** (1).
7. Under **Set access end** set a date far in the future (2). It is important because the report can refresh the data as long as the access key is inside the Set access end period.
8. Select **Generate key** (3). 

<figure>
	<img src="../file-storage-as-data-source/assets/3.png"/>
</figure>

9. Select **Copy key** (1) and go to Power BI Desktop.

<figure>
	<img src="../file-storage-as-data-source/assets/4.png"/>
</figure>

10. Make sure to save this access key. You will need it later.

### Step 3: Open your old Power BI file with Power BI Desktop
In Power BI Desktop, in the **Home** tab (1), select **Transform data** (2). This will open a dropdown. Select **Transform data** (3).


<figure>
	<img src="assets/8.png"/>
</figure>

### Upload the Downloaded Report
   - To upload the file you downloaded in step 1:
     1. In the left navigation sidebar, select the plus icon.
     2. Select "Add Resource File".
     3. Under "File Name", name the file.
     4. Then, drag and drop the file from your local machine onto "Drop file here or click to upload" or select "Drop file here or click to upload" to add the file from your local machine.
     5. In the bottom right corner, select "Save".

### Prepare for Migration
   - File Storage is replacing Data Fabric. If you are migrating from Data Fabric:
     1. Familiarize yourself with File Storage and ensure you meet the prerequisites for using it.
     2. Follow the migration guide to download your data manually.
     3. Upload the data you stored in Data Fabric to File Storage. You will need this data as a data source for your Power BI reports.

### Create a New Report with Data Workbench File Storage

**Obtaining Access Key for Data Workbench File Storage**:
1. Open your workspace in Data Workbench.
2. In your workspace, go to **Data catalogue** page.
3. In the row with a file or folder you want to generate a SAS token for, on the right, select three dots.
4. Under **Set access level**, choose access level (read or read and write).
5. Optionally, under **Set access start**, choose a date from which this file or folder should be accessible.
6. Under **Set access end**, choose a date from which this file or folder will no longer be accessible.
7. Select **Generate key** and a new field called **Access key** will show.
8. Select **Copy key**. 
9. Copy the access key and use it in your VAP report to authenticate and access the data.

Note that you must be a workspace admin in Data Workbench to generate access keys to files and folders.

**Creating a VAP Report Using Data Workbench File Storage**:
1. Start by creating a new Power BI report or opening an existing one.
2. In Power BI, go to the "Home" tab and select "Get Data".
3. Choose "Web" as the data source and enter the URL for the Data Workbench File Storage.
4. Provide the necessary authentication details using the access key generated earlier.
5. Load the data and design your report as needed.
6. Save the report with a meaningful name, including a version number or date for easy identification.

### Connect Report to New Data Source
   - Connect the report to the new data in Data Workbench File Storage.
   - Save the report.
   - Upload the new report to the VAP service.
   - Recommendation: Name the file with a version number or today’s date.

### Scheduled Refresh
   - If the report needs to be refreshed with new data, follow the scheduled refresh steps.

### Manage Old Power BI Reports
1. In Resources, find the old Power BI report.
2. Use the filter to locate the file by name.
3. Hover over the 'Used in reports' column.
  1. If the number is 0: Delete the file.
  1. If more than one report, repeat the steps for all of them.

### Update Report in VAP
Go to the Report section.
1. Find the report name using the filter.
1. Edit the report by switching the file name to the newly uploaded file (latest version or today’s date).
1. Save the report.

### Testing
1. Test on-demand refresh from VAP.
2.  Run the report from Home to ensure it works correctly.

### Repeat for All Reports
1. Follow the above steps for all reports that need to be migrated.

## Conclusion
- Summarize the importance of the migration.
- Provide contact information for support.

## Summary of Key Points
- **Download and upload**: Ensure you download the original Power BI files and upload them to VAP.
- **Prepare for migration**: Familiarize yourself with File Storage and upload your data from Data Fabric to File Storage.
- **Create new reports**: Obtain access keys for your data in File Storage and create new Power BI reports using these keys.
- **Connect and update**: Connect your reports to the new data source, update them in VAP, and ensure they are correctly configured.
- **Test and repeat**: Test the reports to ensure they work correctly and repeat the process for all necessary reports.