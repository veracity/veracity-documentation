---
author: Veracity
description: This is the changelog for the October 2022 release of Data Workbench.
---

# August 2022 release

Release date: 25 August 2022

Read this page to learn what changed in Veracity Data Workbench with the August 2022 release.

## New features

This section covers new features:
- [API integrations tab](#api-integrations-tab)
- [Endpoint for fetching data](#endpoint-for-fetching-data)
- [Add, update, and remove a service account](#add-update-and-remove-a-service-account)
- [New workspace and tenant picker button](#new-workspace-and-tenant-picker-button)
- [Data Catalogue: title bar with the back and action buttons](#data-catalogue-title-bar-with-the-back-and-action-buttons)

### API integrations tab

Now, at the top of the page, there is a tab called "API integrations" that lists service accounts in a workspace and lets you manage them. Thanks to this, you do not need to create a new resource in "My projects".
When you create an account in Data Workbench, you get:

- service account secret
- service account ID
- API key

Now, the values above have useful tooltips and "Copy" buttons.

For details, [see the documentation](apiintegrations.md).

For authorization and authentication for API calls, [see the documentation](authentication.md).

### Endpoint for fetching data

Now, you can query your data and specify custom columns, filters, and pagination. For instructions, [see the documentation](https://developer.veracity.com/docs/section/dataworkbench/apiendpoints#data-sets-endpoints).

### Add, update, and remove a service account

Now, an admin can add, update, and remove a service account. For instructions, [see the documentation](usermanagement.md).

### New workspace and tenant picker button

In the left corner of the "Home" page, an administrator can see a button for picking the tenant and the workspace.

Now, the button:

- In the left corner, displays an avatar with an abbreviated name of the tenant. To see the full name, hover over it. To go to the tenant, select it.
- Displays the name and the email address of the currently signed-in user.
- Displays the full name of the workspace.

If the workspace's name is too long, it will be shortened. To see the full name, hover over the button.

If you are a tenant admin, you can use the picker button to create a new workspace. To do so:

1. In the upper-left corner of the "Home" page, select the workspace and tenant picker button.
2. In the dropdown that appears, at the bottom, select the **Add workspace** button.

### Data Catalogue: title bar with the back and action buttons

Now, when you open a data set in the "Data catalogue" tab, at the top, there is a bar. The bar shows (from left to right):

- A back button (arrow icon).
- The title of a dataset.
- The data set info icon.
- The column picker for editing table properties.
- The filter icon for hiding or showing the filters. The filters show under the name of a data set or a template (for example, "Poseidon Principles Template").
- The save icon.
- The share icon for sharing data sets.

## Changes in existing features

This section covers changes in existing features:
- [Change data set title and description](#change-data-set-title-and-description)
- [Column picker changes](#column-picker-changes)
- [Icon tooltips updated](#icon-tooltips-updated)
- [Message and prompt when you have no data sets](#message-and-prompt-when-you-have-no-data-sets)
- [State of Compliance (SoC) files renamed](#state-of-compliance-soc-files-renamed)

### Change data set title and description

Previously, you could not change the title and description of a data set.

Now, you can do that. To change the title or description of a data set:

1. Open a data set.
2. In the upper-right corner of the row with the name of the data set, select the info icon.
3. Edit the dataset's name and/or description.
4. Select the **Save and close** button.

### Column picker changes

Previously, you could not hide and show the column picker for a data set.

Now, the column picker is hidden by default. To enable it:

1. Open a data set.
2. In the upper-right corner of the row with the name of the data set, select the pencil icon. It will enable the column picker.

Also, Data Workbench has added a button for deselecting all columns in a data set. To do so:

1. Open a data set.
2. In the upper-right corner of the row with the name of the data set, select the pencil icon. It will enable the column picker.
3. In the right corner of the page, under the columns, select the **Deselect all** button.
4. To refresh your data set, in the right corner of the page, select the "Update table" button.

### Icon tooltips updated

The icons within data sets, "Poseidon Principles" template, and "Sea Cargo Charter" template got new tooltip text that shows after you hover over an icon.

### Message and prompt when you have no data sets

Previously, if no data sets were available in your workspace, there was no message informing about that.

Now, Data Workbench displays a message in the "Home" tab and the "Data Catalogue" > "All data" > "Created data sets". The message also prompts you to use a predefined data set, modify it, and save it as a new data set you can use. Also, in "All data" > "Predefined data sets", there is a pop-up explaining how to use predefined data sets to create and share your new data sets.

### State of Compliance (SoC) files renamed

Now, when you download a State of Compliance (SoC) file, the name of the file follows the format "XXXXXXX; FOCR Statement of Compliance yyyy-mm-dd - yyyy-mm-dd.pdf" where:

- XXXXXXXX is replaced by the IMO Number of the vessel.
- yyyy-mm-dd is replaced by the start and end date for the verification period.

## Bugs fixed

This section covers bugs that have been fixed:
- [Unable to deselect properties in a data set](#unable-to-deselect-properties-in-a-data-set)
- [Blank workspace name](#blank-workspace-name)
- [Firefox: horizontal scroll bar under data properties](#firefox-horizontal-scroll-bar-under-data-properties)
- [No response when selecting some areas of the User predefined data set](#no-response-when-selecting-some-areas-of-the-user-predefined-data-set)
- [Data sets returning incorrect asset count](#data-sets-returning-incorrect-asset-count)

### Unable to deselect properties in a data set

Previously, when using the column picker to select columns for a dataset, you could not deselect columns to the far-right using the default screen size. Now, it is fixed.

### Blank workspace name

Previously, you could create a workspace with a blank space instead of a name. Now, this is impossible, and the name of the workspace should be between 1 and 100 characters.

### Firefox: horizontal scroll bar under data properties

Previously, in Firefox, a horizontal scroll bar was displayed under data properties in column picker. Now, it is removed.

### No response when selecting some areas of the User predefined data set

Previously, when selecting some areas of the "Use predefined data set" button, there was no response. Now, it is fixed.

### Data sets returning incorrect asset count

The "Data Catalogue" tab displays the "Available assets" column for each data set. This column shows the number of data rows in a data set. Previously, the "Available assets" count was always showing one irrespective of the number of data rows. Now, it is fixed, and the correct count is shown.
