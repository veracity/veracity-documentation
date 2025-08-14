---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Ingest and Transformation

The Veracity Data Platform supports flexible and secure data ingestion, enabling users to onboard both structured and unstructured data efficiently.

Structured data is ingested into Delta Lake as well-defined datasets. These datasets follow a predefined schema, allowing for validation and formatting during the ingestion process. This ensures data quality and consistency, making it ready for advanced analytics and reporting.

Unstructured data, such as documents, images, or logs, is ingested into file storage in its native format. This data is not processed during ingestion but remains accessible for downstream use cases such as AI, machine learning, or exploratory analysis.

**Data can be ingested via:**

* A user-friendly web portal, designed for intuitive interaction and governance.
* A REST API, enabling automated and programmatic data onboarding for integration with external systems and workflows.

This dual approach ensures that Veracity supports both interactive and automated data operations, empowering users to build insight-driven solutions while maintaining control over data integrity and access.


<figure>
    <img src="assets/structureddata.jpg"/>
    <figcaption>Structured and unstructured data storage</figcaption>
</figure>


## Schema
A schema defines the data model for a table (dataset), including the structure and the validation rules applied during data ingestion. These validation rules can be used to assess the integrity and format of incoming files, such as CSVs stored in File Storage, ensuring data quality and consistency.
[See schema management](https://developer.veracity.com/docs/section/dataplatform/schemamanagem)


## Transformation
Once data is ingested into the Veracity Data Platform—either as structured datasets in Delta Lake or as unstructured files in file storage—it can be further refined and transformed using the integrated analytics environment powered by Azure Databricks.

Data transformation may include:

* Cleansing: Removing inconsistencies or errors.
* Reformatting: Converting data into standardized formats.
* Aggregation: Summarizing data for reporting or analysis.
* Integration: Combining datasets from multiple sources to enrich context.

## How to

* [How to ingest structured data using apis](../storage/datasets.md)
* [How to ingest/upload files using apis](../storage/files.md)
* [How to upload data using Web portal (Data Workbench)](https://developer.veracity.com/docs/section/dataworkbench/datacatalogue)