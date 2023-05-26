---
author: Veracity
description: This is a tutorial how to query data with Data Workbench.
---
# How to query for data?
If you want to query data, follow this tutorial for step-by-step instructions.

## Prerequisites
Prepare the folowing before calling the endpoint for querying data from a data set.

### Authenticate and authorize
Get your API key and a bearer token to authenticate and authorize your calls. See how to do it [here](authentication.md).

### Workspace ID

Find your workspace ID. To do so, see the URL of your workspace in a browser. The part after ```ws/```is the ID of your workspace.
<figure>
	<img src="assets/workspaceid.png"/>
	<figcaption>The image shows where to find the ID of your workspace.</figcaption>
</figure>

### Data set ID
Find the 'datasetId' for a data set you want to query:
1. In Data Workbench, go to **Data catalogue**.
2. Open a data set.
3. Copy the part of the URL after 'datasets'.

<figure>
	<img src="assets/datasetid.png"/>
	<figcaption>The ID of a data set .</figcaption>
</figure>

## To query a data set
To query for data by workspace ID, call the https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/datasets/{datasetId}/query endpoint. 

In the request, you must provide:
* API key and bearer token in the header of your call
* {workspaceId}
* {datasetId}

Below you can see an example of a request.

```json
"pageIndex": 0,
"pageSize": 0,
"columnFilter": [
"string"
],
"queryFilters": [
{
"column": "string",
"filterType": "string",
"filterValues": [
"string"
 ]
 }
],
"sorting": {
"column": "string",
"order": "Ascending"
}
```

Below you can see an example of a successful response (code 200).

```json
"data":[
{}
],
"pagination":{
"pageIndex":1,
"pageSize":10,
"totalPages":10,
"totalCount":100
}
```

## To add filters to data set query


You can add the following query filter operators to your query:
* List
* Equals
* Greater
* GreaterOrEqual
* Less
* LessOrEqual
* NonFromList
* StringContains

**Note that** not all columns are filterable and different columns may support different filters. So, check which filters are supported by the columns in your data set. 

You can do that by getting the default schema version with column information and information on supported query filters. To get it, call the `https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId}/schemas?includeDefaultSchemaVersion=true`.

Below you can see a sample response that tells which columns are filterable and what filter operators they support.

```json
"id": "7c31d976-4d3d-45ea-9234-12f238f7ceaa",
"workspaceId": "00000000-0000-0000-0000-000000000000",
"name": "Lorem ipsum name",
"description": "Lorem ipsum description", 
"schemaVersions": [
	{ "id": "89153dc4-2323-45c9-b70e-241503697315",
	"schemaVersionName": "DCS Period Summary v1",
	"description": "Lorem ipsum description",
	"columns": [
		{ "name": "IMO",
		"displayName": "",
		"type": "Int32",
		"description": "",
		"isFilterable": true, 
		"filterType": "List", 
		"filterTypes": [
			"List",
			"Equals"
		],
		"isSortable": true
		},
		{
			"name": "Vessel_Name",
			"displayName": "",
			"type": "String",
			"description": "",
			"isFilterable": false,
			"filterTypes": [],
			"isSortable": true
			},
			{
				"name": "Period_Start_Date",
				"displayName": "",
				"type": "DateOnly",
				"description": "",
				"isFilterable": true,
				"filterType": "From",
				"filterTypes": [
					"Greater",
					"GreaterOrEqual",
					"Less",
					"LessOrEqual"
				],
				"format": "YYYY-MM-DD",
				"isSortable": true },
				],
				"industry": "Maritime",
				"isPredefined": true,
				"avatarColor": 28,
				"createdBy": "c44e1e55-fa3a-4553-b974-87eb50e41da9",
				"createdOn": "2022-06-07T09:29:57.9584074Z",
				"lastModifiedBy": "c44e1e55-fa3a-4553-b974-87eb50e41da9",
				"lastModifiedOn": "2022-06-07T09:29:57.9584074Z"
			}
```