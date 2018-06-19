---
Title : "Databricks"
Author: "Brede Børhaug"
Contributors: ""
---

## Overview 
Assumption that you in addition to an Veracity Account, you have an Azure Subscription. If you dont have that, start for free at [Microsoft Azure](https://www.azure.com)

Quick-Start 

- [Get started with Databricks](#get-started-with-databricks)
- [Connect cluster to Veracity storage](#connect-cluster-to-veracity-storage)


## Get started with Databricks 
The following section will cover how to commision a Databricks cluster, and connect it to storage in Veracity.

### Commision a Databricks resource
Through the Azure portal you commision a new Databricks workspace, by clicking "Create a Resource", and search for Databricks. Fill out the fields, and click create. Depending on the Veracity container's location, one may choose the location which has the same location. Veracity operate in North Europe and East US.

![](https://veracityprod.blob.core.windows.net/static-documentation/databricks/CreateResource.JPG "Commision the Databricks resource")

When the resource is ordered, azure may take some minutes to get the clusters ready for you to use.

### Connect cluster to Veracity storage
When the Databricks cluster is ready, you can go to the resource in Azure, and click the "Launch Workspace" button. 

![](https://veracityprod.blob.core.windows.net/static-documentation/databricks/startCluster.JPG "Start Databricks")

Then do the following two steps:

1. Create a Databricks cluster. This might take up to 10 minutes. This is done by hitting the button on the right hand side:
![](https://veracityprod.blob.core.windows.net/static-documentation/databricks/CreateCluster.JPG "Create cluster")
The cluster may take up to 10 min to be provisioned.

2. Create a notebook and in the first cell, you must set up the access to the Veracity account using the Shared Access Signature(SAS) in the notebook, and it is done in the following way:

- First get a key to your container from the [https://data.veracity.com](Data Fabric)
- In the first line, you need to set up the connection:
```python
spark.conf.set(
  "fs.azure.sas.{YOUR CONTAINER NAME}.{YOUR STORAGE ACCOUNT NAME}.blob.core.windows.net",
  "{COMPLETE QUERY STRING OF YOUR SAS FOR THE CONTAINER}")
```

Do NOT include the curly braces { } in the container or storage account name in the above.  Container names look like "nameyoupickede5b7213560-bd24-4293-b7f0-87cde3e7c8ea". The storage account name looks like "eu1dnvglpstgcus0000b". Veracity storage account access keys begin with sv and end with rl, rwdl, etc. depending on the type of key.

- In next cell, read data from Veracity storage. In the following example, we read csv files:
```python
%python
df=spark.read.format("csv").option("inferSchema", "true").option("header", "true").load("wasbs://<here-write-container-reference>@ne1dnvglpstgcus0000b.blob.core.windows.net/<file-location>")
```
If your account key grants write permission, you can also write parquet files for faster loading later after reading the csv:

```python
%python
df.write.parquet("wasbs://<here-write-container-reference>@ne1dnvglpstgcus0000b.blob.core.windows.net/<file-location>"
```
 
## GitHub  
Follow our open projects related to ingest on https://github.com/veracity

## Stack Overflow
Stack Overflow is the largest, most trusted online community for developers to learn, share their programming knowledge. The Veracity developer team monitor Stack Overflow forumposts that include the tag Veracity Platform.

[Visit Stack Overflow](https://stackoverflow.com/questions/tagged/veracity+platform?mode=all)



## Video 

## Price model 
The price of Databricks is dynamic and a service provided and charged through Microsoft Azure. The billing will not be going through Veracity. Note that dependent on the use and scale of cluster there may be significant cost related to clusters.
 
 
