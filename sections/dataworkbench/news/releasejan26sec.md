---
author: Veracity
description: This is the changelog for the January 2026 second release of Data Workbench.
---

# January 2026 second release
Read this page to learn what has changed in Veracity Data Workbench with the January 2026 second release.

## New features

### Support for Decimal precision and scale in schema columns
You can now define **Precision** and **Scale** when creating or editing schema columns of type Decimal.  
The UI displays numeric input fields for these properties and validates that the precision is between 1–28, and that scale does not exceed the precision.

## Changes in existing features

### Improvements to the Schemas list page
The Schemas list page has been updated:  
- Sorting is now applied by default on the schema name column (alphabetical).  
- The **Active version** column replaces the previous version column name.  
- Action buttons now show only when you hover over a row.

### Improvements to the Validation Rule page
Action buttons now show only when you hover over a row.

### Schema detail page layout refresh
The schema detail page has been redesigned for a clearer, more consistent editing experience:  
- After saving edits to a schema version, the page no longer jumps back to the Schemas list.  
- The page now uses a full‑screen layout with action buttons placed at the top.  
- Schema information and version details have been repositioned for easier navigation.

### Column table and row table updates
Several improvements were made to the column and row tables within the schema manager:  
- Action buttons are now located at the top of the table.  
- You can now toggle all properties on or off depending on what you want to view.  
- New search capabilities make it easier to find columns by name, display name, or row validation name.

### Updated API client
The Data Workbench now uses a new **OpenAPI‑generated** client library, replacing the previous Autorest‑based implementation.  

This update includes compatibility adjustments for client-side integrations and adopts versioning format **2.0.x**.

## Bugs fixed

### Default sorting issue in schema list page
A defect related to the default sort order on the schema name column has been addressed. Sorting now works as intended.
