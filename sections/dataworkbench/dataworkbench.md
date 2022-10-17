---
author: Veracity
description: This page contains an overview of Data Workbench.
---
# What is Data Workbench?
Data Workbench allows you to:
* Get access to data and use it in your applications.
* Securely share your data and use data shared by others.
* Monitor who uses your data, limit how long it is available, and revoke access to it.
* Build dashboards and reports on top of the data.
* Work with scalable data streams and self-defined non-time-series data streams.

## Tenants and workspaces

Each company or a B2C customer has one tenant in Data Workbench. A tenant can have multiple workspaces. Each workspace has members. Workspace members can be admins or readers. For information on user management, go [here](usermanagement.md).

If you are a tenant admin, you can use the picker button to create a new workspace. To do so:
1. In the upper-left corner of the "Home" page, select the workspace and tenant picker button.
2. In the dropdown that appears, at the bottom, select the **Add workspace** button.

## Connectors and connections
 Data Workbench fetches data from external data sources by using connectors. A connector:
- Is an integration layer between a data provider and the Data Workbench. 
- Uses an API exposed by the provider to query data, and transforms it into a unified format used in Data Workbench.
- Is authorized on the provider's side and follows their authorization policy.
- If the provider enables downloading binary data, a connector stores this data into cloud file stores, so that it can used by customers.

A connection binds together a connector and a tenant's workspace, and it is used by the dataset to query data from a data source. 

To see available connectors and connections in your workspace, go to the **Connections** tab. 
Once you have a connection set up, the Data Catalogue will show the predefined data sets queried from the corresponding source system.

### Becoming a data provider
To become a data provider and integrate with Data Workbench, contact the Data Workbench team for assistance.

To integrate, you will need to implement a standardized API that consists of mandatory and optional endpoints that cover REST API verbs, paths, and contracts for request and response payloads.

Note that:
- The API allows only the REST protocol.
- You need to host the API in your own environment.
- You need to allow Data Workbench to access this API. If you have a firewall, adjust the rules accordingly.

The Data Workbench team will cooperate with you on gathering the requirements for creating a connector. Expect to discuss:
- Technical aspects for server-to-server communication such as base URL of your API, server-to-server API keys, and more.
- Schemas that should be supported by the connector. Data Workbench queries data for a certain schema, and your API also needs the schema to decide how to satisfy the request.
- Custom settings for each schema.
- Definition of settings that must be provided with a new connection.

Also, you need to create connections. Currently, the Data Workbench team does it for you, but Veracity plans to make it self service.

### Data restrictions
Data Workbench can impose restricions on access to data. For each connector, Veracity can configure a definition of mandatory settings that its connections must follow. These settings are represented by a dictionary (string<=>string) meaning they can contain any data (authorization data, environment data, etc). 

## Data sets
To see data sets available in your workspace, go to the **Data Catalogue** tab. 

The **Predefined data sets** tab shows data sets that are queried by connections from their corresponding source systems. These data sets are inherited, and you cannot modify them. However, you can use them to create new data sets.

The **Created data sets** tab shows the data sets that workspace members created.

Each data set has:
* Title and description.
* Column picker – show or hide table columns.
* Filters - filter data.
* Save option – save your changes.
* Share option – share a data set with a user, and set for how long you grant them access.

To see data sets you can use, go to [My data](https://data.veracity.com/containers). 
To see how to manage your data on Data Fabric, go [here](https://help-center.veracity.com/en/collections/2429587-managing-your-data-on-data-fabric).

### Create a data set
To create a derived data set:
1. Select an existing data set.
2. Apply filters to get relevant data.
3. Save the data set.

If you want to upload a new data set, Veracity suggests using an existing template such as Poseidon Principles or Sea Cargo Charter. You can upload data as a CSV file. 

### Share a data set
You can share a snapshot of a data set to file storage in [Data Fabric](https://developer.veracity.com/docs/section/datafabric/datafabric) and specify who can access it and when their access expires.
To share a data set with one or more users:
1. Hover over the row with a data set. Two icons will appear in the right corner of the row.
2. Select the sharing icon (the last one).
3. Under **Share with user**, enter the email address of a user. You can add multiple users.
4. Select the **Add** button to confirm.
5. Under **Share access for**, select how long the data set should be available to the user(s).
6. Select the **Share** button. 

## Activity logs
Data Workbench logs certain events, and gives you access to [activity logs](activitylog.md).
