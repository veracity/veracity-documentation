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
Using the apis these are the steps to follow:
* Step 1: Authenticate towards Veracity api using service account (service principle)
* Step 2: Define dataset with metadata and get SAS token uri from Veracity api
* Step 3: Read CSV file from your location and upload file to storage using received SAS token uri
* Step 4: Start job (if not set to automatic job processing in step 2)
* Step 5: Verify status on upload

## Step 1: Authenticate
### Get Veracity token for service principle/service account
Service Account Id (Client Id), secret and api key (subscription key) for your workspace are defined under tab API Integration in data Workbench Portal.

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
using Newtonsoft.Json.Linq;
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
    var token = (string)Newtonsoft.Json.Linq.JToken.Parse(result)["access_token"];
   return token;
}
```

## Step 2: Prepare update operation
### Prepare dataset update operation and get SAS URI for csv file upload
Using the Veracity token from step 1

**Payload**
-StartAutomatically: If True, the job of processing the file (step 3) will start automatically. However, if set to False, you need to start the job with api-endpoint. This is will trigger the job faster.
-Files can be more than one file. Operations: Upsert, Delete, Overwrite, Append. See operations defined below. Currently only one file is supported.
-DatasetId: id of dataset you want to update. can be retrieved from data workbench portal (see url on selected dataset)

**Operations**
When updating a dataset, you can use one of the following operations:
* **Upsert**: Update existing rows in dataset and ingest new rows (require that row keys are defined in schema)
* **Delete**: Delete rows in dataset where row keys match with row keys in file uploaded (require that row keys are defined in schema)
* **Overwrite**: Owerwrite existing dataset with new content from file uploaded
* **Append**: add data to dataset with content from file uploaded. This operation can only be used on schemas that o NOT have schema keys

**Output**
Job id and sas_uri
job_id is used to [get status of the update](#step-5-check-status) after file is uploaded and job started

**This is a PUT endpoint**

#### Python
```python
import requests
import json

#token from step 1
token = veracityToken
apiKey =  "<api key>"
workspaceId = "<workspace id>"
datasetId = "<dataset id>"

targetFileName = "ImportData.csv"

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
      "fileName": targetFileName,
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

# Extract the SAS token
sas_uri = result.get('sasToken')
update_job_id = result.get('jobId')
```

#### C#
```csharp
//output is a tuple with sasTokenUri and jobId     
  public async Task<(string, string)> GetSASUriForUpsertOperation(string datasetId,string targetFileName, 
      string workspaceId, string veracityToken, string subscriptionKey)
  {
      string sasTokenUri = string.Empty;
      string job_Id = string.Empty;

      string baseUrl = "https://api.veracity.com/veracity/dw/gateway/api/v2";
      string url = $"{baseUrl}/workspaces/{workspaceId}/ingest/dataset/{datasetId}";
      var token = veracityToken;

      //Operations are Upsert, Overwrite, Delete or Append
      var fileOperations = new List<Dictionary<string, object>>
      {
          new Dictionary<string, object>{
          ["fileName"] = targetFileName,
          ["operation"] = "Upsert"
          }
      };

      //if start autoamtically = false, job must be started with seperate endpoint
      var payload = new Dictionary<string, object>
      {           
          {"startAutomatically", false },
          {"files", fileOperations },
      };

      string jsonString = JsonConvert.SerializeObject(payload);
      HttpContent content = new StringContent(jsonString, Encoding.UTF8, "application/json");

      if (_httpClient == null)
          _httpClient = new HttpClient();

      _httpClient.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", subscriptionKey);
      _httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);

      try
      {
          var result = await _httpClient.PutAsync(url, content);
          if (result.IsSuccessStatusCode)
          {
              string json = result.Content.ReadAsStringAsync().Result;
              using JsonDocument doc = JsonDocument.Parse(json);
              JsonElement root = doc.RootElement;
              JsonElement jobId = root.GetProperty("jobId");
              JsonElement sasUri = root.GetProperty("sasToken");
              sasTokenUri = sasUri.ToString().Trim('"');
              job_Id = jobId.ToString().Trim('"');
          }
      }
      catch (Exception ex)
      {
          throw ex;
      }
      return (sasTokenUri, job_Id);
  }
