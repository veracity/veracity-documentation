---
author: Veracity
description: This is the changelog for the May 2025 second release of Data Workbench.
---

---
author: Veracity
description: This is the changelog for the May 2025 second release of Data Workbench.
---

# May 2025 second release

Read this page to learn what has changed in Veracity Data Workbench with the May 2025 second release.

These changes improve how you manage data access and enhance visibility into requests others make to access your data sets.

## New features

## Manage data set access with the Requests tab

A new **Requests** tab is now available in the **Data catalogue** section of the Data Workbench. It helps you handle data sharing requests from other users in a clear and structured way.

<figure>
	<img src="assets/request1.png"/>
</figure>

The tab includes two subtabs:

- **Requests awaiting your action** – shows incoming requests from users asking for access to your data sets.
- **Completed requests** – stores the full history of requests and their outcomes.

When someone requests access to a data set you manage, you’ll receive an **email notification** with a direct link to review and act on the request.

In the **Requests awaiting your action** tab, you can also refine the view by clicking the **Add filter** button above the table on the left. You can filter requests by **Schema** and **Request from** to find specific entries faster.

## Take action directly in the interface

In the **Requests awaiting your action** view, each row displays request details including request date, schema, IMO, and time period (for example, data from December 2023 to December 2024).

When you hover over a request’s **status**, three action icons appear:

- **View** (1) – shows who made the request and what they are asking for.
- **Approve request** (2) – grants the user access to the data set.
- **Decline request** (3)– denies the request.

<figure>
	<img src="assets/request2.png"/>
</figure>

When you **accept** a request:
- The data set is immediately shared with the requester.
- It appears in their **Data Catalogue**.
- The request moves to the **Completed requests** tab with a status of **Approved**.

When you **decline** a request:
- The data set is **not shared**.
- The action **cannot be undone**.
- The request is still recorded in the **Completed requests** tab with a status of **Declined**.

All past decisions—approved, declined, or processing—are visible in the **Completed requests** view for auditing and tracking.