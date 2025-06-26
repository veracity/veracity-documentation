---
author: Veracity
description: This is the changelog for the May 2025 release of Data Workbench.
---

# May 2025 release
Read this page to learn what has changed in Veracity Data Workbench with the May 2025 release.

## New features
This section covers new features.

### Choose dataset download format
You can now choose your preferred file format when downloading datasets. When you open a dataset from the **Data catalogue** and click the **Download** button in the top-right corner, you will see a new dropdown menu with the options **Download as CSV** and **Download as Excel**. 

This feature is available for normal datasets, shared datasets, and guest view datasets.

## Bugs fixed
Previously, if you accessed a tenant URL using incorrect letter casing (for example, entering the tenant alias in lowercase instead of matching the actual casing), the workspace would redirect but display a 400 Bad Request error and fail to load dataset metadata. This issue is now fixed, and tenant aliases are handled correctly regardless of case sensitivity in the URL.
