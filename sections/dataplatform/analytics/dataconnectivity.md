---
author: Veracity
description: This page explains how to utilize the analytics capabilities
---

# Connectivity to other datasources

Recommended approach is to ingest data to Veracity datalake using apis or SAS keys. These data are then available directly for Analytics.

## How to connect existing databases:

Recommended approach is to migrate these databases to managed datalake or SQL Warehouse in Veracity data platform

JDBC and ODBC: Databricks provides built-in integrations to many cloud-native data systems, as well as extensible JDBC support to connect to other data systems.  

The source system should be on Verit and Verit Networks to ensure connectivity.

If source system is not on Verit; the data can be queried using Rest-apis directly from Analytics environment

## Connectors

When datasets are available in Veracity Data platform through connectors, data is not ingested to the platform. For the analytics environment to be able to use these data, the data must be queries using the Veracity query apis.
