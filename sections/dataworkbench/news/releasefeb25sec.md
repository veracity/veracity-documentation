---
author: Veracity
description: This is the changelog for the February 2025 second release of Data Workbench.
---

# February 2025 Data Validator release
Data Validator is a new feature that lets end-users to define their own data schemas and validation rules. This feature enables users to validate data files against the defined schemas and validation rules, ensuring data quality and consistency.

## Key capabilities
Learn what you can do with Data Validator.

### Create validation rules
   - Users can define custom validation rules by specifying conditions such as required fields, data types, thresholds, and more.
   - Validation rules can be configured with error, warning, or correction severity levels.

### Create schemas
   - Users can create new data schemas and define the structure, including columns and their properties.
   - Validation rules can be associated with specific columns within a schema.

### Connect validation rules to schemas
   - Users can easily connect the defined validation rules to the appropriate schemas.
   - This allows the validation rules to be applied during the data validation process.

### Set up folder validation
   - Users can configure specific folders in the Data catalogue to apply validation rules.
   - When files are uploaded to these folders, the data validation process will automatically run.

### Validate files
   - Users can upload data files to the configured folders, and the Data Validator will validate the data against the associated schemas and rules.
   - Validation results, including errors and warnings, are provided, and corrected data files are generated.

### API integration:
   - The OVD team can leverage the Data Map API and the new Data Validator UI package to integrate the validation functionality programmatically.
   - This allows for seamless integration with external systems and workflows.

### Known limitations
- The validation process may be impacted by large file sizes or complex validation rules. Users should consider these factors when designing their validation workflows.