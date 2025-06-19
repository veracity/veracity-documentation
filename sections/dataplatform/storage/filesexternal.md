---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# File storage
This feature lets you upload files of any type into your Azure Data Lake. Files are stored as unstructured data in Veracity File storage and cannot be queried using SQL-like operations. Subscriptions to Veracity File Storage is required.

## External storage
External storage is a data storage account from your company that was added to your Data Lake File storage (ie.e Mounting of datalakes). If you want to add a new external storage account, contact Veracity support and provide connection strings to this account.

## API endpoints

Note: The Ingest api-endpoints are different for uploading files to filestorage vs uploading datasets **See section Storage**

To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json).


### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).
**When authenticating using service account, the service account needs WRITE permissions. When creating a service account, its role is by default READER. To give it Write access, send request to [Veracity support](https://support.veracity.com/?r=1) requesting Admin role to <service account id> in <workspace id>**

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)
See section **Data Workbench API**

## Ingest process

Using the apis these are the three steps to follow:
1. Authenticate towards Veracity api using client credentials
2. Get SAS token uri from Veracity api  (differnet endpoint than for getting SAS Uri for datasets)
3. Read CSV file from your location and upload file to storage using received SAS token uri

See code examples below for each step in the process.

### Python code example
#### Step 1: Get Veracity token for service principle/service account
```json
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

#### Step 2: Get SAS URI for Datasets (not for filestorage)
Using veracityToken  from step 1

```json
import requests
import json
from datetime import datetime, timedelta
 
mySubcriptionKey =   <myServiceAccountApiKey>
workspaceId = <workspaceId in DWB>
#folder name only i.e "Test", folder must exist
dwbFolderName = <name of folder in DWB Filestorage>
 
