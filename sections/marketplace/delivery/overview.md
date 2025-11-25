---
author: Veracity
description: Delivering the purchased service
---

# Delivering the purchased service

> After a purchase is made, the goal is simple: **get customers using what they bought** quickly and securely. For most services, the critical step is **granting user access** to the right people.

**Delivering the purchased service** on Veracity focuses on three outcomes:

- **Automated delivery** — turn an order into access with minimal manual steps.
- **Great onboarding** — guide customers smoothly from "paid" to "productive".
- **Self-service user access management** — let customers add and manage their own users.

<br/>

To support these outcomes, Veracity provides platform capabilities you can adopt as needed:

- **Secure access with Veracity Identity sign-in**  
  After checkout, users already have Veracity accounts and can sign in to your application.\
  [Read more](https://developer.veracity.com/docs/section/identity/identity)

- **Veracity Access Hub**
  A ready-made self-service interface for inviting users, assigning seats, and managing access. Built on top of Veracity Tenant Management.\
  [Read more](https://developer.veracity.com/docs/section/customerservices/accesshub)

- **Veracity Tenant Management**  
  Services and APIs for building multi-tenant solutions with secure access management.\
  [Read more](https://developer.veracity.com/docs/section/tenantmanagement/tenantmanagement)

- **Visibility on the Veracity _My Services_ dashboard**
  Streamline the user onboarding process by making your application visible on the user's _My Services_ dashboard, ensuring a consistent UX while your app remains where value is delivered.\
  [Read more](https://developer.veracity.com/article/about-myservices)

<br/>

There are multiple ways to connect your product to these capabilities. This page outlines the main patterns and helps you choose the right one.

<br/>

## Integration patterns

1. **Self-service access with Veracity Access Hub and Tenant Management**\
   Leverage [Access Hub](https://developer.veracity.com/docs/section/customerservices/accesshub) for automated onboarding and self-service access management. Also supports showing an application tile on the user’s _My Services_ dashboard.\
   _Access Hub requires your application to use [Veracity Identity](https://developer.veracity.com/docs/section/identity/identity) and [Veracity Tenant Management](https://developer.veracity.com/docs/section/tenantmanagement/tenantmanagement)._

2. **Application-hosted access (event-driven via order messages)**\
   If your application already manages access, subscribe to [order messages](ordermessage.md) and update your own app-specific entitlements (e.g., seats, plans) when purchases are made.

3. **Hybrid approach (2 + 3)**\
   Combine [My Services](https://developer.veracity.com/article/about-myservices) visibility and single sign-on with fine-grained or app-specific access rules in your own UI via APIs/integrations.

4. **Using order messages for custom purchase types**\
   For purchases that don’t map to an "installed capability", for example task- or usage-based purchases, handle them in your application and use [order messages](ordermessage.md) to trigger the right workflow or update usage.

5. **Manual or guided onboarding**\
   Whether you're starting sales before full automation or your solutions requires complex, manual activation steps, you can run a **manual flow**. The order confirmation from Veracity can set expectations for delivery timelines and manual or guided onboarding, and you can use email notifications or [order messages](ordermessage.md) to trigger delivery steps. As you scale, replace steps with automation.

<br/>

Choose the patterns that match your product. Many teams start with **Access Hub** for fast time-to-value.
