---
author: Veracity
description: This is the changelog for the June 2024 fourth release of Data Workbench.
---

# June 2024 fourth release

Read this page to learn what has changed in Veracity Data Workbench with the June 2024 fourth release.

## New features
This section covers new features.

### Download SoC from a data set
We have added an endpoint for downloading Statement of Compliance (SoC) PDF file based on workspaceId, datasetId, and documentId.

To download SoC, call the following endpoint using your [workspaceId](https://developer.veracity.com/docs/section/dataworkbench/apiendpoints#workspace-id), [datasetId](https://developer.veracity.com/docs/section/dataworkbench/apiendpoints#data-sets-endpoints) (see Data set endpoints), and documentId.

`https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/datasets/documents/download`

To get documentID, call the `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/datasets/{datasetId}/query` endpoint. In the response, locate the **File_Link** field and copy it; this **is the documentId**.

