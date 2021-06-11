---
author: Benedikte Kallåk
description: Description of quick start section
---

# Alarms & Events
Veracity IoT sensor pipline handles continuous streams of high-volume timeseries data. Veracity Alrams & Events handle event driven data. 
These events can be triggered by systems based on sensor values, rules, etc. Events can also be manually triggered and be used to report any data. For instance, events are triggered only when sensors exceed a certain value. This will reduce data sent to shore; which is useful when bamdwidth is an issue.

Each event contains more data (metadata) than sensor data. Each event contains informationa bout voyage, position and untis used. This simplifies analytics of these data.

## Event types
Veracity support a topic based events and have defined:

- Topology report: Equipment with system data
- Health report: Status on equipment
- Generic reports: Use dataset to ingest events
