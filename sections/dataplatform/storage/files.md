---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Upload files to Filestorage
This feature lets you upload files of any type into your Azure Data Lake. Files are stored as unstructured data in Veracity File storage and cannot be queried using SQL-like operations. Subscriptions to Veracity File Storage is required.

### Internal and external storage
* Internal storage is a data storage account that comes together with your Veracity Data Lake File Storage.
* External storage is a data storage account from your company that was added to your Data Lake File storage (ie.e Mounting of datalakes). If you want to add a new external storage account, contact Veracity support and provide connection strings to this account. For [details regarding apis](filesexternal.md)

## API endpoints
Note: The Ingest api-endpoints are different for uploading files to filestorage vs uploading datasets **See api section File Storages**.  To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json).

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints). See section **Data Workbench API**

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).
**When authenticating using service account, the service account needs WRITE permissions. When creating a service account, its role is by default READER. To give it Write access, send request to [Veracity support](https://support.veracity.com/?r=1) requesting Admin role to service_account_id in workspace_ id**

## Ingest process to Filestorage
Using the apis these are the three steps to follow:
* Step 1: Authenticate towards Veracity api using client credentials
* Step 2: Get SAS token uri from Veracity api  (Note: different endpoint than for getting SAS Uri for datasets)
* Step 3: Upload file from localpath to storage using received SAS token uri
* Step 4: Update metadata

## Step 1: Authenticate
### Get Veracity token for service principle/service account
**To write data, the user/service account needs WRITE permissions (admin role). When creating a service account, its role is by default READER. To give it Write access, send request to [Veracity support](https://support.veracity.com/?r=1) requesting Admin role to "service account id" in "workspace id"**

#### Python
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
#### C#
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
    HttpResponseMessage authResponse = httpClient.PostAsync(url, new FormUrlEncodedContent(postData)).Result;
    var result = await authResponse.Content.ReadAsStringAsync();
    var token = (string)JToken.Parse(result)["access_token"];
    return token;
``` 

## Step 2: Get SAS URI for Filestorage
Using the Veracity token from step 1, ensure user/service account has Write access.

**Input payload**
Payload options:
* `path` is optional. It is the path to the resource for which you're generating the SAS token. If you don't provide a path, the default path will be used. The default path is the `ContainerName` (i.e. root level)
* `readOrWritePermission` : Set write to be able to Write. **Ensure service account has Write access (ie. has Admin role in workspace )**
* `StartsOn` is optional. It is the start date when the SAS token becomes valid. If not provided, it takes the current UTC date time.
* `ExpiresOn` is when the SAS token stops being valid. It should be greated than `StartsOn` and can't be a past date.
* `StorageName` is optional. If used, it should be a valid name of a data set in File storage. If not provided, it takes the default internal storage data set.

**Output**
Either full sas uri path or split into objects (resourceUri and sasToken) depending on wether '?format=object' is used in query string.

#### Python
```python
import requests
import json
from datetime import datetime, timedelta
 
mySubcriptionKey = dbutils.secrets.get(scope="secrets", key="bkal_subKey")
workspaceId = "<workspace id>"
#if path not provided, root is used
dwbFolderName = "<folder name>"
 
def get_sas_token(veracity_token, folder, workspace_id, subscription_key):
    base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
    endpoint = f"/workspaces/{workspace_id}/storages/sas?format=object"
    url = base_url + endpoint
    expires_on = (datetime.utcnow() + timedelta(hours=2)).isoformat() + "Z"
 
    payload = {
      "path": folder,
      "readOrWritePermission": "Write",
      "expiresOn": expires_on
    }

    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Authorization": f"Bearer {veracity_token}",
        "User-Agent": "python-requests/2.31.0"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching SAS token: {e}")
        return None

sas_uri_object = get_sas_token(veracity_token= veracityToken,  folder=dwbFolderName, workspace_id=workspaceId,subscription_key= mySubcriptionKey)
sasToken = sas_uri_object.get("sasToken")
resourceUri = sas_uri_object.get("resourceUri")
```

#### C#
```csharp
using Azure.Storage.Files.DataLake;
using System.Net.Http.Headers;
using System.Text;
using Newtonsoft.Json;

public async Task<string> GetSASUri(string veracityToken, string folder, string workspaceId, string subscriptionKey)
{
    string url = $"https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/storages/sas";
    // use ?format=object if you want an object to be returned with parsed SAS URI

    DateTime expiresOn = DateTime.UtcNow.AddHours(1);
    string expiresOnStr = expiresOn.ToString("O");

    //path is folder name in storage container
    var postData = new Dictionary<string, string>
    {
        {"path", folder},
        {"readOrWritePermission", "Write"},
        {"expiresOn", expiresOnStr }
    };

    string jsonString = JsonConvert.SerializeObject(postData);
    HttpContent content = new StringContent(jsonString, Encoding.UTF8, "application/json");

    if (_httpClient == null)
        _httpClient = new HttpClient();

    _httpClient.BaseAddress = new Uri(url);

    _httpClient.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", subscriptionKey);
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
``` 

## Step 3: Upload file 
### Upload file using SAS URI from Step 2
File is uploaded using Microsoft libraries 

#### Python
```python
from azure.storage.filedatalake import DataLakeFileClient
from urllib.parse import urlparse
import os
from urllib.parse import urlparse

localFilePath = "/Workspace/Shared/Demo/TestData/weatherdata.csv"
#target file name does not need to be same as source path
targetFileName = "MyTestData.csv"

#sas token from step 2
sas_token = sasToken

# === PARSE resource uri from step 2 ===
parsed_url = urlparse(resourceUri)
# get account combining schema (https) and netlock
account_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
file_system_name = parsed_url.path.strip("/").split("/")[0]
folder_path = "/".join(parsed_url.path.strip("/").split("/")[1:])

# === COMBINE FOLDER + FILE NAME ===
file_path = f"{folder_path}/{targetFileName}"

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
    result = file_client.upload_data(file_data, overwrite=True)

# If an etag is returned after an upload, it means the file was successfully written to Azure Data Lake.
etag = result.get("etag")
if result.get("etag") and result.get("last_modified"):
    print(f"✅ Upload successful with etag {etag}.")
else:
    print(f"⚠️ Upload failed")
```

#### C#

```csharp
public async Task<string> UploadFileToFileStorage(string sasToken, string filepath, Dictionary<string, string> metadata)
{
    var sasUri = new System.Uri(sasToken);
    var containerClient = new DataLakeDirectoryClient(sasUri);

    string remoteFileName = Path.GetFileName(filepath);
    var fileClient = containerClient.GetFileClient(remoteFileName);

    string repsonse_status = "Unknown";
    using (FileStream fsSource = new FileStream(filepath, FileMode.Open, FileAccess.Read))
    {
        bool overwrite = true;
        var response = await fileClient.UploadAsync(fsSource, overwrite, CancellationToken.None);
        repsonse_status = response.GetRawResponse().Status.ToString();
    }
    //metadata is optional
    if (metadata != null && metadata.Count > 0)
        await fileClient.SetMetadataAsync(metadata);

    return repsonse_status;
}
```
## Step 4: Update metadata
### Ingest metadata to existing file or folder 

Use sas-token uri from Step 2 and use DataLakeFileClient to update metadata
#### Python

```python
from azure.storage.filedatalake import DataLakeFileClient
from urllib.parse import urlparse
import os
from urllib.parse import urlparse

#If URI points to folder
targetFileName = "MyTestData2.csv"

#sas token and resource uri from step 2
sas_token = sasToken
resource_uri = resourceUri

# === PARSE resource uri from step 2 ===
parsed_url = urlparse(resource_uri)
# get account combining schema (https) and netlock
account_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
file_system_name = parsed_url.path.strip("/").split("/")[0]
folder_path = "/".join(parsed_url.path.strip("/").split("/")[1:])

# === COMBINE FOLDER + FILE NAME ===
file_path = f"{folder_path}/{targetFileName}"

# === CREATE FILE CLIENT ===
file_client = DataLakeFileClient(
    account_url=account_url,
    file_system_name=file_system_name,
    file_path=file_path,
    credential=sas_token
)

#Example of metadata - is optional
metadata = {
    "Customer": "123",
    "Site": "ABC"    
}
result = file_client.set_metadata(metadata)
# If an etag is returned after an upload, it means the file was successfully written to Azure Data Lake.
etag = result.get("etag")
if result.get("etag") and result.get("last_modified"):
    print(f"✅ Upload metadata successful with etag {etag}.")
else:
    print(f"⚠️ Upload metadata failed")

```
#### C#
```csharp
    async Task UploadMetadataToFile(string sasToken, string remoteFileName,  Dictionary<string, string> metadata)
    {
        var sasUri = new System.Uri(sasToken);
        var containerClient = new DataLakeDirectoryClient(sasUri);
                
        var fileClient = containerClient.GetFileClient(remoteFileName);
           
        if (metadata != null && metadata.Count > 0)
        {
            var response = await fileClient.SetMetadataAsync(metadata);
        }
    }
``` 

