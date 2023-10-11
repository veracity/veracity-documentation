---
author: Veracity
description: This is the changelog for the second October 2023 release of Data Workbench.
---

# October 2023 second release

Read this page to learn what has changed in Veracity Data Workbench with the second October 2023 release.

## New features

### Generate ready-to-use Python script for API integrations

Now, in API integrations, you can generate a sample Python code that will include your credentials. Then, you can download it and immediately start making API calls with it.

To generate the code:
1. Go to API integrations > Service accounts.
2. Select a service account.
3. Under **Generate sample Python code**, select the **Generate** button.

US 495134

### Use tags for data sets

Now, you can add tags to data sets so that you can find the data sets you are looking for easier and faster. You can also edit and delete tags.

To edit or delete tags for a data set, open the data set, go to the **Details** tab, and next to **Tags**, select the pencil icon. To delete a tag, select the **X** icon next to its name. To edit a tag, remove the old one and create a new tag.

To add a tag to a data set:

1.In **Data catalogue**, open the data set.
2.Go to the **Details** tab.
3. Under **Tags**, select **Add tags**.
4. Enter key and value, and then select **Add**.
5. To save the tag, select **Save and close**.

Note that you can also add tags when you are creating a new data set.

For example, if you want to add a tag 'Tonnage : 5000':
1. For key, enter 'Tonnage'.
2. For value, enter '5000'.

Each data set can have up to 100 tags. For each tag, maximum length is 65 characters for the key and 256 characters for the value

US 493225, 495313, 490896, and others

## Changes in existing features

## Bugs fixed

Previously, in API integrations > Service accounts, the Endpoints base URL was calling the first version of the API. Now, it is updated and calls the second (the current) version of the API.

Bug 499239

Previously, in API integrations > Service accounts > Access to data sets, when you removed access to a data set, this change wasn't visible in the UI unless you refreshed the page. Now, this is fixed.

Bug 499245

Previously, recent data sets were not displayed on Home page. Now, this is fixed.

Bug 500473


