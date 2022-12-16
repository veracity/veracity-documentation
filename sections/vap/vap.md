---
author: Veracity
description: Overview of the Veracity Adapter for Power BI.
---

# Veracity adapter for Power BI

## Overview

Veracity Adapter for Power BI (VAP) allows sharing Power BI reports with your users without requiring them to purchase a Power BI licence and install the software. The only step your users need to take is to sign in to Veracity. The VAP service is hosted and maintaned by Veracity, so that you can focus on the content.

The Veracity Adapter for Power offers:
* Convenient access for end-users. Sign in to Veracity and access the reports that are automatically updated.
* Secure sharing of your reports, interactive dashboards, and other data.
* Managing your reports, users, and their access permissions.
* Maintenance and updates handled by Veracity.
* Easy scaling.
* Optionally, a Marketplace page for monetising your data and reports.

For details about the service, see the [VAP Marketplace page](https://store.veracity.com/veracity-adapter-for-power-bi-vap).

For quick-start tutorials, go [here](vap-saas-tutorial/1-introduction.md).

## How to access VAP

To access your VAP service:
1. Go to the Veracity page.
2. In the top navigation menu, select "My Services".
3. Find the tile with the name of your VAP service and select it.

## Home tab

The Home tab of your Veracity Power Adapter for Power BI (VAP) shows the entities you have access to and the reports in them. To go to a report, open a tab with its name. To go to a different entity, select the Home tab again, and then choose the entity you want to go to.

## Admin tab

The Admin tab shows [administrator tasks](admintab.md).

## Permissions

What you can do in VAP depends on your [user role](userroles.md). Usually, the end users consume reports, and the admin users handle administrator tasks such as creating reports, configuring the VAP service, and so on.

## Bookmarks

Admin users can enable personal and report bookmarks. Personal bookmarks work like links to the part of the report on which they were created, and you can share them with others to let them easily navigate to the relevant part of the report. Report bookmarks are the same, but they are created by the report author and cannot be modified by users.

## Data sources and security

VAP workspaces are hosted in Microsoft cloud either in the UE or USA, depending on where your service is set up. For maxium safety, DNV owns private premium capacities and does not share them with anyone.

VAP does not store your data and it cannot access it. VAP only stores the report and data set ID, so that they can be loaded from their source location into your reports in VAP. 

VAP supports using multiple data sources in your Power BI report. The data sources and credentials you use when creating your report are automatically imported into VAP. If you want to override and update them, you can do so from VAP.

You can use the following data sources:
* Your Power BI report. VAP will import the data from it. Suitable if the data changes seldom.
* Refreshable data sources stored in the cloud. Suitable if the data changes frequently.

VAP supports the following refreshable data sources:
* Azure SQL Database through direct query. VAP refreshes data each time the users views the report.
* Veracity Data Fabric containers (to see your containers, in Veracity's top navigation bar, select "My data"). You can set up data to refresh daily, weekly, or monthly. The maximum number of daily refreshes is 48 which means the data would be refreshed approximately every 30 minutes. 
* Azure Analysis Services. VAP refreshes data each time the users views the report.
* On Permises Databases through Gateway.

Azure Analysis Services can offer the fastest way of refreshing report data, while Azure SQL Database may be the slowest (depending on the data model and the amount of data).

## Row-level security
Placeholder text.

## Quick start

For quick start tutorials, go [here](vap-saas-tutorial/1-introduction.md).