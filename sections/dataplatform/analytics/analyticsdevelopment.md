---
author: Veracity
description: This page explains how to utilize the analytics capabilities
---

# Develop analytics scripts

## Upload analytics script to tenant

See how to [upload scripts from UI in data Workbench](https://developer.veracity.com/docs/section/dataworkbench/analytics)



## Connect to Asset model
How to connect to Asset model from Python
```Python
import requests
import json
import os

res = None
try:
  data = {'scope':'https://dnvglb2cprod.onmicrosoft.com/83054ebf-1d7b-43f5-82ad-b2bde84d7b75/.default',
          'grant_type': 'client_credentials',
          'client_id': os.environ["MMS_CLIENT_ID"],
          'client_secret' : os.environ["MMS_CLIENT_SECRET"]}
  auth = requests.post("https://login.veracity.com/dnvglb2cprod.onmicrosoft.com/b2c_1a_signinwithadfsidp/oauth2/v2.0/token"
  ,data= data) 
  token = auth.json()['access_token']
  res = requests.get(f"https://api.veracity.com/veracity/mms/query/dnves/api/v1/sites/{currentSiteId}",
        headers= {'Authorization': f'Bearer {token}','Ocp-Apim-Subscription-Key': os.environ["Ocp-Apim-Subscription-Key"]})
except Exception as e:
  print(e)

````

## Connect to datasets
How to use data from DWB in scripts
```Python
delta_table_path = f"abfss://{containerName}@{storageAccountName}.dfs.core.windows.net/{datasets}"
da= spark.read.load(delta_table_path)
currentSiteId = da.dropDuplicates(["SiteId"]).select("SiteId").collect()[0]['SiteId']

````
How to write data to DWB
```Python
get data from DWB
delta_table_path = f"abfss://{containerName}@{storageAccountName}.dfs.core.windows.net/{datasets}"
df = spark.read.load(path).toPandas()

delta_output_path = f"abfss://{containerName}@{storageAccountName}.dfs.core.windows.net/{outputFolderPath}"
# Write the output to the output path so as it will be converted to a dataset
df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").option("header","True").save(delta_output_path)
````

## Onoboard analytics
DWB supports two kind of scripts, workspace script and provider script. Users can upload workspace scripts on his/her own, but cannot upload provider script.

### Workspace scripts
```Python
import requests
import json
import pandas as pd
 
# containerName, storageAccountName, datasets and outputFolderPath are parameters passed to the script
# Do not override
 
 
# Read Datasets passed as input, dataset ids are comma seperated in case of multiple datasets
path = f"abfss://{containerName}@{storageAccountName}.dfs.core.windows.net/{datasets}"
 
# Write the output to the output path so as it will be converted to a dataset
delta_output_path = f"abfss://{containerName}@{storageAccountName}.dfs.core.windows.net/{outputFolderPath}"
 
df = spark.read.load(path).toPandas()
df['TS'] = pd.to_datetime(df['TS'])
 
 
# Get the site information from MMS API example to get site information for site :688e6e66-907a-4510-a60d-854125b41ff8
# kindly replace the placeholders with actual values
data = {'scope':"MMS_SCOPE",
          'grant_type': 'client_credentials',
          'client_id': "MMS_CLIENT_ID",
          'client_secret' : "MMS_CLIENT_SECRET"}
auth = requests.post("MMS_TOKEN_URL"
  ,data= data) 
token = auth.json()['access_token']
res = requests.get(f"{'MMS_API_URL'}/v1/sites/688e6e66-907a-4510-a60d-854125b41ff8",
        headers= {'Authorization': f'Bearer {token}','Ocp-Apim-Subscription-Key': "MMS_APIM_SUBSCRIPTION_KEY"})
siteinfo = res.json()
 
# Get the DC capacity from the site information
dc_cap = [item['value'] for item in  res.json()['metadata'] if item['name'] == 'CapacityDC'][0]
 
 
df_monthly = (df.resample("MS", on="TS")
        .agg(
            {
                "Energy": "sum",
                "GTI": "sum",
            }
        )
        .reset_index()
    )
 
df_monthly["TS"] = pd.to_datetime(df_monthly["TS"]).dt.strftime(
    "%m/%Y"
)
 
df_monthly['PR'] = 100*df_monthly["Energy"]/(dc_cap*df_monthly["GTI"])
 
 
# Write the output to the output path so as it will be converted to a dataset
spark.createDataFrame(df_monthly).write.format("delta").mode("overwrite").option("overwriteSchema", "true").option("header","True").save(delta_output_path)
````

### Provider scripts
Provider scripts are advanced and require folders of sub-scripts and additional files. Currently DWB Support needs to onboard the provider script.
User can cooperate with DWB Onboarding team to upload provider scripts. Provider scripts cannot be viewed and deleted in DWB UI.
