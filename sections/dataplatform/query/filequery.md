---
author: Veracity
description: This is a tutorial how to call API endpoints of Data Workbench with sample Python code.
---

# Query files

## API endpoints
To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json).
See section Storages

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)


## Query for files

You can access files via API if you generate a SAS token. To query for data on file storage you need to perform the following steps:

1. Authenticate towards Veracity api using client credentials or user authentication.
2. Get SAS token uri from Veracity api
3. Get data content (files, folders, metadata etc.)
4. Get all files in 
See code examples below for each step in the process.

### Code example

**Main program**

```csharp
using Azure.Storage.Files.DataLake;
using Azure.Storage.Files.DataLake.Models;
using Newtonsoft.Json.Linq;
using System.Net.Http.Headers;

//read secrets and parameters
string filename = "";
string workspaceId = "";
string subscriptionkey = "";
var client_id = "";
var client_secret = "";


string token = await GetToken(client_id, client_secret);
string sasToken = await GetSASToken(token, workspaceId, subscriptionkey);
await UploadFile( sasToken, filename);

```

**Step 1: Get Veracity token for authentication**
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

**Step 2: Get SAS token**

To generate a SAS token, call the `{baseurl}/workspaces/{workspaceId:guid}/storages/sas` endpoint with the POST method using the Veracity token from step 1.
Create a SAS token for a given folder with Read access

```csharp
 async Task<string> GetSASToken(string veracityToken, string folder, string workspaceId, string subscriptionKey)
 {
     string url = $"https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/storages/sas";

     DateTime expiresOn = DateTime.UtcNow.AddHours(1);
     //path is folder name in storage container
     SasRequest request = new SasRequest()
     {
         Path = folder,
         ReadOrWritePermission = "Read",
         ExpiresOn = expiresOn
     };
     string jsonBody = JsonConvert.SerializeObject(request );
     HttpContent content = new StringContent(jsonBody, Encoding.UTF8, "application/json");
     
    if (_httpClient == null)
         _httpClient = new HttpClient();

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


 internal class SasRequest    {

    [JsonProperty("path")]
    public string Path {get;set;}

    [JsonProperty("readOrWritePermission")] 
    public string ReadOrWritePermission { get; set; }
    
    [JsonProperty("expiresOn")]
    public DateTime ExpiresOn { get; set; }
}

 ```

**Step 3: Read files in folder**
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

To get all storage data sets of a workspace, call the following endpoint with a GET method.
`{baseurl}/workspaces/{workspaceId:guid}/storages/storagedatasets`



## Python sample for calling the endpoints
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
query_endpoint = f"https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspace_id}/storages/storagedatasets"

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
