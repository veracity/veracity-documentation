---
author: Veracity
description: Overview of data sources and security in the Veracity Adapter for Power BI.
---

# Data sources and security in Power BI reports

VAP workspaces are hosted in Microsoft cloud either in the UE or USA, depending on where your service is set up. For maxium safety, DNV owns private premium capacities and does not share them with anyone.

VAP does not store your data and it cannot access it. VAP only stores the report and data set ID, so that they can be loaded from their source location into your reports in VAP. 
As Power BI report developer, please make sure you keep your Power BI file, source code, in a secure folder. It's a good idea to agree with coleagues where to store these files, in case some leave the company or are out of office when updates have to be done.

VAP supports using multiple data sources in your Power BI report. The data sources and credentials you use when creating your report are part of your Power BI file. If you want to override and update them, you can do so from VAP. These updates are written down on the Power BI file and not store or captured in VAP.

You can use the following data sources:
* You import the data from the source file when developing your Power BI report. Suitable if the data changes seldom.
* Refreshable data sources stored in the cloud. Suitable if the data changes frequently.

VAP supports the following refreshable data sources:
* Azure SQL Database through direct query. VAP refreshes data each time the users views the report.
* Veracity Data Fabric containers (to see your containers, in Veracity's top navigation bar, select "My data"). You can set up data to refresh daily, weekly, or monthly. The maximum number of daily refreshes is 48 which means the data would be refreshed approximately every 30 minutes. 
If you want to create a Veracity Data Fabric container and do not have that access level go here https://store.veracity.com/veracity-data-fabric-secure-data-sharing
* Azure Analysis Services. VAP refreshes data each time the users views the report.
* On Permises Databases through Gateway.

Azure Analysis Services can offer the fastest way of refreshing report data, while Azure SQL Database may be the slowest (depending on the data model and the amount of data).

## Row-level security

Use row-level security (RLS) if you want to store all data in one report and show each user only the data they should have access to. Note that what users see in VAP is controlled by the report settings that are configured in Microsoft Power BI.

To use RLS:
1. Implement RLS in your Power BI report file. For details, follow the [Microsoft tutorial](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-rls).
2. [When creating a report in VAP](admin-tab/manage-reports.md), provide the required values for row-level security.
