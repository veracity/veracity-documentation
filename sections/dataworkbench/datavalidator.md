---
author: Veracity
description: This page contains an overview of Data Validator.
---
# Data Validator
Data Validator is a powerful tool designed to help users ensure the quality and integrity of their data. It allows you to perform a variety of checks on your datasets, such as validating data types, checking for missing values, verifying data formats, and more. By using Data Validator, you can quickly identify and address issues in your data before they impact your analyses or applications.

This guide will walk you through the features of Data Validator and provide step-by-step instructions on how to use them effectively. We will cover the following sections in the recommended order of use:

## How to get started
To use Data Validator, you will need the following:
* A Data Workbench workspace in which you are workspace admin.
* A File Storage subscription.
* Subscriptions to Schema Management, Rule Management, and File Validation.
If you need help in getting them or checking everything is configured correctly, contact Data Workbench support.

## To access Data Validator
1. Sign into a Data Workbench workspace where you are an admin user.
1. Navigate to the **Data catalogue** page.
1. Select **Schema manager** in the upper right corner to access schema and validation rule management.
1. Navigate to **Data catalogue** > **File storage** to access File storage and validation setup.

## To create a new schema
1. In **Schema manager**, select **Create schema** in the upper right corner.
1. Fill in the **Name** and, optionally, **Short name** for the schema. Choose descriptive names that reflect the data you will be working with.
1. Optionally, under **Description**, describe the purpose of this schema and its intended use.
1. Select Add column to define a column.

### To define a column
For each column:
1. Fill in the **Name (internal name)**: this is a required field and should be unique within the schema. It's used for referencing the column in expressions or code.
2. Fill in the **Display name (user-friendly name)**: this is how the column will be presented in the user interface. It's limited to 100 characters.
3. Optionally, add a **Description**: for the column to provide more context. Select **Add** to expand the description field.
4. Select the appropriate **Data Type**: (for example, Boolean, Decimal, Int64) from the dropdown menu. This defines the kind of data the column is expected to hold.
5. Set the **Order** of the column in the dataset. '0' means it will be the first column.
6. Configure the column properties using the toggles:
   - **Sortable**: Enable if you want users to be able to sort the data by this column.
   - **Filterable**: Enable if you want users to be able to filter the data based on this column's values.
   - **Required**: Enable if the column must have a value for every row in the dataset.
7. Select the **Meta type**: for the column. Choose **Validation** if you want to apply validation rules to this column. Other meta types might be available depending on your Data Validator setup.
8. If you selected **Validation** as the Meta type:
   - Select a **Validation rule**: from the dropdown menu. This dropdown will list the validation rules that you've already created in your workspace. You can use the filter to search for specific rules by name.
9. Select the **Severity level**: from the dropdown menu:
   - **Correction**: If the data doesn't match the rule, it will be automatically corrected using the Fallback value defined in the validation rule.
   - **Error**: If the data doesn't match the rule, the entire row will be flagged as an error and potentially removed from the dataset, depending on how you're using Data Validator.
   - **Warning**: If the data doesn't match the rule, the row will be flagged as a warning, but it will still be kept in the dataset.
10. Select **Add**: to associate the selected validation rule and severity with the column. You'll see the added rule below.
11. Repeat steps 3-4 for all columns in your data.
12. Select **Save**: A toast message will confirm successful saving.
13. Select the newly created **schema**: to open Schema details.

## To create validation rules
1. **In Schema manager**: select the Validation rules tab.
2. **Select Create validation rule**: in the upper right corner.
3. **Fill in the Name**: for the validation rule (for example, "Required Email"). This is a required field and should be unique.
4. **Define the validation conditions**: You can use one or more of the following options:
   - **Data type (optional)**: Select the expected data type from the dropdown menu (for example, String, Integer, Boolean, Date). This is optional; if not specified, the data type will not be checked during validation.
   - **Min length (optional)**: Enter the minimum allowed length for string values. This field is only applicable if you've selected "String" as the data type or haven't specified a data type.
   - **Max length (optional)**: Enter the maximum allowed length for string values. This field is only applicable if you've selected "String" as the data type or haven't specified a data type.
   - **Min (optional)**: Enter the minimum allowed numerical value. This field is only applicable if you've selected a numerical data type (Integer, Float, etc.) or haven't specified a data type.
   - **Exclusive min**: Select "Yes" if you want the minimum value to be exclusive (meaning values equal to the minimum are invalid). Select "No" if you want the minimum to be inclusive. This field is only relevant if you've provided a "Min" value.
   - **Max (optional)**: Enter the maximum allowed numerical value. This field is only applicable if you've selected a numerical data type (Integer, Float, etc.) or haven't specified a data type.
   - **Exclusive max**: Select "Yes" if you want the maximum value to be exclusive. Select "No" if you want it to be inclusive. This field is only relevant if you've provided a "Max" value.
   - **Pattern (optional)**: Enter a regular expression to define an allowed pattern for string values (for example, for validating email or phone number formats). This field is only applicable if you've selected "String" as the data type or haven't specified a data type.
   - **Enum (optional)**: Enter a comma-separated list of allowed values. For example, you might enter "US, CA, MX" for a country code field. This field is useful for restricting values to a predefined set. Select Add to add the enum values.
   - **Fallback value (optional)**: Enter a default value that will be used if the data fails validation and you've set the "Severity" to "Correction" when applying the validation rule to a column. This is useful for automatically correcting invalid data. The information icon next to the field clarifies its function.
5. **Must not be empty**: Select "Yes" to specify that the field cannot be empty. This adds an implicit "Required" validation. Select "No" if empty values are acceptable.
6. **Error message**: Enter the message to be displayed if the data does not pass the validation. Be descriptive and user-friendly. Use magic numbers {0}, {1}, {2}, and {3} for dynamic messages (column name, value, row index, rule name).
7. Optionally, to cancel the changes, select Cancel.
8. To save the changes in the validation rule, select **Save**.

## To connect validation rules to a schema
1. In **Schema manager**, select the **pencil icon** next to your schema.
2. Select the **pencil icon** next to the column you want to validate.
3. In the **Meta type** dropdown, select **Validation**.
4. In the **Validation rule** dropdown, select the appropriate validation rule.
5. In the **Severity** dropdown, choose:
   - **Error**: The row will be removed if validation fails.
   - **Warning**: The row will be kept, but flagged.
   - **Correction**: The value will be replaced with the fallback value if validation fails.
6. Select **Add**. The rule will appear at the bottom.
7. Repeat steps 2-6 for all columns needing validation.
8. Select **Save** to save the schema with validation rules.

