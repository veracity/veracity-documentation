---
author: Veracity
description: This page lists API endpoints for Data Workbench.
---
# API endpoints

You can use the following API endpoints for Data Workbench:
* [Workspace endpoints](#workspace)
* [Connector and connections endpoints](#connect)
* [Data sets endpoints](#data)

To see response codes for the API, go [here](#response).

## <a name="workspace"></a>Workspace endpoints

Each customer has one tenant in Data Workbench. A tenant can have multiple workspaces.

To get a list of workspace schemas for a specific workspace, call the https://dwdev.veracity.com/gateway/api/v1/workspaces/{workspaceId}/schemas endpoint. You must provide {workspaceId}(string, $UUID).

Below you can see an example of a successful request (code 200).
<pre><code>
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "workspaceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "string",
    "description": "string",
    "schemaVersions": [
      {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "schemaVersionName": "string",
        "description": "string",
        "columns": [
          {
            "name": "string",
            "displayName": "string",
            "type": "String",
            "description": "string",
            "isFilterable": true,
            "filterType": "List"
          }
        ],
        "schemaId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "workspaceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "createdBy": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "createdOn": "2022-08-10T14:51:11.785Z",
        "lastModifiedBy": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "lastModifiedOn": "2022-08-10T14:51:11.785Z",
        "isDefault": true,
        "avatarColor": 0
      }
    ],
    "industry": "string",
    "isPredefined": true,
    "avatarColor": 0,
    "createdBy": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "createdOn": "2022-08-10T14:51:11.785Z",
    "lastModifiedBy": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "lastModifiedOn": "2022-08-10T14:51:11.785Z"
  }
]
</pre></code>

## <a name="connect"></a>Connectors and connections

Each workspace contains data that is imported from source systems and validated by the [Data Validator API](https://api-portal.veracity.com/docs/services/DataValidatorApi/operations/ColumnValidator_AddColumnValidator).
To see the connections a workspace uses, go to the **Connections** tab in your workspace.

You can list all connections used by a workspace by calling the https://dwdev.veracity.com/gateway/api/v1/workspaces/{workspaceId}/connections endpoint. You must provide {workspaceId} (string, #UUID) in your call.

Below you can see an example of a successful request (code 200).
<pre><code>
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
</pre></code>

You can also list all the connectors used by a workspace by calling the https://dwdev.veracity.com/gateway/api/v1/workspaces/{workspaceId}/connectors endpoint. You must provide {workspaceId} (string, #UUID) in your call.

Below you can see an example of a successful request (code 200).
<pre><code>
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
</pre></code>

## <a name="data"></a>Data sets endpoints

You can use the following endpoints:
* [Get all data sets for a workspace](#allData)
* [Get specific data sets by ID](#data)
* [Query for data sets by ID and with additional properties](#dataMore)

<a name="allData"></a>To get all data sets available in a workspace, call the https://dwdev.veracity.com/gateway/api/v1/workspaces/{workspaceId}/datasets endpoint. You must provide {workspaceId} (string, $UUID).
You can use additional properties in your query:
* {isBaseDataset} – boolean; by default, no value; you can set it to "true" or "false"
* pageIndex – integer($int32)
* pageSize – integer($int32)
* sortColumn – string
* sortDirection – string; by default, no value; you can set it to "ascending" or "descending"

Below you can see an example of a request URL that uses all additional properties.
<pre><code>
https://dwdevtest.veracity.com/gateway/api/v1/workspaces/0c2208da-4f16-4af5-9255-d5c70384cda5/datasets?isBaseDataset=true&pageIndex=1&pageSize=1&sortColumn=1&sortDirection=Ascending
</pre></code>

Below you can see an example of a successful request (code 200).
<pre><code>
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
</pre></code>

<a name="data"></a>To get data sets by workspace ID and data set ID, call the https://dwdev.veracity.com/gateway/api/v1/workspaces/{workspaceId}/datasets/{datasetId} endpoint. You must provide the {workspaceId} (string, $UUID) and the {datasetId}(string, $UUID).

Below you can see an example of a successful request (code 200).
<pre><code>
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
</pre></code>

<a name="dataMore"></a>To query for data by workspace ID, data set ID, and some additional properties, call the https://dwdev.veracity.com/gateway/api/v1/workspaces/{workspaceId}/datasets/{datasetId}/query endpoint.
You must provide the {workspaceId} (string, $UUID) and the {datasetId}(string, $UUID). You can use additional properties in your query. 

Below you can see a sample request body.

<pre><code>{
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
</pre></code>

Below you can see an example of a successful request (code 200).

<pre><code>
{
  "data": [
    "string"
  ],
  "pagination": {
    "pageIndex": 0,
    "pageSize": 0,
    "totalPages": 0,
    "totalCount": 0
  }
}
</pre></code>

## <a name="response"></a>Response codes

You can get the following response codes when you send API calls:

* 200 code when the request was successful. Returns Query Data Found.
* 201 code when the resource was successfully created.
* 400 code for the invalid model. See schemas to find out the correct model to use in your API call.
* 401 code when you are unauthorized to access a resource.
* 404 code when the resource was not found.
* 500 code for an internal server error.
* 502 when you have called a bad gateway.