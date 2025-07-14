---
author: Veracity
description: This page explains how to utilize the analytics capabilities
---
# Veracity Analytics Environment
Veracity enables an advanced analytics environment using Azure Databricks and ensuring compliance with security best practices.

Azure Databricks is a unified, open analytics platform for building, deploying, sharing and maintaining analytics and AI solutions at scale. Databricks allows you to do large scale analytics, data engineering processes, workflows, AI and machine learning. In Azure Databricks, notebook is the primary tool for creating data science and machine learning workflows.

[Azure Databricks documentation](https://learn.microsoft.com/en-us/azure/databricks/)

To buy subscription for Analytics Environment, contact support@veracity.com

## How does Databricks connect to Veracity data platform storage

A dedicated Databricks environment is enabled for a single workspace in Veracity Data Workbench on request. Veracity managed Databricks environments enable Unity Catalog, a unified governance solution for data and AI assets on Databricks.

<figure>
  <img src="assets/dataplatformAnalytics.PNG"/>  
</figure>

All structured data (datasets) and all files stored in the Data Workbench workspace are available in the databricks catalog and can be processed. New datasets and files can be created and synched back to Veracity Data Workbench datalake.

To upload data directly to Veracity dataplatform storage, see [Upload dataset](https://developer.veracity.com/docs/section/dataplatform/storage/datasets)  and [Upload files](https://developer.veracity.com/docs/section/dataplatform/storage/files)


## Data management 

A Databricks Catalog is created for each Data workbench workspace you have access to that has Analytics enabled. You will see these  under **Catalog** as **vdp_tenant_workspaceName**

Databricks uses two primary securable objects to store and access data:

- **Tables** govern access to tabular data: This is were all datasets from your Veracity workspace will be listed. This includes shared datasets from other workspaces.
- **Volumes** govern access to non-tabular data: This is where all files from Veracity filestorage is listed. **Note:** See exception for shared files/folders below.

**For more information**
- [The unity catalogue model](https://docs.databricks.com/aws/en/data-governance/unity-catalog)
- [Datbase objects](https://docs.databricks.com/aws/en/database-objects/)

Users can not create new catalogs since share is not enabled.

### Shared files/folders
Shared files and folders from other workspaces, will currently NOT appear in Databricks Volume section. This feature is depending on a Databricks update planned this year. The workaround for using shared files/folders in Analytics is:

1. Share files/folders from one DWB workspace to the workspace with Write access. [Share files]()
2. Create sas token from DWB file/folder.  [Create SAS token]()
3. Access shared files in Databricks using SAS token. [Use Sas token in Python]

Shared datasets are available under DataBricks catalog Tables.

## Users and access
When users are added to Data Workbench, they will be synced with databricks user group (Readers or Admins Group).

**Note:** Only internal user(dnv.com ) will be granted access to databricks environment.

The role the user has in the Veracity Data Workbench workspace [affects permissions in Databricks](matrix.md).

## Workspace
With the Databricks workspace browser you can create, browse, and organize Databricks objects, including notebooks, libraries, experiments, queries, dashboards, and alerts, in a single place. 

You can create private folders or shared folders.  When organizing work under shared, all users in Veracity Data Workbench workspace can see the folder.

A private folder can be shared with individual users.

## Development

Developing in the workspace is a great way to quickly get familiar with Databricks APIs. Databricks supports Python, SQL, Scala, R, and other developer-focused features in the workspace, including helpful tools and utilities.

Notebooks are a common tool in data science and machine learning for developing code and presenting results. In Azure Databricks, notebooks are the primary tool for creating data science and machine learning workflows.

[How to get started](https://learn.microsoft.com/en-us/azure/databricks/developers/)


## Variables and parameters
Use variables to make your script more dynamic.  Multiple values can be passed to the notebook using Widgets or Notebook parameters.

[See how to handle secrets in Databricks](secretmgm.md)

### Notebook parameters
When executing the notebook via a Databricks job, parameters should be passed dynamically.
Notebook parameters should be used when calling one Notebook from another and need to pass values.

[For more information](https://docs.databricks.com/aws/en/jobs/parameters)

### Widgets
Use widgets when running a notebook interactively and manually changing the parameters.
[How to use Widgets](https://learn.microsoft.com/en-us/azure/databricks/notebooks/widgets)

To escape table names and column names that clash with SQL keywords, enclose the name between two grave accent marks `` (ASCII value 96).

```python
dbutils.widgets.text("filepath", "full_file_path")
dbutils.widgets.text("datasetName", "`myTableName`")
```
Read widget paramter into variable
```python
filename = dbutils.widgets.get("filepath")
```

### Decalare variables
DECLARE variable is a user-defined variable that can hold a single hardcoded values that do not change often. It acts as a container to store and manipulate data during the execution of a script or code. 

[For more information](https://learn.microsoft.com/en-us/azure/databricks/sql/language-manual/sql-ref-syntax-ddl-declare-variable)

## Libraries
How to manage libraries on cluster and notebook level, [see library management](https://developer.veracity.com/docs/section/dataplatform/analytics/analyticslibraries)

## Handle secrets
How to manage secrets in a secure way, [see details](https://developer.veracity.com/docs/section/dataplatform/analytics/secretmgm)

## Read datasets
Datasets in your Dataworkbench is automatically available as Tables in Azure Databricks.

Use Sql Editor or Notebook with Sql to query dataset from tables.

To read dataset using python
table name (datasetName) is stored in Widget

```python
dsName = dbutils.widgets.get("datasetName")
df2 = spark.table(dsName)
``` 

```python
dsName = dbutils.widgets.get("datasetName")
query = f"select * from {dsName}"
df = spark.sql(query)
```

When using sql, use the widgetname directly to parameterize tableNmae
```python
%sql
select * from ${datasetName} where Value > 1000
```
This result is stored as _sqldf and can be used in other Python and SQL cells.

## Read files from Volume

The choice between Pyspark or Pandas depends on the size and complexity of your dataset and the nature of your application. If you are working with small to medium-sized datasets, Pandas is a good choice. If you are dealing with big data or real-time processing, Pyspark is a better option. Pandas loads data in memory before running queries, so it can only query datasets that fit into memory. Spark can query datasets that are larger than memory by streaming the data and incrementally running computations

openpyxl provides fine-grained control over reading and writing Excel files. The read_only mode significantly improves performance when reading large files

Read CSV is faster that reading XLSX

```
filename = dbutils.widgets.get("filepath")
df2= pd.read_csv(filename)
```


## Synchronize with datasets in Data workbench
Datasets in Data workbench are synchronized into tables in the Databricks environment. 

### Create new tables in databricks
New datasets can be created from Databricks and synchronized with Data Workbench. This is especially useful for data transformations (medallion architecture). For creating new tables in Databricks that need to be synced to Data Workbench, use Veracity internal library named **dataworkbench** that comes pre-installed to the cluster. 

In below example demo dataframe is written to dataset in Data Workbench using library "dataworkbench"
```python
import dataworkbench

df = spark.createDataFrame([("a", 1), ("b", 2), ("c", 3)], ["letter", "number"])

datacatalogue = dataworkbench.DataCatalogue()
datacatalogue.save(
    df,
    "Dataset Name",
    "Description",
    tags={"asset": ["123"], "level": ["Silver"]},
    schema_id="abada0f7-acb4-43cf-8f54-b51abd7ba8b1"  # Using an existing schema ID, if not provided a new schema is created
)
```
The code above will create a dataset with the existing schema id "current active version". 
If schema_id is not provided, a new schema will be created based on the definition in the table.


### Updating existing tables using overwrite

For existing tables that are synchronized between Databricks and Data Workbench, you can directly overwrite the table using Spark's write methods.

```python
# Create a new DataFrame
df = spark.createDataFrame([
    ("d", 1), 
    ("e", 2), 
    ("f", 5)
], ["letter", "number"])


# Overwrite the existing table
df.write.mode("overwrite").saveAsTable("TableNameOverwrite")
```

### Updating existing tables using append mode

When you want to add new rows to an existing table:
```python
# Append new data to the existing table 
df.write.mode("append").saveAsTable("TableName")`
```

**Common modes:**
*   `overwrite`: Completely replaces the existing table
*   `append`: Adds new rows to the existing table
*   `ignore`: Skips insertion if data already exists
*   `error`: Raises an error if data conflicts (default behavior)

## Synchronize files with Data workbench
There is no action required to synchronize files between Veracity data platform file storage and the Databricks environment. Files uploaded to Veracity data platform filestorage are visible in Databricks under Data Catalog/Default/Volumes. New files stored in Volume in databricks are visible in data platform file storage in same sub-folders.

## Write files
If creating a new file in Volume, you can create a new directory from workspace or from notebook

**Example:**
```py
import os
os.mkdir('/Volumes/<path>/default/filestorage/MyDir')

##outputfilename is stored in widget
filename = dbutils.widgets.get("outputfilepath")
df.to_csv(filename, index= False) 
```

## Connect to Asset model using API
How to connect to Asset model from Python

[Explore Asset Model Query API](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/DataFabric-MMS-Query-API-swagger.json)

This example; use client id and secret from API-integration and retrieves a token which is used in the following apis.

### Authenticate
```py
import requests
import json

# Token URL for authentication 
token_url = "https://login.microsoftonline.com/dnvglb2cprod.onmicrosoft.com/oauth2/token"
clientId = "CLIENT_ID"
secret =  "SECRET"
# define the request payload    
payload = {"resource": "https://dnvglb2cprod.onmicrosoft.com/83054ebf-1d7b-43f5-82ad-b2bde84d7b75",
          "grant_type": "client_credentials",
          "client_id": clientId,
          "client_secret" :secret
          }
response = requests.post(token_url, data=payload)   
if response.status_code == 200:
        access_token = response.json().get("access_token")
else:
        print(f"Error: {response.status_code}")
```

### Retrive site information
```py
tenantId = "DNVES"
siteId = SITE_ID  (get from variable)
subscriptionKey = SUBKEY
queryurl = f"https://api.veracity.com/veracity/mms/query/{tenantId}/api/v1/sites/{siteId}"

header = {"Authorization": f"Bearer {access_token}", "Ocp-Apim-Subscription-Key": subscriptionKey,
          "Content-Type": "application/json"}
response = requests.get(queryurl, headers=header)

```

### Get devices 
```py
tenantId = "DNVES"
siteId = SITE_ID  (get from variable)
subscriptionKey = SUBKEY

queryurl = f"https://api.veracity.com/veracity/mms/query/{tenantId}/api/v1/sites/{siteId}/devices?start=0&pageSize=1000&sortColumn=Description&sortDirection=0&productTypeFilter=Inverter"

header = {"Authorization": f"Bearer {access_token}", "Ocp-Apim-Subscription-Key": subscriptionKey,
          "Content-Type": "application/json"}
response = requests.get(queryurl, headers=header)
```

