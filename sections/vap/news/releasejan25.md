---
author: Veracity
description: This is the changelog for the release 4.20 of Veracity Adapter for Power BI (VAP).
---
# VAP 4.20 release

We released a new landing page, added support for Data Workbench uploaded data sets as data source in VAP reports, and made some technical improvements. 

Also, Veracity has discontinued Data Fabric, which might mean you need to migrate your data and update your reports if you were using Data Fabric.

## New features

### New landing page with your VAP services
We have introduced a new landing page showing all the services you have acccess to. For your convenience, the page first shows the services that you use the most.  You can access it at [https://insight.dnv.com/](https://insight.dnv.com/) or [https://insight.veracity.com/](https://insight.veracity.com/).

What changes:
- If you access VAP through My Services or a saved bookmark, nothing changes for you.
- If you have access to multiple VAP services, you can find them all on this landing page.
- If you type the wrong service URL, you are redirected to the landing page where you can select the correct service.


### New data source for reports: uploaded data sets
We have added another type of Data Workbench data set you can use as the data source in your reports: uploaded data sets. [See how to use them in your reports](../file-storage-as-data-source/introduction.md).

## Action required for Data Fabric
If your reports use data from Veracity My Data (Data Fabric), you must update them now. Otherwise, they will no longer show updated data.

To migrate:
1. Migrate your data from Data Fabric to Data Workbench File Storage. [See how.](../../dataworkbench/filestorage/migrating.md)
2. Follow the [Migration Guide for VAP users](../dfmigration.md).