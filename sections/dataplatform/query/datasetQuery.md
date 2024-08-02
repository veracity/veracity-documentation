---
author: Veracity
description: This is a tutorial how to call API endpoints of Data Workbench with sample Python code.
---
# Query datasets using API
This page gives you sample Python code for calling API endpoints, links to our Data Integrations and SDK GitHub repository, and recaps relevant information.

## Data Integrations and SDK
Data Workbench uses data integrations as an integration layer allowing integrating with data providers. You might want to see [detailed explanation including SDK.](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2Fveracity%2FData-Workbench-Connector%2Fmain%2FConnector%2520SDK.docx&wdOrigin=BROWSELINK)

If you want to see or use the SDK API demo, [go to this repository](https://github.com/veracity/Data-Workbench-Connector/tree/main).

## Prerequisites
If you want to use the sample code provided below, you will need to check for the following information.

### API endpoints
For a list of API endpoints, go [here](../apiendpoints.md).

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../authentication.md).

### Workspace ID and dataset ID
To find your workspace ID, see the URL of your workspace in a browser or use api XXX


## Sample Python code for calling API endpoints
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
query_endpoint = f"https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspace_id}/datasets/{dataset_id}/query"

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