---
author: Veracity
description: Tutorial on setting up and testing an API in the Veracity ecosystem.
---

# How to set up and test a Veracity API with user access and authentication
If you want to register an API, configure authentication, and grant users access for testing, this tutorial will guide you through the steps. You will learn how to:
- Register your API using the correct resource types.
- Secure it with Veracity Identity.
- Use Veracity Access Hub (if applicable) or manage access internally.

## Register your API in My Projects
To publish and secure your API, you need three resources:

1. **Application (App/API)** - defines authentication (scopes, Client ID).
2. **API Product** - controls visibility, access policies, and subscriptions.
3. **API Specification** - defines endpoints via OpenAPI/Swagger.

Follow these steps in order.

## Step 1: Create an API resource to define the scopes
This enables OAuth2 authentication and token validation.

1. In your resource group, select **New Resource**.
2. Choose **App/API**.
3. On the **Configure** step:
   - Name your API.
   - Under **Client application**, select **None** (this is an API, not a client).
   - Tick **This is an API**.
   - Under **Scope name(s)**, add one or more scopes (for example, `user_impersonation`).
   - Add a description.
4. Optionally, on the **Advanced** step, under **Authorized client applications**, add client applications that should be allowed to request tokens for this API.
   - You need the **Application ID** of the client.
   - Adding one client from a project grants access to all clients in that project.
5. On the **Summary** step, review and select **Submit**.

You'll get a **Client ID** (used as `aud` in tokens) and can define scopes.

