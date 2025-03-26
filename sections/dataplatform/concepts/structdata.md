---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Structured and unstructured data
Structured data has a predefined data model and is formatted to a set data structure before being placed in data storage (using schema), whereas unstructured data is stored in its native format and not processed until it is used 


## Structured data
Structured data is data that fits neatly into data tables and includes discrete data types such as numbers, short text, and dates. These data are called datasets.
When ingesting datasets, a pre-defined schema defining the columns for the structured data is required and the data is mapped and validated according to this schema.

* Easier querying and analytics: Structured data can be easily queries using sql-like queries from REST api or from Analytics environment.
* Better data integrity: Structured data enforces schema constrains ensuring data consistency


## Unstructured data
Unstructured data can be of any file format and includes all files like images, videos, PDFs, logs, text files, etc. Unstructured data does not require a schema to be defined. 

* High flexibility: Can store any format
* No predefined schema
* File storage can still be used for CSV files including file validation.


## Schema
A schema defines the model for the data in a table.

[See schema management](https://developer.veracity.com/docs/section/dataplatform/schemamanagem)


## Catalogue
The Data catalogue within the workspace shows all schemas defined, and all data available within hte security boundary.