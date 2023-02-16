---
author: Veracity
description: This is the changelog for the release 4.5 of Veracity Adapter for Power BI (VAP).
---
# VAP 4.5 release
Release date: 13 February 2023

Read this page to learn what has changed in Veracity Adapter for Power BI.

## New features
This section covers new features:
* [Export all pages to PDF or Power Point](#export-all-pages-to-pdf-or-power-point)
* [See the tutorial again](#see-the-tutorial-again)
* [Stricter personal data handling](#stricter-personal-data-handling)
* [New background module for time consuming tasks](#new-background-module-for-time-consuming-tasks)

### Export all pages to PDF or Power Point
Previously, you were able to print only report pages you had open. There was no option to print all pages of a Power BI report.

Now, you can export all report pages to PDF or Power Point, and then print them with a time stamp. 

To enable this for a report:
1. Go to the **Manage report** tab.
2. Toggle **Able to export data**.
3. Under Able to export data, toggle **Able to export as PDF** or **Able to export as PPT**.

To export a report as a PDF or PPT:
1. Go to the **Home** tab.
2. Open a report.
3. In the right corner, in the top bar, select **Export** and then select **PDF** or **PPT**.

Note that:
* Exporting can take some time.
* Map types can have limited support.

To learn more about the limitations, go [here](https://learn.microsoft.com/en-us/power-bi/developer/embedded/export-to#considerations-and-limitations).

### See the tutorial again
Previously, once you have seen a tutorial connected to the report, there was no option to see it again.

Now, you can see the tutorial again:
1. Open a report with a tutorial.
2. In the top bar, select **Show tutorial again**.

To see VAP release tutorials again:
1. In the top bar, next to the notification icon, select the question mark icon.
2. Select **See tutorials again**.

Note that seeing those tutorials depends on your access level.

<figure>
	<img src="assets/tutorials-again.png"/>
</figure>

### Stricter personal data handling
VAP has enhanced personal data handling:
* Now, when you upload a report, you have to confirm whether you use personal data. If you do, you will receive some warning messages and questions that should help you in properly handling personal information.
* There are some new limitations for reports, web apps, images or PDFs containing personal data.
* If you use personal data, you will not be able to set access to public view nor allow self-subscribing.

### New background module for time-consuming tasks

Now, in the Admin tab, you can find a new module called Background Jobs. It was developed to improve performance on time-consuming tasks. In this module, you can check the status for the jobs running in the background.

Now, batch adding users will be run as a background task.

## Changes in existing features
* Both Admin API and Capacity API have been enriched with new endpoints to improve integration between services.
* Improved security.
* Reduced technical debt.