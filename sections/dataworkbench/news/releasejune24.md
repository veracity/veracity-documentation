---
author: Veracity
description: This is the changelog for the June 2024 release of Data Workbench.
---

# June 2024 release

Read this page to learn what has changed in Veracity Data Workbench with the June 2024 release.

## Stream data sets
This release is for Veracity Data Platform and enables data streaming. The streaming feature expands upon the existing Data Workbench's BYOD (Bring Your Own Data) feature and succeeds Veracity IoT Platform, which became a legacy software.

Note that:
* Streaming is currently in the MVP (Minimum Viable Product) state.
* To start using data streaming, contact the [onboarding team](mailto:onboarding@veracity.com) for help with the setup or migration (if you are a Veracity IoT Platform customer).

### What is streaming data?
When you stream data, you send real-time data continuously, and the data is processed as it flows through the system. Streaming data is commonly used for real-time analytics, IoT devices, application telemetry, sensor data, and so on.

Veracity supports the Maritime and Renewable Energy industries by collecting such data and further developing and exploring relevant use cases.

### What does streaming feature do?
Streaming gives you a managed solution that supports the following needs:

* Continuous ingest of standardized data.
* Long-term storage of large and growing data sets (historian).
* Basic Query.
* Data Sharing.
* Connectivity with external analytics tools (for example, Spark).

Note that the streaming feature supports migrating customer data from the legacy Veracity IoT platform (Time Series) subject to standard hourly rates.

### Where can I learn how to stream data?
You can learn how to stream data [from the documentation](https://dev.azure.com/dnvgl-one/Veracity%20Data%20Platform/_wiki/wikis/Veracity-Data-Platform.wiki/10465/Streaming).


## New features
This section covers new features.

### Stream (append) data into a workspace data set
Now, you can stream (append) data to a data set in your workspace.

You can stream data using Azure IoT Hub (MQTT, AQMP, HTTPS) or Azure Event Hub (AQMP, HTTPS).

### Support for standardized ingest schemas for time-series data
Streaming supports standardized ingest schemas for time-series data.

### Support for Crimson and SparkplugB time-series protocols
Streaming supports Crimson and SparkplugB time-series protocols.