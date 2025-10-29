---
author: Veracity
description: This page explains how to utilize the analytics capabilities
---

# Connectivity to other datasources

## Migrate into datalake

Recommended approach is to ingest data to Veracity datalake using apis or SAS keys. These data are then available directly for Analytics:
-Datasets are visible as Tables in Databricks Catalog
-Filestorage as Volume/Filestorage in Databricks Catalog


## Share from another workspace
If the data you want access to from Analytics is not in the related Data Workbench workspace, but in another workspace in Veracity Data platform then sharing is recommended. Set up a share on workspace level from one Veracity workspace to another (B2B sharing). If Workspace B has analytics enabled and when sharing on workspace level from workspace A to Workspace B; data from workspace A is available in Databricks catalog.  Note: Currently this applies to datasets only. Shaerd files from Filestorage needs to be accessed using SAS-keys.

Shared datasets are available in the Analytics Environment as a Table. Shared files will soon be available.

Connect to data using SAS key is also possible

For more [details about sharing of datasets](../datasharing.md)

## Access single file using SAS key
Data from other storage containers can be accessed from Analytics using SAS key. See how to [generate SAS key from the portal](https://developer.veracity.com/docs/section/dataworkbench/filestorage/ase#to-generate-a-sas-token). SAS-keys can also be generated using the api-endpoint.

```
from urllib.parse import urlparse, parse_qs
#the complete sas key from dataworkbench - should be stores as secret
dfs_url = "https://prdstorageconst01weu.dfs.core.windows.net/......"

parsed = urlparse(dfs_url)
sas_token = parsed.query  # everything after '?'
storage_account = parsed.hostname.split('.')[0] 
container = parsed.path.split('/')[1]  
file_path = '/'.join(parsed.path.split('/')[2:]) 

print(sas_token)
print(storage_account)
print(container)
print(file_path)

spark.conf.set(
    f"fs.azure.sas.{container}.{storage_account}.blob.core.windows.net",
    sas_token
)

# Build abfss:// path
abfss_path = f"wasbs://{container}@{storage_account}.blob.core.windows.net/{file_path}"
 
# Load CSV file with Spark
df_spark = spark.read.csv(abfss_path, header=True, inferSchema=True)
 
# Display the Spark DataFrame
df_spark.display()

```

## Access folder using SAS key

```
from urllib.parse import urlparse, parse_qs
from pyspark.dbutils import DBUtils

#the complete sas key from dataworkbench - should be stores as secret
dfs_url = "https://prdstorageconst01weu.dfs.core.windows.net/......"

parsed = urlparse(dfs_url)
sas_token = parsed.query  # everything after '?'
storage_account = parsed.hostname.split('.')[0]  
container = parsed.path.split('/')[1]  
folder_path = '/'.join(parsed.path.split('/')[2:])  

print(sas_token)
print(storage_account)
print(container)
print(folder_path)

# Set Spark config for abfss
spark.conf.set(
    f"fs.azure.sas.{container}.{storage_account}.blob.core.windows.net",
    sas_token
)

dbutils = DBUtils(spark)

files = dbutils.fs.ls(f"wasbs://{container}@{storage_account}.blob.core.windows.net/{folder_path}/")
for f in files:
    print(f.path)
    # Load CSV file with Spark
    df = spark.read.csv(f.path, header=True, inferSchema=True) 
    # Display the Spark DataFrame
    df.display()
    
```

## How to connect existing databases:

Recommended approach is to migrate these databases to managed datalake or SQL Warehouse in Veracity data platform

JDBC and ODBC: Databricks provides built-in integrations to many cloud-native data systems, as well as extensible JDBC support to connect to other data systems.  

The source system should be on Verit and Verit Networks to ensure connectivity.

If source system is not on Verit; the data can be queried using Rest-apis directly from Analytics environment

## Connectors

When datasets are available in Veracity Data platform through connectors, data is not ingested to the platform. For the analytics environment to be able to use these data, the data must be queried using the Veracity query apis.
