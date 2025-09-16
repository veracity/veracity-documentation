---
author: Veracity 
description: Tutorial for testing your API using Veracity.
---

# How to Set Up and Test a Veracity API with User Access and Authentication

This tutorial guides you through setting up a new API on the Veracity platform, configuring it for testing, and granting access to test users. It addresses common questions from developers who have created an API in **My Projects**, but are unsure how to:
- Allow test users to access the service before production.
- Choose the correct authentication flow when the client type is set to "None".
- Decide which access control model to use with **Veracity Access Hub**.

By following this guide, you'll:
- Register your API correctly.
- Configure authentication using Veracity Identity Provider (IDP).
- Grant test users access via Veracity Access Hub.
- Choose the right access model for your use case.

## Create and Register Your API

Before users can access your API, it must be registered in the Veracity platform.

### Go to My Projects
1. Navigate to [https://developer.veracity.com/projects/](https://developer.veracity.com/projects/).
2. Select an existing project or create a new one.

> **Note**: A project organizes your resource groups. Use one project per product or service.  
### Create a Resource Group
1. In your project, select **Create new resource group**.
2. Choose an environment (for example, `devtest`, `staging`).
3. Add a descriptive name (for example, `MyApi-Staging`).

> You can test your API in non-production environments. Production deployment is optional for testing.  

### Add an API Resource
1. In the resource group, select **New Resource**.
2. Choose **API Product** and complete the configuration:
   - Name your API.
   - Set **Is public?** to *off* (private during testing).
   - Enable **CORS** if needed.
3. Submit to publish the API Product.

Then, create an **API Specification**:
1. Select **New Resource** again.
2. Choose **API Specification**.
3. Upload your OpenAPI/Swagger file or link.
4. Assign it to the API Product you just created.
5. Set an API suffix and version (optional).

Your API is now registered and ready for authentication setup.

## Configure Authentication for Your API

Your API must accept and validate access tokens from Veracity IDP.

### Select "None" for API Resources
When creating the client application in **My Projects > Settings**, select **"None"** if this is a backend API (not a user-facing app).

### Define Scopes for Your API
Scopes control what permissions client apps request when calling your API.

1. In **My Projects**, open your API resource.
2. On the **Configure** tab, under **Scope name(s)**, add one or more scopes:
   - Example: `user_impersonation`
   - Full format: `https://your-api-domain.com/user_impersonation`
3. Add a description (for example, "Allows user-level access to MyApi").

> These scopes will be used by client apps when requesting tokens.  

### Validate Access Tokens in Your API
Each incoming request must include a Bearer token. Your API must:

1. Extract the token from the `Authorization` header.
2. Validate it using the Veracity metadata endpoint: https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/.well-known/openid-configuration?p=B2C_1A_SignInWithADFSIdp
3. 3. Check:
- Token signature using `jwks_uri`.
- `aud` (audience) matches your API's Client ID.
- `exp` (expiration) is valid.
- `scp` (scope) includes your defined scope (for example, `user_impersonation`).

> If validation fails, return `401 Unauthorized`.  

## Grant Test Users Access

You can grant access to test users even if your API is not in production.

### Use Veracity Access Hub
1. Go to [https://accesshub.veracity.com/](https://accesshub.veracity.com/).
2. Ensure you are in the correct **company account** (use profile > Switch company account if needed).

> Only **Tenant Admins** and **Application Admins** can manage access.  

### Add Test Users to Your Company Account
1. Go to the **Users** page.
2. Select **Add users**.
3. Enter the email addresses of your test users.
4. Select **Add**.

> Users without a Veracity account will receive an invitation.  

### Grant Access to Your API
1. Go to the **Applications** page.
2. Find your API (or register it if not listed).
3. Select **Add user**.
4. Choose the test users who should access your API.
5. Assign an access level if available (for fully managed apps).

> This grants basic access. Detailed permissions are handled in your app (hybrid model).  

## Choose the Right Access Control Model

Decide how much access control you delegate to Veracity.

### Fully Managed by Veracity
- You manage all access in **Veracity Access Hub**.
- Assign users and roles directly.
- Best for simple apps with standard roles.

### Hybrid Access Control (Recommended)
- Grant basic access in **VAH**.
- Handle detailed permissions in your app using the `userId` claim from the token.
- Example: User is granted access in VAH → Your app checks database: "Is this user in Finance? If yes, show Finance data."

### Complex Access Models
- All access logic is in your app.
- VAH only shows who has access (for audit/compliance).
- Best for apps with dynamic, project-based permissions.

### Recommendation
Use **Hybrid Access Control** for most use cases. It balances ease of setup with flexibility in your application logic.