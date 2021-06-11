---
author: Benedikte Kallåk
description: Description of quick start section
---

# Alarms & Events
Veracity Alarams & Events handle event driven data. Events can be triggered by various systems based on sensor values, rules, etc. For instance, events are triggered only when sensors exceed a certain value. This will reduce data sent to shore; which is useful when bamdwidth is an issue.
Events can also be manually triggered and be used to report any data.

Each event contains more data (metadata) than sensor data. Each event contains information about voyage, position and untis used. This simplifies the use og this data such as 3rd party analytics.

## Event types
Veracity support a topic based events and have defined:

- Topology report: Equipment with system data
- Health report: Status on equipment
- Generic reports: Use dataset to ingest events
