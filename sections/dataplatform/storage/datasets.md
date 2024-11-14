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

### Create a new dataset

- Get SAS token
- Read CSV file from your location
- Push file to storage using SAS token

#### Get SAS token
To generate a SAS token, call the `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/ingest` endpoint with the POST method.

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
#### Code examples

```csharp

 var containerClient = new DataLakeDirectoryClient(sasToken);
 var containerFileClient = containerClient.GetFileClient(filename);
  using (FileStream fsSource = new FileStream(filename, FileMode.Open, FileAccess.Read))
  {
      var response = await containerFileClient.UploadAsync(fsSource, opts, CancellationToken.None);     
  };
```

### Append to a dataset
