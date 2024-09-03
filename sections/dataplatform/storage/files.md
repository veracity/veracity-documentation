---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Filestorage
This feature allows you to store any file in the datalake. Files are stored as unstructured data and can not be queried sql-like.

## File storage endpoints

You can upload files via API if you generate a SAS token.

### Get SAS token
To generate a SAS token, call the `https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId:guid}/storages/sas` endpoint with the POST method.

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


### Upload files using API

```csharp

 var containerClient = new DataLakeDirectoryClient(sasToken);
 var containerFileClient = containerClient.GetFileClient(filename);
  using (FileStream fsSource = new FileStream(filename, FileMode.Open, FileAccess.Read))
  {
      var response = await containerFileClient.UploadAsync(fsSource, opts, CancellationToken.None);     
  };
```



