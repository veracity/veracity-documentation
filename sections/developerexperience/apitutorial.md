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

> For details, see [My Projects guide – creating and managing resources](../developerexperience/introduction.md).

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

> For more, see [Publishing APIs in API Explorer](https://developer.veracity.com/docs/section/publishing/publish-api-explorer).

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

> For more, see [Publish API specifications](https://developer.veracity.com/docs/section/publishing/publish-api-explorer#to-publish-api-specifications).

## Validate Tokens in Your API

Every request must include a Bearer token in the `Authorization` header.

Your API must:
1. Extract the token from the `Authorization` header.
2. Validate it using the metadata endpoint: https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/.well-known/openid-configuration?p=B2C_1A_SignInWithADFSIdp
3. Check:
- Signature using `jwks_uri`.
- `aud` matches your **API's Client ID** (from the Application resource).
- `exp` is not expired.
- `scp` includes your defined scope (e.g., `user_impersonation`).
4. If validation fails, return `401 Unauthorized`.

> For details, see [Authentication for APIs](https://developer.veracity.com/docs/section/identity/authentication/overview).

## Use Veracity Access Hub for Access Management
If your API is part of a service available in the **Veracity Marketplace**, you can use **Veracity Access Hub (VAH)** to manage user access.

> **Important limitation**:  
> Veracity Access Hub only supports access management for services purchased via the **Veracity Marketplace**.  
> For services in Energy, Maritime (for example, Fleet Status, Certification), or Classification, continue using existing tools like [Maritime Access Management (MAM)](https://maritime.dnv.com/mam/Users).

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

> This grants access at the company account level. Your application may still enforce additional permissions (hybrid model).

> For full steps, see [Veracity Access Hub Guide – Managing Users](__VAH_GUIDE_LINK__#users) and [Applications](__VAH_GUIDE_LINK__#applications).

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