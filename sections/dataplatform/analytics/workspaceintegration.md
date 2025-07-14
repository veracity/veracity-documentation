---
author: Veracity
description: This page explains how to utilize the analytics capabilities
---
# Using files and datasets
All structured data (datasets) and all files stored in the Data Workbench workspace are available in the databricks catalog and can be processed. New datasets and files can be created and synched back to Veracity Data Workbench datalake.

Databricks uses two primary securable objects to store and access data:

- **Tables** govern access to tabular data: This is were all datasets from your Veracity workspace will be listed. This includes shared datasets from other workspaces.
- **Volumes** govern access to non-tabular data: This is where all files from Veracity filestorage is listed. **Note:** See exception for shared files/folders below.


## Read datasets
Datasets from Data workbench are automatically available as Tables in Azure Databricks.

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

## Synchronize datasets
Datasets in Data workbench are synchronized into **tables** in the Databricks environment. You can update existing tables in Databricks and then the dataset in Data workbench is automatically updated.

When creating a new table in Databricks, it is not automatically synched back to Data workbech and it requires a 

### Updating existing tables using overwrite
For existing tables that are synchronized between Databricks and Data Workbench, you can directly overwrite the table using Spark's write methods.

```py
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
```py
# Append new data to the existing table 
df.write.mode("append").saveAsTable("TableName")`
```

**Common modes:**
*   `overwrite`: Completely replaces the existing table
*   `append`: Adds new rows to the existing table
*   `ignore`: Skips insertion if data already exists
*   `error`: Raises an error if data conflicts (default behavior)


### Create new tables in databricks
New datasets can be created from Databricks and synchronized with Data Workbench. This is especially useful for data transformations (medallion architecture). For creating new tables in Databricks that need to be synced to Data Workbench, use Veracity internal library named **dataworkbench** that comes pre-installed to the cluster. 

* Create a table in databricks and write that table to a new dataset, or
* Create a dataframe and write the dataframe to a new dataset in Data workbench 

In below example demo dataframe is written to dataset in Data Workbench using library "dataworkbench"

```py
import dataworkbench
df = spark.createDataFrame([("a", 1), ("b", 2), ("c", 3)], ["letter", "number"])
datasetName = "My dataset"
description = "a dataset description"
metadata = {"asset": ["123"], "level": ["Silver"]}

datacatalogue = dataworkbench.DataCatalogue()
datacatalogue.save(
    df,
    description.
    "Description",
    tags={"asset": ["123"], "level": ["Silver"]},
    schema_id="abada0f7-acb4-43cf-8f54-b51abd7ba8b1"  # Using an existing schema ID, if not provided a new schema is created
)
```
The code above will create a dataset with the existing schema id "current active version". 
If schema_id is not provided, a new schema will be created based on the definition in the table.

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
```
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
```
tenantId = "DNVES"
siteId = SITE_ID  (get from variable)
subscriptionKey = SUBKEY
queryurl = f"https://api.veracity.com/veracity/mms/query/{tenantId}/api/v1/sites/{siteId}"

header = {"Authorization": f"Bearer {access_token}", "Ocp-Apim-Subscription-Key": subscriptionKey,
          "Content-Type": "application/json"}
response = requests.get(queryurl, headers=header)

```

### Get devices 
```
tenantId = "DNVES"
siteId = SITE_ID  (get from variable)
subscriptionKey = SUBKEY

queryurl = f"https://api.veracity.com/veracity/mms/query/{tenantId}/api/v1/sites/{siteId}/devices?start=0&pageSize=1000&sortColumn=Description&sortDirection=0&productTypeFilter=Inverter"

header = {"Authorization": f"Bearer {access_token}", "Ocp-Apim-Subscription-Key": subscriptionKey,
          "Content-Type": "application/json"}
response = requests.get(queryurl, headers=header)
```

