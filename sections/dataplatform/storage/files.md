---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# File storage
This feature lets you upload files of any type into Azure Data Lake. Files are stored as unstructured data and cannot be queried using SQL-like operations.
Subscriptions to File Storage required.

## Internal and external storage

* Internal storage is a data storage account that comes together with your Data Lake File Storage.

* External storage is a data storage account from your company that was added to your Data Lake File storage (ie.e Mounting of datalakes)

If you want to add a new external storage account, contact Veracity support and provide connection strings to this account.

## API endpoints
To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json).
See section Ingest

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)

## Ingest process

1. Authenticate towards Veracity api using client credentials or user authentication.
2. Get SAS token uri from Veracity api
3. Read CSV file from your location and upload file to storage using received SAS token uri 

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

#### Get a SAS token for internal storage
To generate a SAS token, call the `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/storages/sas` endpoint with the POST method.

```
async Task<string> GetSASToken(string veracityToken, string workspaceId, string subscriptionKey)
{
    string url = $"https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/storages/sas";
    //path is folder name in storage container
    string jsonBody = "{\"path\":\"Test\",\"readOrWritePermission\":\"Write\",\"expiresOn\":\"2025-03-26T09:04:12.297Z\"}";

    HttpContent content = new StringContent(jsonBody, Encoding.UTF8, "application/json");         
    HttpClient _httpClient = new HttpClient();
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

#### Get a SAS token for external storage
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


**Step 3: Upload files using the SAS token received**

In this example we utilize Microsoft library to access the filestorage by using the aquired SAS-token from step 2.
```csharp
async Task UploadFile(string sasToken, string filename)
{
    var sasUri = new System.Uri(sasToken);
    var containerClient = new DataLakeDirectoryClient(sasUri);
    
    string remoteFileName = Path.GetFileName(filename);
    var containerFileClient = containerClient.GetFileClient(remoteFileName);
    
    using (FileStream fsSource = new FileStream(filename, FileMode.Open, FileAccess.Read))
    {
        bool overwrite = false;
        var response = await containerFileClient.UploadAsync(fsSource, overwrite, CancellationToken.None);
    };
}
   
```


## List SAS policies for internal storage
To list all SAS policies for internal storage, call the `https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId:guid}/storages/policies` endpoint with the GET method.

## List SAS policies for external storage
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

## Revoke a SAS policy for internal storage
To revoke a SAS token for internal storage, you don't revoke the token directly. Instead, you revoke the policy that the token is attached to.  Revoking the policy revokes all SAS tokens associated with that policy.

To revoke a SAS policy, call the following endpoint with the DELETE method:
`https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId:guid}/storages/sas/revoke`

Note that:
* You must be a workspace admin to revoke SAS policies.
* This endpoint accepts an optional query parameter called `policyToRevoke`.

Regarding `policyToRevoke` parameter, here are some important considerations:
* **If you don't provide the** `policyToRevoke` **parameter**: You'll revoke all SAS policies for the entire storage container (workspace). This means all active SAS tokens for that container will be revoked, regardless of which policy they were associated with.
* **If you do provide the** `policyToRevoke` **parameter**: You'll revoke only the specified policy. This means only the active SAS tokens associated with that specific policy will be revoked. Other tokens tied to different policies will remain active.

## Revoke a SAS policy for external storage
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