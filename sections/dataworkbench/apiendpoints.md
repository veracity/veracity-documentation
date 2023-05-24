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

## Workspace ID

To find your workspace ID, see the URL of your workspace in a browser. The part after ```ws/```is the ID of your workspace.

Note that 'workspaceId' is a string in UUID format.

<figure>
	<img src="assets/workspaceid.png"/>
	<figcaption>The image shows where to find the ID of your workspace.</figcaption>
</figure>

## Workspace endpoints

Each customer has one tenant in Data Workbench. A tenant can have multiple workspaces.

To get a list of workspace schemas for a specific workspace, call the https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId}/schemas endpoint. 

In the request, you must provide:
* [Authorization and authentication](authentication.md)
* [{workspaceId}](https://developer.veracity.com/docs/section/dataworkbench/apiendpoints#workspace-id)

To get the schema, add to the request `includeDefaultSchemaVersion=true`.

Below you can see an example of a successful response (code 200).

```json
 {

    "result": [

        {

            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",

            "name": "string",

            "description": "string",

            "workspaceId": "3fa85f64-5717-4562-b3fc-2c963f66afa68",

            "connectionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",

            "createdBy": "3fa85f64-5717-4562-b3fc-2c963f66afa6",

            "createdOn": "2022-05-04T07:37:19.2074539Z",

            "lastModifiedBy": "3fa85f64-5717-4562-b3fc-2c963f66afa6",

            "lastModifiedOn": "2022-05-04T07:37:19.2074539Z",

            "schemaInfo": {

                "schemaVersionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",

                "schemaName": "string"

            },

            "queries": [],

            "columns": [],

            "isBaseDataset": true

        }

    ],

    "pageIndex": 1,

    "pageSize": 100,

    "totalCount": 100,

    "totalPages": 1

}
```

To query activity logs for a workspace, call the endpoint https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId}/ledger providing the ID of the workspace.

In the request, you must provide:
* [Authorization and authentication](authentication.md)
* [{workspaceId}](https://developer.veracity.com/docs/section/dataworkbench/apiendpoints#workspace-id)

You can add to the request a page size and page index, for example `PageSize=1&PageIndex=5`.

Below you can see an example of a successful response (code 200).

```json
{

    "result": [

        {

            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",

            "workspaceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",

            "userId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",

            "userName": "string",

            "resource": {

                "3fa85f64-5717-4562-b3fc-2c963f66afa6": "string"

            },

            "payload": {

                "additionalProp1": "3fa85f64-5717-4562-b3fc-2c963f66afa6",

                "additionalProp2": "3fa85f64-5717-4562-b3fc-2c963f66afa6",

                "eventType": "string"

            },

            "eventName": "string",

            "timestamp": "2023-05-24T08:45:08.1759463Z"

        }

    ],

    "pageIndex": 1,

    "pageSize": 1,

    "totalCount": 100,

    "totalPages": 100

}
```

## Connectors and connections
To see the connections a workspace uses, go to the **Connections** tab in your workspace.

You can list all connections used by a workspace by calling the https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId}/connections endpoint. 

In the request, you must provide:
* [Authorization and authentication](authentication.md)
* [{workspaceId}](https://developer.veracity.com/docs/section/dataworkbench/apiendpoints#workspace-id)

Below you can see an example of a successful response (code 200).
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

You can list all the connectors used by a workspace by calling the https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId}/connectors endpoint. 

