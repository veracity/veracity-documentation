---
author: Benedikte Kallåk
description: Description of quick start section
---

# Alarms & Events
Veracity Alarms & Events handle event driven data. Events can be triggered by various systems based on sensor values, rules, etc. For instance, events are triggered only when sensors exceed a certain value. This will reduce data sent to shore, which is useful when bandwidth is an issue.
Events can also be manually triggered and be used to report any "event" from asset.

Each event contains more data (metadata) than what is typical for sensordata. Each event contains information about voyage, position and unit used. This simplifies the use og this data such as for 3rd party analytics.

Most events are related to equipment. Veracity supports the ISO 19848 standard for naming equipment using DNV's VIS schema.

For more details about [Veracity IoT Sensor data handling](overview.md)

## Event types
Veracity support a topic-based events (reports) and have defined:

- [Topology report](topology-message.md): Equipment with system data.
- [Health report](health-message.md): Status on equipment
- [Generic reports](generic-message.md): Use userdefined topic and ingest events using the generic Dataset format.
