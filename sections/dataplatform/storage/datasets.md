---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Datasets
Datasets are structured data and defined using schemas. Data can be queried using query language.
Data is ingested using an api to receive SAS token and then SAS token is used to upload CSV.

## API endpoints
To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json).
See section Ingest

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)

## Ingest process

1. Authenticate towards Veracity api using client credentials
2. Get SAS token uri from Veracity api
3. Read CSV file from your location and upload file to storage using received SAS token uri

When ingesting a dataset, you can:
* Create a new dataset based on given schema,
* Append data to exisiting dataset
* Update existing dataset (soon to be released)

### Create a new dataset

**Main program**

```csharp
using Azure.Storage.Files.DataLake;
using Azure.Storage.Files.DataLake.Models;
using Newtonsoft.Json.Linq;
using System.Net.Http.Headers;

//read secrets and parameters
string filename = "";
string schemaId = "";
string veracityUserId = "";
string workspaceId = "";
string appKey = "";
var client_id = "";
var client_secret = "";


string token = await GetToken(client_id, client_secret);
string sasToken = await GetSASToken(token, workspaceId, appKey);
await UploadStructuredDataset(workspaceId, sasToken, filename, schemaId, veracityUserId);

```

**Step 1: Get Veracity token for authentication**
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

**Step 2: Get SAS token**
To generate a dfs SAS token, call the `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/ingest` endpoint with the POST method using the Veracity token from step 1.

Subscription key for your workspace is defined under tab API Integration.

```csharp

Guid _requestId = Guid.Empty;
async Task<string> GetSASToken(string veracityToken, string workspaceId, string subscriptionKey)
{
    string url = $"https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/ingest";

    var token = veracityToken;
    HttpClient _httpClient = new HttpClient();
    _httpClient.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", subscriptionKey);
    _httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
    HttpContent content = null;
    var result = await _httpClient.PostAsync(url, content);
    if (result.IsSuccessStatusCode)
    {
        string sasKey = result.Content.ReadAsStringAsync().Result;

        _requestId = GetRequestId(result.Headers);
        return sasKey.Trim('"');
    }
    return null; 

}
```
From the response you get sas key ans well as a request id. The request id can be used to Poss the status of the ingest job.



[!Note]
If DataLakeDirectoryClient can not be used, you would need the blob SAS token
You can generate a blob SAS token URL by calling `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/ingest?type=blob`

**Step 3: Upload  dataset using SAS key from step2**

Get schemaId from [Schema management](..\schemamanagem.md). If schema is not created, create one.

```csharp
async Task UploadStructuredDataset(string workspaceId, string sasToken, string filename, string schemaId, string veracityUserId)
{
    var sasUri = new System.Uri(sasToken);
    string remoteFileName  = Path.GetFileName(filename);
    var containerClient = new DataLakeDirectoryClient(sasUri);
    var containerFileClient = containerClient.GetFileClient(remoteFileName);
    var correlationId = Guid.NewGuid();
    var metadata = new Dictionary<string, string>
        {
            { "userId", veracityUserId },
            { "correlationId", correlationId.ToString() },
            { "datasetName", "Weather data" },
            { "description", "weather data"},
            { "tags", "{}" },
            { "schemaId", schemaId.ToString() } 
        };
    var opts = new DataLakeFileUploadOptions { Metadata = metadata };
    using (FileStream fsSource = new FileStream(filename, FileMode.Open, FileAccess.Read))
    {
        var response = await containerFileClient.UploadAsync(fsSource, opts, CancellationToken.None);
    };

    //poll for response

}
```

### Append to a existing dataset
To append to an exisiting data set, the SAS token Uri is different since it need information about the datasetId

To generate a dfs SAS token, call the `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/ingest?datasetId={datasetId}` endpoint with the POST method.

You can generate a blob SAS token URL by calling `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/ingest?datasetId={datasetId}&type=blob`


### Overwrite a existing dataset

#### Get append SAS token

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
