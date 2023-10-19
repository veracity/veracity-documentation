---
author: Veracity
description: Overview of VAP roles and permissions.
---

# User roles

In Veracity Adapter for Power BI (VAP), each user role grants different permissions:
* DataReader - can read reports, suitalbe for regular users.
* ReportAdmin - can manage files, webs, and reports.
* DataAdmin - can manage files, reports, and entities.
* UserAdmin - can manage users.
* SystemAdmin - can manage files, webs, reports, entities, users, and configure VAP.

Roles are assigned and revoked by user admins and system admins.

## DataReader

This role is suitable for end-users of your VAP service as it allows them to read and interact with the reports and web connections they have been given access to.

## ReportAdmin

This role is suitable for people who should be able to:
* Upload and delete Power BI reports and files (your reports are based on them).
* Create reports in VAP.
* Connect your web app to be shown and shared through VAP.

## DataAdmin

This role is suitable for data administrators who organize how your reports are shown to end users and give them access. Data admins can:
* Upload and delete Power BI reports and files (your reports are based on them).
* Create reports in VAP.
* Group and structure your reports, and give access to them.

## UserAdmin

This role is suitable for user administrators who should be able to:
* Create, edit, and delete users.
* Assign and revoke the following user roles: DataReader and UserAdmin.

If you need to assign or revoke a DataAdmin or ReportAdmin role, ask a System Admin to do so.

## SystemAdmin

This role is suitable for people who should be able to manage everything in your VAP service. Veracity advises to assign this role to a limited number of people.
