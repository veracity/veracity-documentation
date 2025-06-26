---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Storage

Data is stored in Azure Data Lake. The data is either stored as structured data using Delta tables or as unstructrured data using file storage.

## Structured data
Structured data is data that fits neatly into data tables and includes discrete data types such as numbers, short text, and dates. These data are called datasets.
When ingesting datasets, a pre-defined schema defining the columns for the structured data is required and the data is mapped and validated according to this schema.

-Easier querying and analytics: Structured data can be easily queries using sql-like queries from REST api or from Analytics environment.
-Better data integrity: Structured data enforces schema constrains ensuring data consistency

## Unstructured data
Unstructured data can be of any file format and includes all files like images, videos, PDFs, logs, text files, etc. Unstructured data does not require a schema to be defined. 

- High flexibility: Can store any format
- No predefined schema
- File storage can still be used for CSV files including file validation.

**You need subscription to File Storage to store unscructured data in Veracity**

## Scaling

Data Lake enables you to capture data of any size, type, and ingestion speed in one single place for operational and exploratory analytics. There is no limit to the amount of data you can store in a Data Lake Store account. Your Data Lake Store can store trillions of files where a single file can be greater than a petabyte in size.

It doesn't impose any limits on account sizes, file sizes, or the amount of data that can be stored in the data lake. Individual files can have sizes that range from a few kilobytes (KBs) to a few petabytes (PBs)

With Azure Data Lake Store you can analyze all of its data in a single place with no artificial constraints.

## Retention
It is possible to specify number of days a file will be available in storage. Default is forever.
