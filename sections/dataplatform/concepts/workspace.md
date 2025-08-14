---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Workspace

Each workspace in the Veracity Data Platform acts as a secure boundary for your data. Think of it as a separate container within the data lake—isolated from others to ensure privacy and protection.

This means:

* Data in one workspace cannot be accessed from another unless explicitly shared.
* Each workspace has its own security controls and permissions.
* It’s designed to keep your data safe, organized, and under your control.


## Roles
Within a workspace users can have roles which gives access to different features such as who can upload data, analyse data, add users, edit analytics scripts etc.

## Tenants
In the Veracity Data Platform, a workspace is associated with a tenant, which typically represents a single organization or legal entity.

While a tenant usually corresponds to one company, it is possible for a company to operate across multiple tenants—for example, to support different business units, regions, or compliance requirements.

This structure provides a clear separation of data, governance, and access control, ensuring that each workspace operates within the secure and compliant boundaries defined by its respective tenant.

For more information, see [Tenant and Workspace management](../tenantmgm.md)

## Client Accounts for Secure Application Integration
In the Veracity Data Platform, client accounts are primarily used to facilitate secure authentication for application and system integrations. These accounts enable external applications to interact with the platform in a controlled and compliant manner, ensuring that data access is governed by robust identity and access management policies.

By leveraging client accounts, organizations can automate data workflows, integrate with third-party systems, and maintain consistent security standards across their digital ecosystem.