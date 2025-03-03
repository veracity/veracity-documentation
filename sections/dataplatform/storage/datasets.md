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

- Get SAS token
- Read CSV file from your location
- Push file to storage using SAS token

### Create a new dataset

#### Get SAS token
To generate a dfs SAS token, call the `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/ingest` endpoint with the POST method.

You can generate a blob SAS token URL by calling `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/ingest?type=blob`

#### Code examples

```csharp

 var containerClient = new DataLakeDirectoryClient(sasToken);
 var containerFileClient = containerClient.GetFileClient(filename);
 var correlationId = Guid.NewGuid();
 var metadata = new Dictionary<string, string>
        {
            { "userId", veracityUserId },
            { "correlationId", correlationId.ToString() },
            { "datasetName", datasetName },
            { "description", datasetDescription},
            { "tags", "{}" },
            { "schemaId", schemaId.ToString() } //optinal
        };
  var opts = new DataLakeFileUploadOptions { Metadata = metadata };
  using (FileStream fsSource = new FileStream(filename, FileMode.Open, FileAccess.Read))
  {
      var response = await containerFileClient.UploadAsync(fsSource, opts, CancellationToken.None);     
  };
```

### Append to a existing dataset

#### Get append SAS token
To generate a dfs SAS token, call the `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/ingest?datasetId={datasetId}` endpoint with the POST method.

You can generate a blob SAS token URL by calling `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/ingest?datasetId={datasetId}&type=blob`

#### Code examples

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
            { "schemaId", schemaId.ToString() } //optinal
        };
  var opts = new DataLakeFileUploadOptions { Metadata = metadata };
  using (FileStream fsSource = new FileStream(filename, FileMode.Open, FileAccess.Read))
  {
      var response = await containerFileClient.UploadAsync(fsSource, opts, CancellationToken.None);     
  };
```

### Overwrite a existing dataset

#### Get append SAS token
To generate a dfs SAS token, call the `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/ingest?datasetId={datasetId}` endpoint with the POST method.

You can generate a blob SAS token URL by calling `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/ingest?datasetId={datasetId}&type=blob`

#### Code examples

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
