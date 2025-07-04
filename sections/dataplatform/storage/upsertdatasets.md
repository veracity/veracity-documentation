---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Update Datasets
Datasets are structured data and defined using schemas. Dataset content can be updated with operation commands: upsert, append, overwrite and delete.

## API endpoints

Note: The Ingest api-endpoints are different for uploading datasets vs uploading files to filestorage. To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json). **See section Dataset Ingest**

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints).  See section **Data Workbench API**

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).
**When authenticating using service account, the service account needs WRITE permissions. When creating a service account, its role is by default READER. To give it Write access, send request to [Veracity support](https://support.veracity.com/?r=1) requesting Admin role to "service account id" in "workspace id"**

For code example, see step 1 below.

## Update process
Using the apis these are the three steps to follow:
1. Authenticate towards Veracity api using service account (service principle)
2. Get SAS token uri from Veracity api
3. Read CSV file(s) from your location and upload file to storage using received SAS token uri
4. Verify status on upload

## Python code example
### Step 1: Authentication: Get Veracity token for service principle/service account
Service Account Id (Client Id), secret and api key (subscription key) for your workspace are defined under tab API Integration in Data Workbench Portal.

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

### Step 2: Prepare dataset update operation and get SAS URI for csv file upload
Using the Veracity token from step 1

**Payload**
-Files can be more than one file. Operations: Upsert, Delete, Overwrite, Append. See operations defined below.
-Tags are metadata for the dataset, and is an array of key/values. Tags are optional and can be removed or null.
-Start Automatically: If True, the job of processing the file (step 3) will start automatically. However, if set to False, you need to start the job with api-endpoint. This is will trigger the job faster.
-Provider: Use "BYOD" (will be made optional)

**Output**
Job id and sas_uri

**Operations**
When updating a dataset, you can use one of the following operations:
* **Upsert**: Update existing rows in dataset and ingest new rows (require that row keys are defined in schema)
* **Delete**: Delete rows in dataset where row keys match with row keys in file uploaded (require that row keys are defined in schema)
* **Overwrite**: Owerwrite existing dataset with new content from file uploaded
* **Append**: add data to dataset with content from file uploaded. This operation can only be used on schemas that o NOT have schema keys

**This is a PUT endpoint**
```python
import requests
import json

#token from step 1
token = veracityToken
apiKey =  "<api key>"
workspaceId = "<workspace id>"
datasetId = "<dataset id>"

fileNameToImport = "ImportData.csv"

base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
endpoint = f"/workspaces/{workspaceId}/ingest/dataset/{datasetId}"
url = base_url + endpoint

headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": apiKey,
    "Authorization": f"Bearer {token}",
    "User-Agent": "python-requests/2.31.0"
}

payload = {
"files": [
    {
      "fileName": fileNameToImport,
      "operation": "Upsert"
    }
],
"startAutomatically": False
}

try:
    response = requests.put(url, json=payload, headers=headers)
    response.raise_for_status()   
except requests.exceptions.RequestException as e:
    print(f"Error fetching sas uri: {e}")
    
result = response.json()

# Extract the SAS token and job id
sas_uri = result.get('sasToken')
job_id = result.get('jobId')
```

job_id is used to [get status of the update](https://developer.veracity.com/docs/section/dataplatform/storage/datasets#verify-upload-status)

#### Delete data
Payload
```
"files": [
    {
      "fileName": "FileWithRowsToDelete.csv",
      "operation": "Delete"
    }
],
```
#### Multi operations

Updating multiple files with different operations will soon be supported

Payload
```
"files": [
    {
      "fileName": "FileWithRowsToDelete.csv",
      "operation": "Delete"
    },
     {
      "fileName": "FileWithRowsToInsert.csv",
      "operation": "Upsert"
    }
],
```

### Step 3: Upload file to process using SAS URI from Step 2
We are using Microsoft libraries to upload data. The file will be processed using the operation defined in step 2.

```python
from azure.storage.filedatalake import DataLakeFileClient, DataLakeDirectoryClient
from urllib.parse import urlparse
import os
import asyncio
from azure.core.exceptions import ResourceExistsError
import uuid
from urllib.parse import urlparse

localFilePath = <full path to file to be uploaded>

# sas uri from step 2
sas_folder_url = sas_uri
# Parse the SAS URI
parsed_url = urlparse(sas_folder_url)
account_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
file_system_name = parsed_url.path.strip("/").split("/")[0]
folder_path = "/".join(parsed_url.path.strip("/").split("/")[1:])
sas_token = parsed_url.query

#Must be same filename as in step 2
target_file_name = fileNameToImport

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


# Upload file content
with open(localFilePath, 'rb') as file_data:
    file_contents = file_data.read()
    file_client.append_data(data=file_contents, offset=0, length=len(file_contents))
    file_client.flush_data(len(file_contents))

print("Dataset update job started - check status using jobId from step 2.")
```
After file is uploaded, use job_id from step 2 to request status of the processing. [Get status of the upload](https://developer.veracity.com/docs/section/dataplatform/storage/datasets#verify-upload-status)

### Step 3b: Start processing the uploaded file(s) 
**This step only applies when  "startAutomatically": False in step 2**

```python
base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
endpoint = f"/workspaces/{workspaceId}/ingest/job/{job_id}/start"
url = base_url + endpoint

headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": apiKey,
    "Authorization": f"Bearer {veracityToken}",
    "User-Agent": "python-requests/2.31.0"
}

try:
    response = requests.post(url, json=None, headers=headers)
    response.raise_for_status()   
except requests.exceptions.RequestException as e:
    print(f"Error starting job: {e}")
    
result = response.json()
```
After file is uploaded, use job_id to request status of the processing. [Get status of the upload](https://developer.veracity.com/docs/section/dataplatform/storage/datasets#verify-upload-status)


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

### Step 1: Authentication: Get Veracity token for service principle/service account
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

### Step 2: Prepare dataset update operation and get SAS URI for dataset file upload
Using the Veracity token from step 1

When updating a dataset, you can use one of the following operations:
* **Upsert**: Update existing rows in dataset and ingest new rows (require that row keys are defined in schema)
* **Delete**: Delete rows in dataset where row keys match with row keys in file uploaded (require that row keys are defined in schema)
* **Overwrite**: Owerwrite existing dataset with new content from file uploaded
* **Append**: add data to dataset with content from file uploaded. This operation can only be used on schemas that o NOT have schema keys

**This is a PUT endpoint**

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

### Step 3: Upload file to process using SAS URI from Step 2
We are using Microsoft libraries to upload data. The file will be processed using the operation defined in step 2.

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
File is uploaded, but not processed. To [request processed status, use job_id from step 2](https://developer.veracity.com/docs/section/dataplatform/storage/datasets#verify-upload-status-step-4)




