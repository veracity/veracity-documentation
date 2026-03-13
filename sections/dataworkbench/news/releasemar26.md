---
author: Veracity
description: This is the changelog for the second March 2026 release of Data Workbench.
---

# March 2026 second release
Read these release notes to learn what has changed in the second March release of Data Workbench.

## New features

### Approve or decline multiple data sharing requests
Users can request that data owners share datasets with them. Data owners or administrators review these requests in Data Catalogue > Requests > Requests awaiting your action.

You can now approve or decline multiple requests at the same time.

To handle multiple requests:

1. Go to **Data Catalogue**.
2. Open **Requests awaiting your action**.
3. Tick the box next to each request you want to process.
4. In the top-right corner of the page, select **Approve** or **Decline**.

This allows you to manage several data sharing requests in a single action.

## Changes in existing features

### Add a note when declining a data sharing request
When declining a data sharing request, you can now provide a message explaining the reason for the decision.

After selecting **Decline**, a confirmation dialog appears where you can enter a note. The requester receives this message so they understand why the request was not approved.

### Additional information when creating a workspace
Tenant administrators now see additional guidance when creating a new workspace that:
- Reminds them some features are added to a workspace on request (for example, File storage or Analytics).
- Adds a link to contact Support to add additional features (if the workspace requires them).

### Improved validation rule selection in schema editor
When editing a schema and selecting validation rules for a column, predefined and custom validation rules may have identical names, making it difficult to know which rule was created in your workspace (custom) and which was added by default (predefined).

Because of that, we have added a "Predefined" tag next to predefined rules.

### Removed columns from dataset list
In **Data Catalogue**, the dataset list previously included **Type** and **Source** columns.

These columns have been removed based on user feedback indicating that the information was not useful.

## Bugs fixed

### Corrected text in validation rule dialog

Fixed an issue where the **View validation rule** dialog displayed the word **“undefined”** below the **Max** header. The incorrect text has been removed.
