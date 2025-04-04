---
author: Veracity
description: Overview of data sources and security in the Veracity Adapter for Power BI.
---

# Data sources and security in Power BI reports
VAP workspaces are hosted in the Microsoft cloud, either in the EU or the USA, depending on your service location. For maximum security, DNV owns private premium capacities and does not share them with others.

VAP does not store or access your data. It only retains the report and dataset ID to load them from their source location into your reports in VAP.

## Best practices for Power BI developers
If you are a Power BI report developer:
- Store your Power BI files and source code in a secure folder.
- Ensure access for coworkers who may need to substitute for you when you are unavailable.

## Supported data sources
VAP allows multiple data sources in your Power BI report. The data sources and credentials you use when creating your report are part of your Power BI file. You can override and update them in VAP, but changes are made directly to the Power BI file—VAP does not store or capture them.

### Types of data sources
You can use the following data sources:
* Data imported from source files when developing your Power BI report. Suitable for data that rarely changes.
* Refreshable data sources stored in the cloud. Suitable if the data changes frequently.

### Supported refreshable data sources
VAP supports the following refreshable data sources:
- Azure SQL Database through direct query. VAP refreshes data each time the users views the report.
- Veracity Data Fabric containers (to see your containers, in Veracity's top navigation bar, select "My data"). You can set up data to refresh daily, weekly, or monthly. The maximum number of daily refreshes is 48 which means the data would be refreshed approximately every 30 minutes. 
If you want to create a Veracity Data Fabric container and do not have the necessary access level, you can obtain it [here](https://store.veracity.com/veracity-data-fabric-secure-data-sharing).
- Azure Analysis Services. VAP refreshes data each time the users views the report.
- On-Premises Databases (via Gateway).
- Data Workbench File storage. See [the tutorial](file-storage-as-data-source/introduction.md).
- Data Workbench uploaded structured data set. Found in Data Workbench in Data Catalogue > Created data sets, with "Type" marked as "Uploaded". Those data sets must be [structured](../dataplatform/concepts/structdata.md).

### Performance considerations
- Azure Analysis Services typically provides the fastest data refreshes.
- Azure SQL Database may be the slowest, depending on the data model and dataset size.

## Row-level security (RLS)
Use RLS to store all data in one report while restricting access to users based on their roles. VAP displays data according to the report settings configured in Microsoft Power BI.

To use RLS:
1. Implement RLS in your Power BI report file. For details, follow the [Microsoft tutorial](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-rls).
2. [When creating a report in VAP](admin-tab/reports.md), provide the required role name for row-level security.
3. When creating an entity in VAP, provide the required value for [row-level security](admin-tab/entities.md).
