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

For details, see [Data Workbench on Marketplace](https://store.veracity.com/b692-2dd3fb6b0225-workbench).

## Tenants and workspaces

Each company or a B2C customer has one tenant in Data Workbench. A tenant can have multiple workspaces. Each workspace has members. Workspace members can be admins or readers. For information on user management, go [here](usermanagement.md).

## Connectors and connections
Each workspace has connectors and connections. A connector defines a way of connectivity between Veracity and a source system. A connection is an instance of a connector, and it is used by the dataset to query data from a data source.

To see available connectors and connections in your workspace, go to the **Connections** tab. 

For details on setting up a connection, go [here](connectors.md). Once you have set up a connection, the Data Catalogue will show the predefined data sets queried from the corresponding source system.

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

