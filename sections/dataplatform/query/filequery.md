---
author: Veracity
description: This is a tutorial how to call API endpoints of Data Workbench with sample Python code.
---

# Query files

## API endpoints
To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json).
See section Storages

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)

## File storage endpoints
You can access files via API if you generate a SAS token.

To generate a SAS token, call the `{baseurl}/workspaces/{workspaceId:guid}/storages/sas` endpoint with the POST method.

Below, you can see a sample request payload. In the response, you will get a SAS token as a string.


```json
{
"path": "string",
  "readOrWritePermission": "Read",
  "startsOn": "2024-05-14T09:04:12.297Z",
  "expiresOn": "2024-05-14T09:04:12.297Z",
  "storageName": "string"

}
```

Note that:
* `path` is optional. It is the path to the resource for which you're generating the SAS token. If you don't provide a path, the default path will be used. The default path is the ContainerName or SubFolder which was specified when creating the internal storage connection.
* `readOrWritePermission` can take the value `read` or `write` depending on the access type you want to give to the resource. A workspace admin can generate tokens giving both `read` and `write` access. If you have Reader access to a workspace, you can only give `read` access. Also, Service Accounts should generate only `read` tokens.
* `StartsOn` is optional. It is the start date when the SAS token becomes valid. If not provided, it takes the current UTC date time.
* `ExpiresOn` is when the SAS token stops being valid. It should be greated than `StartsOn` and can't be a past date.
* `StorageName` is optional. If used, it should be a valid name of a data set in File storage. If not provided, it takes the default internal storage data set.

To get all storage data sets of a workspace, call the following endpoint with a GET method.
`{baseurl}/workspaces/{workspaceId:guid}/storages/storagedatasets`

Below is a sample response.

```json
[
        {
            "id": "ddbf7526-abc3-45e2-bfd9-a2223a431a12",
            "name": "Storage Name",
            "description": "storage dataset",
            "workspaceId": "ddbf7526-abc3-45e2-bfd9-a2223a431a12",
            "connectionId": "ddbf7526-abc3-45e2-bfd9-a2223a431a12",
            "createdBy": "00009000-0000-0000-0000-000000000001",
            "createdOn": "2024-05-13T10:23:30.4419593Z",
            "lastModifiedBy": "00000000-0000-0000-0000-000000000000",
            "lastModifiedOn": "0001-01-01T00:00:00Z",
            "schemaInfo": 
            {
               "schemaVersionId": "b24c06ae-6a23-482e-90fc-2791c2819450",
               "schemaName": "File Metadata Schema V1"
            },
            "queries": [],
            "columns": [],
            "isBaseDataset": false,
            "tags": {}
        }
]

```

## Sample Python for calling the endpoints
You can use the sample Python code below to call Data Workbench endpoints.

```json
import requests

# Configuration
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
subscription_key = "YOUR_SUBSCRIPTION_KEY"
workspace_id = "YOUR_WORKSPACE_ID"
dataset_id = "YOUR_DATASET_ID"

# Query endpoint URL    
query_endpoint = f"https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspace_id}/storages/storagedatasets"

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

''' 
Response Schema:

{
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": {}
    },
    "pagination": {
      "type": "object",
      "properties": {
        "pageIndex": {
          "type": "integer",
          "format": "int32"
        },
        "pageSize": {
          "type": "integer",
          "format": "int32"
        },
        "totalPages": {
          "type": "integer",
          "format": "int32"
        },
        "totalCount": {
          "type": "integer",
          "format": "int32"
        }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
'''
```
