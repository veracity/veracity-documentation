---
author: Veracity
description: This page explains how to utilize the analytics capabilities
---
# Using files and datasets from Data Catalog
All structured data (datasets) and all files stored in the Data Workbench workspace are available in the Databricks Catalog and can be processed. New datasets and files can be created and synched back to Veracity Data Workbench datalake. Databricks uses two primary securable objects to store and access data:

- **Tables** govern access to tabular data: This is were all datasets from your Veracity workspace will be listed. This includes shared datasets from other workspaces. New tables must be synched back to Datasets using workbench library
- **Volumes** govern access to non-tabular data: This is where all files from Veracity filestorage is listed. **Note:** See exception for shared files/folders below. Same file storage used from Data workbenech, so no action needed to sync new files back to Data workbench.

## Read datasets
Datasets from Data workbench are automatically available as Tables in Azure Databricks.

Use Sql Editor or Notebook with Sql to query tables. To read dataset using python use table name from Catalog/Tables or from Widget

```python
dsName = dbutils.widgets.get("datasetName")
df2 = spark.table(dsName)

# example of sql query in python
query = f"select * from {dsName} where Value > 1000"
df = spark.sql(query)
```

When using sql, use IDENTIFIER(:widgetName) to get the datasetName
```
%sql
select * from IDENTIFIER(:inputDataset) where Value > 300
```

## Synchronize datasets
Datasets in Data workbench are synchronized into **Tables** in the Databricks environment. You can update existing tables in Databricks and then the dataset in Data workbench is automatically updated. When creating a new table in Databricks, it is *not* automatically synched back to Data workbech and it requires using **dataworkbench** library.

**Common modes:**
*   `overwrite`: Completely replaces the existing table
*   `append`: Adds new rows to the existing table
*   `ignore`: Skips insertion if data already exists
*   `error`: Raises an error if data conflicts (default behavior)


### Updating existing tables using overwrite
For existing tables that are already synchronized between Databricks and Data Workbench, you can directly overwrite the table using Spark's write methods.

```python
# Create a new DataFrame -
df = spark.createDataFrame([
    ("d", 1), 
    ("e", 2), 
    ("f", 5)
], ["letter", "number"])

# Overwrite the existing table
df.write.mode("overwrite").saveAsTable("TableNameOverwrite")
```

### Updating existing tables/datasets using append mode
When you want to add new rows to an existing table:

```python
# Append new data to the existing table 
df.write.mode("append").saveAsTable("TableName")`
```


### Create new tables and synch to Data Workbench
New datasets can be created from Databricks and synchronized with Data Workbench. This is especially useful for data transformations (medallion architecture). For creating new tables in Databricks that need to be synced to Data Workbench, use Veracity internal library named **dataworkbench** that comes pre-installed to the cluster. 

* Create a table in databricks and write that table to a new dataset, or
* Create a dataframe and write the dataframe to a new dataset in Data workbench 

In below example demo dataframe is written to dataset in Data Workbench using library "dataworkbench"

```python
import dataworkbench
tablename = "BKAL2003"
##Dataset name CANNOT be same as table name, since table already exists and hence will give an error when creating a table from DWB
datasetName = "BKAL2003_1"
description = "Some description"
metadata = {"asset": ["123"], "level": ["Silver"]}
schemaId= "<schema id>"

df_read = spark.read.table(tablename)
datacatalogue = dataworkbench.DataCatalogue()
datacatalogue.save(
   df_read,
   datasetName,
   description,
   tags= metadata,
   schema_id= schemaId # Using an existing schema ID   
)
```
The code above will create a dataset with the existing schema id "current active version". 
If schema_id is not provided, a new schema will be created based on the definition in the table.

## Read files from Volume
The choice between Pyspark or Pandas depends on the size and complexity of your dataset and the nature of your application. If you are working with small to medium-sized datasets, Pandas is a good choice. If you are dealing with big data or real-time processing, Pyspark is a better option. Pandas loads data in memory before running queries, so it can only query datasets that fit into memory. Spark can query datasets that are larger than memory by streaming the data and incrementally running computations

**Note:** openpyxl provides fine-grained control over reading and writing Excel files. The read_only mode significantly improves performance when reading large files. Read CSV is faster that reading XLSX

```python
import pandas as pd
inputfile = "voulume path - find file in Volume and get colume path"
#If reading from widget
#inputfile = dbutils.widgets.get("inputFileName")

pDf = pd.read_excel(inputfile, sheet_name="Sheet1") 
display(pDf)
```

## Synchronize files with Data workbench
There is no action required to synchronize files between Veracity data platform file storage and the Databricks environment. Files uploaded to Veracity data platform filestorage are visible in Databricks under Data Catalog/Default/Volumes. New files stored in Volume in databricks are visible in data platform file storage in same sub-folders.

## Write files to Volume
If creating a new file in Volume, you can create a new directory from workspace or from notebook

```python
import os
os.mkdir('/Volumes/<path>/default/filestorage/MyDir')

##outputfilename is stored in widget
filename = dbutils.widgets.get("outputfilepath")
df.to_csv(filename, index= False) 
```

