---
author: Veracity
description: This is the changelog for the February 2025 second release of Data Workbench.
---

# February 2025 Data Validator release
We are releasing Data Validator, a new feature for Data Workbench that empowers you to ensure the quality and consistency of your data through customizable validation rules and automated checks. This release streamlines data quality management, helping you identify and correct errors early in the data lifecycle.

## Key features 

*   **Flexible validation rules:** Define a wide range of validation rules based on data type, length, regular expressions, allowed values (enums), and more. Combine multiple conditions within a single rule for complex validation scenarios.
*   **Schema-level integration:** Connect validation rules directly to your data schemas, specifying the severity of validation failures (Correction, Error, Warning). Easily manage and reuse validation rules across different schemas.
*   **Automated file validation:** Set up automatic validation of files uploaded to designated folders in File Storage. Data Validator will process your data according to the defined rules and provide detailed reports.
*   **Row-level validation:** Implement validation rules that span multiple columns, ensuring data consistency across related fields. Use logical operators (AND, OR) to define complex dependencies.
*   **Schema versioning:** Manage different versions of your schemas, allowing you to track changes and easily revert to previous versions. Activate specific schema versions for validation.
*   **Fallback indicators:** Track which data points have been automatically corrected using fallback values. This provides transparency and auditability for your data validation process.

## Known limitations
The validation process may be impacted by large file sizes or complex validation rules. Users should consider these factors when designing their validation workflows.

## Documentation
[See Data Validator documentation](../datavalidator.md) for detailed instructions and examples.