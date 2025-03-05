---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# File storage
This feature lets you store any file in the Azure Data Lake. Files are stored as unstructured data and cannot be queried using SQL-like operations.

## Internal and external storage
Internal storage is a data storage account that comes together with your Data Lake File Storage.

External storage is a data storage account from your company that was added to your Data Lake File storage (ie.e Mounting of datalakes)

If you want to add a new external storage account, contact Veracity support and provide connection strings to this account.

## File storage endpoints
You can upload files to File storage via API. To do so, generate a SAS token.

### Get a SAS token for internal storage
To generate a SAS token, call the `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/storages/sas` endpoint with the POST method.

Below, you can see a sample request payload.


```json
{
"path": "string",
  "readOrWritePermission": "Read",
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

### Get a SAS token for external storage
To generate a SAS token, call the `https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId:guid}/storages/external/sas` endpoint with the POST method.

Below, you can see a sample request payload.


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


### Upload files using API

In this example we utilize Microsoft library to access the filestorage by using the aquired SAS-token.
```csharp

 var containerClient = new DataLakeDirectoryClient(sasToken);
 var containerFileClient = containerClient.GetFileClient(filename);
  using (FileStream fsSource = new FileStream(filename, FileMode.Open, FileAccess.Read))
  {
      var response = await containerFileClient.UploadAsync(fsSource, opts, CancellationToken.None);     
  };
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