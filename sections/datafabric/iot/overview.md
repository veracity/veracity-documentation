---
author: Veracity
description: Gives an overview of the Veracity IoT services and related components.
---

# Overview of  Veracity IoT
Veracity IoT is a managed service for handling sensor data and alarms & events. 
Veracity IoT sensor data handles continuous streams of high-volume timeseries data allowing remote monitoring of operations.
Veracity Alarams & Events handle event driven data. Events can be triggered by various systems based on sensor values, rules, etc. For instance, events are triggered only when sensors exceed a certain value. This will reduce data sent to shore; which is useful when bamdwidth is an issue.
Events can also be manually triggered and be used to report any data.


# Modules in Veracity IoT
It consists of several modules:

- Sensor data support
- Alarms and Events support
- Ingest pipelines
- Storage
- Api for access
- Data quality service
- PowerBi connector
- Timeseries and alarams & events visualization

## ISO 19848 Standard
ISO 19848 naming standard is used in both Sensor data and event handling.

ISO 19848 format of messages is supported for both ingest and egest of sensor data.


## Ingest sensor data
Datpoints can be streamed into Veracity IoT hub or ingested from CSV files.


## APIs at core

Access your data directly from our REST api.

## Contextualization
Sensor data is contextualized with meta data defined for the sensor as well as a location in an asset functional hierarchy. For maritime assets; DNVGL VIS structure is being used.


## Combine data with world class analytics tools
Veracity Power BI conenctor allows you to access the Veracity IoT ApI directly from Power Bi using Veracity authentication.

## Security and data protection
Only users with access to asset and permission to defined dataset can access sensor data. A dataset is a set of channels (sensor tags).