```

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

Updating multiple files with different operations will **soon** be supported

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

## Step 3: Upload CSV file
### Upload file with update content using SAS URI from Step 2
We are using Microsoft libraries to upload data. The file will be processed using the operation defined in step 2. After file is uploaded (and started), use job_id from step 2 to request status of the processing. [Get status of the upload](https://developer.veracity.com/docs/section/dataplatform/storage/datasets#verify-upload-status)

* localFilepath is path for file to be uploaded
* targetFileName must be same as in step 2

#### Python
```python
from azure.storage.filedatalake import DataLakeFileClient, DataLakeDirectoryClient
from urllib.parse import urlparse
import os
import asyncio
from azure.core.exceptions import ResourceExistsError
import uuid
from urllib.parse import urlparse

localFilePath = "<local path to file>"

#Must be same filename as in step 2
target_file_name = targetFileName

# sas uri from step 2
sas_folder_url = sas_uri
# Parse the SAS URI from step 2
parsed_url = urlparse(sas_folder_url)
account_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
file_system_name = parsed_url.path.strip("/").split("/")[0]
folder_path = "/".join(parsed_url.path.strip("/").split("/")[1:])
sas_token = parsed_url.query
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
```

#### C#
```csharp
public async Task<int> UploadFileToDataset(string sasUriToken, string localFilepath, string targetFileName)
{
    var sasUri = new System.Uri(sasUriToken);
    string remoteFileName = targetFileName;
    var containerClient = new DataLakeDirectoryClient(sasUri);
    var containerFileClient = containerClient.GetFileClient(remoteFileName);
    
    using (FileStream fsSource = new FileStream(localFilepath, FileMode.Open, FileAccess.Read))
    {
        var response = await containerFileClient.UploadAsync(fsSource, true, CancellationToken.None);
        return response.GetRawResponse().Status;
    };
}
```

## Step 4: Start job processing
### Start processing the uploaded file(s) and store as delta tables
**This step only applies when "StartAutomatically" = False in step 2**

job_id from step 2 is used to [get status of the update](#step-5-check-status) after file is uploaded and job started

#### Python
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

#### C#
```csharp
public async Task<string> StartProcessingJob(string jobId, string workspaceId, string veracityToken, string subscriptionKey)
{
    string url = $"https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/ingest/job/{jobId}/start";
    var token = veracityToken;
    if (_httpClient == null)
        _httpClient = new HttpClient();

    _httpClient.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", subscriptionKey);
    _httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
    HttpContent content = null;
    try
    {
        var result = await _httpClient.PostAsync(url, content);
        if (result.IsSuccessStatusCode)
        {
            string status = result.Content.ReadAsStringAsync().Result;
            return status;
        }
    }
    catch (Exception ex)
    {

    }
    return $"Cannot start job {jobId}";
}

```

## Step 5: Check status
### Verify upload status
Since upload dataset takes 30-40 sec and processing is an asynchronous operation, status can be queried using status endpoint with the job_id from step 2.

Before upload is completed status will show:
{'jobId': '<job_id>', 'status': 'Running', 'operations': ['Create'], 'notebookErrorMessage': '', 'validationError': []}

After completion status shows:
{'jobId': 'job_id', 'status': 'Completed', 'operations': ['Create'], 'notebookErrorMessage': '', 'dataSetName': 'dataset name', 'datasetId': 'dataset_id', 'validationError': []}


#### Python
```python
import requests
apiKey =  "<api key>"
workspaceId = "<workspace id>"

base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
endpoint = f"/workspaces/{workspaceId}/ingest/job/{job_id}/status"
url = base_url + endpoint

headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": apiKey,
    "Authorization": f"Bearer {veracityToken}",
    "User-Agent": "python-requests/2.31.0"
}

try:
    response = requests.get(url,  headers=headers)
    response.raise_for_status()   
except requests.exceptions.RequestException as e:
    print(f"Error fetching job status: {e}")
    
result = response.json()
```
#### C#
```csharp
public async Task<string> GetJobStatus(string jobId, string workspaceId, string veracityToken, string subscriptionKey)                     
{
    string url = $"https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/ingest/job/{jobId}/status";
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
    return $"Cannot retrieve status for job {jobId.ToString()}";
}
```
