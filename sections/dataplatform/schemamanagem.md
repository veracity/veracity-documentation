---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Schema management
Datasets stored in a workspace in Data Workbench must be based on a schema. A schema is like the definition of a table defining the columns of the schema. Schemas can be created and managed in the portal or using APIs. You need to be Admin in workspace to modify a schema.

## Versioning
A schema can have several versions. When creating a schema, a first version is autoamtically created. Only one version can be active at one time.

## Schema API endpoints
To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json). **See section Schemas**

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](auth.md).

## Authenticate
### Get Veracity token for service principle/service account
Service Account Id (Client Id), secret and api key (subscription key) for your workspace are defined under tab API Integration in data Workbench Portal.

#### Python
```python
import requests
import json

# Token URL for authentication 
token_url = "https://login.microsoftonline.com/dnvglb2cprod.onmicrosoft.com/oauth2/token"
clientId =  <myServiceAccountId>
secret =   <myServiceAccountSecret>

# define the request payload    
payload = {"resource": "https://dnvglb2cprod.onmicrosoft.com/83054ebf-1d7b-43f5-82ad-b2bde84d7b75",
          "grant_type": "client_credentials",
          "client_id": clientId,
          "client_secret" :secret
          }
response = requests.post(token_url, data=payload)   
if response.status_code == 200:
        veracityToken = response.json().get("access_token")
else:
        print(f"Error: {response.status_code}")
```
#### C#
```csharp
using Newtonsoft.Json.Linq;
async Task<string> GetToken(string clientId, string clientSecret)
{
    var url = "https://login.microsoftonline.com/dnvglb2cprod.onmicrosoft.com/oauth2/token";
    var grant_type = "client_credentials";
    var resource = "https://dnvglb2cprod.onmicrosoft.com/83054ebf-1d7b-43f5-82ad-b2bde84d7b75";

    var postData = new Dictionary<string, string>
       {
           {"grant_type", grant_type},
           {"client_id", clientId},
           {"client_secret", clientSecret},
           {"resource", resource},
       };
    using HttpClient httpClient = new HttpClient();
    httpClient.BaseAddress = new Uri(url);
    HttpResponseMessage authResponse = httpClient.PostAsync(url, new FormUrlEncodedContent(postData)).Result;
    var result = await authResponse.Content.ReadAsStringAsync();
    var token = (string)Newtonsoft.Json.Linq.JToken.Parse(result)["access_token"];
   return token;
}
```

## Create a new schema
In the example below a schema is created with two columns. 
To define "rowValidators" in input payload - Validator must be subcribed to (Validation Rule Management).

