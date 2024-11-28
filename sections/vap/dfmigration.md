---
author: Veracity
description: This is a migration guide for VAP reports from Data Fabric to Data Workbench File storage.
---

# Migration Guide for VAP Users: Data Fabric to Data Workbench File Storage

## Introduction
- **Purpose**: This guide aims to assist VAP users in migrating their data storage from Data Fabric to Data Workbench File Storage.
- **Audience**: VAP users with existing reports using Data Fabric.

## Prerequisites
- Access to the original Power BI files.
- Access to VAP and Data Workbench File Storage.
- Necessary permissions to upload and manage reports in VAP.

## Steps for Migration

### Locate and Download Original Power BI File
   - If you struggle to find the original Power BI file, download it from your service:
     1. Go to the VAP Admin tab and navigate to the Resources section.
     2. Use the filter to locate the .PBIX file by name.
     3. Select the file and click on the download icon to save it to your local machine.

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