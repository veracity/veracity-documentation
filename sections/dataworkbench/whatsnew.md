---
author: Veracity
description: Public changelog with important announcements.
---

# Data Workbench Changelog

This page contains changelog for Data Workbench.

## September 2022 release

Release date: September 2022

Read this page to learn what changed in Veracity Data Workbench with the September 2022 release.

### New features

This section covers new features.

#### Activity logs

The activity log provides transparency into what have happen to your data in a workspace. It provides information about who did something, to what data, which users and when it happen. This way a data set does not just go missing without a trace and you can also see how data is shared and revoked at different time, plus more. For details, [see the documentation](activitylog.md).

In later follow up, we will add filters, that really enables you to look into the data you are interested in.

### Changes in existing features

This section covers changes in existing features.

#### "Members" tab renamed to "Workspace"

The "Members" tab, located at the top of the page, has been renamed to "Workspace".

Now, to see workspace members:

1. In the workspace, go the **Workspace** tab.
2. In the left corner, go to the **Members** tab.

#### Added "Activity log" tab

Now, when you go the "Data Catalogue" or "Workspace" tab, you will see a new sub-tab called "Activity log".

#### Better filter handling

Improved handling for working with apply and clear filters for data set details, SCC and Poseidon page.

- "Clear filter" button will be hidden when the filter is not set yet
- "Apply" button will be disabled when the filter is not set
- A button called "Clear filters" was added to clear all the filters

#### Prompt before leaving unsaved changes

Now you will be prompted if you have unsaved changes and try to leave the data set details page.

#### API integrations improvements

1. In the service account list, updated the mouse hover state to be less intrusive
2. Moved the **“+ Add account”** button to the top of the service account list and make it always visible
3. In the service account list, scroll to the newly created account while creating

#### Calendar improvements

The calendar is part of different filters in the application.

1. In SCC and Poseidon page, add visible indication of which dates have available data for them
2. Added input field, making it possible to manually enter a date
3. The calendar always will have the same height, for easier browsing
4. In SCC and Poseidon page, enforce date ranger behavior, disallowing selecting a from date that is later than a to date

#### Misc other changes

1. In create dataset, workspace and service account name input fields, add letter counter and max length indicator
2. Classification status will now refetch and update the classifications even if the user is idle in the page
3. In data catalogue page, add sticky headers and scrollbar making them always visible and available
4. Add native tooltip for all data that can overflow. This way you can hover any data to see the full content.
5. In the data set list, remove the superficial “assets” word in the rows. It already says “available assets” in the header
6. Data set name is limited to 64 in order to align with Data Fabric

### Bugs fixed

This section covers bugs that have been fixed.

1. Fixed columns are not evenly spread across rows in column picker for readers
2. Margin in navigation tabs are not consistent in different page
3. Fixed spin box displaying during saving dataset is truncated
4. Page goes to unexpected page after click "back" button in browser
5. Better handling of longer data set names
6. Firefox: Fixed operation icons are not displayed when mouse hovering on data set record
7. Decrease the margin between dataset list table and the end border of page
8. Scrollbar is displayed on Create new data set dialog box
9. Fix gap between title and filters for Poseidon and SCC templates

## August 2022 release

Release date: 25 August 2022

Read this page to learn what changed in Veracity Data Workbench with the August 2022 release.

### New features

This section covers new features.

#### API integrations tab

Now, at the top of the page, there is a tab called "API integrations" that lists service accounts in a workspace and lets you manage them. Thanks to this, you do not need to create a new resource in "My projects".
When you create an account in Data Workbench, you get:

- service account secret
- service account ID
- API key

Now, the values above have useful tooltips and "Copy" buttons.

For details, [see the documentation](apiintegrations.md).

For authorization and authentication for API calls, [see the documentation](authentication.md).

#### Endpoint for fetching data

