---
author: Veracity
description: This is the changelog for the May 2023 second release of Data Workbench.
---

# May 2023 second release

Release date: May 2023

Read this page to learn what has changed in Veracity Data Workbench with the second release in May 2023.

## New features

### Marketplace banner
Now, [guest users](releasejan23.md) will see a marketing banner at the top of the page, prompting them to purchase Data Workbench in the Veracity marketplace.

US 444470

### Endpoint for getting workspaces grouped by TenantID
Now, you can use the following endpoint to see all the workspaces you have access to grouped by TenantId. This should help you in sharing access to those workspaces.

Endpoint:

450623

## Changes in existing features

### Redirect from guest access for tenant or workspace members
If you are a member of a Data Workbench tenant or workspace, when someone shares access to their tenant or workspace with you, you see this under the **Shared with me** tab and not in a [guest access](releasejan23.md). Thanks to this, the guest access does not limit you, and you can explore the shared tenant or workspace, keeping access to all Data Workbench features.

US 446805

### API endpoints for improved filtering and sorting
In the previous release, we have improved filtering and sorting. For details, go [here](releasemay23.md). Now, you can benefit from them through API endpoints.

US 451971

### Endpoint base URL in API integrations
In **API Integrations**, under **Endpoints base URL**, after 'workspaces', we have added your workspace ID. 
For example, for the endpoint base URL 'https://api-test.veracity.com/veracity/dw/gateway/api/v1/workspaces/56e9535f-9639-403f-9e39-9a34ccf60d75', the workspace ID is '56e9535f-9639-403f-9e39-9a34ccf60d75'.

US 451654

### Direct link to the documentation in API integrations
Previously, the link to the documentation below  **API Integrations** and under **Endpoints base URL** was taking you to a general section of the docs. Now, it takes you directly to the documentation on the API endpoints. 

US 451654