---
author: Veracity
description: This is the changelog for the May 2023 second release of Data Workbench.
---

# May 2023 second release

Release date: May 2023

Read this page to learn what has changed in Veracity Data Workbench with the second release in May 2023.

## New features

### Marketplace banner
Now, [guest users](releasejan23.md) will see a marketing banner at the top of the page, advising to purchase Data Workbench in the Veracity marketplace.

## Changes in existing features

### Redirect from guest access for tenant or workspace members
If you are a member of a Data Workbench tenant or workspace, when someone shares access to their data set you, you see this under the **Shared with me** tab and not in [guest access](releasejan23.md). 

Thanks to this, guest access does not limit you, and you can explore the shared tenant or workspace, keeping access to all Data Workbench features.

### API endpoints for improved filtering and sorting
In the previous release, we have improved filtering and sorting. For details, go [here](releasemay23.md). Now, you can benefit from them through [API endpoints](../apiendpoints.md).

### Changed get data sets and query activity logs endpoints

The endpoints below were changed to version 2 that supports filtering and sorting. We recommend using them. However, the previous version (v1) of those endpoints still works.

The endpoint for getting available data sets changed to `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/datasets`.

The endpoint for getting a specific data set by its ID changed to `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/datasets/{datasetId} endpoint`.

The endpoint for querying for data by workspace ID changed to `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/datasets/{datasetId}/query`.

For current information on endpoints, go to [the API documentation](../apiendpoints.md).

### Endpoint base URL in API integrations
In **API Integrations**, under **Endpoints base URL**, after 'workspaces', we have added your workspace ID. 

For example, for the endpoint base URL `https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/56e9535f-9639-403f-9e39-9a34ccf60d75`, the workspace ID is `56e9535f-9639-403f-9e39-9a34ccf60d75`.

### Direct link to the documentation in API integrations
Previously, the link to the documentation below  **API Integrations** and under **Endpoints base URL** was taking you to a general section of the docs. Now, it takes you directly to the documentation on the API endpoints. 