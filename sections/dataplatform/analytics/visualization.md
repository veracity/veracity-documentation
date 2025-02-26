---
author: Veracity
description: This page explains how to utilize the analytics capabilities
---

# Visualize analytic results

## Visualization in Databricks
Databricks has built-in support for charts and visualizations in both Databricks SQL and in notebooks. 

[Visualizations in Databricks notebooks](https://docs.databricks.com/aws/en/visualizations/)

[Visualization in Databricks SQL](https://docs.databricks.com/aws/en/sql/user/visualizations/)
	
However, these results can not be shared with users outside dnv.

## Visualization using Power BI from Dataworkbench

Analytics can write their output to a dataset in data workbench and all files written will be available.
Power BI can connect to a dataset or to a file in filestoage and a report can be developed.
Veracity Adapter for PowerBI (VAP) can be used to distribute the report to the external customers.

You can see the new dataset in the same workspace you executed the script of Dataworkbench UI.
<figure>
	<img src="../assets/pythonexecution-datasets.png"/>
</figure>


