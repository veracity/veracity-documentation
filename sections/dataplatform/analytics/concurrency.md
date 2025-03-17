---
author: Veracity
description: This page explains how to utilize the analytics capabilities
---

# Multi users and concurrency

Veracity Analytics environment is a serverless compute enabled by Databricks.

Databricks offers built-in collaboration features, allowing multiple users to work on the same project concurrently. It also provides the ability to easily share and collaborate on notebooks and data. When multiple users are working on same workspace at the same time; you can see them as an icon in the top right and you should see their cursor in the file.

When multiple users run the same Databricks notebook, it is essential to follow best practices to avoid conflicts, ensure reproducibility and optimize resource usage.

## Execute Notebook as jobs
Notebooks running as jobs via scheduler or api execute independently, ensuring concurrency across different jobs.
Use %run

## Execute Notebook Interactively
Users running notebooks interactively share same cluster. If the cluster is overloaded, execution may queue of slow down.
If multiple users edit same notebook, the latest version overwrites previous changes.

### Best practices

**Use parameters to make notebook configurable**
Use widgets to allow users to input parameters at runtime without modifying notebook code to customize execution.

```python
dbutils.widgets.text("input_path", "/Volumes/vdp_dnves_advisory/default/filestorage/")
dbutils.widgets.text("datasetName", "")
dbutils.widgets.text("output1", "")
dbutils.widgets.text("output2", "")

```
You can choose to have default value.
When running the script interactively; change the values for the parameters using the UI (see parameters listed on top of the Notebook). This does not affect concurrent runs.

**Avoid hardcoded paths**
Stote temporary data in either user-specific folders or folders set by input parameters to avoid overwriting data

**Concurrent data modifications (tables or volume)**
Azure Databricks uses Delta Lake by default for all reads and writes and builds upon the ACID guarantees provided by the open source Delta Lake protocol. ACID stands for atomicity, consistency, isolation, and durability.

**Use Git for version Control**
Use Azure devops for version control of Databricks Notebooks , [for more details](devopsintegration.md)
