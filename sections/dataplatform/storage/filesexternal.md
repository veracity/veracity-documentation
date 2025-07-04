---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---
# External Filestorage
External storage is a data storage account from your company that was added to your Data Lake File storage (ie.e Mounting of datalakes). If you want to add a new external storage account, contact Veracity support and provide connection strings to this account.

## API endpoints

Note: The Ingest api-endpoints are different for uploading files to filestorage vs uploading datasets **See section Storage and endpoints with "external" in path**. To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json).
For code exampple, see step 1 below.

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).
**When authenticating using service account, the service account needs WRITE permissions. When creating a service account, its role is by default READER. To give it Write access, send request to [Veracity support](https://support.veracity.com/?r=1) requesting Admin role to service_account_id> in workspace_id

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints). See section **Data Workbench API**

## Ingest process

Using the apis these are the three steps to follow:
1. Authenticate towards Veracity api using client credentials
2. Get SAS token uri from Veracity api  (different endpoint than for getting SAS Uri for Veracity filestorage)
3. Read CSV file from your location and upload file to storage using received SAS token uri

See code examples below for each step in the process.

## Python code example
### Step 1: Get Veracity token for service principle/service account
```python
import requests
import json

# Token URL for authentication 
token_url = "https://login.microsoftonline.com/dnvglb2cprod.onmicrosoft.com/oauth2/token"
clientId =  <myServiceAccountId>
secret =   <myServiceAccountSecret>

# define the request payload    
payload = {"resource": "https://dnvglb2cprod.onmicrosoft.com/83054ebf-1d7b-43f5-82ad-b2bde84d7b75",
          "grant_type": "client_credentials",
          "client_id": clientId,
          "client_secret" :secret
          }
response = requests.post(token_url, data=payload)   
if response.status_code == 200:
        veracityToken = response.json().get("access_token")
else:
        print(f"Error: {response.status_code}")

```

### Step 2: Get SAS URI for External Filestorage
Using veracityToken  from step 1
**Ensure service account has Write access (ie. has Admin role in workspace )**

```python

import requests
import json
from datetime import datetime, timedelta
 
myApiKey =  <service account api key>
workspaceId =<workspace id>

#folder name, i.e "Test", folder must exist. If not provided you get access to storage container level (root level)
dwbFolderName = <name of folder in File Storage>
 

def get_sas_token(veracity_token, folder, workspace_id, subscription_key):
    base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
    endpoint = f"/workspaces/{workspace_id}/storages/external/sas"
    url = base_url + endpoint
    expires_on = (datetime.utcnow() + timedelta(hours=5)).isoformat() + "Z"
 
    payload = {
        "settings": {
           "containerName": "string",
           "connectionString": "string"
        },
      "filters": {
        "path": dwbFolderName,
        "readOrWritePermission": "Write",
        "expiresOn": expires_on
       }
    }

    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": mySubcriptionKey,
        "Authorization": f"Bearer {veracityToken}",
        "User-Agent": "python-requests/2.31.0"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching SAS token: {e}")
        return None


sas_uri = get_sas_token(veracity_token= veracityToken,  folder=dwbFolderName, workspace_id=workspaceId,subscription_key= mySubcriptionKey)
print("SAS Token:", sas_uri)
```
The result contains the SAS token as a string. Below, you can see the sample request payload

```json
{
            "settings": {
              "containerName": "string",
              "connectionString": "string"
            },
            "filters": {
               "path": "18a4a7ab-022c-4964-9d1b-6cc77e252a67/test.csv",
               "readOrWritePermission": "Read",
               "startsOn": "2024-05-14T09:04:12.297Z",
               "expiresOn": "2024-05-14T09:04:12.297Z",
               "storageName": "StorageDataset"
            }
}
```
Note that:
* `containerName` is the name of the container for which the SAS policy needs to be granted.
* `connectionString` is the connection string of the external storage account.
* `path` is optional. It is the path to the resource for which you're generating the SAS token. If you don't provide a path, the default path will be used. The default path is the `ContainerName` which was specified when creating the external storage connection.
* `readOrWritePermission` can take the value `read` or `write` depending on the access type you want to give to the resource. A workspace admin can generate tokens giving both `read` and `write` access. If you have reader access to a workspace, you can only give `read` access. Also, Service Accounts should generate only `read` tokens.
* `StartsOn` is optional. It is the start date when the SAS token becomes valid. If not provided, it takes the current UTC date time.
* `ExpiresOn` is when the SAS token stops being valid. It should be greated than `StartsOn` and can't be a past date.
* `StorageName` is optional. If used, it should be a valid name of a data set in File storage. If not provided, it takes the default external storage data set.

If path is set to "" (empty string), path points default to root level of storage container.

### Step 3: Upload file using SAS URI 
File is uploaded using Microsoft libraries using SAS uri in step 2

```python
from azure.storage.filedatalake import DataLakeFileClient
from urllib.parse import urlparse
import os
from urllib.parse import urlparse

localFilePath = <path to file>
target_file_name = os.path.basename(localFilePath)  

# sas uri from step 2
sas_folder_url = sas_uri

# === PARSE SAS URL ===
parsed_url = urlparse(sas_folder_url)
account_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
file_system_name = parsed_url.path.strip("/").split("/")[0]
folder_path = "/".join(parsed_url.path.strip("/").split("/")[1:])
sas_token = parsed_url.query

# === COMBINE FOLDER + FILE NAME ===
file_path = f"{folder_path}/{target_file_name}"

# === CREATE FILE CLIENT ===
file_client = DataLakeFileClient(
    account_url=account_url,
    file_system_name=file_system_name,
    file_path=file_path,
    credential=sas_token
)

# === CREATE FILE AND UPLOAD ===
file_client.create_file()

with open(localFilePath, "rb") as file_data:
    file_client.upload_data(file_data, overwrite=True)
```
When returning 200, file upload was successful.


## SAS policy for external storage

### List SAS policies for external storage
To list all SAS policies for external storage, call the `https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId:guid}/storages/external/policies` endpoint with the POST method.
Below, you can see a sample request payload.

```json
{
          "containerName": "string",
          "connectionString": "string"                 
}
```

Note that:
* `containerName` is the name of the container for which the SAS policy needs to be granted.
* `connectionString` is the connection string of the external storage account.


### Revoke a SAS policy for external storage
To revoke a SAS token for external storage, you don't revoke the token directly. Instead, you revoke the policy that the token is attached to. Revoking the policy revokes all SAS tokens associated with that policy.

To revoke a SAS policy, call the following endpoint with the DELETE method:
`https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId:guid}/storages/sas/external/revoke`

Note that:
* You must be a workspace admin to revoke SAS policies.
* This endpoint requires a payload with the following fields:
```json
{
    "settings": {
        "containerName": "string",
        "connectionString": "string"
    },
    "policyName": "rl-policy"
}
```

Regarding the payload fields, here are some important considerations:
* `containerName`: This is the name of the container where the SAS policy you want to revoke is applied. It is required.
* `connectionString`: This is the connection string for the external storage account. It is required.
* `policyName`: This is the name of the specific policy you want to revoke. It is required. Unlike revoking internal storage policies, you must specify the `policyName` for external storage. There's no option to revoke all policies for a container in a single call.