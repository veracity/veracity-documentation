---
author: Veracity
description: This is the changelog for the May 2024 release of Data Workbench.
---

# May 2024 release
Read this page to learn what has changed in Veracity Data Workbench with the May 2024 release.

## New features
This section covers new features.

### New columns for OVD schemas
We have added the following columns to the OVD schemas:
* Check_Group (string, max 50 characters)
* Count_Warnings, Int32
* Count_Issues_CII, Int32
* Count_Warnings_CII, Int32
* Count_Issues_ETS, Int32
* Count_Warnings_ETS, Int32

If you want to access all the updated OVD schemas, use the `Check_Group` column.

## Changes in existing features
This section covers changes in existing features.

### Described columns in predefined OVD datasets
We have added descriptions to columns in predefined OVD datasets.

### Corrected one column type in DCS Period Summary
Previously, in the DCS Period Summary, the Consumption Methanol column's type was set to Boolean. Now, it is corrected, and this column type is Decimal, so it shows the actual number.