In the request, you must provide:
* [Authorization and authentication](authentication.md)
* [{workspaceId}](https://developer.veracity.com/docs/section/dataworkbench/apiendpoints#workspace-id)

Below you can see an example of a successful response (code 200).
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

<a name="datasetid"></a> Data set ID is a string in UUID format. 

To check the 'datasetId' for a data set:
1. In Data Workbench, go to **Data catalogue**.
2. Open a data set.
3. Copy the part of the URL after 'datasets'.

<figure>
	<img src="assets/datasetid.png"/>
	<figcaption>The ID of a data set .</figcaption>
</figure>

For example, for the URL https://dw.veracity.com/ws/6fa70833-de9a-4fca-8754-ed57cbfbded7/dataCatalogue/datasets/3b516e0c-6fa7-44c7-aa6c-7aef5aee4c73, the data set ID is 3b516e0c-6fa7-44c7-aa6c-7aef5aee4c73.

You can use the following endpoints:
* [Get all data sets for a workspace](#allData)
* [Get specific data sets by ID](#data)
* [Query for data sets by ID and with additional properties](#dataMore)
* [Query for activity logs for a data set](#ledger)

<a name="allData"></a>To get all available data sets, call the https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/datasets endpoint. 

In the request, you must provide:
* [Authorization and authentication](authentication.md)
* [{workspaceId}](https://developer.veracity.com/docs/section/dataworkbench/apiendpoints#workspace-id)

You can add the following to the request:
* Get only base data sets with `isBaseDataset=true`.
* Set page size and index, for example `PageSize=1&PageIndex=5`.
* Sort columns with `sortColumn`.
* Sort direction with `sortDirection=ascending` or `sortDirection=descending`.

Below you can see an example of a successful response (code 200).
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

<a name="data"></a>To get a specific data set by its ID, call the https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/datasets/{datasetId} endpoint. 

In the request, you must provide:
* [Authorization and authentication](authentication.md)
* [{workspaceId}](https://developer.veracity.com/docs/section/dataworkbench/apiendpoints#workspace-id)
* [{datasetId}](#datasetid)

Below you can see an example of a successful response (code 200).
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
"queries": [
       {
           "column": "string",
           "filterType": "string",
           "filterValues": [
               "string"
           ]
       }
],
"columns": [
"string"
],
"isBaseDataset": true
}
```

<a name="dataMore"></a>To query for data by workspace ID, call the https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/datasets/{datasetId}/query endpoint. 

In the request, you must provide:
* [Authorization and authentication](authentication.md)
* [{workspaceId}](https://developer.veracity.com/docs/section/dataworkbench/apiendpoints#workspace-id)
* [{datasetId}](#datasetid)

Below you can see an example of a successful response (code 200).

```json
{

    "result": [

        {

            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",

            "name": "string",

            "description": "string",

            "workspaceId": "3fa85f64-5717-4562-b3fc-2c963f66afa68",

            "connectionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",

            "createdBy": "3fa85f64-5717-4562-b3fc-2c963f66afa6",

            "createdOn": "2022-05-04T07:37:19.2074539Z",

            "lastModifiedBy": "3fa85f64-5717-4562-b3fc-2c963f66afa6",

            "lastModifiedOn": "2022-05-04T07:37:19.2074539Z",

            "schemaInfo": {

                "schemaVersionId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",

                "schemaName": "string"

            },

            "queries": [],

            "columns": [],

            "isBaseDataset": true

        }

    ],

    "pageIndex": 1,

    "pageSize": 100,

    "totalCount": 100,

    "totalPages": 1

}
```

<a name="ledger"></a>To query activity logs (ledgers) for a dataset, call the https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId}/datasets/{datasetId}/ledger[?PageSize][&PageIndex] endpoint providing the ID of the workspace and the dataset.

In the request, you must provide:
* [Authorization and authentication](authentication.md)
* [{workspaceId}](https://developer.veracity.com/docs/section/dataworkbench/apiendpoints#workspace-id)
* [{datasetId}](#datasetid)

You can add the following to the request:
* Page size and index, for example, `PageSize=1&PageIndex=5`.

## Response codes

You can get the following response codes when you send API calls:

* 200 code when the request was successful. Returns Query Data Found.
* 201 code when the resource was successfully created.
* 400 code for the invalid model. See schemas to find out the correct model to use in your API call.
* 401 code when you are unauthorized to access a resource.
* 404 code when the resource was not found.
* 500 code for an internal server error.
* 502 when you have called a bad gateway.
