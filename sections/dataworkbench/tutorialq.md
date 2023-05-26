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
{
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
} 
```

Below you can see an example of a successful response (code 200).

```json
    {
    "data": [

        {}

    ],

    "pagination": {

        "pageIndex": 1,

        "pageSize": 10,

        "totalPages": 10,

        "totalCount": 100

    }
}
```