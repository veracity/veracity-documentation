---
author: Veracity
description: This is a tutorial how to call API endpoints of Data Workbench with sample Python code.
---

# Query datasets using API

## API endpoints
To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json).
See section Datasets

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)

## Query datasets

### Get all datasets

```
POST: {baseurl}/workspaces/{workspaceId}/datasets/query

Body in request:
{
  "isBaseDataset": true,
  "pageIndex": 0,
  "pageSize": 0,
  "sortColumn": "string",
  "sortDirection": "Ascending",
  "datasetName": "string",
  "tags": {},
  "createdAfter": "string",
  "createdBefore": "string",
  "schemaVersionIds": [
    "string"
  ]
}
```

Example
```
{ 
    "PageIndex": 1,
    "PageSize": 100,         
  "SortColumn": "CreatedOn",
  "SortDirection" : "Descending"     
}
```

### Get information about a dataset
```
GET: {baseurl}/workspaces/{workspaceId}/datasets/{datasetId}
```

Example response

``` json
{
    "id": "2bb34d81-75fd-4053-9d4c-c96e1cf94744",
    "name": "derektest",
    "description": "derektest created by Python execution",
    "workspaceId": "f60eee63-4bc3-45af-a8e2-8105733f5453",
    "connectionId": "9bf38e23-d95a-484a-99b2-61e461fc9b75",
    "createdBy": "e6270571-7f09-4b75-b599-3740236f6bc1",
    "createdOn": "2024-08-28T17:55:59.111436Z",
    "lastModifiedBy": "e6270571-7f09-4b75-b599-3740236f6bc1",
    "lastModifiedOn": "2024-08-28T17:55:59.1114368Z",
    "schemaInfo": {
        "schemaVersionId": "0f2b7174-e964-4f31-8187-91b796f2d064",
        "schemaName": "derektest Schema-2024-08-28 17:55:53"
    },
    "queries": [],
    "columns": [],
    "isBaseDataset": false,
    "tags": {
        "SiteId": [
            "44b17070-f7d5-423b-8ace-90c5e0d6813a"
        ]
    }
}
```

### Query data within a dataset

```
POST: {baseurl}/workspaces/{workspaceId}/datasets/{datasetId}/query
```
The request body contains the filters
```json
{
  "pageIndex": 0,
  "pageSize": 0,
  "queryFilters": [
    {
      "column": "string",
      "filterType": "List",
      "filterValues": [
        "string"
      ]
    }
  ],
  "columnFilter": [
    "string"
  ],
  "sorting": {
    "column": "string",
    "order": "Ascending"
  }
}```



Example
The following filter will filter on timestamp and data channel ids. In addition return datapoints in descending order.
```json
{
"pageIndex": 1,
"pageSize": 500,
"columnFilter": [
"Timestamp", "DataChannelId", "Value", "_ValueNumeric"
],
"queryFilters": [
    {
      "column": "Timestamp",
      "filterType": "Greater",
      "filterValues": [
        "2024-05-01"
      ]
    },
    {
      "column": "Timestamp",
      "filterType": "Less",
      "filterValues": [
        "2024-05-03"
      ]
    },
    {
      "column": "DataChannelId",
      "filterType": "Equals",
      "filterValues": [
        "HAYS_FC-RUN1-TT01",
        "Emerson_700XA-MOL_PCT_0"
      ]
    }
  ],
"sorting": {
       "column": "Timestamp",
       "order": "Descending"
   }
}
```

### How to get column names for your dataset
The GET dataset repsons provides schema id for the dataset

``` json
    "schemaInfo": {
        "schemaVersionId": "0f2b7174-e964-4f31-8187-91b796f2d064",
        "schemaName": "derektest Schema-2024-08-28 17:55:53"
    },
  
```


You can query the schema endpoint to list all columns in the schema and use these for filters in the dataset query

```json
GET {baseurl}workspaces/{workspaceid}/schemas/schemaversions/{schemaVersionId}
```

### To query share owners by data set ID list
You can query who shared the data sets with you so that you understand the data set context by using the POST method and calling the following endpoint.

`https://api.veracity.com/veracity/dw/gateway/api/v1/{workspaceId:guid}/shares/sharedBy/Query`

Below you can see a sample request payload.

```json
{
"datasetIds": [
    "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  ]
}
```

Below you can see a sample response.

```json
[ {
        "datasetId": "f80b0de1-3b1d-4a64-aa4d-88d6073ff1cd",    // ID of the data set
        "sharedBy": {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",   // ID of the shared user
            "sharedByType": "User",
            "name": "User Name"  // Name of the shared user
        }
    },
]
```

Note that:
* If the data sets were shared with a person, you must be this person or the person who initiated the share. 
* If the data sets were shared with a workspace, you must be a member of this workspace.



## Sample Python code for calling API endpoints
You can use the sample Python code below to call Data Workbench endpoints.
```json

# Configuration
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
subscription_key = "YOUR_SUBSCRIPTION_KEY"
workspace_id = "YOUR_WORKSPACE_ID"
dataset_id = "YOUR_DATASET_ID"

# Query endpoint URL    
query_endpoint = "{baseurl}/workspaces/{workspace_id}/datasets/{dataset_id}/query"

# Token URL for authentication 
token_url = "https://login.microsoftonline.com/dnvglb2cprod.onmicrosoft.com/oauth2/token"

# Token payload for authentication request
token_payload = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    "resource": "https://dnvglb2cprod.onmicrosoft.com/83054ebf-1d7b-43f5-82ad-b2bde84d7b75"
}

# Function to retrieve access token
def get_token():
    try:
        response = requests.post(token_url, data = token_payload)
        return response.json()["access_token"]
    except Exception as e:
        print(f"Failed to retrieve access token: {e}")

# Headers for the API request    
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Authorization': f"Bearer {get_token()}"
}

# Payload for the query request
query_payload = {
  # Request body
  # Add properties as needed
  # See documentation 
}

# Function to call the query endpoint and return the response as a dictionary object
def call_query_endpoint(url):
    try:
        response = requests.post(url = url, headers = headers, json = query_payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
    except Exception as e:
        print(f"error occured: {e}")

# Call the query endpoint and retrieve the result
query_res_dict = call_query_endpoint(query_endpoint)
print(query_res_dict)

```