Now, you can query your data and specify custom columns, filters, and pagination. For instructions, [see the documentation](https://developer.veracity.com/docs/section/dataworkbench/apiendpoints#data-sets-endpoints).

#### Add, update, and remove a service account

Now, an admin can add, update, and remove a service account. For instructions, [see the documentation](usermanagement.md).

#### New workspace and tenant picker button

In the left corner of the "Home" page, an administrator can see a button for picking the tenant and the workspace.

Now, the button:

- In the left corner, displays an avatar with an abbreviated name of the tenant. To see the full name, hover over it. To go to the tenant, select it.
- Displays the name and the email address of the currently signed-in user.
- Displays the full name of the workspace.

If the workspace's name is too long, it will be shortened. To see the full name, hover over the button.

If you are a tenant admin, you can use the picker button to create a new workspace. To do so:

1. In the upper-left corner of the "Home" page, select the workspace and tenant picker button.
2. In the dropdown that appears, at the bottom, select the **Add workspace** button.

#### Data Catalogue: title bar with the back and action buttons

Now, when you open a data set in the "Data catalogue" tab, at the top, there is a bar. The bar shows (from left to right):

- A back button (arrow icon).
- The title of a dataset.
- The data set info icon.
- The column picker for editing table properties.
- The filter icon for hiding or showing the filters. The filters show under the name of a data set or a template (for example, "Poseidon Principles Template").
- The save icon.
- The share icon for sharing data sets.

### Changes in existing features

This section covers changes in existing features.

#### Change data set title and description

Previously, you could not change the title and description of a data set.

Now, you can do that. To change the title or description of a data set:

1. Open a data set.
2. In the upper-right corner of the row with the name of the data set, select the info icon.
3. Edit the dataset's name and/or description.
4. Select the **Save and close** button.

#### Column picker changes

Previously, you could not hide and show the column picker for a data set.

Now, the column picker is hidden by default. To enable it:

1. Open a data set.
2. In the upper-right corner of the row with the name of the data set, select the pencil icon. It will enable the column picker.

Also, Data Workbench has added a button for deselecting all columns in a data set. To do so:

1. Open a data set.
2. In the upper-right corner of the row with the name of the data set, select the pencil icon. It will enable the column picker.
3. In the right corner of the page, under the columns, select the **Deselect all** button.
4. To refresh your data set, in the right corner of the page, select the "Update table" button.

#### Icon tooltips updated

The icons within data sets, "Poseidon Principles" template, and "Sea Cargo Charter" template got new tooltip text that shows after you hover over an icon.

#### Message and prompt when you have no data sets

Previously, if no data sets were available in your workspace, there was no message informing about that.

Now, Data Workbench displays a message in the "Home" tab and the "Data Catalogue" > "All data" > "Created data sets". The message also prompts you to use a predefined data set, modify it, and save it as a new data set you can use. Also, in "All data" > "Predefined data sets", there is a pop-up explaining how to use predefined data sets to create and share your new data sets.

#### State of Compliance (SoC) files renamed

Now, when you download a State of Compliance (SoC) file, the name of the file follows the format "XXXXXXX; FOCR Statement of Compliance yyyy-mm-dd - yyyy-mm-dd.pdf" where:

- XXXXXXXX is replaced by the IMO Number of the vessel.
- yyyy-mm-dd is replaced by the start and end date for the verification period.

### Bugs fixed

This section covers bugs that have been fixed.

#### Unable to deselect properties in a data set

Previously, when using the column picker to select columns for a dataset, you could not deselect columns to the far-right using the default screen size. Now, it is fixed.

#### Blank workspace name

Previously, you could create a workspace with a blank space instead of a name. Now, this is impossible, and the name of the workspace should be between 1 and 100 characters.

#### Firefox: horizontal scroll bar under data properties

Previously, in Firefox, a horizontal scroll bar was displayed under data properties in column picker. Now, it is removed.

#### No response when selecting some areas of the "Use predefined data set"

Previously, when selecting some areas of the "Use predefined data set" button, there was no response. Now, it is fixed.

#### Data sets returning incorrect asset count

The "Data Catalogue" tab displays the "Available assets" column for each data set. This column shows the number of data rows in a data set. Previously, the "Available assets" count was always showing one irrespective of the number of data rows. Now, it is fixed, and the correct count is shown.
