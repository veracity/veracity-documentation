---
author: Benedikte Kallåk
description: Gives an overview of the Veracity IoT services and related components.
---

# Enabeling real-time support
Veracity Events are based on an event-driven architecture enabeling services to be loosely coupled using a publish-subscribe mechanism where some function as data publishers and others as consumers. Consumers received events to their own private queue and do not need to poll an api to get latest events.

## Event types:
Veracity supports any event type by supporting customer specific event types (templates) and each event type consists of different datapoints by defining templates for these events/reports.  

Examples of event types:
* Log abstact (noon report)
* Bunker delivery note
* Voyage updates
* Equipment topology and equipment health reports
* Observation

