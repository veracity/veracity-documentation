---
author: Veracity
description: This is the changelog for the release 4.18 of Veracity Adapter for Power BI (VAP).
---
# VAP 4.18 release

Read this page to learn what has changed in the Veracity Adapter for Power BI. 

## New Features

This section covers new features.

### Paginated report support

Now, in VAP, you can upload a paginated report. Note that the report must be in .rdl format.

#### Service principal required

To upload a paginated report, you must use a Service Principal account. Note that all VAP services set up after 4.18 use Service Principal. However, if your VAP service was set up before 4.18 with a master account, you must set up another service to use paginated reports.

#### How to upload a paginated report

To upload a paginated report:
1. From the left sidebar, select the plus icon and the **Add Resource File** button and upload the RDL file.
2. Then, from the left sidebar, select the plus icon and then, select the **Add Report** button. Under **Report Type**, select **RDL report**.
3. Add the report to the entity.


#### Supported data sources

See how to add a data source to a paginated report.
* You can connect a database as a data source directly. We support Azure SQL database.
* You can connect a semantic model as a data source. We support Azure SQL database, on-premises SQL database, Web, File and Azure Blob, and more.

#### Report reloading

The report reloads after an hour of interacting with it. When it happens, you will see a reload icon. To continue reading the report, wait for the report to finish reloading.


#### Session expiry

If you do not interact with a paginated report for ten minutes, your session expires.

### Direct interaction with report for user with one entity

Now, if you have access to only one entity, you can interact with the report directly.

### Other improvements

We have worked on Front Door improvements, Embed API support, and Service Principal.

## Changes in existing feaures

This section covers changes in existing features.

### Notification includes name of entity when access granted or revoked

Now, when you grant a user access to entity or revoke it, then, when you notify them about it, they notification includes the name of the entity they got or lost access to.


