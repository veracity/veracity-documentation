---
author: Veracity
description: This is the changelog for the release 4.20 of Veracity Adapter for Power BI (VAP).
---
# VAP 4.20 release

We released a new landing page, added support for reports with data from Data Workbench File Storage, and made some technical improvements. 

Also, Veracity has discontinued Data Fabric, which might mean you need to migrate your data and update your reports if you were using Data Fabric.

## New features

### New landing page with your VAP services
We have introduced a new landing page showing all the services you have acccess to. For your convenience, the page first shows the services that you use the most.  You can access it at [https://insight.dnv.com/](https://insight.dnv.com/) or [https://insight.veracity.com/](https://insight.veracity.com/).

What changes:
- If you access VAP through My Services or a saved bookmark, nothing changes for you.
- If you have access to multiple VAP services, you can find them all on this landing page.
- If you type the wrong service URL, you are redirected to the landing page where you can select the correct service.


### Support for reports with data from Data Workbench File Storage
You can now develop and share reports that use data from Data Workbench File Storage. For details, go [here](../file-storage-as-data-source/introduction.md).

## Changes in existing features

### Database migration tool
A database migration tool is now available to automatically migrate database changes to SQL databases in the TEST, STAG, and PROD environments through the CI/CD pipeline.

### Delete old data source connection
After updating Data Fabric and Data Workbench File Storage data source URLs, old data source connections will now be deleted automatically.

## Action required for Data Fabric
If your reports use data from Veracity My Data (Data Fabric), you must update them now. Otherwise, they will no longer show updated data.

To migrate:
1. Migrate your data from Data Fabric to Data Workbench File Storage. [See how.](../../dataworkbench/filestorage/migrating.md)
2. Follow the [Migration Guide for VAP users](../dfmigration.md).