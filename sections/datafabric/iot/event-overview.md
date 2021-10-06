---
author: Benedikte Kallåk
description: Description of quick start section
---

# Events
Veracity Events handle event driven data. Events can be system alerts, system events or user reporting. 
System events can be triggered by various systems based on sensor values, rules, etc. I.e., events are triggered only when sensors exceed a certain value. 


## Contextualization
All events should refer to a reference model of the asset. The reference model (codebook) describes the categorization of the asset. I.e. the functional hierarchy and/or components. 
Data Channel is a concept that represents virtual data transmission channels. A DataChannelId refers to an identifier in the used reference model (codebook) and is used to 
contextulaize the event to the correct location in the assetmodel (digital twin).
ISO 19848 Annexes B and C,described two types of categorising rules and example of the codebooks JSMEA and VIS. These are not designed to unify Data Channel ID and Veracity can support any codebook. 
Each event refers to a datachannelid which represents the events reference to the asset categorization. This reference can be to spesific equipment or operational event.


## Event types
Events are defined by templates and Veracity allows ingest of any event template. 
A specialized event is the the equipment event that allows for topology inserts and updates as well as health messages.

Examples of events:
- BunkerDeliveryNote
- Voyage updates
- Equipment readings
- Observation


