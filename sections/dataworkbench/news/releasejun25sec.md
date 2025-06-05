---
author: Veracity  
description: This is the changelog for the June 2025 API release of Data Workbench.  
---

# June 2025 API release

Read this page to learn what has changed in Veracity Data Workbench APIs with the June 2025 release.

These updates enhance how you manage schemas using the API by introducing support for key columns.

## New features

### Manage key columns via API

You can now set and retrieve the `"isKey"` property for schema columns using the Data Workbench API. This property marks a column as a key, which is important for enforcing row uniqueness and enabling row-level updates or deletions.

If `"isKey"` is set to `true`, the column is treated as a key. The value is optional and defaults to `null` if not specified.

**Note that** a key column should contain unique values to ensure that operations like row updates or deletions behave as expected.
