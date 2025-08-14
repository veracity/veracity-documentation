---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# How to get started
In order to use the Veracity Dataplatform you need access to a tenant and at least one workspace. Onboarding team will setup a tenant and define tenant owner and workspace administrator. Contact support@veracity.com
There is a seperate subscription for File Storage and for Analytics.

## Testing/Piloting
You can get access to a pilot area for a limited time-period.

## Workspace
In the Veracity Data Platform, a workspace is associated with a tenant, which typically represents a single organization or legal entity.  While a tenant usually corresponds to one company, it is possible for a company to operate across multiple tenants—for example, to support different business units, regions, or compliance requirements.

If your service is multi-tenant, the tenants to support should be reflected in DWB as well. Within each tenant you need at least one workspace. Workspaces can be created using Dataworkbench api. This can only be done by tenant admin.

## Client account 
In the Veracity Data Platform, client accounts are primarily used to facilitate secure authentication for application and system integrations. These accounts enable external applications to interact with the platform in a controlled and compliant manner, ensuring that data access is governed by robust identity and access management policies.

By leveraging client accounts, organizations can automate data workflows, integrate with third-party systems, and maintain consistent security standards across their digital ecosystem.
See how to [create a client service principle that can access your workspace](https://developer.veracity.com/docs/section/dataworkbench/apimanagement)

## Way forward

* [How to define schema for structured data](https://developer.veracity.com/docs/section/dataplatform/schemamanagem)

* How to upload data to your workspace:
- [Structured data](https://developer.veracity.com/docs/section/dataplatform/storage/datasets)
- [Files (unstructured)](https://developer.veracity.com/docs/section/dataplatform/storage/files)
- [Stream](https://developer.veracity.com/docs/section/dataplatform/storage/streaming)

* How to query data from your workspace
- [Dataset query](https://developer.veracity.com/docs/section/dataplatform/query/datasetquery)
- [File query](https://developer.veracity.com/docs/section/dataplatform/query/filequery)

* [How to model your asset](https://developer.veracity.com/docs/section/dataplatform/mms/mmsintroduction)

* [How to query your asset models](https://developer.veracity.com/docs/section/dataplatform/mms/assetmodelquery)

* [How to use analytics environement](https://developer.veracity.com/docs/section/dataplatform/analytics/analyticsdevelopment)


