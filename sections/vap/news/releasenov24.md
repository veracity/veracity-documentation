---
author: Veracity
description: This is the changelog for the release 4.18 of Veracity Adapter for Power BI (VAP).
---
# VAP 4.18 release

Read this page to learn what has changed in the Veracity Adapter for Power BI. 

## New Features

This section covers new features.

### Paginated report support

Now, you can upload a paginated report. Note that the report must be in .rdl format.

#### Service Principal required

To upload a paginated report, your VAP service must use a Service Principal account. If your service is a new setup using Service Principal, then the **Paginated Report** toggle button can be turned on in Admin. You cannot upload the paginated report file for the legacy Power BI Service Principal. If you try to do so, you will get the error message 'Paginated report is not enabled to upload'. 

#### Supported data sources

We support the following methods to add a data source to a paginated report.
* You can connect a database as a data source directly. We support Azure SQL database.
* You can connect a semantic model as a data source. We support Azure SQL database, on-premises SQL database, Web (API call), files (.csv, .json, and more) and Azure Blob.

#### Report reloading

The report reloads after an hour of interacting with it. When it happens, you will see a reload icon. To continue reading the report, wait for the report to finish reloading.


#### Session expiry

If you do not interact with a paginated report for ten minutes, your session expires.

### Direct interaction with a report for the user with one entity

Now, if you have access to only one entity, you can interact with the report directly.

### Two levels of bookmarks supported

Now, in the bookmark dropdown, you can interact with two levels of bookmarks. It applies to reports where the report developer creates two levels of report bookmarks and toggles on the **Bookmarks based on report file** report feature.

### Other improvements

We have worked on Front Door improvements, Embed API support, and Service Principal.


## Changes in existing features

This section covers changes in existing features.

### The name of the entity in the notification

Now, when you grant a user access to an entity or revoke it and notify them about it, the notification includes the name of this entity.