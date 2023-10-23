---
author: Veracity
description: This is the changelog for the fourth October 2023 release of Data Workbench.
---

# October 2023 fourth release

Read this page to learn what has changed in Veracity Data Workbench with the fourth October 2023 release.

## Changes in existing features

### Access shared data sets using API

When a business partner has shared with you access to a data set, you can add it to your workspace. Then, it is available through Data Workbench UI. However, before this change, you couldn't access your shared data sets through API calls. 

Now, when calling the following endpoints, you also get the data sets that were shared with you and added to your workspace:
* With GET, to get all data sets: `/gateway/api/v2/workspaces/{workspaceId}/datasets`.
* With GET, to get a data set by its ID: `/gateway/api/v2/workspaces/{workspaceId}/datasets/{datasetId}`.
* With POST, to query for data by workspace and data set ID: `/gateway/api/v2/workspaces/{workspaceId}/datasets/{datasetId}/query`.

For details on API endpoints, go [here](../apiendpoints.md).
