---
author: Benedikte Kallåk
description: This section describes the context.
---

# Contextualization

A digital twin represents a digital model of the asset using a reference model (codebook) describing a categorization of the asset such as a functional hierarchy as well as the naming scheme for identifying each item.  ISO 19848 (Annex B and C) describes two types of categorizing or identification schemas (JSMEA and VIS).  
Vessel Information Structure (VIS) is DNV’s logical structure of ship functions as well as components and systems used on the ship. VIS supports tools for compiling unique name-strings for sensors installed on ships. In the future other identification schemas (naming rules) may also be introduced in the ISO 19848 standard. 
All sensors and event types should be named according to a naming-standard described in a chosen virtual reference model of the asset. 

Data Channel is a concept that represents virtual data transmission channels such as sensor-data or events. A Data Channel is composed of Data Channel ID and Data Channel Property. Data Channel ID uniquely identifies the logical data channels according to naming schema whereas Data Channel Property defines attributes (metadata) of the Data Channel. 

Connecting all data related to an asset to such a reference model, provides context to the data and enables data consumption (queries) based on standard naming instead of OEM-specific sensor names.

[More information about VIS/Gmod](https://vista.dnv.com/docs)
