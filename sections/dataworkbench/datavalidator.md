---
author: Veracity
description: This page contains an overview of Data Validator.
---
# Data Validator
Data Validator is a powerful tool designed to help users ensure the quality and integrity of their data. It allows you to perform a variety of checks on your datasets, such as validating data types, checking for missing values, verifying data formats, and more. By using Data Validator, you can quickly identify and address issues in your data before they impact your analyses or applications.

This guide will walk you through the features of Data Validator and provide step-by-step instructions on how to use them effectively. We will cover the following sections in the recommended order of use:

1. [Getting Started with Data Validator](#getting-started)
2. [Loading Your Dataset](#loading-dataset)
3. [Setting Up Validation Rules](#setting-up-rules)
4. [Data Type Validation](#data-type-validation)
5. [Missing Value Detection](#missing-value-detection)
6. [Range and Constraint Checks](#range-checks)
7. [Format Validation](#format-validation)
8. [Executing the Validation](#executing-validation)
9. [Reviewing Validation Results](#reviewing-results)
10. [Exporting Reports and Taking Action](#exporting-reports)
11. [Conclusion](#conclusion)

## Getting Started with Data Validator
To use Data Validator, you must:
* Be a Data Workbench user.
* Have a File Storage license?
* Something else?

To activate Data Validator:
* Step 1?

**To open Data Validator**:
1. Go to Data Catalogue.
1. In the top right corner, select **Schema manager**.

## To create a validation rule
1. Select the **Validation rules** tab. 
1. In the top right corner, select **Create validation rule**.

## Loading Your Dataset

Before you can validate your data, you need to load it into Data Validator.

### Steps to Load a Dataset

- Step 1: Click on the "File" menu in the top-left corner.
- Step 2: Select "Open Dataset" or simply click the "Open" button on the toolbar.
- Step 3: In the file dialog that appears, navigate to the location of your dataset file.
  - Supported file formats typically include CSV, Excel (.xlsx), JSON, and XML.
- Step 4: Select your dataset file and click "Open".
- Step 5: The dataset will be loaded, and you will see a preview of your data in the workspace area.

### Example Scenario

*You have a CSV file named customer_data.csv containing customer information. You want to validate this data before using it in your CRM system.*

- Load customer_data.csv following the steps above.

## 3. Setting Up Validation Rules

Before running validations, you need to define the rules that Data Validator will use to check your data.

### Accessing Validation Rules

- Step 1: Click on the "Validation Rules" tab or menu.
- Step 2: You will see a list of available validation types that you can apply to your data.

### Defining Global or Column-Specific Rules

- You can set rules that apply to the entire dataset or specific columns.
- It is recommended to set up rules in the following order:
  1. Data Type Validation
  2. Missing Value Detection
  3. Range and Constraint Checks
  4. Format Validation

## 4. Data Type Validation

Ensuring that each column contains the expected data type is crucial for data integrity.

### Steps for Data Type Validation

- Step 1: In the "Validation Rules" section, select "Data Type Validation".
- Step 2: A list of columns from your dataset will be displayed.
- Step 3: For each column, specify the expected data type:
  - String/Text
  - Integer
  - Float/Decimal
  - Date/Time
  - Boolean
- Step 4: Optionally, set additional constraints like maximum length for strings.

### Example Scenario

*In customer_data.csv, the Age column should be an integer, and the Email column should be a string.*

- Set the Age column to Integer.
- Set the Email column to String with an optional maximum length of 255 characters.

## 5. Missing Value Detection

Identifying missing or null values helps you understand data completeness.

### Steps for Missing Value Detection

- Step 1: In "Validation Rules", select "Missing Value Detection".
- Step 2: Choose whether to check all columns or select specific ones.
- Step 3: Define what constitutes a missing value (e.g., empty cells, NULL, N/A).
- Step 4: Choose whether to allow or disallow missing values in each column.

### Example Scenario

*You want to ensure that the Customer_ID and Email columns have no missing values.*

- Select the Customer_ID and Email columns.
- Set missing values to Not Allowed.

## 6. Range and Constraint Checks

Validate that numerical values fall within acceptable ranges or meet specific conditions.

### Steps for Range Checks

- Step 1: Select "Range and Constraint Checks" from the "Validation Rules".
- Step 2: Choose the numerical columns you want to validate.
- Step 3: Define the minimum and maximum acceptable values.


- Step 4: Optionally, add custom constraints or expressions.

### Example Scenario

*The Age column should contain values between 18 and 99.*

- Select the Age column.
- Set the minimum value to 18 and the maximum value to 99.


## 7. Format Validation

Ensure that data matches a specific format, such as email addresses, phone numbers, or dates.

### Steps for Format Validation

- Step 1: In "Validation Rules", choose "Format Validation".
- Step 2: Select the columns that require format checks.
- Step 3: Specify the expected format using predefined patterns or regular expressions.
  - Common formats include:
    - Email Address
    - Phone Number
    - Date Formats (e.g., YYYY-MM-DD)
    - Custom Regular Expressions

### Example Scenario

*You need to verify that the Email column contains valid email addresses.*

- Select the Email column.
- Choose the Email Address format from the predefined options.

## 8. Executing the Validation

After setting up all your validation rules, you're ready to run the validation.

### Steps to Run Validation

- Step 1: Click on the "Validate" button, usually found at the top of the application or within the "Validation Rules" section.
- Step 2: Data Validator will process your dataset according to the rules you've defined.
- Step 3: A progress bar or indicator will show the validation status.

## 9. Reviewing Validation Results

Once the validation is complete, you need to review the results to identify and address any issues.

### Steps to Review Results

- Step 1: Upon completion, a "Validation Results" window or tab will open.
- Step 2: The results are typically categorized into:
  - Errors: Data that failed validation rules.
  - Warnings: Data that may be problematic but not necessarily incorrect.
  - Passes: Data that met the validation criteria.
- Step 3: Click on each category to view detailed records.
  - You can often sort or filter the results for easier analysis.

### Example Scenario

*You find that some records in the Email column failed the format validation.*

- Review the specific entries.
- Identify common issues (e.g., missing @ symbol, typos).

## 10. Exporting Reports and Taking Action

After reviewing the results, you may want to export the findings or take corrective actions.

### Exporting Validation Reports

- Step 1: In the "Validation Results" window, click on the "Export Report" button.
- Step 2: Choose the desired format (e.g., PDF, Excel, CSV).
- Step 3: Select the components of the report you wish to include (e.g.


, summary, detailed errors).
- Step 4: Save the report to your desired location.

### Taking Corrective Actions

- Option 1: Manual Correction
  - Edit the erroneous data directly within Data Validator if supported.
- Option 2: Export Error Records
  - Export the records with errors for correction in another tool.
- Option 3: Apply Auto-Corrections
  - Use Data Validator’s built-in auto-correction features if available.
    - For example, setting default values for missing data.

### Example Scenario

*You decide to export the error report and correct the Email entries in Excel.*

- Export the error records.
- Open them in Excel and correct the email addresses.
- Reload the corrected dataset into Data Validator and re-run the validation.

## 11. Conclusion

Data Validator is an essential tool for anyone looking to maintain high data quality standards. By following this guide, you should be able to:

- Load and prepare your dataset for validation.
- Define and apply various validation rules.
- Execute validations and interpret the results.
- Take appropriate actions based on validation outcomes.

Ensuring your data is accurate and reliable not only improves the quality of your analyses but also enhances decision-making processes. Don’t hesitate to explore advanced features of Data Validator, such as custom scripting, integration with databases, and automated scheduling of validations.

Additional Tips:

- Regular Validation: Incorporate data validation into your regular data management workflow.
- Stay Updated: Check for updates to Data Validator to access new features and improvements.
- Support Resources: Utilize tutorials, forums, and customer support provided by the Data Validator team for additional help.