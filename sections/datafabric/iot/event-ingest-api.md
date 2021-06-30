---
author: Benedikte Kallåk
description: This section describes the Event Ingest Api
---

# Ingest Alarms & Events to Veracity

Data is ingested into Veracity using API. 
- The api is accessible from [api-portal](https://api-portal.veracity.com/). 
- Select api: *Data Fabric IoT Event Ingest API*

## Authentication
Authorization: Use bearer-token
See how to authenticate for the api [click here]( authenticate-api.md).

## Security Model
Only users (incl. application credentials) that has access to an asset can ingest data to an asset.

## Setup
Before data can be ingested to Veracity the following must be done:
1.	Vessel must be registered by Veracity administrator
2.	You must have access to the assets you are ingesting data for


## Ingest event
- Url: https://api.veracity.com/veracity/ioteventsingest/api/v1/Event
- Authorization: Bearer token [click here]( authenticate-api.md)
- Ocp-Apim-Subscription-Key: from application client or B2C user
- The body contains the JSON message

Veracity support a topic-based events (reports) and have defined:
Only the content of BODY vary between the reports

- [Topology report](topology-message.md): Equipment with system data.
- [Health report](health-message.md): Status on equipment
- [Generic reports](generic-message.md): Use user-defined topic and ingest events using the generic Dataset format.

### Event topic
Topic is user-defined, and should be used in order for categorization and easy access

### Asset information
- Name
- Array of ids. I.e. Use schema IMO and imo no
- TimeStampUtc: Timestamp when message was sent from asset (Not when event happened)

### Header 
#### Event
        
- "EventId":  a unique id
- "TimeStampUtc": timestamp for event, UTC: format: "2021-04-06T14:22:48.950716+02:00"
- "TimeStampLocal": timestamp for event, localtime format: "2021-04-06T14:22:48.950716+02:00"
- "EventSource": name of source system
- "NumberOfBodyElements": Body is an array of equipment elements; no of these elements
- "ReportMethod": automatically or manual
- "TriggerType": regular_daily, regular_ etc (user defined)
- "OperatingMode": Sailing, other:
- "VoyageId":         
- "SourceId": Source system for GEO position
- "Latitude": latitude for when event is sent
- "Longitude": 
- "Location": can be null. Name of port
- ReportedBy:         
    

#### Body
Body is an array of equipment elements containing 
- Id and 
- SystemData for Topology report, or 
- HealthData for health-reports, or 
- Dataset for generic events

##### Equipment Id
In order to standardize the naming of equipment, we propose to use the schema DNV-VIS and VIS codes from IMO19848.
            
- Schema: DNV-Vis
- Version: 3.3
- Code: unique VIS code for this equipment
- Name: name of equipment
- Custom: can be used to set custom classification using Class and Type
             