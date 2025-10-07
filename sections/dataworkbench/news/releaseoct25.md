---
author: Veracity
description: This is the changelog for the October 2025 release of Data Workbench.
---

# October 2025 release
Read this page to learn what has changed in Veracity Data Workbench with the October 2025 release.

## New features

### Create uploaded data sets
Workspace admins can now create new uploaded data sets directly from the **Data catalogue**.  

A new **Upload new data set** button is available in both the **Predefined data sets** tab and the **Created data sets** tab **if your workspace has Schema management subscription**.

When you select this button, you go through the following steps:
1. **Upload a CSV file** - Drag and drop a file or select it from your computer. 
	- This file must comply with the requirements: maximum size 1 GB, comma as delimiter, all columns with headers, no special characters in the filename.  
2. **Select a schema** - In the next dialog, choose one schema to validate your file against. You can search by schema name, or use the **Show** link to open the schema details before selecting it.  
   - You can go back and select a different file if needed.  
   - Only schemas with an active locked version appear in this list.  
3. **Validation** - The system checks your file against the selected schema. Warnings or errors are shown at the top of the dialog. You must resolve any issues before continuing.  
4. **Enter data set details** - If validation succeeds, you are prompted to provide a unique data set name and, optionally, a description.  
5. **Upload and track progress** - Select **Upload** to finish. You are taken back to the Data catalogue tab, and a toast notification in the corner shows upload progress. The toast updates until the upload is complete and displays either success or failure (with an error ID if failed).  

## Changes in existing features

### Column order in data sets
Previously, when creating a data set with an assigned schema, the dataset view did not respect the column order defined in the schema. Instead, it displayed columns in the JSON response order.  
Now, data set details show columns in the order configured in the schema definition.