**output**
Schema created with schema id and a schema version id. When creating a schema, the active schema Version 1 will also be created and the version name is '[Schema name] V1'. Note: When uploading a new dataset, schema version id is used [see how to upload dataset](https://developer.veracity.com/docs/section/dataplatform/storage/datasets#step-2-prepare-dataset-for-upload)

Configure each column by setting:
* **isSortable:** Enable if you want users to be able to sort the data by this column.
* **isFilterable:** Enable if you want users to be able to filter the data based on this column's values.
* **isRequired:** Enable if the column must have a value for every row in the dataset. This is a critical validation rule since missing a required column will cause validation to fail.

####  Python
```python
apiKey =  "<my api key>"
workspaceId = "<workspace id>"

base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
endpoint = f"/workspaces/{workspaceId}/schemas/add"
url = base_url + endpoint

headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": apiKey,
    "Authorization": f"Bearer {veracityToken}",
    "User-Agent": "python-requests/2.31.0"
}

payload = {
  "name": "Test Schema2",
  "shortName": "Test",
  "description": "some description",
  "columns": [
    {
      "name": "TS",
      "displayName": "Timestamp",
      "type": "DateTime",
      "format": "YYYY-MM-DDThh:mm:ss",
      "isRequired": True,  
      "isSortable": True,
      "description": "time stamp",
      "isFilterable": True,
      "isKey": True,
      "order": 0      
    },
    {
      "name": "Temp",
      "displayName": "Temperature",
      "type": "Decimal",
      "isRequired": True,  
      "isSortable": True,
      "description": "temp",
      "isFilterable": True,
      "isKey": False,
      "order": 1      
    }
  ]  
}
try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()   
    result = response.json()
    schemaId = result.get("id")
    schemaVersionId = result.get("schemaVersions")[0].get("id")

except requests.exceptions.RequestException as e:
    print(f"Error creating a schema: {e}") 
```

**Rule validation**
To set validation rules, subscription to Rule validation is required.
```json
"validations": [
   {
          "severity": "Error",
          "validatorId": "string"
   }
],      
"metaType": "Validation",
```

## Modify schema
When modifying a schema, you can set new name, description and short name using **Patch** endpoint.
To change the columns, you need to either add new schema version or modify columns in an existing schema version.

####  Python
```python
apiKey =  "<api key>"
workspaceId = "<workspace id>"
schema_id = "<schema id>"

base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
endpoint = f"/workspaces/{workspaceId}/schemas/{schema_id}"
url = base_url + endpoint

headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": apiKey,
    "Authorization": f"Bearer {veracityToken}",
    "User-Agent": "python-requests/2.31.0"
}

payload = {
  "name": "new schema name",
  "description": "new description",
  "shortName": "Test100"
}
try:
    response = requests.patch(url, json=payload, headers=headers)
    response.raise_for_status()   
    result = response.json()   
    print(result)  
except requests.exceptions.RequestException as e:
    print(f"Error updating schema: {e}")    
```

## Add new schema version
In this example, a new version of previos schema is created where a new column is added.
####  Python
```python
apiKey =  "<api key>"
workspaceId = "<workspace id>"
schema_id = "<schema id>"

base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
endpoint = f"/workspaces/{workspaceId}/schemas/schemaversions/add"
url = base_url + endpoint

headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": apiKey,
    "Authorization": f"Bearer {veracityToken}",
    "User-Agent": "python-requests/2.31.0"
}

payload = {  
  "schemaId": schema_id,
  "schemaVersionName": "Version 2",
  "description": "some description of version",
  "columns": [
    {
      "name": "TS",
      "displayName": "Timestamp",
      "type": "DateTime",
      "format": "YYYY-MM-DDThh:mm:ss",
      "isRequired": True,  
      "isSortable": True,
      "description": "time stamp",
      "isFilterable": True,
      "isKey": True,
      "order": 0      
    },
    {
      "name": "Temp",
      "displayName": "Temperature",
      "type": "Decimal",
      "isRequired": True,  
      "isSortable": True,
      "description": "temp",
      "isFilterable": True,
      "isKey": False,
      "order": 1      
    },
    {
      "name": "Wind",
      "displayName": "Wind",
      "type": "Decimal",
      "isRequired": True,  
      "isSortable": True,
      "description": "wind",
      "isFilterable": True,
      "isKey": False,
      "order": 2      
    }
  ]  
}
try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()   
    result = response.json()   
    print(result)
    schema_version_id = result
  
except requests.exceptions.RequestException as e:
    print(f"Error updating schema: {e}")
```
## Modify schema version
This is a PATCH operation. 
In this example, a column is removed from the schema_version from previous example.
####  Python
```python
apiKey =  "<api key>"
workspaceId = "<workspace id>"
schema_id = "<schema id>"
schema_version_id = "<schema version id>"

base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
endpoint = f"/workspaces/{workspaceId}/schemas/{schema_id}/schemaversions/{schema_version_id}"
url = base_url + endpoint

headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": apiKey,
    "Authorization": f"Bearer {veracityToken}",
    "User-Agent": "python-requests/2.31.0"
}

payload = {  
  "schemaId": schema_id,
  "schemaVersionName": "Version 2",
  "description": "some description of version",
  "columns": [
    {
      "name": "TS",
      "displayName": "Timestamp",
      "type": "DateTime",
      "format": "YYYY-MM-DDThh:mm:ss",
      "isRequired": True,  
      "isSortable": True,
      "description": "time stamp new desc",
      "isFilterable": True,
      "isKey": True,
      "order": 0      
    },  {
      "name": "Wind",
      "displayName": "Wind",
      "type": "Decimal",
      "isRequired": True,  
      "isSortable": True,
      "description": "wind",
      "isFilterable": True,
      "isKey": False,
      "order": 1      
    }
  ]  
}
try:
    response = requests.patch(url, json=payload, headers=headers)
    response.raise_for_status()   
    result = response.json()   
    print(result)
    schema_version_id = result.get("id")
  
except requests.exceptions.RequestException as e:
    print(f"Error updating schema: {e}")
```
## Set schema versions active
A schema can have one active version (i.e. the default version). When using Validator, this is the schema being used.

#### Python
```python
apiKey =  "<api key>"
workspaceId = "<workspace id>"
schema_id = "<schema id>"
schema_version_id = "<schema version id>"
base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
endpoint = f"/workspaces/{workspaceId}/schemas/{schema_id}/schemaversions/{schema_version_id}/activate"
url = base_url + endpoint

headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": apiKey,
    "Authorization": f"Bearer {veracityToken}",
    "User-Agent": "python-requests/2.31.0"
}

try:
    response = requests.post(url, json=None, headers=headers)
    response.raise_for_status()   
    result = response.json()   
    print(result)
  
except requests.exceptions.RequestException as e:
    print(f"Error activating schema: {e}")
```

## Modify schema version
This is a PATCH operation. 
In this example, a column is removed from the schema_version from previous example.
####  Python
```python
apiKey =  "<api key>"
workspaceId = "<workspace id>"
schema_id = "<schema id>"
schema_version_id = "<schema version id>"

## Get schema and versions
Only the active schema_version is listed with columns.
#### Python
```python
apiKey =  "<api key>"
workspaceId = "<workspace id>"
schema_id = "<schema id>"

base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
endpoint = f"/workspaces/{workspaceId}/schemas/{schema_id}"

url = base_url + endpoint

headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": apiKey,
    "Authorization": f"Bearer {veracityToken}",
    "User-Agent": "python-requests/2.31.0"
}
try:
    response = requests.get(url, json=payload, headers=headers)
    response.raise_for_status()     
    result = response.json()
      # get version id for first version
    version_id =   result.get("schemaVersions")[0].get("id")
    print(version_id)
except requests.exceptions.RequestException as e:
    print(f"Error fetching schema {e}")
```

## Lock schema version
A locked schema version can not be modified with PATCH and a new schema version needs to be created.

#### Python
```python
apiKey =  "<api key>"
workspaceId = "<workspace id>"
schema_id = "<schema id>"
schema_version_id = "<schema version id>"

base_url = "https://api.veracity.com/veracity/dw/gateway/api/v2"
endpoint = f"/workspaces/{workspaceId}/schemas/{schema_id}/schemaversions/{schema_version_id}/lock"
url = base_url + endpoint

headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": apiKey,
    "Authorization": f"Bearer {veracityToken}",
    "User-Agent": "python-requests/2.31.0"
}
try:
    response = requests.post(url, json=No```pythonne, headers=headers)
    response.raise_for_status()   
    result = response.getstatus_code()
    print(result)
except requests.exceptions.RequestException as e:
    print(f"Error locking schema: {e}")
```

## Rule validation
To set validation rules, subscription to Rule validation is required. [For more information about valuidator](https://developer.veracity.com/docs/section/dataworkbench/datavalidator)