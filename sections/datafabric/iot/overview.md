---
author: Benedikte Kallåk
description: This section is an overview of Veracity IoT.
---

# Veracity IoT

Veracity IoT is a managed service and infrastructure for handling high volume sensor data and aggregated data such as events.

## Sensor data
**Veracity IoT** supports continuous streams of high-volume timeseries data allowing remote monitoring of operations. 

## Events
Events are Veracity IoT provides real-time support for events such as system alerts, system events or user reporting. Event are less frequent and represents a change in state, an alarm, user logged information such as bunker delivery note.
An event can consist of several datapoints (attributes). The format of an event should be defined by its EventType.

<figure>
	<img src="assets/veracity-iot.png"/>
	<figcaption>Veracity IoT</figcaption>
</figure>

### Event Driven Architecture
**Veracity Event Broker** is a cloud based infrastructure enabling real-time access to data using the publish/subscribe pattern of event-driven architecture . The consumer can listen to events on their private queue for real-time access and use a rest api for historians.
An event-driven architecture uses events to trigger and communicate between decoupled services and is common in modern applications built with microservices.

## Main Features
* Ingest gateways for high volume sensors and events
* Secure storage
* Data permission and access rights
* Real-time support using subscription model
* Query Apis for data access
* Data quality service
* Timeseries and events explorer
* Connectors to major platforms
* Power Bi Connection
