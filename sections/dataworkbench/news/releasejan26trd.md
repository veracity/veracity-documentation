---
author: Veracity
description: This is the changelog for the January 2026 third release of Data Workbench.
---

# January 2026 third release

Read this page to learn what has changed in Veracity Data Workbench with the January 2026 third release.

## Changes in existing features
This section covers changes in existing features.

### Edit shared datasets after sharing

You can now edit and save shared datasets without canceling and re-sharing them. The **Save** button is now active for shared datasets.

A warning will appear when saving changes to alert you of downstream impacts.

If you reduce the dataset’s scope by removing assets or columns, the change propagates to all linked shares, which may cause them to break. Invalid datasets will display a clear error message explaining the issue.

### Simplified dataset names in SPP templates

Auto-generated dataset names in SPP templates no longer include the workspace name prefix, making them shorter and easier to read.
