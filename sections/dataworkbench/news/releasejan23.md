---
author: Veracity
description: This is the changelog for the January 2023 release of Data Workbench.
---

# January 2023 release

Release date: January 2023

Read this page to learn what has changed in Veracity Data Workbench with the January 2023 release.

## New features

This section covers new features:
* [Guest access](#guest-access)
* [Revoke data set access](#revoke-data-set-access)

### Guest access
Now, you can share data sets with users that are not part of your workspace. The users are notified by email and can access the data sets by the link in the notification message or by going from the **Data catalogue** to **Shared with me** tab.
The guest users can use the "Info", "Filter", and "Download" action buttons, but they cannot edit data sets.

### Revoke data set access
Now, you can revoke user's access to a data set, and they are notified about that by email. For details, [see the documentation](../dataworkbench.md#to-revoke-access-to-a-data-set).

## Changes in existing features

This section covers changes in existing features:
* [Data set type](#data-set-type)
* [Data type column](#data-type-column)
* [Shared with me tab](#shared-with-me-tab)
* [Share data sets without expiration date](#share-data-sets-without-expiration-date)
* [Share data sets with service accounts](#share-data-sets-with-service-accounts)

### Data set type
Now, when sharing or saving a data set, you can choose between:
* Snapshot - share the current version of this data set (no automatic updates).
* Dynamic - this data set will be updated whenever there are any changes made to it.

### Data type column
Now, lists of data sets have a new "Type" column that indicates whether the data set is a live data stream (dynamic) or a data snapshot. Live data streams are updated continously, and the data snapshots only show the state of the data set at the time they were taken (corresponds to the displayed timestamp).

### Shared with me tab
Now, in the "Data catalogue", there is a new tab called "Shared with me". The tab shows all the data sets that have been shared with you.

### Share data sets without expiration date
Previously, when sharing a data set, you had to decide on the expiration date for the share. Now, you can share data sets for an unlimited time.

### Share data sets with service accounts
Now, you can share data sets with service accounts.

## Bugs fixed

This section covers bugs that have been fixed:
* placeholder