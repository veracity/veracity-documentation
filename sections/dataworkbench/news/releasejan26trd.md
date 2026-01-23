---
author: Veracity
description: This is the changelog for the January 2026 third release of Data Workbench.
---

# January 2026 third release

Read this page to learn what has changed in Veracity Data Workbench with the January 2026 third release.

## Changes in existing features
This section covers changes in existing features.

### Edit shared datasets after sharing

You can now edit and save shared data sets without canceling and re-sharing them. The **Save** button is now active for shared datasets.

A warning will appear when saving changes to alert you of downstream impacts. 

**Note that**:
* When you increase the scope, shares remain unaffected.
* When you decrease the scope, it affects shares.
* When you completely change the scope by replacing originally shared columns or filters, shares break.
* When you update the base data set to "select all columns", downstream shares reflect all available columns.
* When you add a filter on a column not selected by downstream shares, downstream data set becomes invalid.
* When you remove a filter and its corresponding column from the base data set, downstream shares become invalid.

Invalid data sets display a clear error message explaining the issue.

### Simplified dataset names in SPP templates

Auto-generated dataset names in SPP templates no longer include the workspace name prefix, making them shorter and easier to read.
