---
author: Veracity
description: This is the changelog for the January 2026 release of Data Workbench.
---

# January 2026 release
Read this page to learn what has changed in Veracity Data Workbench with the January 2026 release.

In Data Workbench, you control with whom you share your data sets and there are logs for each data set share. This release lets you get the information when a data set was shared and when sharing permission were modified for the last time. 

## Added creation and modification timestamps to Share relevant endpoints in Gateway API 
API users can now retrieve `CreatedOn` and `LastModifiedOn` timestamps when querying or retrieving a Share record. These fields are included in the ShareGetDto response for both **Get share by ID** and **Query shares** operations, enabling better tracking and automation based on share lifecycle events.

- Both fields are returned as UTC datetime values.
- `CreatedOn` reflects the timestamp when the share was first created.
- `LastModifiedOn` reflects the timestamp of the most recent update.