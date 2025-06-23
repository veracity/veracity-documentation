---
author: Veracity
description: This is a tutorial how to call API endpoints of Data Workbench with sample Python code.
---

# Query files

## API endpoints
To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json). See section **Storages**


### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).

## Query for files

You can access files via API if you generate a SAS token. To query for data on file storage you need to perform the following steps:

1. Authenticate towards Veracity api using client credentials or user authentication.
2. Get SAS token uri from Veracity api - with READ access
3. Get data content (files, folders, metadata etc.)

See code examples below for each step in the process.

## Python Code example

### Step 1: Get Veracity token for authentication using Veracity service principle
```python
import requests

# Token URL for authentication 
token_url = "https://login.microsoftonline.com/dnvglb2cprod.onmicrosoft.com/oauth2/token"
clientId = <service account id>
secret = <service account secret>

# define the request payload    
payload = {
    "resource": "https://dnvglb2cprod.onmicrosoft.com/83054ebf-1d7b-43f5-82ad-b2bde84d7b75",
    "grant_type": "client_credentials",
    "client_id": clientId,
    "client_secret": secret
}

response = requests.post(token_url, data=payload)
if response.status_code == 200:
    veracityToken = response.json().get("access_token")
else:
    print(f"Error: {response.status_code}")

print(veracityToken)  # Will print None if request fails
```

### Step 2: Get SAS Uri for folder

```python
import requests
import json
from datetime import datetime, timedelta
 
mySubcriptionKey = <my service account api key>
workspaceId = <workspace id in DWB>
dwbFolderName = <folder name - if not provided root folder is used>
 
def get_sas_token(veracity_token, folder, workspace_id, subscription_key):
    base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
    endpoint = f"/workspaces/{workspace_id}/storages/sas"
    url = base_url + endpoint
    expires_on = (datetime.utcnow() + timedelta(hours=5)).isoformat() + "Z"
 
    payload = {
      "path": dwbFolderName,
      "readOrWritePermission": "Read",
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

sas_uri = get_sas_token(veracity_token= veracityToken,  folder=dwbFolderName, workspace_id=workspaceId,subscription_key= mySubcriptionKey)
print("SAS Token:", sas_uri)
```

In payload, if path is set to "empty string", path points default to root level of storage container.

### Step 3: Read folder and file content using SAS uri 

```python
from azure.storage.filedatalake import DataLakeServiceClient
from urllib.parse import urlparse

# Your SAS URI from step 2
sas_url = sas_uri

# Parse the URL
parsed_url = urlparse(sas_url)
account_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
file_system_name = parsed_url.path.strip("/").split("/")[0]
folder_path = "/".join(parsed_url.path.strip("/").split("/")[1:]) if len(parsed_url.path.strip("/").split("/")) > 1 else ""
sas_token = parsed_url.query if parsed_url.query.startswith('sv=') else ''

# Create the service client
service_client = DataLakeServiceClient(account_url=account_url, credential=sas_token)
directoryClient = service_client.get_directory_client(file_system_name, folder_path) if folder_path else None

filesystem_client = service_client.get_file_system_client(file_system=file_system_name)

# List files in the folder
paths = filesystem_client.get_paths(path=folder_path, recursive=False)
pathsLst = list(paths)

print(f"\nContents of folder '{folder_path}':")
for path in pathsLst:
    print(f"- {path.name} (Directory: {path.is_directory})")   


print(f"\nContents of all files in '{folder_path}':")
# list content of each file in folder
for path in pathsLst:
    print(f"- {path.name} :")   
    downloaded_bytes = filesystem_client.get_file_client(path).download_file().readall()
    # Decode and print the content
    file_content = downloaded_bytes.decode('utf-8')  # Adjust encoding if needed
    print(file_content)


```

### Read storage datasets using Veracity api

```python
import requests
import json
from datetime import datetime, timedelta
 
mySubcriptionKey = <api key>
workspaceId = <workspace id>
dwbFolderName = "Test"

base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
endpoint = f"/workspaces/{workspaceId}/storages/storagedatasets"
url = base_url + endpoint
 
headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": mySubcriptionKey,
    "Authorization": f"Bearer {veracityToken}",
    "User-Agent": "python-requests/2.31.0"
}

try:
    response = requests.get(url, json=payload, headers=headers)
    response.raise_for_status()   
except requests.exceptions.RequestException as e:
    print(f"Error fetching SAS token: {e}")
    
result = response.json()
print(result)
```


## C# Code example

#### Step 1: Get Veracity token for authentication using Veracity service principle
Client Id, secret and subscription key for your workspace are defined under tab API Integration in data Workbench Portal.
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

#### Step 2: Get SAS uri

To generate a SAS token, call the `{baseurl}/workspaces/{workspaceId:guid}/storages/sas` endpoint with the POST method using the Veracity token from step 1.
Create a SAS token for a given folder with Read access

```csharp
 
 public async Task<string> GetSASToken(string veracityToken, string folder, string workspaceId, string subscriptionKey)
 {
     string url = $"https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/storages/sas";

     DateTime expiresOn = DateTime.UtcNow.AddHours(1);
     string expiresOnStr = expiresOn.ToString("O");
                 
     //path is folder name in storage container
     var postData = new Dictionary<string, string>
     {
         {"path", folder},
         {"readOrWritePermission", "Read"},
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


### Step 3: Read files in folder
In step 2 the sas token was generated for a folder and this example iterates all files in that folder and reads metadata and content

```csharp
  public async Task ReadFiles(string sasToken)
  {
    
      var sasUri = new System.Uri(sasToken);
      var containerClient = new DataLakeDirectoryClient(sasUri);

      await foreach (var pathitem in containerClient.GetPathsAsync())
      {
          //build file url based on directory uri
          var fileUrl = $"{sasToken.Split('?')[0].Replace(containerClient.Name, pathitem.Name)}?{sasToken.Split('?')[1]}";
     
          //build file client for file
          var fileClient = new DataLakeFileClient(new System.Uri(fileUrl));
                    
          var metadata = new Dictionary<string, string>();
          var propertyResponse = await fileClient.GetPropertiesAsync();
          if (propertyResponse != null && propertyResponse.Value != null)
          {
              metadata = (Dictionary<string, string>)propertyResponse.Value.Metadata;
          }

          //read content                
          var response = await fileClient.ReadAsync();
          using var reader = new StreamReader(response.Value.Content);
          string content  = reader.ReadToEnd();                             

      }
  }
```
### Read metadata

```csharp
          //build file client for file
          var fileClient = new DataLakeFileClient(new System.Uri(fileUrl));
                    
          var metadata = new Dictionary<string, string>();
          var propertyResponse = await fileClient.GetPropertiesAsync();
          if (propertyResponse != null && propertyResponse.Value != null)
          {
              metadata = (Dictionary<string, string>)propertyResponse.Value.Metadata;
          }
```


