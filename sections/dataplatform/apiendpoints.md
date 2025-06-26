---
author: Veracity
description: This page explains user management for a workspace in Data Workbench.
---

# Data platform APIs

|API| Note|Explore api|Base url|
|--|--|--|--|
| Data Workbench API | Storage, data query, validation and schema management |[Data workbench gateway api ](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json)|https://api.veracity.com/veracity/dw/gateway/api/v2|
| Asset Model Ingest |For updating asset metadata, assessments and portfolios| [Asset Model Ingest](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/DataFabric-MMS-Ingest-API-swagger.json)|https://api.veracity.com/veracity/mms/ingest|
|Asset Model Query| For query asset models, evaluationg rulesets | [Asset Model Query](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/DataFabric-MMS-Query-API-swagger.json)|https://api.veracity.com/veracity/mms/query|
|Asset Model Schema|For maintaining the standard and publish|[Asset Model Standard](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/DataFabric-MMS-Schema-API-swagger.json)|https://api.veracity.com/veracity/mms/schema|
|Eventbroker - Ingest|For event providers|[Eventbroker Ingest](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/DataFabric-IoTEventBrokerIngestAPI-swagger.json)|https://api.veracity.com/veracity/ioteventbrokeringest|
|Eventbroker - Query|For event consumers|[Eventbroker Query](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/DataFabric-IoTEventBrokerQueryAPI-swagger.json)|https://api.veracity.com/veracity/ioteventbrokerquery|
|IOT Query Proxy|For sensor data|[IOT Query](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/DataFabric-IoT-TimeSeriesAPI-V3-swagger.json)|https://api.veracity.com/veracity/|


## Response codes

You can get the following response codes when you send API calls:

* 200 code when the request was successful. Returns Query Data Found.
* 201 code when the resource was successfully created.
* 400 code for the invalid model. See schemas to find out the correct model to use in your API call.
* 401 code when you are unauthorized to access a resource.
* 404 code when the resource was not found.
* 500 code for an internal server error.
* 502 when you have called a bad gateway.
