---
author: Veracity
description: This page lists API endpoints for Data Workbench.
---
# API endpoints

You can use the following API endpoints for Data Workbench:
* [Workspace endpoints](#workspace-endpoints)
* [Connector and connections endpoints](#connectors-and-connections)
* [Data sets endpoints](#data-sets-endpoints)

To see response codes for the API, go [here](#response-codes).

## Workspace endpoints

Each customer has one tenant in Data Workbench. A tenant can have multiple workspaces.

To get a list of workspace schemas for a specific workspace, call the https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId}/schemas endpoint. You must provide `{workspaceId}`(string, $UUID).

Below you can see an example of a successful request (code 200).

```json
[
    {
        "id": "7c312976-3d3d-4te3-9234-12f238f71234",
        "workspaceId": "00000000-0000-0000-0000-000000000000",
        "name": "DCS Period Summary",
        "description": "Aggregated emissions per DCS period including verification status, grouped by owner and flag",
        "industry": "Maritime",
        "isPredefined": true,
        "avatarColor": 55,
        "createdBy": "c44e1e55-fa3a-4553-b974-87eb50e41234",
        "createdOn": "2022-05-23T11:42:34.9558871Z",
        "lastModifiedBy": "c44e1e55-1232-4553-b974-87eb50e41234",
        "lastModifiedOn": "2022-05-23T11:42:34.9558871Z"
    },
 {
        "id": "2a0b9aa7-b7d5-4fbb-9a59-850459cd1234",
        "workspaceId": "e03c005e-1adf-456a-9d84-3f8694831234",
        "name": "TEST Name",
        "description": "TEST DESCRIPTION",
        "industry": "",
        "isPredefined": false,
        "avatarColor": 60,
        "createdBy": "2f3t7ee2-1234-4d25-af86-f5364fcb1234",
        "createdOn": "2022-06-07T06:49:35.5587386Z",
        "lastModifiedBy": "2f2e7ae3-1234-4d25-af86-f5364fcb1234",
        "lastModifiedOn": "2022-06-17T08:55:25.063984Z"
    }
]
```

## Connectors and connections
To see the connections a workspace uses, go to the **Connections** tab in your workspace.

You can list all connections used by a workspace by calling the https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId}/connections endpoint. You must provide `{workspaceId}` (string, #UUID) in your call.

Below you can see an example of a successful request (code 200).
```json
[
  {
    "connectionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "connectionName": "string",
    "connector": {
      "connectorId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "name": "string",
      "connectorType": "string",
      "description": "string",
      "dataProvider": "string",
      "connectorConfiguration": {
        "connectionSettings": [
          {
            "key": "string",
            "name": "string",
            "description": "string"
          }
        ]
      },
      "schemaSupport": {
        "supportedSchemaVersions": [
          {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "schemaVersionName": "string",
            "settings": [
              {
                "key": "string",
                "value": "string",
                "type": "string",
                "description": "string"
              }
            ]
          }
        ]
      }
    },
    "schemaSupport": {
      "supportedSchemaVersions": [
        {
          "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "schemaVersionName": "string"
        }
      ]
    },
    "connectionConfiguration": {
      "connectionSettingValues": [
        {
          "key": "string",
          "value": "string"
        }
      ]
    }
  }
]
```

You can also list all the connectors used by a workspace by calling the https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId}/connectors endpoint. You must provide `{workspaceId}` (string, #UUID) in your call.

Below you can see an example of a successful request (code 200).
```json
[
  {
    "connectorId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "string",
    "connectorType": "string",
    "description": "string",
    "dataProvider": "string",
    "connectorConfiguration": {
      "connectionSettings": [
        {
          "key": "string",
          "name": "string",
          "description": "string"
        }
      ]
    },
    "schemaSupport": {
      "supportedSchemaVersions": [
        {
          "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "schemaVersionName": "string",
          "settings": [
            {
              "key": "string",
              "value": "string",
              "type": "string",
              "description": "string"
            }
          ]
        }
      ]
    }
  }
]
```

## Data sets endpoints

You can use the following endpoints:
* [Get all data sets for a workspace](#allData)
* [Get specific data sets by ID](#data)
* [Query for data sets by ID and with additional properties](#dataMore)

<a name="allData"></a>To get all data sets available in a workspace, call the https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId}/datasets endpoint. You must provide `{workspaceId}` (string, $UUID).
You can use additional properties in your query:
* {isBaseDataset} – boolean; by default, no value; you can set it to "true" or "false"
* {pageIndex} – integer($int32)
* {pageSize} – integer($int32)
* {sortColumn} – string
* {sortDirection} – string; by default, no value; you can set it to "ascending" or "descending"

Below you can see an example of a request URL that uses all additional properties.
https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId}/datasets?isBaseDataset=true&pageIndex=1&pageSize=1&sortColumn=1&sortDirection=Ascending

Below you can see an example of a successful request (code 200).
```json
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "string",
    "description": "string",
    "workspaceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "connectionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "createdBy": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "createdOn": "2022-08-10T14:31:12.825Z",
    "lastModifiedBy": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "lastModifiedOn": "2022-08-10T14:31:12.825Z",
    "schemaInfo": {
      "schemaVersionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "schemaName": "string"
    },
    "queries": {
      "additionalProp1": [
        "string"
      ],
      "additionalProp2": [
        "string"
      ],
      "additionalProp3": [
        "string"
      ]
    },
    "columns": [
      "string"
    ],
    "isBaseDataset": true
  }
]
```

<a name="data"></a>To get data sets by workspace ID and data set ID, call the https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId}/datasets/{datasetId} endpoint. You must provide the `{workspaceId}` (string, $UUID) and the {datasetId}(string, $UUID).

Below you can see an example of a successful request (code 200).
```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "name": "string",
  "description": "string",
  "workspaceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "connectionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "createdBy": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "createdOn": "2022-08-10T14:37:47.568Z",
  "lastModifiedBy": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "lastModifiedOn": "2022-08-10T14:37:47.568Z",
  "schemaInfo": {
    "schemaVersionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "schemaName": "string"
  },
  "queries": {
    "additionalProp1": [
      "string"
    ],
    "additionalProp2": [
      "string"
    ],
    "additionalProp3": [
      "string"
    ]
  },
  "columns": [
    "string"
  ],
  "isBaseDataset": true
}
```

<a name="dataMore"></a>To query for data by workspace ID, data set ID, and some additional properties, call the https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId}/datasets/{datasetId}/query endpoint.
You must provide the `{workspaceId}` (string, $UUID) and the {datasetId}(string, $UUID). You can use additional properties in your query. 

Below you can see a sample request body.

```json
{
  "pageIndex": 0,
  "pageSize": 0,
  "columnFilter": [
    "string"
  ],
  "queryFilters": {
    "additionalProp1": [
      "string"
    ],
    "additionalProp2": [
      "string"
    ],
    "additionalProp3": [
      "string"
    ]
  }
}
```

Below you can see an example of a successful request (code 200).

```json
{
  "data": [
    {}
  ],
  "pagination": {
    "pageIndex": 0,
    "pageSize": 0,
    "totalPages": 0,
    "totalCount": 0
  }
}
```

## Response codes

You can get the following response codes when you send API calls:

* 200 code when the request was successful. Returns Query Data Found.
* 201 code when the resource was successfully created.
* 400 code for the invalid model. See schemas to find out the correct model to use in your API call.
* 401 code when you are unauthorized to access a resource.
* 404 code when the resource was not found.
* 500 code for an internal server error.
* 502 when you have called a bad gateway.
