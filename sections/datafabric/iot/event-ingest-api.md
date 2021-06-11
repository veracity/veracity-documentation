---
author: Benedikte Kallåk
description: Description of quick start section
---

# Ingest Alarms & Events to Veracity

Data is ingested into Veracity using API. 
The api is accessible from [api-portal](https://api-portal.veracity.com/). 

# Subscribe to API

Data can be accessed using Veracity IoT api. The API is managed by Azure API management and hence you need a subscription. 
1.	Go to Veracity api portal:[api-portal](https://api-portal.veracity.com/)
2.	Sign in
3.	Select Product
4.	Select Veracity Platform API. This api contains all the Veracity platform APIs which allow you to integrate with platform and enjoy the platform features by calling related API, it contains all the legacy "My service API" and "Data fabric API".
5.	Select Subscribe
6.	After subscription, your access keys are available from Products

# Run api from portal
1.	Go to Veracity api portal:[api-portal](https://api-portal.veracity.com/)
2.	Sign in
3.	Select "Data Fabric IoT Event Ingest API"
4.	Try It


To group the endpoints in api-portal, select the "group by tag" button.

## Security Model
Only users that has access to an asset can access data from this asset.

## Setup
Before data can be ingested to Veracity the following must be done:
1.	Vessel must be registered by Veracity administrator
2.	You must have access to the assets you are ingesting data for

## Authentication
You access the API either as a B2C user or with application credentials when invoking the api from code.

# Event types
Veracity support a topic based events and have defined:

- Topology report: Equipment with system data
- Health report: Status on equipment
- Generic reports: Use dataset to ingest events
