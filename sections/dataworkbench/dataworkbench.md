---
author: Veracity
description: This page contains an overview of Data Workbench.
---
# What is Data Workbench?
Data Workbench lets you:
* Get access to data and use it in your applications.
* Securely share your data and use data shared by others.
* Monitor who uses your data and revoke access to it.
* Build dashboards and reports on top of the data.
* Work with scalable data streams and self-defined non-time-series data streams.

## Tutorials
If you prefer watching than reading, see our [video tutorials](https://help-center.veracity.com/en/collections/3824716-data-workbench?_gl=1*7qojbi*_ga*MjQwOTQ4NzExLjE2NTg1MDk5OTQ.*_ga_DYYE3X0DZL*MTcxMTQ0MjYwMC4xOC4xLjE3MTE0NDI3ODcuMC4wLjA.).

Also, you might want to see:
* [How to query data](tutorial/tutorialq.md)
* [How to call API endpoints](tutorial/tutorial2.md).

## Tenants and workspaces
Each company or a B2C customer has one tenant in Data Workbench. A tenant can have multiple workspaces. Each workspace has members. Workspace members can be admins or readers. For information on user management, go [here](workspace.md).

### To create a new workspace
If you are a tenant admin, you can use the picker button to create a new workspace:
1. In the upper-left corner of the "Home" page, select the workspace and tenant picker button.
2. In the dropdown that appears, at the bottom, select the **Add workspace** button.

## Data integrations
 Data Workbench fetches data from external data sources by using data integrations. A data integration:
* Is an integration layer between a data provider and the Data Workbench. 
* Uses an API exposed by the provider to query data, and transforms it into a unified format used in Data Workbench.
* Is authorized on the provider's side and follows their authorization policy.
* If the provider enables downloading binary data, a data integration stores this data into cloud file stores, so that it can used by customers.
 
To see available data integrations in your workspace, go to the **Data integrations** tab. 

Once you have a data integration set up, the Data Catalogue will show the predefined data sets queried from the corresponding source system.

### Become a data provider
To become a data provider and integrate with Data Workbench, contact the Data Workbench team for assistance.

To integrate, you will need to implement a standardized API that consists of mandatory and optional endpoints that cover REST API verbs, paths, and contracts for request and response payloads.

Note that:
* The API allows only the REST protocol.
* You need to host the API in your own environment.
* You need to allow Data Workbench to access this API. If you have a firewall, adjust the rules accordingly.

The Data Workbench team will cooperate with you on gathering the requirements for creating a data integration. Expect to discuss:
* Technical aspects for server-to-server communication such as base URL of your API, server-to-server API keys, and more.
* Schemas that should be supported by the data integration. Data Workbench queries data for a certain schema, and your API also needs the schema to decide how to satisfy the request.
* Custom settings for each schema.
* Definition of settings that must be provided with a new data integration.

Also, you need to create data integrations. Currently, the Data Workbench team does it for you, but Veracity plans to make it self service.

### Data restrictions
Data Workbench can impose restricions on access to data. For each data integration, Veracity can configure a definition of mandatory settings that its data integrations must follow. These settings are represented by a dictionary (string<=>string) meaning they can contain any data (authorization data, environment data, etc). 

## Data catalogue
To see data sets available in your workspace, go to the **Data Catalogue** tab. For detailed documentation, go [here](datacatalogue.md).

## Using APIs
You can integrate APIs with Data Workbench. See:
* [How to start using APIs with Data Workbench](apimanagement.md).
* [API endpoints you can use](apiendpoints.md).
* [How to authenticate and authorize your API calls](authentication.md).

## Activity logs
Data Workbench logs certain events, and gives you access to [activity logs](workspace.md).
