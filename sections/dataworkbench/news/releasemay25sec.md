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

- **Requests awaiting your action** - shows incoming requests from users asking for access to your data sets.
- **Completed requests** - stores the full history of requests and their outcomes.

When someone requests access to a data set you manage, you'll receive an **email notification** with a direct link to review and act on the request.

Both subtabs include a **filter** option. Click **Add filter** above the table on the left to narrow results by **Schema** or **Request from**.

## Take action directly in the interface

In the **Requests awaiting your action** view, each row displays request details including request date, schema, IMO, and time period.

When you hover over a request's **status**, three action icons appear:

- **View details** - shows who made the request and what they are asking for.
- **Accept request** - grants the user access to the data set.
- **Decline request** - denies the request.

You can also process the request from the **Request details** page by clicking the request date or the **View** icon.

<figure>
	<img src="assets/request2.png"/>
</figure>

When you **accept** a request:
- A data set is created in **both the requester and the receiver** workspaces.
- The request moves to the **Completed requests** tab with a status of **Approved**.

When you **decline** a request:
- The data set is **not shared**.
- The action **cannot be undone**.
- The request is recorded in the **Completed requests** tab with a status of **Declined**.

Even after a request has been approved, you can **revoke access** by declining it later. Go to the **Completed requests** tab, hover over the approved request, and click the **Decline** icon.

All past decisions -approved, declined, or processing- are visible in the **Completed requests** view for auditing and tracking.