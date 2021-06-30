---
author: Veracity adapter for Power BI
description: VAP tutorial - Advanced settings
---

# Configuration
[Previous - Summary and next steps](6-summary.md)

Most of the configurations in VAP is preconfigured from the start. There are some opportunities for you to change the service dependent on your needs. These changes can be done in the configure section.

In this section, we have the following settings:

- Header icon
- Service Analytics
- Entity types
- Tenant properties
- Entity type properties
- Tenant documents
- Refresh schedule plan
- Footer properties

## Header icon
The default icon for the VAP service is the Veracity by DNV wordmark. You can change the icon to your preference. To do so, click the edit header icon and upload your icon. We support most file types, and you will be able to crop the icon during upload. 

## Statistics report
The statistics report provide you with insight into your VAP service. Both concerning the operational aspects and the customer aspects.

## Entity types
Entity types define the naming used in the <i>Manage Entities</i> section of the <i>Admin</i> menu. A typical entity could then be something like project, ship, windfarm, company or similar. You will further work with the entities in the Manage Entity section. 

## Tenant properties
Tenant properties are information about your service. There is some basic information you can edit, like invoicing details, owner of the service etc. 

## Entity type properties
Entity type properties are the properties that will be sent to Power BI during runtime to utilize row-level security. For details on setup, see the VAP manual with examples. Row-level-security is a VAP Pro feature.

## Tenant documents
Tenant documents are documents you want to make available to all users from the end-users main screen. This is where you typically would publish marketing doccuments, FAQ, invitations to events etc.


## Refresh schedule plan
Refresh schedule plan is a VAP Pro feature, enabling you to ensure that the data in your reports are up to date. The VAP service will then refresh the data in your Power BI reports on the schedule of your choosing. Be aware that this schedule will affect your monthly consumption.

## Footer properties
The footer section enables you to customize parts of the footer section. You can define the header, support contact, copyright text etc.