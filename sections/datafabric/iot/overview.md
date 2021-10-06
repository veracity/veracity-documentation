---
author: Veracity
description: Gives an overview of the Veracity IoT services and related components.
---

# Overview of Veracity IoT
Veracity IoT is a managed service for handling sensor data and other processed and aggregated data. 
- Veracity IoT sensor data handles continuous streams of high-volume timeseries data allowing remote monitoring of operations. 
- Veracity Events handle event driven data. Events can be system alerts, system events or user reporting. 
System events can be triggered by various systems based on sensor values, rules, etc. I.e., events are triggered only when sensors exceed a certain value. 


## Modules in Veracity IoT
It consists of several modules:

- Sensor data support
- Events support handling A&E and alerts
- Ingest pipelines
- Storage
- Query Api for data access
- Data quality service
- PowerBi connector
- Timeseries and events explorer

## Contextualization
All sensors and events should refer to a reference model of the asset. The reference model (codebook) describes the categorization of the asset. I.e. the functional hierarchy and/or components. 
Data Channel is a concept that represents virtual data transmission channels. A DataChannelId refers to an identifier in the used reference model (codebook) and is used to 
contextulaize the sensor value or event to the correct location in the assetmodel (digital twin).
ISO 19848 Annexes B and C,described two types of categorising rules and example of the codebooks JSMEA and VIS. These are not designed to unify Data Channel ID and Veracity can support any codebook. 

Sensor data also contextualized with meta data defined for the sensor such as units, range and remarks.


## ISO 19848 Standard
ISO 19848 naming standard is used in both sensor data and event handling.

ISO 19848 format of messages is supported for both ingest and egest of sensor data.


## Ingest sensor data
Datpoints can be streamed into Veracity IoT hub or ingested from CSV files.

## Ingest events
Events are ingested using Veracity api.

## APIs at core
Access your data directly from our REST api.

## Combine data with world class analytics tools
Veracity Power BI conenctor allows you to access the Veracity IoT ApI directly from Power Bi using Veracity authentication.

## Security and data protection
Only users with access to asset and permission to defined dataset can access sensor data. A dataset is a set of channels (sensor tags).

