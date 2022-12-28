---
author: Veracity
description: Overview of data sources and security in the Veracity Adapter for Power BI.
---

# Data sources and security

VAP workspaces are hosted in Microsoft cloud either in the UE or USA, depending on where your service is set up. For maxium safety, DNV owns private premium capacities and does not share them with anyone.

VAP does not store your data and it cannot access it. VAP only stores the report and data set ID, so that they can be loaded from their source location into your reports in VAP. 

VAP supports using multiple data sources in your Power BI report. The data sources and credentials you use when creating your report are automatically imported into VAP. If you want to override and update them, you can do so from VAP.

You can use the following data sources:
* Your Power BI report. VAP will import the data from it. Suitable if the data changes seldom.
* Refreshable data sources stored in the cloud. Suitable if the data changes frequently.

VAP supports the following refreshable data sources:
* Azure SQL Database through direct query. VAP refreshes data each time the users views the report.
* Veracity Data Fabric containers (to see your containers, in Veracity's top navigation bar, select "My data"). You can set up data to refresh daily, weekly, or monthly. The maximum number of daily refreshes is 48 which means the data would be refreshed approximately every 30 minutes. 
* Azure Analysis Services. VAP refreshes data each time the users views the report.
* On Permises Databases through Gateway.

Azure Analysis Services can offer the fastest way of refreshing report data, while Azure SQL Database may be the slowest (depending on the data model and the amount of data).

## Row-level security

Use row-level security (RLS) if you want to store all data in one report and show each user only the data they should have access to. Note that what users see in VAP is controlled by the report settings that are configured in Microsoft Power BI.

To use RLS:
1. Implement RLS in your Power BI report file. For details, follow the [Microsoft tutorial](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-rls).
2. [When creating a report in VAP](admin-tab/manage-reports.md), provide the required values for row-level security.