---
author: Veracity
description: This is the changelog for the fourth October 2023 release of Data Workbench.
---

# October 2023 fourth release

Read this page to learn what has changed in Veracity Data Workbench with the fourth October 2023 release.

## Changes in existing features

### Access shared data sets using API

When a business partner has shared with you access to a data set, you can add it to your workspace. Then, it is available through Data Workbench UI. However, before this change, you couldn't access your shared data sets through API calls. 

Now, when calling the following endpoints with the GET method, you also get the data sets that were shared with you and added to your workspace:
* '/gateway/api/v2/workspaces/{workspaceId}/datasets'
* '/gateway/api/v2/workspaces/{workspaceId}/datasets/{datasetId}'

Once you got the shared data sets, you can add them to your Service Account's scope so that your API consumers can access them.


