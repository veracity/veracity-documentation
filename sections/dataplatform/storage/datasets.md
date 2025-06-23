---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Datasets
Datasets are structured data and defined using schemas. Data can be queried using query language. Data is ingested using an api to receive SAS token and then SAS token is used to upload CSV.

## API endpoints

Note: The Ingest api-endpoints are different for uploading datasets vs uploading files to filestorage. To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json). **See section Ingest**

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints).  See section **Data Workbench API**

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).
**When authenticating using service account, the service account needs WRITE permissions. When creating a service account, its role is by default READER. To give it Write access, send request to [Veracity support](https://support.veracity.com/?r=1) requesting Admin role to "service account id" in "workspace id"**

## Ingest/Upload process
Using the apis these are the three steps to follow:
1. Authenticate towards Veracity api using service account (service principle)
2. Get SAS token uri from Veracity api
3. Read CSV file from your location and upload file to storage using received SAS token uri
4. Verify status on upload

When ingesting a dataset, you can:
* Create a new dataset based on given schema,
* Append data to exisiting dataset (soon to be released)
* Update existing dataset (soon to be released)

## Python code example
### Step 1: Authentication: Get Veracity token for service principle/service account
Service Account Id (Client Id), secret and api key (subscription key) for your workspace are defined under tab API Integration in data Workbench Portal.

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

### Step 2: Get SAS URI for Datasets (not for filestorage)
Using the Veracity token from step 1

```python
import requests
import json
from datetime import datetime, timedelta
 
myApiKey =  <service account api key>
workspaceId = <workspace id in DWB>>

base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
endpoint = f"/workspaces/{workspaceId}/ingest"
url = base_url + endpoint

headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": myApiKey,
    "Authorization": f"Bearer {veracityToken}",
    "User-Agent": "python-requests/2.31.0"
}

try:
    response = requests.post(url, headers=headers)
    response.raise_for_status()        
    request_id = response.headers.get("X-Request-Id")
    sas_uri = response.json()            
except requests.exceptions.RequestException as e:
    print(f"Error fetching SAS token: {e}")
```

request_id is used in step 4 to get status of the upload.

### Step 3a: Upload file as new dataset using SAS URI from Step 2
We are using Microsoft libraries to upload data

```python
from azure.storage.filedatalake import DataLakeFileClient, DataLakeDirectoryClient
from urllib.parse import urlparse
import os
import asyncio
from azure.core.exceptions import ResourceExistsError
import uuid
from urllib.parse import urlparse

localFilePath = <full path to file to be uploaded>
description = "some dataset description"
schemaId = <Schema id from DWB>
veracityUser = uuid.UUID(int=0)

# sas uri from step 2
sas_folder_url = sas_uri
# Parse the SAS URI from step 2
parsed_url = urlparse(sas_folder_url)
account_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
file_system_name = parsed_url.path.strip("/").split("/")[0]
folder_path = "/".join(parsed_url.path.strip("/").split("/")[1:])
sas_token = parsed_url.query

target_file_name = os.path.basename(localFilePath)

# === COMBINE FOLDER + FILE NAME ===
file_path = f"{folder_path}/{target_file_name}"

# === CREATE FILE CLIENT ===
file_client = DataLakeFileClient(
    account_url=account_url,
    file_system_name=file_system_name,
    file_path=file_path,
    credential=sas_token
)

# Create a new file (overwrite if exists)
file_client.create_file()

# Metadata, tags are optional and is a key/value set representing custom metadata such as asset id, project id, customer etc,
correlation_id = str(uuid.uuid4())
metadata = {
    "userId": str(veracityUser),
    "correlationId": correlation_id,
    "datasetName": target_file_name,
    "description": description,
    "tags": "{}",
    "schemaId": str(schemaId)
}

# Upload file content
with open(localFilePath, 'rb') as file_data:
    file_contents = file_data.read()
    file_client.append_data(data=file_contents, offset=0, length=len(file_contents))
    file_client.flush_data(len(file_contents))
    file_client.set_metadata(metadata)

print("New dataset created and uploaded - check status using request_id.")
```

File is uploaded, but not processed before the response. **To request processed status, see step 4.**


### Step 3b: Append to exisiting dataset using SAS URI from Step 2
We are using Microsoft libraries to upload data

```python


```

### Step 3c: Upsert exisiting dataset using SAS URI from Step 2
We are using Microsoft libraries to upload data

```python


```

## C# Code example 

```csharp
using Azure.Storage.Files.DataLake;
using Azure.Storage.Files.DataLake.Models;
using Newtonsoft.Json.Linq;
using System.Net.Http.Headers;

//read secrets and parameters
string filename = <filepath to upload>;
string schemaId = <schema id>;
string veracityUserId = <user id of user uploading>;
string workspaceId = <DWB workspace id>;
string appKey = <my service account subscription key>;
var client_id = <my service account ID>;
var client_secret = <my service account secret>;
```

### Step 1: Get Veracity token for authentication
Service account Id, secret and subscription key for your workspace are defined under tab API Integration in data Workbench Portal.
If you want to use user authentication, [see further details in Veracity Identity Documentation](https://developer.veracity.com/docs/section/identity/identity).

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

### Step 2: Get SAS token using Veracity token
To generate a dfs SAS token for datasets, call the `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/ingest` endpoint with the POST method using the Veracity token from step 1.

Subscription key for your workspace is defined under tab API Integration.

```csharp

  public async Task<(string,string)> GetSASToken(string veracityToken, string workspaceId, string subscriptionKey)
  {
      //output is a tuple with sasTokenUri and RequestId
      string sasTokenUri = string.Empty;
      string request_Id = string.Empty; // to be used to request status
      string url = $"https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/ingest";

      var token = veracityToken;
      if (_httpClient == null)
           _httpClient = new HttpClient();

      _httpClient.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", subscriptionKey);
      _httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
      HttpContent content = null;
      try
      {
          var result = await _httpClient.PostAsync(url, content);
          
          var values = result.Headers.GetValues("X-Request-Id");
          var requestId = values.FirstOrDefault();
          if (!String.IsNullOrWhiteSpace(requestId))
          {
              if (Guid.TryParse(requestId, out var requestIdGuid))
                  request_Id = requestIdGuid.ToString();
          }
          //use requestIdGuid to request status of operation using endpoint - need to wait 30-60 sec

          if (result.IsSuccessStatusCode)
          {
              string sasKey = result.Content.ReadAsStringAsync().Result;
              sasTokenUri = sasKey.Trim('"');
              Dictionary<string, string> sasUriAndRequestId = new Dictionary<string, string>();
              return (sasTokenUri, request_Id);
          }             
      }
      catch (Exception ex)
      {

      }    
      return (null, null);
  }

```
Methods returns tuple that can be read like this: 
```csharp
var(sasToken, requestId) = await ingestDataSetHandler.GetSASToken(token, workspaceId, apiKey);
```
The request id can be used to receive the status of the ingest job (see step 4)

[!Note]
If DataLakeDirectoryClient can not be used, you would need the blob SAS token
You can generate a blob SAS token URL by calling `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/ingest?type=blob`

### Step 3: Upload new dataset using SAS uri

Get schemaId from [Schema management](..\schemamanagem.md). If schema is not created, create one.

```csharp
async Task UploadStructuredDataset(string workspaceId, string sasToken, string filepath, string schemaId, string veracityUserId)
{
    var sasUri = new System.Uri(sasToken);
    string remoteFileName  = Path.GetFileName(filepath);  //filepath is full path to file to be uploaded
    var containerClient = new DataLakeDirectoryClient(sasUri);
    var containerFileClient = containerClient.GetFileClient(remoteFileName);
    var correlationId = Guid.NewGuid();
    var description = "some description";
    var metadata = new Dictionary<string, string>
        {
            { "userId", veracityUserId },
            { "correlationId", correlationId.ToString() },
            { "datasetName", remoteFileName },
            { "description", description},
            { "tags", "{}" },
            { "schemaId", schemaId.ToString() } 
        };
    var opts = new DataLakeFileUploadOptions { Metadata = metadata };
    using (FileStream fsSource = new FileStream(filename, FileMode.Open, FileAccess.Read))
    {
        var response = await containerFileClient.UploadAsync(fsSource, opts, CancellationToken.None);
    };

    //poll for response using the request id from step 2  

}
```
File is uplaoded, but not processed before the response. To request processed status, see step 4.

### Step 3b: Append to a existing dataset
To append to an exisiting data set, the SAS token Uri is different since it need information about the datasetId

To generate a dfs SAS token, call the `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/ingest?datasetId={datasetId}` endpoint with the POST method.

You can generate a blob SAS token URL by calling `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/ingest?datasetId={datasetId}&type=blob`


### Step 3c: Overwrite a existing dataset

In this example we utilize Microsoft library to access the filestorage by using the aquired SAS-token.

```csharp

 var containerClient = new DataLakeDirectoryClient(sasToken);
 var containerFileClient = containerClient.GetFileClient(filename);
 var correlationId = Guid.NewGuid();
 var metadata = new Dictionary<string, string>
        {
            { "userId", veracityUserId.ToString() },
            { "correlationId", correlationId.ToString() },
            { "datasetName", datasetName },
            { "description", datasetDescription},
            { "tags", "{}" },
            { "operation", "overwrite"},
            { "schemaId", schemaId.ToString() } //optinal
        };
  var opts = new DataLakeFileUploadOptions { Metadata = metadata };
  using (FileStream fsSource = new FileStream(filename, FileMode.Open, FileAccess.Read))
  {
      var response = await containerFileClient.UploadAsync(fsSource, opts, CancellationToken.None);     
  };
```

## Verify upload status (Step 4)
Since upload dataset takes 30-40 sec, status can be queried using status endpoint with the request_if from step 2.

Before uplad is completed status will show:
{"status":"Started","correlationId":"00000000-0000-0000-0000-000000000000"}

After completion:
Example:
{"status":"Completed","correlationId":"00000000-0000-0000-0000-000000000000","dataSetName":"weatherdata.csv","datasetId":"6b34f3c6-1e70-4676-beda-0b2dc604433a"}


## Python code example
```python
import requests

#request id from step 2
requestId = request_id

base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
endpoint = f"/workspaces/{workspaceId}/ingest/{requestId}/status"

url = base_url + endpoint

headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": myApiKey,
    "Authorization": f"Bearer {veracityToken}",
    "User-Agent": "python-requests/2.31.0"
}

response = requests.get(url, headers=headers)
response.raise_for_status()      
if response.status_code == 200:
    status = response.json()
else:
    print(f"Error: {response.status_code}")

print(status)
```

## C# Code example

```csharp
 async Task<string> GetStatus(Guid requestId, string veracityToken, string workspaceId, string subscriptionKey)                     
{

    string url = $"https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/ingest/{requestId}/status";

    var token = veracityToken;
    if (_httpClient == null)
        _httpClient = new HttpClient();

    _httpClient.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", subscriptionKey);
    _httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
    try
    {
        var result = await _httpClient.GetAsync(url);
        if (result.IsSuccessStatusCode)
        {
            string status = result.Content.ReadAsStringAsync().Result;
            return status;
        }
    }
    catch (Exception ex)
    {

    }
    return $"Cannot retrieve status for request id {requestId.ToString()}";
}
```