> For details, see [My Projects guide – creating and managing resources](https://developer.veracity.com/docs/section/developerexperience/introduction).

## Step 2: Create an API product to control access
This determines if your API appears in API Explorer and manages policies.

1. In the same resource group, select **New Resource**.
2. Choose **API Product**.
3. On the **Configure** tab:
   - Name the product.
   - Set **Is public?** to *off* (keep private during testing).
   - Set **Require subscription approval?** as needed.
   - Add a description.
4. On the **Advanced** tab:
   - Enable **CORS** if web clients will call your API.
   - Optionally enable **throttling**.
5. Select **Submit**.

You'll get an **API Product ID** and can generate subscription keys.

## Step 3: Create and assign an API Specification
This defines your API's endpoints and connects them to the API Product.

1. In the same resource group, select **New Resource**.
2. Choose **API Specification**.
3. On the **Configure** tab:
   - Name the specification.
   - Under **API Products**, select the **API Product** you just created.
   - Under **Upload type**, select the format in which you will provide the API specification (for example, OpenAPI YAML/JSON, URL).
   - Under **API Specification**, paste your specification or a URL to it.
   - Set **API suffix** (for example, `/v1`).
   - Optionally set API **Version**.
   - Set **Backend URL** (where your API is hosted).
4. Select **Submit**.

Your API is now fully defined and ready for testing.

## Validate Tokens in Your API
Every request must include a Bearer token in the `Authorization` header.

Your API must:
1. Extract the token from the `Authorization` header.
2. Validate it using the metadata endpoint: https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/.well-known/openid-configuration?p=B2C_1A_SignInWithADFSIdp
3. Check:
- Signature using `jwks_uri`.
- `aud` matches your **API's Client ID** (from the Application resource).
- `exp` is not expired.
- `scp` includes your defined scope (for example, `user_impersonation`).
4. If validation fails, return `401 Unauthorized`.

> For details, see [Authentication for APIs](https://developer.veracity.com/docs/section/identity/authentication/overview).

## Use Veracity Access Hub for Access Management
If your API is part of a service available in the **Veracity Marketplace**, you can use **Veracity Access Hub (VAH)** to manage user access.

> **Important limitation**:  
> Veracity Access Hub only supports access management for services purchased via the **Veracity Marketplace**.  
> For services in Energy, Maritime (for example, Fleet Status, Certification), or Classification, continue using existing tools like [Maritime Access Management (MAM)](https://maritime.dnv.com/mam/Users).

### Check User Access via VTM API
If your API is integrated with Veracity Access Hub, you can use the **Veracity Tenant Management (VTM) API** to check if a user has access and what role they have.

#### Consider what API version to use
- For **new APIs** ("green field" development): use **VTM API v4** [(see the specification)](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/v4-api-swagger.json).
- For **existing APIs** under maintenance or extension: You may continue using **V3** [(see the specification)](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/identity/services-openapi), but plan to **migrate to V4**.

**Note that** V4 is the current standard and recommended for all new integrations.
> For more, see [VTM documentation](https://developer.veracity.com/docs/section/tenantmanagement/tenantmanagement#overview).

#### How to check access (using V4)
To verify user's access using VTM API V4:

1. After validating the bearer token, extract:
   - `userId` (from token claim)
   - `tenantId` (from tenant selector or URL)
   - `applicationId` (your API's Client ID)

2. Call: `GET /tenants/{tenantId}/applications/{applicationId}/licenses/{userId}`

3. If the response is `200 OK`, the user has access. You can:
- Check `accessLevel` for built-in roles.
- Read `properties` for custom permissions.

### Can I use VAH for a non-production or non-Marketplace API?
Not through self-service. Currently, **only Marketplace-purchased services** can be installed in a company account.

However, if you want to **test access management** before production, you can request a **test tenant** where your API is installed.

### How to get your non-Marketplace API into a company account
1. Open a support ticket at [https://support.veracity.com](https://support.veracity.com).
2. Include:
- Your **API Product ID** (from My Projects > API Product > Settings).
- Your **Company Account ID** (from VAH URL or Details page).
- A description of the test scenario.
3. Veracity staff will:
- Create a tenant (if needed).
- Manually install your service.
- Notify you when it's ready.

### Grant Access to test users
Once your API appears in VAH under **Applications**, you can manage access for test users.

1. In [Veracity Access Hub](https://accesshub.veracity.com/), go to the **Users** page.
2. Select **Add users** and enter the email addresses of your test users.
	- Users without a Veracity account will receive an invitation to create one.
3. Go to the **Applications** page.
4. Find your API in the list.
5. Select **Add user** and choose the test users who should have access.
6. Assign the appropriate access level if available (for example, Viewer, Editor).
7. For audit and visibility, you can also:
	- Revoke access at any time.
	- View all users with access.
	- Add users in bulk via user groups (if enabled).

> This grants access at the company account level. Your application may still enforce additional permissions [(hybrid access control model)](https://developer.veracity.com/docs/section/customerservices/accesshub#overview).

> For full steps, see [Veracity Access Hub Guide – Managing Users](https://developer.veracity.com/docs/section/customerservices/accesshub#users) and [Applications](https://developer.veracity.com/docs/section/customerservices/accesshub#applications).

## Manage access internally (for non-marketplace or custom access APIs)
If your API is not part of a Marketplace offering, or you need full control over permissions, manage access in your application.

1. Validate the access token (as described above).
2. Extract the `userId` claim from the token.
3. Use `userId` to look up roles/permissions in your database.
4. On each request, after validating the token, check if the user has permission to perform the action.

Example:
- Token includes `userId: abc123`
- Your app checks: "Is `abc123` in the 'Admin' group?"
- If yes, allow access.

This gives you full control and works independently of Veracity Access Hub.

### Access Models for User Permissions

There are two main models for managing user access to your API:
- Modern model using Veracity Services API v4 with Veracity Access Hub (recommended for New APIs).
- Existing model using Veracity Services API v3 and subscription keys (for maintenance only).

For new APIs, we recommend the modern model:
- Using **Veracity Access Hub** to manage user access.
- Checking permissions via **VTM API v4**.
- Leveraging tenant-aware roles, access levels, and group-based permissions.

This model supports modern, scalable, and secure access control.

> For details, see [Veracity Tenant Management documentation](https://developer.veracity.com/docs/section/tenantmanagement/tenantmanagement).

Some older APIs use the existing model:
- **Subscription keys** (shared via Developer Portal) for access.
- **VTM API v3** to validate access and permissions.

While this model is still in use, it lacks integration with Veracity Access Hub and offers limited scalability.

> Use this only for **maintaining or extending existing APIs**.
> If using V3, plan to **migrate to V4** over time.
> For more, see [Veracity MyServices API](https://developer.veracity.com/docs/section/identity/services-openapi).

## Going to production
If you've tested your API in a non-production environment and used Veracity Access Hub (VAH) for access management, see the [Onboarding Guide](https://developer.veracity.com/docs/section/onboarding/onboarding) for detailed instructions on how to go live.

Below, you can see a short overview of how to go with your API to production:

1. **Ensure your service meets technical requirements**:
   - Implement sign-in/out with Veracity IDP.
   - Use the Policy API on every sign-in.
   - Manage subscriptions in sync with Veracity (GDPR compliance).
   - Use HTTPS and support modern browsers.

2. **Contact the onboarding team**:
   - Request verification of your non-production setup.
   - After approval, you'll get **production credentials**.

3. **Publish to production**:
   - Use production credentials to configure your live environment.
   - Request final verification from the onboarding team.

4. **Your API can be bought from the Veracity Marketplace**:
   - Once live, your service can be purchased via the **Veracity Marketplace**.
   - Customers will install it in their company account and manage access with Veracity Access Hub.