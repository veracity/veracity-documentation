---
author: Veracity
description: This is the changelog for the April 2025 release of Data Workbench.
---

# Data Validator April 2025 release
Read this page to learn what has changed in Veracity Data Workbench's Data Validator feature with the April 2025 release.

## New features
This section covers new features.

### Added tags and Validation Information in Data Validator
Now, in File storage, when you open a folder with validation enabled:
- In the **Tags** column, you can see the tags associated with the schema used for validating a file or folder.
- If you are a workspace admin, you can remove and add the tags.
- You can select the three dots in the row with the folder's or file's name to open **Validation Information**.

Validation Information shows the following information:
- The folder's name.
- What schema is used for validation.
- What tags are assigned to this folder.

If you are a workspace admin, you can change the schema used for validation and add or remove the tags.

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

### Validation rule dialog improvements
We have improved the UI for the **Create Validation Rule** and **Edit Validation Rule** dialogs to enhance usability.

- 'Data Type' is now a mandatory field.
- The 'Data Type' dropdown includes more options:
  - New categories: **String**, **Date & Time**, **Number**, **Boolean**.
  - Added support for 'Date Only' and 'Time Only'.
- Input fields now dynamically adjust based on the selected data type.