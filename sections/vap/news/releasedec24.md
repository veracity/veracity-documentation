---
author: Veracity
description: This is the changelog for the release 4.19 of Veracity Adapter for Power BI (VAP).
---
# VAP 4.19 release

Read this page to learn what has changed in the Veracity Adapter for Power BI. 

## New Features
This section covers new features.

### New '+' button added to all modules
We have added a new '+' button to all the modules' top right corner. It allows you to add resources, reports, entities, and users directly within the module, without navigating to the left-side menu.

### On-demand refresh of paginated reports supported
Now, the on-demand refresh for paginated reports in Power BI is supported. It allows you to refresh the data in your reports whenever you need the most current information. We recommend you use this feature for reports relying on real-time data or requiring frequent updates.

**Note that**:
* Scheduled refresh of paginated reports **is not** supported.
* Most Power BI semantic models using dynamic data sources cannot be refreshed in a paginated report. To check if your dynamic data source can be refreshed, follow [this instruction](https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-data#refresh-and-dynamic-data-sources).

### Improved failure messages of on-demand refresh and scheduled refresh
We have improved the failure messages of on-demand refresh and scheduled refresh. Now, when you select the **Refresh History** button of a file, the status of the latest refreshes is displayed in a clearer way. The failure message has a tooltip over which you can hover to view and error code from Microsoft PBI.

### Make your VAP service ready to share paginated reports with your customers
We have defined a process to migrate a VAP service workspace to a new service principal workspace to allow for paginated report. 

Now, VAP team can help you move your service to support paginated report. 

Paginated reports are ideal for presenting content with tightly controlled rendering requirements, such as certificates, audit findings, test results, purchase orders, and long tabular data that must be printed on multiple pages. These reports ensure that your data is presented in a precise and organized manner, meeting the high standards of professional documentation.

### FAQ page
To inform you about the issues we are currently working on in VAP, we have created a [FAQ page](https://community.veracity.com/t/are-there-any-known-vap-issues/260).

### Infrastructure and security improvements
We have introduced some infrastructure and security improvements.

### .NET 8 Isolated model
We have worked on a .NET 8 Isolated model in VAP.