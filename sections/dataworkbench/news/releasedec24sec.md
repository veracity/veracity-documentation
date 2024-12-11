---
author: Veracity
description: This is the changelog for the December 2024 release of Data Workbench.
---

# December 2024 second release

Read this page to learn what has changed in Veracity Data Workbench with the December 2024 release.

## New features
This section covers new features.

### Create and edit a workspace schema
Now, as a workspace admin, you can create and edit a workspace schema.

### Fetch a schema version detail
Now, as a developer, you can fetch a schema version detail by `schemaversionID`.

### Scope access based on subscriptions
Now, the scope to which the user groups have access is based on the subscription of the workspace to which they belong.

Users of the workspace with the 'schema management' subscription can access schema management.

Users of the workspace whith the 'schema management' subscription and 'validation rule management' subscription can access schema management and validation rule management.

### View DataMap subscriptions in ledger
Now, as a developer, you can view the DataMap subscription events in ledger.

### Get subscriptions by workspace
As a developer, you can get subscriptions by workspace by using the GET method and calling the following endpoint:
`/api/v1/subscriptions/workspaces/{workspaceId}`

### Add a subscription (POST method)
As a developer, you can add a SchemaManagement or ValidationRuleManagement subscription by using the POST method and calling the following endpoint:
`/api/v1/subscriptions`

### Add a subscription (PUT method)
As a developer, you can add a SchemaManagement or ValidationRuleManagement subscription by using the PUT method and calling the following endpoint:
`/api/v1/subscriptions/{subscriptionId}`

### Check a subscription
As a developer, you can check a SchemaManagement or ValidationRuleManagement subscription by using the GET method and calling the following endpoint:
`api/v1/subscriptions/{subscriptionId}`

### Remove a subscription 
As a developer, you can remove a SchemaManagement or ValidationRuleManagement subscription by using the DELETE method and calling the following endpoint:
`/api/v1/subscriptions/{subscriptionId}`

### Retrieve a DataMap subscription by workspace
As a developer, you can retrieve a DataMap subscription by workspace using the GET method and calling the following endpoint in Facade:
`/api/v1/subscriptions/workspaces/{workspaceId}/subscription`

### Create a schema using workspaceId
As a developer, you can create a schema by using `workspaceId` as a part of the route. To do it, use the POST method and call the following endpoint:
`/api/v1/DataMaps/{workspaceId}/Schemas`

You can also use this endpoint as a user if the workspace is the owner of the schema and has the Schema Management module subscription.

### Patch a schema version using workspaceId
As a developer, you can patch a schema version by using `workspaceId` as a part of the route. To do it, use the PATCH method and call the following endpoint:
`/api/v2/DataMaps/{workspaceId}/Schemas/{schemaId}/Versions/{schemaVersionId})`

As a user, you can also apply changes to the endpoint above to patch a schema version. To do it, use the PATCH method and call the following endpoint:
`v1/facade/workspaces/{workspaceId}/schemas/{schemaId}/versions/{versionId}`

**Note that**:
* The schema `workspaceId` must the same as the `workspaceId` being called.
* The workspace must subscribed to the DataMap 'SchemaManagement.

### Add a schema version 
As a user, you can add a schema version by using by using the POST method and calling the following endpoint:
`/api/v1/DataMaps/{workspaceId}/Schemas/Version`

**Note that**:
* You must apply these changes to an existing endpoint.
* The schema `workspaceId` must the same as the `workspaceId` being called.
* The workspace must subscribed to the DataMap 'SchemaManagement.

## Make a schema version default
As a user, you can make a schema version default by using the PATCH method and calling the folllowing endpoint:
`/api/v1/DataMaps/{workspaceId}/Schemas/{schemaId}/Versions/{schemaVersionId}`

**Note that**:
* You must apply these changes to an existing endpoint.
* The schema `workspaceId` must the same as the `workspaceId` being called.
* The workspace must subscribed to the DataMap 'SchemaManagement.

## Patch a schema
As a user, you can patch a schema by using the PATCH method and calling the folllowing endpoint:
`/api/v1/DataMaps/{workspaceId}/Schemas/{schemaId}`

**Note that**:
* You must apply these changes to an existing endpoint.
* The schema `workspaceId` must the same as the `workspaceId` being called.
* The workspace must subscribed to the DataMap 'SchemaManagement.

## Changes in existing features
This section covers changes in existing features.


