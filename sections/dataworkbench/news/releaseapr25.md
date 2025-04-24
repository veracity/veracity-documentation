---
author: Veracity
description: This is the changelog for the April 2025 release of Data Workbench.
---

# Data Workbench April 2025 release
Read this page to learn what has changed in Veracity Data Workbench's Data Validator feature with the April 2025 release.

## New features
This section covers new features.

### Added tags column
Now, in File storage, when you have a folder with validation enabled:
- In the **Tags** column, you can see the tags associated with the schema used for validating a folder.
- If you are a workspace admin, you can remove and add the tags by clicking on a tag and using the dialog window that shows.
<figure>
	<img src="../news/assets/tags.png"/>
</figure>

### Added Validation information
You can select the three dots in the row with the folder's name to open **Validation information** that shows:
- What schema is used for validation.
- What tags are assigned to this folder.
- The description of the validation.

If you are a workspace admin, you can change the schema used for validation, edit its description, and add or remove the tags.
<figure>
	<img src="../news/assets/validationinfo.png"/>
</figure>

## Changes in existing features
This section covers changes in existing features.

### Schema version locking
Now, if you are a workspace admin, you can lock a schema version to prevent further edits.

- When you edit a schema in Data Catalogue > Schema Manager > Schemas, you can use the **Lock this version** button, which is under **Versions** on the left side.
- This button is only available if the schema has been created in the current workspace.
- When you select **Lock this version**, a confirmation prompt informs you that:
  - Once locked, the schema version cannot be edited.
  - All fields and buttons related to editing will be disabled.
  - You can still create a new schema version and make edits there.
- Locking a schema does not affect whether it is active or inactive.

<figure>
	<img src="../news/assets/lockschema.png"/>
</figure>

### Validation rule dialog improvements
We have improved the UI for the **Create Validation Rule** and **Edit Validation Rule** dialogs to enhance usability.

- 'Data Type' is now a mandatory field.
- Input fields now dynamically adjust based on the selected data type.

### Running Analytics on Shared Datasets
The Data Workbench now supports sharing datasets, enabling users to execute Python code on shared datasets.

### Writing Back Data From Databricks to Dataworkbench

When integrating data from a Databricks environment back into Dataworkbench, we follow a structured approach based on the Medallion Architecture. This ensures data is processed in layers, improving quality, structure, and usability. The three stages are as follows:

1) **Bronze Layer** – Raw & Unstructured Data
This stage handles raw, unprocessed data, including unstructured and semi-structured formats.
Data can be read from or written to the filestorage volume in its native form (e.g., JSON, Parquet, CSV, Delta).
External tables can also reference this volume, providing direct access to raw data without transformation.
2) **Silver Layer** – Structured & Intermediate Processing
At this stage, data is refined and transformed into a structured format, making it easier to work with.
Users can create tables or save dataframes as tables, enabling optimized querying and processing.
This layer is particularly useful for joins, aggregations, and deduplication, serving as an intermediate storage before final synchronization.
3) **Gold Layer** – Optimized & Ready for Dataworkbench
The final stage prepares data for full integration into Dataworkbench.
Data must be stored in BYOD (Bring Your Own Data) storage, ensuring compatibility with Dataworkbench’s functionality.
Once in BYOD storage, users can leverage Dataworkbench’s full suite of capabilities, including data sharing, SAS token authentication, and UI-based data access.
