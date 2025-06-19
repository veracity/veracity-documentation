---
author: Veracity
description: This page explains how to utilize the analytics capabilities
---

# Configurations of Azure Databricks
Veracity supports several configurations of Azure Databricks 


## All purpose Compute
Provisioned compute used to analyze data in notebooks. You can create, terminate, and restart this compute using the UI, CLI, or REST API.

Default setup is: Standard_DS3_v2, 14-28 GB, 4-8 cores

## Jobs Compute Policy for Jobs & Pipeline Execution
Provisioned compute used to run automated jobs. The Azure Databricks job scheduler automatically creates a job compute whenever a job is configured to run on new compute. The compute terminates when the job is complete. You cannot restart a job compute. See Configure compute for jobs.

To enable pipeline / jobs execution without granting automatic cluster creation privileges, 2 cluster policies are enabled.

1. VDP Multi Node Compute Policy
Node Type: STANDARD_DS3_V2
Maximum Instances: 2
No Init Scripts allowed

2. VDP Single Node Compute Policy
Node Type: STANDARD_DS3_V2
No Init Scripts allowed

