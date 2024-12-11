---
author: Veracity
description: This is the changelog for the December 2024 release of Data Workbench.
---

# December 2024 second release

Read this page to learn what has changed in Veracity Data Workbench with the December 2024 release.

## New features
This section covers new features.

### Schema management
Schema management is a feature that helps users view and manage the schemas.

To access the 'Schema management' feature, your workspace needs to have the 'SchemaManagement' subscription. Contact the Data Workbench team to add 'SchemaManagement' subscription to your workspace.
 
Once your workspace has a subscription, you will see the **Schema manager** button under the **Data catalogue** page to access it.
 
There are two types of schemas.
* **Predefined schemas** - public schemas that may be used by other workspaces.
* **Custom schemas** - workspaces created by your workspace.

In this schema management feature, we support:
* **View schemas** - to view schemas' details such as name, description, different schema versions, and their columns information.
* **Create schemas** - to create 'custom' workspace schema.
* **Edit schemas** - to edit schema info, edit existing versions' details, create a new schema version, or change the active version.

### Fetch a schema version detail
Now, as a developer, you can fetch a schema version detail by `schemaversionID`.

### View DataMap subscriptions in Ledger
Now, as a developer, you can view the DataMap subscription events in Ledger.

### Get subscriptions by workspace
As a developer, you can get subscriptions by workspace by using the GET method and calling the following endpoint.

`/api/v1/subscriptions/workspaces/{workspaceId}`

### Add a subscription (POST method)
As a developer, you can add a SchemaManagement or ValidationRuleManagement subscription by using the POST method and calling the following endpoint.

`/api/v1/subscriptions`

### Add a subscription (PUT method)
As a developer, you can add a SchemaManagement or ValidationRuleManagement subscription by using the PUT method and calling the following endpoint.

`/api/v1/subscriptions/{subscriptionId}`

### Check a subscription
As a developer, you can check a SchemaManagement or ValidationRuleManagement subscription by using the GET method and calling the following endpoint.

`api/v1/subscriptions/{subscriptionId}`

### Remove a subscription 
As a developer, you can remove a SchemaManagement or ValidationRuleManagement subscription by using the DELETE method and calling the following endpoint.

`/api/v1/subscriptions/{subscriptionId}`

### Retrieve a DataMap subscription by workspace
As a developer, you can retrieve a DataMap subscription by workspace by using the GET method and calling the following endpoint in Facade:

`/api/v1/subscriptions/workspaces/{workspaceId}/subscription`

## Changes in existing features
This section covers changes in existing features.

### Create a schema Gateway endpoint update
We have updated the following Gateway endpoint which you could call with the POST method.

`/workspaces/{workspaceId}/schemas/add`

Now, it points to the new endpoint in DataMaps which you can call with the POST method.

`api/v1/DataMaps/{workspaceId}/Schemas`

**Note that** the create schema functionality does not change even though it now internally refers to the new endpoint.

### Activate a schema version Gateway endpoint update
We have marked the following Gateway endpoint which you could call with the PATCH method as obsolete.

`/workspaces/{workspaceId}/schemas/{schemaId}/schemaversions/{schemaVersionId}`

To activate a schema version, we have introduced a new endpoint you can call with the POST method.

`/workspaces/{workspaceId}/schemas/{schemaId}/schemaversions/{schemaVersionId}/activate`

Now, this endpoint points to the new endpoint in DataMaps which you can call with the POST method.

`api/v1/DataMaps/{workspaceId}/Schemas/{schemaId}/Versions/{schemaVersionId}/activate`

**Note that** the activate a schema version functionality does not change even though it now internally refers to the new endpoint.