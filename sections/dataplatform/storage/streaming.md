---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Streaming

"Streaming" is a valuable additional feature which enhances and expands the capabilities of the Veracity Data Platform. It is built on top of and extends the functionality within the Data Workbench BYOD component (bring your own data). It is the successor to parts of the (now legacy) Veracity IoT Platform.

# What is Streaming Data?

"Streaming" data refers to continuous, real-time data which is generated, transmitted, processed and transmitted in a steady-flow. Such data is typically produced by sources such as sensors, control systems, IoT devices or telemetry from applications. It is delivered continuously rather than sent in batch uploads. 

Applications for such data could be monitoring systems, weather data, electric grid data or financial trading. 

Veracity is supporting the Maritime and Renewable Energy industries with the collection of such data and the further development/exploration of relevant use cases.


# Streaming Feature

The streaming feature of the Veracity Data Platform is designed to provide a managed solution to support the following needs:

- Continuous ingest of standardized data
- Long term storage of large and growing data sets (historian)
- Basic Query
- Data Sharing
- Connectivity with external analytics tools (e.g. Spark)

Additionally:

- Support migration path for customers of the legacy Veracity IoT platform (Time Series). Migration of customer data can be performed, subject to normal hourly rates.


## Setup an end-to-end working example:

* Enable set up of a streaming dataset with correct schema
* Send data
* Query data



| Step | Step Name | |
|--|--|--|
| 1 | Create Tenant | if not exist customer |
| 2 | Create Workspace | if not exist customer |
| 3 | Decide/Select | Choose standardised, or define your own (onboarding can help with that) |
| 4 | Install Custom Schema | onboarding |
| 5 | Create Dataset | onboarding |
| 6 | Send Data | <we will provide samples c#, nodejs, python> |
| 7 | Query Data | same as other datasets |



Links

https://learn.microsoft.com/en-us/python/api/overview/azure/event-hubs?view=azure-python
https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-dotnet-standard-getstarted-send
https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-java-get-started-send