def get_sas_token(veracity_token, folder, workspace_id, subscription_key):
    base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
    endpoint = f"/workspaces/{workspace_id}/ingest"
    url = base_url + endpoint
    expires_on = (datetime.utcnow() + timedelta(hours=5)).isoformat() + "Z"
 
    payload = {
      "path": dwbFolderName,
      "readOrWritePermission": "Write",
      "expiresOn": expires_on
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

sas_token = get_sas_token(veracity_token= veracityToken,  folder=dwbFolderName, workspace_id=workspaceId,subscription_key= mySubcriptionKey)
```

### Step 3: Upload file using SAS URI from Step 2

```json
from azure.storage.filedatalake import DataLakeFileClient
from urllib.parse import urlparse
import os
from urllib.parse import urlparse

localFilePath = <path to file>
target_file_name = os.path.basename(localFilePath)  

# sas uri from step 2
sas_folder_url = sas_token

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


### C# Code example


```csharp
using Azure.Storage.Files.DataLake;
using Azure.Storage.Files.DataLake.Models;
using Newtonsoft.Json.Linq;
using System.Net.Http.Headers;

//read secrets and parameters
string filename = <filepath to upload>;
string workspaceId = <DWB workspace id>;
string appKey = <my service account api key>;
var client_id = <my service account ID>;
var client_secret = <my service account secret>;

```

#### Step 1: Get Veracity token for authentication
Client Id, secret and subscription key for your workspace are defined under tab API Integration in data Workbench Portal.
If you want to use user authentication, [see further details in Veracity Identity Documentation](https://developer.veracity.com/docs/section/identity/identity).

**Note: In order to use client credentials, this service principle needs Admin access to workspace. This will be available as self service shortly.** But, for now contact support@veracity.com  and request Admin role on service principle "servicePrincipeID" in workspace "workspaceID"**


```csharp
async Task<string> GetToken(string clientId, string clientSecret)
{
    var url = "https://login.microsoftonline.com/dnvglb2cprod.onmicrosoft.com/oauth2/token";
    var grant_type = "client_credentials";
    var resource = "https://dnvglb2cprod.onmicrosoft.com/83054ebf-1d7b-43f5-82ad-b2bde84d7b75";

    var postData = new Dictionary<string, string>
       {
           {"grant_type", grant_type},
           {"client_id", clientId},
           {"client_secret", clientSecret},
           {"resource", resource},
       };
    using HttpClient httpClient = new HttpClient();
    httpClient.BaseAddress = new Uri(url);
    HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Post, httpClient.BaseAddress);
    request.Content = new FormUrlEncodedContent(postData);
    HttpResponseMessage authResponse = httpClient.PostAsync(url, new FormUrlEncodedContent(postData)).Result;
    var result = await authResponse.Content.ReadAsStringAsync();
    var token = (string)JToken.Parse(result)["access_token"];
    return token;
}

```

#### Step 2: Get a SAS token for internal storage
You need a SAS token with write access to the folder (path) where file should be uploaded. To generate a SAS token, call the `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/storages/sas` endpoint with the POST method using the Veracity token from step 1.


```csharp
 async Task<string> GetSASToken(string veracityToken, string folder, string workspaceId, string appKey)
 {
     string url = $"https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/storages/sas";

     DateTime expiresOn = DateTime.UtcNow.AddDays(1);
     //path is folder name in storage container
     SasRequest request = new SasRequest()
     {
         Path = folder,
         ReadOrWritePermission = "Write",
         ExpiresOn = expiresOn
     };

     string jsonBody = JsonConvert.SerializeObject(request );    
     HttpContent content = new StringContent(jsonBody, Encoding.UTF8, "application/json");
     
    if (_httpClient == null)
         _httpClient = new HttpClient();

     _httpClient.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", appKey);
     _httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", veracityToken);
     try
     {
         var result = await _httpClient.PostAsync(url, content);
         if (result.IsSuccessStatusCode)
         {
             string sasKey = result.Content.ReadAsStringAsync().Result;
             return sasKey.Trim('"');
         }
     }
     catch (Exception ex)
     {

     }
     return null;
 }


internal class SasRequest    {

    [JsonProperty("path")]
    public string Path {get;set;}

    [JsonProperty("readOrWritePermission")] 
    public string ReadOrWritePermission { get; set; }
    
    [JsonProperty("expiresOn")]
    public DateTime ExpiresOn { get; set; }
}

```


Below, you can see a sample request payload.

```json
{
"path": "string",
  "readOrWritePermission": "Write",
  "startsOn": "2024-05-14T09:04:12.297Z",
  "expiresOn": "2024-05-14T09:04:12.297Z",
  "storageName": "string"

}
```
The result contains the SAS token as a string.

Note that:
* `path` is optional. It is the path to the resource for which you're generating the SAS token. If you don't provide a path, the default path will be used. The default path is the `ContainerName` which was specified when creating the internal storage connection.
* `readOrWritePermission` can take the value `read` or `write` depending on the access type you want to give to the resource. A workspace admin can generate tokens giving both `read` and `write` access. If you have reader access to a workspace, you can only give `read` access. Also, Service Accounts should generate only `read` tokens.
* `StartsOn` is optional. It is the start date when the SAS token becomes valid. If not provided, it takes the current UTC date time.
* `ExpiresOn` is when the SAS token stops being valid. It should be greated than `StartsOn` and can't be a past date.
* `StorageName` is optional. If used, it should be a valid name of a data set in File storage. If not provided, it takes the default internal storage data set.


#### Step 3: Upload file using SAS URI 
In this example we utilize Microsoft library to access the filestorage by using the aquired SAS-token from step 2.

```csharp
 async Task UploadFile(string sasToken, string filepath)
 {
     var sasUri = new System.Uri(sasToken);
     var containerClient = new DataLakeDirectoryClient(sasUri);
     
     string remoteFileName = Path.GetFileName(filepath);
     var fileClient = containerClient.GetFileClient(remoteFileName);
     
     using (FileStream fsSource = new FileStream(filepath, FileMode.Open, FileAccess.Read))
     {
         bool overwrite = true;
         var response = await fileClient.UploadAsync(fsSource, overwrite, CancellationToken.None);

         //example upload metadata to file - OPTIONAL
          Dictionary<string, string> metadata = new Dictionary<string, string>();
          metadata.Add("Asset", "123");
          metadata.Add("Project", "5454");
          var respone = await fileClient.SetMetadataAsync(metadata);           

     };

 }
``` 

## Ingest metadata to file or folder 
Use DataLakeFileClient to set metadata during upload or later.

```csharp
  Dictionary<string, string> metadata = new Dictionary<string, string>();
  metadata.Add("Asset", "123");
  metadata.Add("Project", "5454");
  var respone = await fileClient.SetMetadataAsync(metadata); 
``` 


## Get a SAS token for external storage
To generate a SAS token, call the `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/storages/external/sas` endpoint with the POST method.

Below, you can see the sample request payload


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

The result contains the SAS token as a string.

Note that:
* `containerName` is the name of the container for which the SAS policy needs to be granted.
* `connectionString` is the connection string of the external storage account.
* `path` is optional. It is the path to the resource for which you're generating the SAS token. If you don't provide a path, the default path will be used. The default path is the `ContainerName` which was specified when creating the external storage connection.
* `readOrWritePermission` can take the value `read` or `write` depending on the access type you want to give to the resource. A workspace admin can generate tokens giving both `read` and `write` access. If you have reader access to a workspace, you can only give `read` access. Also, Service Accounts should generate only `read` tokens.
* `StartsOn` is optional. It is the start date when the SAS token becomes valid. If not provided, it takes the current UTC date time.
* `ExpiresOn` is when the SAS token stops being valid. It should be greated than `StartsOn` and can't be a past date.
* `StorageName` is optional. If used, it should be a valid name of a data set in File storage. If not provided, it takes the default external storage data set.

## SAS Policies
### List SAS policies for internal storage
To list all SAS policies for internal storage, call the `https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId:guid}/storages/policies` endpoint with the GET method.

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

## Revoke a SAS policy

### Revoke a SAS policy for internal storage
To revoke a SAS token for internal storage, you don't revoke the token directly. Instead, you revoke the policy that the token is attached to.  Revoking the policy revokes all SAS tokens associated with that policy.

To revoke a SAS policy, call the following endpoint with the DELETE method:
`https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId:guid}/storages/sas/revoke`

Note that:
* You must be a workspace admin to revoke SAS policies.
* This endpoint accepts an optional query parameter called `policyToRevoke`.

Regarding `policyToRevoke` parameter, here are some important considerations:
* **If you don't provide the** `policyToRevoke` **parameter**: You'll revoke all SAS policies for the entire storage container (workspace). This means all active SAS tokens for that container will be revoked, regardless of which policy they were associated with.
* **If you do provide the** `policyToRevoke` **parameter**: You'll revoke only the specified policy. This means only the active SAS tokens associated with that specific policy will be revoked. Other tokens tied to different policies will remain active.

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