---
author: Veracity
description: This is a tutorial how to call API endpoints of Data Workbench with sample Python code.
---

# Query files

## API endpoints
To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json). See section **File Storages**

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).

## Query for files
You can access files via API if you generate a SAS token. To query for data on file storage you need to perform the following steps:

* Step 1: Authenticate towards Veracity api using client credentials or user authentication.
* Step 2: Get SAS token uri from Veracity api - with READ access
* Step 3: Read data content (files, folders, metadata etc.)
See code examples below for each step in the process.

## Step 1: Authentication
### Get Veracity token for authentication using Veracity service principle

#### Python
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
    HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Post, httpClient.BaseAddress);
    request.Content = new FormUrlEncodedContent(postData);
    HttpResponseMessage authResponse = httpClient.PostAsync(url, new FormUrlEncodedContent(postData)).Result;
    var result = await authResponse.Content.ReadAsStringAsync();
    var token = (string)JToken.Parse(result)["access_token"];
    return token;
    }
```

## Step 2: Get SAS Uri
### get SAS URI for folder

**Input payload**
Payload options:
* `path` is optional. It is the path to the resource for which you're generating the SAS token. If you don't provide a path, the default path will be used. The default path is the `ContainerName` (i.e. root level)
* `readOrWritePermission` : Should be "Read"
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
 
myApiKey =  <service account api key>
workspaceId =<workspace id>

#folder name, i.e "Test", folder must exist.
#If not provided you get access to storage container level (root level)
dwbFolderName = <name of folder in File Storage>

def get_sas_token(veracity_token, folder, workspace_id, subscription_key):
    base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
    endpoint = f"/workspaces/{workspace_id}/storages/sas?format=object"
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

## Step 3: Read folder and file content
Using SAS URI from step 2

#### Python
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

#### C#
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

## Read metadata
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


