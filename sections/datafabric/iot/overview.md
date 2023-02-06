---
author: Benedikte Kallåk
description: Gives an overview of the Veracity IoT services and related components.
---

# Overview of Veracity IoT
Veracity IoT is a managed service for handling sensor data as well as processed and aggregated data such as events, alerts and reporting. 
- Sensor data: Veracity IoT supports continuous streams of high-volume timeseries data allowing remote monitoring of operations. 
Veracity supports several protocols for sensordata, such as ISO 19848, SpakplugB and Wits0/WitsML.
- Events: Veracity IoT supports events for less frequent data such as system alerts, system events or user reporting. 
System events can be triggered based on sensor values and rules such as when sensor readings exceed a certain value. 
User reporting combined with sensor readings supports log-abstracts that can be used for services such as MRV/DCS. Veracity supports any event type by supporting customer specific event types (templates).


## Contextualization
A digital twin represents a digital model of the asset using a reference model (codebook) describing a categorization of the asset such as a functional hierarchy as well as the naming scheme for identifying each item.  ISO 19848 (Annex B and C) describes two types of categorizing or identification schemas (JSMEA and VIS).  
Vessel Information Structure (VIS) is DNV’s logical structure of ship functions as well as components and systems used on the ship. VIS supports tools for compiling unique name-strings for sensors installed on ships. In the future other identification schemas (naming rules) may also be introduced in the ISO 19848 standard. 
All sensors and event types should be named according to a naming-standard described in a chosen virtual reference model of the asset. 
Data Channel is a concept that represents virtual data transmission channels such as sensor-data or events. A Data Channel is composed of Data Channel ID and Data Channel Property. Data Channel ID uniquely identifies the logical data channels according to naming schema whereas Data Channel Property defines attributes (metadata) of the Data Channel. 
Connecting all data related to an asset to such a reference model, provides context to the data and enables data consumption (queries) based on standard naming instead of OEM-specific sensor names.

[More information about VIS/Gmod.](../../datastandards/vesselinformationsystem.md)

## Supporting operational readiness
Operational data can be categorized into a) raw data (sensor data), b) operational events, system alarms and alerts as well as c) reports. 
- Sensor data consists of small data-packages (high volume) of timestamp, value and channel id (tag id). Veracity supports continuous stream as well as CSV import of sensor data.
- Events cover operational events, system events and alerts. Events does also have timestamp but can consist of several datapoints and aggregated values usually sent with lower frequency. 
- Reports are a type of event consisting of composite data-structures often with aggregated raw data as well as some metadata. These reports are delivered with timestamp at a low frequency. Equipment topology and equipment health reports can be shared with DNV class for digital assurance services such as eNaut and D-class. Bunker delivery notes and daily log abstract can be used for supporting automatic MRV/DSC reporting.


## Event types:
Veracity supports different event types, and each event type consists of different datapoints by defining templates for these events/reports.  

Examples of event types:
- Log abstact (noon report)
- Bunker delivery note
- Voyage updates
- Equipment topology and equipment health reports
- Observation

Rawdata, events and reports can be used by service specific applications, dashboards etc. if data owner has given consent for data sharing for each service using the data.

## Main Features
- Storage
- Data permission and access rights
- Query Api for data access
- Ingest gateways
- Data quality service
- PowerBi connector
- Timeseries and events explorer
- Connectors to major platforms


## Ingest sensor data
Datpoints can be streamed into Veracity IoT hub or ingested from CSV files.


## Ingest events
Events are ingested using Veracity event api.

## Connctors
Connectors already exist for platforms such as Kongsberg Maritime (Kognifai, Kims), Høeglund and Enamor.

## APIs at core
Access your data directly from our REST api.

## Security and data protection
Only users with access to asset and permission to defined dataset can access sensor data. A dataset is a set of channels (sensor tags).

