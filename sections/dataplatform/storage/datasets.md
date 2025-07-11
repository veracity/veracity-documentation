---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Datasets
Datasets are structured data and defined using schemas. Data can be queried using query language. Data is ingested using an api to receive SAS token and then SAS token is used to upload CSV.

## API endpoints

Note: The Ingest api-endpoints are different for uploading datasets vs uploading files to filestorage. To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json). **See section Dataset Ingest**

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints).  See section **Data Workbench API**

### Authentication and authorization
To authenticate and authorize your calls, you need API key and a bearer token [here](../auth.md). **To write data, the user/service account needs WRITE permissions (admin role). When creating a service account, its role is by default READER. To give it Write access, send request to [Veracity support](https://support.veracity.com/?r=1) requesting Admin role to "service account id" in "workspace id"**

## Ingest/Upload dataset process
Using the apis these are the steps to follow:
* Step 1: Authenticate towards Veracity api using service account (service principle)
* Step 2: Define dataset with metadata and get SAS token uri from Veracity api (Note: different endpoint than for getting SAS Uri for filestorage)
* Step 3: Read CSV file from your location and upload file to storage using received SAS token uri
* Step 4: Start job (if not set to automatic job processing in step 2)
* Step 5: Verify status on upload

## Prerequisite
A schema must be defined before you can upload a dataset. A schema is defined using Schema Management in the Portal, or [using the api](https://developer.veracity.com/docs/section/dataplatform/schemamanagem). 

When uploading a dataset it is the **schema version id** that is used (and not schema id). When using the api, schema version id is received in response. However, when schema is created in Data Workbench portal, you only see the schema_id (in url). To get schema version id, use schema Id and query the GET endpoint, [see how to get it](#get-schema-version-id).

## Step 1: Authenticate
### Get Veracity token for service principle/service account
Service Account Id (Client Id), secret and api key (subscription key) for your workspace are defined under tab API Integration in data Workbench Portal. **To write data, the user/service account needs WRITE permissions (admin role). When creating a service account, its role is by default READER. To give it Write access, send request to [Veracity support](https://support.veracity.com/?r=1) requesting Admin role to "service account id" in "workspace id"**

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

## Step 2: Prepare dataset for upload
### Define dataset with metadata and get SAS URI for uploading csv file
Using the Veracity token from step 1, ensure user/service account has Write access.
This step prepare upload operation and get SAS URI to upload file content. Ensure you have schema version id, [see how to get it](#get-schema-version-id)

**Payload**
* datasetName: name of dataset 
* SchemaVersionId: The id of the version of the schema
* Files: Currently only support for one file. 
* Operations: "Create" (when this is a new dataset)
* Filename used does not need to match the source filename (local filepath used in step 3), but must match the target filename used in step 3. I.e you can use a generic filename such as ImportData.csv
* DatasetDescription: Description field is optional
* Tags: Tags are metadata for the dataset, and is an array of key/values. Tags are optional. In the example below; customer and site are keys and "ABC" and "123" are values.
* Start Automatically: If True, the job of processing the file uploaded (step 3) will start automatically. However, if set to False, you need to start the job with api-endpoint. This is will trigger the job faster.
* Provider: Use "BYOD" (will be made optional)

**Output**
Job id and sas_uri
job_id is used to [get status of the upload](https://developer.veracity.com/docs/section/dataplatform/storage/datasets#verify-upload-status)

#### Python
```python
import requests
import json

#from step 1
token = veracityToken
apiKey =  "<api key>"
workspaceId = "<workspace id>"
schemaVersionId = "<schema version id>"

base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
endpoint = f"/workspaces/{workspaceId}/ingest/dataset"
url = base_url + endpoint

#Name to see in DWb
datasetName = "WindData"
targetFileName = "ImportData.csv"
description = "some dataset description"

headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": apiKey,
    "Authorization": f"Bearer {token}",
    "User-Agent": "python-requests/2.31.0"
}

payload = {
  "datasetName": datasetName,
  "datasetDescription": description,
  "schemaVersionId": schemaVersionId,
  "files": [
    {
      "fileName": targetFileName,
      "operation": "Create"
    }
  ], 
  "tags": [{
            "Key": "Customer",
            "Values": ["ABC"]
        },
        {
            "Key": "Site",
            "Values": ["123"]
        }
  ],
  "provider": "BYOD",
  "startAutomatically": False
}

try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()   
except requests.exceptions.RequestException as e:
    print(f"Error fetching sas uri: {e}")
    
result = response.json()
# Extract the SAS token
sas_uri = result.get('sasToken')
job_id = result.get('jobId')
```

#### C#

```csharp
using Azure.Storage.Files.DataLake;
using Newtonsoft.Json;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;

//output is a tuple with sasTokenUri and jobId       
 public async Task<(string, string)> GetSASUriForCreateOperation(string datasetName, string description, 
     string schemaVersionId, string targetFileName, string workspaceId,
     string veracityToken, string subscriptionKey)
 {
     string sasTokenUri = string.Empty;
     string job_Id = string.Empty;

     string baseUrl = "https://api.veracity.com/veracity/dw/gateway/api/v2";
     string url = $"{baseUrl}/workspaces/{workspaceId}/ingest/dataset";
     var token = veracityToken;
                 
     var fileOperations = new List<Dictionary<string, object>>
     {
         new Dictionary<string, object>{
         ["fileName"] = targetFileName,
         ["operation"] = "Create"
         }
     };

     //Example of how metadata can be created on dataset
     var tags = new List<Dictionary<string, object>> {
         new Dictionary<string, object> {
             ["Key"] = "Customer",
             ["Values"] = new List<string> { "ABC" }
         },
         new Dictionary<string, object> {
             ["Key"] = "Site",
             ["Values"] = new List<string> { "123" }
         }
     };

     //if start autoamtically = false, job must be started with seperate endpoint after fileupload
     var payload = new Dictionary<string, object>
     {
         {"datasetName", datasetName},
         {"datasetDescription", description},
         {"schemaVersionId",  schemaVersionId},
         {"provider", "BYOD"},
         {"startAutomatically", false },
         {"files", fileOperations },
         {"tags", tags }
     };

     string jsonString = JsonConvert.SerializeObject(payload);
     HttpContent content = new StringContent(jsonString, Encoding.UTF8, "application/json");

     if (_httpClient == null)
         _httpClient = new HttpClient();
 
     _httpClient.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", subscriptionKey);
     _httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
     
     try
     {
         var result = await _httpClient.PostAsync(url, content);                
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

## Step 3: Upload CSV file
### Upload file using SAS URI from Step 2
We are using Microsoft libraries to upload data

After file is uploaded and processing is triggered, use job_id from step 2 to request status of the processing. [Get status of the upload](https://developer.veracity.com/docs/section/dataplatform/storage/datasets#verify-upload-status)

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

#Source file
localFilePath = "<local file path>"

#Same file name as from step 2
target_file_name = targetFileName

# sas uri from step 2
sas_folder_url = sas_uri
# Parse the SAS URI from step 2
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
# Create a new file (overwrite if exists)
file_client.create_file()

# Upload file content
try:
    with open(localFilePath, 'rb') as file_data:
        file_contents = file_data.read()
        file_client.append_data(data=file_contents, offset=0, length=len(file_contents))
        file_client.flush_data(len(file_contents))
        print("✅ File uploaded successfully, check status for file processing using jobId from step 2")
except Exception as e:
    print(f"❌ General error occurred: {e}")
```
#### C#
```csharp
using Azure.Storage.Files.DataLake;
using Newtonsoft.Json;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;

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
After file is uploaded, use job_id to request status of the processing. [Get status of the upload](https://developer.veracity.com/docs/section/dataplatform/storage/datasets#verify-upload-status)

Use job_id from step 2

#### Python
```python
#from step 1
token = veracityToken
base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
endpoint = f"/workspaces/{workspaceId}/ingest/job/{job_id}/start"
url = base_url + endpoint

headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": apiKey,
    "Authorization": f"Bearer {token}",
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

## Get schema version id
Schema version id must be used to uplad a new dataset. Fetch schema id from url in Dataworkbench Portal (Schema management)

#### Python
```python
apiKey =  "<api key>"
workspaceId = "<Workspace id>"
schemaId = "<Schema id>"

base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
endpoint = f"/workspaces/{workspaceId}/schemas/{schemaId}"
url = base_url + endpoint

headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": apiKey,
    "Authorization": f"Bearer {veracityToken}",
    "User-Agent": "python-requests/2.31.0"
}

try:
    response = requests.get(url, json=None, headers=headers)
    response.raise_for_status()   
except requests.exceptions.RequestException as e:
    print(f"Error starting job: {e}")
    
result = response.json()

# Get the list of schema versions
schema_versions = result.get('schemaVersions')

# Get the first element - or iterate if there are several
first_schema_version = schema_versions[0]
# get id of schema version
schemaVersionId = first_schema_version.get('id')
```

#### C#
```csharp
public async Task<string> GetSchemaVersionId(string schemaId, string workspaceId, string veracityToken, string subscriptionKey)
{
    string schemaVersionId = null;
    if (!string.IsNullOrEmpty(schemaId))
    {
        string baseUrl = "https://api.veracity.com/veracity/dw/gateway/api/v2";
        string url = $"{baseUrl}/workspaces/{workspaceId}/schemas/{schemaId}";
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
                string json = result.Content.ReadAsStringAsync().Result;
                using JsonDocument doc = JsonDocument.Parse(json);
                JsonElement root = doc.RootElement;
                //in this example, reading first version
                JsonElement schemaVersions = root.GetProperty("schemaVersions")[0];
                var id = schemaVersions.GetProperty("id");
                return id.ToString();
            }
        }
        catch (Exception ex)
        {

        }                
    }
    return schemaVersionId;        
}
```

