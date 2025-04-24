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
If the data you want access to from Analytics is not in the related Data Workbench workspace, but in another workspace in Veracity Data platform then sharing is recommended. Set up a share on workspace level from one Veracity workspace to another (B2B sharing). If Workspace B has analytics enabled and when sharing on workspace level from workspace A to Workspace B; data from workspace A is available in Databricks catalog.

Shared datasets are available in the Analytics Environment as a Table. Shared files will soon be available.

Connect to data using SAS key is also possible

For more [details about sharing of datasets](../datasharing.md)

## Connect to stroage account using SAS key
Data from other storage containers can be accessed from Analytics using SAS key.

```
storage_account_name = "prdstorageconst01weu"
container_name = "container id" #same as workspace id in DWB
 
#If sas token received from DWB, only use part after '?'
sas_token = "sv=XXXXXX"

spark.conf.set("fs.azure.account.auth.type.prdstorageconst01weu.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.prdstorageconst01weu.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.prdstorageconst01weu.dfs.core.windows.net", sas_token)
 
#folder and file name
filename = "Test/DemoCustomerInput.csv" 
src_path = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/{filename}"
 
display(df)
```

## How to connect existing databases:

Recommended approach is to migrate these databases to managed datalake or SQL Warehouse in Veracity data platform

JDBC and ODBC: Databricks provides built-in integrations to many cloud-native data systems, as well as extensible JDBC support to connect to other data systems.  

The source system should be on Verit and Verit Networks to ensure connectivity.

If source system is not on Verit; the data can be queried using Rest-apis directly from Analytics environment

## Connectors

When datasets are available in Veracity Data platform through connectors, data is not ingested to the platform. For the analytics environment to be able to use these data, the data must be queried using the Veracity query apis.
