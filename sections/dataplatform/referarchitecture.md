---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Reference Architecture
Veracity consists of a collection of integrated capabilities. Based on the use case to be solved; we recommend different capabilities to be combined.


## Use case: Analytics on customer delivered data
In this use case, you build a service based on analytics. This use-case does not require any deployment.


|**Capability**| **Recommendation**|**Considerations**| 
|--|--|--|
|Veracity Idp|Yes.The analytic script use client id to access apis. User logs on to Veracity through the Data workbench portal | |
|Client id |Service account is setup in your workspace under API integration | | 
|Tenant/workspace setup in DWB| Create a workspace in your tenant. Invite users into this workspace| One tenant per customer| 
|Veracity Tenant Manager| | |
|Storage | Store data as structured data in Data lake | Predefined schemas |
|Ingest | Upload CSV files into DWB using api or through portal | Define schema | 
|Asset model|To model metadata about assets and its components (devices) | Does the site/asset already exist in Asset Registry | 
|Analytics|Upload analytics scripts into DWB | | 
|Trigger analytics|When datasets are uploaded, should analytics be triggered automatically | |  
|Visualize analytic results | DWB portal is used. Dataset  | | 

## Use case: Build Web-app with user login
In this use-case you build a separate web application that you host using GSS-IT or other host. The service can have internal storage, but uses Veracity Data platform for customer ingest of data.

|**Capability**| **Recommendation**|**Considerations**| 
|--|--|--|
|Veracity Idp|Yes. The user token aquired during logon, must be passed to the apis of the data platform| | 
|Tenant/workspace setup in DWB| Create a workspace in your tenant. Invite users into this workspace| One tenant per customer|
|Veracity Tenant Manager| | |
|Storage | Store data as structured data in Data lake | Predefined schemas  |
|Ingest | Upload CSV files into DWB using api or through portal | |
|Analytics|Secure integration with Databricks analytics environment | |
|Trigger analytics|Analytics can be triggered from your service using APIs or by events|Q3/Q4| 
|Presentation | Service reads datasets and visualize them| |

## Use case: Real time event handling   

In this use case, the service will react to received events immediately by constantly listening to an event queue (subscription) 

|**Capability**| **Recommendation**|**Considerations**| 
|--|--|--|
|Event broker|Yes|Provide body for the event ingest|
|Veracity Idp|Yes. Client ids can be used to access the event broker| | 
|Subscribe to events| Use azure functions| Can subscribe to all events or special topics| 

