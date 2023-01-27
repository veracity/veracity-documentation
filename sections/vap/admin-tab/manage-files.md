---
author: Veracity
description: Overview of the Manage Files tab in the admin tab.
---

# Manage Files

Once you have built your report in Power BI, you can upload it into VAP and share access to it with your clients. By default, VAP will use the data sources from the report, but you can override and update them when uploading a file. For details on data sources and security, go [here](../vap.md#data).

Below the "Manage Files" heading (top centre), you can see if your Power BI files are stored in the EU or USA.
Supported file formats are PBIX, PDF, PNG, JPEG, GIF, JSON. If you want to add release notes, upload a JSON file that follows the [Report Release Note template](configure.md).

The "Manage Files" page shows all uploaded files in a table. To sort them by a specific column, select the column. 

In the right corner of each row you can:
* Refresh data (for [refreshable data sources](../data.md)).
* Schedule a data refresh (for [refreshable data sources](../data.md)).
* See history.
* Edit the file, see report ID and dataset ID or file name.
* Delete the file.

The actions above are listed from the first to the last icon from the left.

## To upload a file

To upload a file:
1. Select the **Upload a file** button.
2. Select the **Choose File** button and select the file from your local machine.
3. Read and accept the service terms.
4. Respond to personal data questions.
5. In the **Name** field, provide the name for the file. Veracity recommends including in the file name information that would help recognize the latest version of the file, such as, for example, the client's name, the report's date, and the upload date.
6. In the right corner, select the **Upload** button.

If you get a warning when VAP checks your report's data sources, follow the troubleshooting recommended in the warning. A warning may come if your datasource can not be automaticly refreshed. It is dependent on where you have your data files. Still you can use the file an view the analytics through VAP. When you change the data on your storage, upload a new version and change the connection to the latest file in Manage Report.
In the warnings messages use the icons in the dropdown, to change settings when needed. It is recomended to set the credentils for a database, through these icons, the first time that database is used in the service.

