---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Datasharing

Vertacity dataplatform supports several types of secure sharing of data:

**Share selected dataset to user (B2C share) or business (B2B share)
**Share selected file or folder and share to user (B2C share) or to business (B2B share)
**Share data  by generating SAS key for workspace, folder or file


## Share dataset
### Share single dataset to individual user (B2C sharing)
From Data Catalog, select dataset and share to user using email. User can be external to the tenant.
The receiver will receive an email and when opening the workspace they can only see the dataset shared to them. Dataset can be viwed and downloaded.

If the receiver selects to view this dataset into a Veracity workspace user has access to; the dataset is shared to a workspace and all users in this workspace will see it.

### Share single dataset to another workspace (B2B sharing)
If a dataset already has been shared to a user and receiver added this dataset to a workspace, a workspace sharing is enabled. Next time a sharing is to be performed, the "sharer" can select receiving workspace automatically from the dropdown list.

### Share datasets using SAS key
Select dataset and Generate Sas access kyes. This key is Read only and last until given end-date.

From api you can generate sas token for whole workspace or for individual dataset.

## Share files from filestorage
### Share single file or folder to individual user (B2C sharing)
Select single file or whole folder and select share icon. User can be external to the tenant.
The receiver will receive an email and when opening the workspace they can only see the dataset shared to them. Dataset can be viwed and downloaded.

### Share single file or folder to individual user (B2C sharing)
Select single file or whole folder and select share icon. If a file already has been shared to a user and receiver added this dataset to a workspace, a workspace sharing is enabled. Next time a sharing is to be performed, the "sharer" can select receiving workspace automatically from the dropdown list. *Will be available shortly.*

### Share files using SAS key
From Filestorage SAS keys can be generated for single file, folder or workspace level.

## Share using API endpoints
To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json).
(see subsection Shares)

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](auth.md).

## Get share owner info

```
POST {baseurl}/workspaces/{workspaceId}/schemas endpoint. 
```
BODY

```json
{
  "datasetIds": [
    "string"
  ]
}
```

The response lists xxx