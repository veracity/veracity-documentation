---
author: Veracity
description: This is the changelog for the September 2022 release of Data Workbench.
---

# September 2022 release

Release date: September 2022

Read this page to learn what changed in Veracity Data Workbench with the September 2022 release.

## New features

This section covers new features:
- [Activity logs](#activity-logs)

### Activity logs

The activity log provides transparency into what have happened to your data in a workspace. It provides information about who did something, to what data, which users and when it happened. For details, [see the documentation](activitylog.md).

In future releases, Veracity will enable filtering data sets, so that you can look into the data you are interested in.

## Changes in existing features

This section covers changes in existing features:
- [Members tab renamed to Workspace](#members-tab-renamed-to-workspace)
- [Added Activity log tab](#added-activity-log-tab)
- [Improved filter handling](#improved-filter-handling)
- [Prompt-before-leaving-unsaved-changes](#prompt-before-leaving-unsaved-changes)
- [API integrations improvements](#api-integrations-improvements)
- [Calendar improvements](#calendar-improvements)
- [Other changes](#other-changes)

### Members tab renamed to Workspace

The "Members" tab, located at the top of the page, has been renamed to "Workspace".

Now, to see workspace members:

1. In the workspace, go the **Workspace** tab.
2. In the left corner, go to the **Members** tab.

### Added Activity log tab

Now, when you go the "Data Catalogue" or "Workspace" tab, you will see a new sub-tab called "Activity log".

### Improved filter handling

Improved handling for working with applying and clearing filters for data set details, SCC and Poseidon page.

- "Clear filter" button is hidden when the filter is not set yet.
- "Apply" button is disabled when the filter is not set.
- A button called "Clear filters" was added to clear all the filters.

### Prompt before leaving unsaved changes

Now, if you have unsaved changes and try to leave the data set details page, you will be prompted to save them.

### API integrations improvements

- In the service account list, updated the mouse hover state to be less intrusive.
- Moved the **“+ Add account”** button to the top of the service account list and made it always visible.
- In the service account list, after you have created an account, the page scrolls to it.

### Calendar improvements

The calendar is part of different filters in the application.

- In SCC and Poseidon page, added visible indication of which dates have available data for them.
- Added input field, making it possible to manually enter a date
- The calendar always will have the same height, for easier browsing
- In SCC and Poseidon page, enforce date ranger behavior, disallowing selecting a from date that is later than a to date

### Other changes

- In create dataset, workspace and service account name input fields, added letter counter and max length indicator.
- Classification status will now refetch and update the classifications even if the user is idle on the page.
- In data catalogue page, added sticky headers and scrollbar making them always visible and available.
- Added native tooltip for all data that can overflow. This way you can hover over any data to see the full content.
- In the data set list, removed the superficial “assets” word in the rows. It already says “available assets” in the header.
- Data set name is limited to 64 characters to align with Data Fabric.

## Bugs fixed

This section covers bugs that have been fixed:

- Fixed columns are not evenly spread across rows in column picker for readers.
- Margins in navigation tabs are not consistent in different page.
- Fixed spin box displaying during saving dataset is truncated.
- Page goes to unexpected page after click "back" button in browser.
- Better handling of longer data set names.
- Firefox: Fixed operation icons are not displayed when mouse hovering on data set record.
- Decreased the margin between dataset list table and the end border of page.
- Scrollbar is displayed on the "Create new data set" dialog box.
- Fixed the gap between title and filters for Poseidon and SCC templates.