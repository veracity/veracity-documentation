---
author: Veracity
description: Gives an overview of the Veracity IoT services and related components.
---

# Overview of  Veracity IoT
Veracity IoT is a managed service for handling sensor data. It consists of several modules:
- Ingest pipeline
- Storage
- Api for access
- Data quality service
- PowerBi connector
- Timeseries visualization

## Ingest sensor data
Datpoints can be streamed into Veracity IoT hub or ingested from CSV files.


## APIs at core

Access your data directly from our REST api.

## Contextualization
Sensor data is contextualized with meta data defined for the sensor as well as a location in an asset functional hierarchy. For maritime assets; DNVGL VIS structure is being used.

## ISO 19848 format
ISO 19848 is supported for ingest of data. This format is also used by the rest-api.

## Combine data with world class analytics tools
Veracity Power BI conenctor allows you to access the Veracity IoT ApI directly from Power Bi using Veracity authentication.

## Security and data protection
Only users with access to asset and permission to defined dataset can access sensor data. A dataset is a set of channels (sensor tags).

