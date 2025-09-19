---
author: Veracity
description: Tutorial for testing your API using Veracity.
---

# How to set up and test a Veracity API with user access and authentication
If you want to register an API, configure authentication, and grant users access for testing, this tutorial will guide you through the steps. You will learn how to:  

- Register your API in My Projects.  
- Decide if your API is tenant-aware or not.  
- For tenant-aware APIs, use Veracity Access Hub to manage access.  
- For non-tenant-aware APIs, manage access directly in your application.  

## Register your API in My Projects
Start by registering your API in **My Projects**.  

1. Go to [https://developer.veracity.com/projects/](https://developer.veracity.com/projects/).  
2. Create a **project** if you do not already have one.  
3. In your project, create a **resource group**. Choose the environment: `devtest`, `staging`, or `production`.  
4. In the resource group, create a **resource** of type **API**.  

For details, see [My Projects guide – creating and managing resources](../developerexperience/introduction.md).  

> Note: In this tutorial we focus on how to grant access and test your API. For this purpose, you should choose the **DevTest** or **Staging** environment. If you want to publish your API to production, [follow this process](../onboarding/onboarding.md).  

### Configure the API product
1. Name your API.  
2. Set "Is public?" to off (keep private while testing).  
3. Enable CORS if needed.  
4. Create an API specification by uploading or linking your OpenAPI/Swagger file and assign it to the API product.  

### Configure authentication
1. In your API resource, go to **Settings**.  
2. For **Client type**, select "None" if your API is a backend service. This marks it as a resource server, not a client.  
3. Define one or more scopes under **Scope names**. These scopes will be used by client apps when requesting tokens. Example:  
   - Scope: `https://your-api-domain.com/user_impersonation`  
   - Description: "Allows user-level access to MyApi"  

### Validate tokens in your API
Every request must include a bearer token. Your API must:  

1. Extract the token from the `Authorization` header.  
2. Validate it using the Veracity metadata endpoint `https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/.well-known/openid-configuration?p=B2C_1A_SignInWithADFSIdp`. 
3. Check:
	- Token signature using jwks_uri.
	- `aud` (audience) matches your API's Client ID.
	- `exp` (expiration) is valid.
	- `scp` (scope) includes your defined scope (for example, user_impersonation).
4. If validation fails, return `401 Unauthorized`.   

For more details, see [authentication and authorization with Veracity Identity](https://developer.veracity.com/docs/section/identity/authentication/overview).

## Check if your app is tenant aware
If your application or API is tenant-aware, we recommend that you use **Veracity Access Hub (VAH)** to manage access.  

If your application or API is not tenant-aware, you must manage access entirely in your application. In that case, skip ahead to [non-tenant aware apps](#non-tenant-aware-apps).

## Tenant-aware apps (using Veracity Access Hub)

### Check if you already have a company account
1. Go to [Veracity Access Hub](https://accesshub.veracity.com/) and sign in.
2. If you have access, you will see your company account listed.
3. If you do not see a company account, ask internally who purchased the service for your organization. The purchaser becomes the Tenant Admin by default. When you identify this person, ask them to check if they have access to Access Hub and if they can add you as a Tenant Admin.  
4. If you cannot identify the purchaser or cannot confirm access, open a support ticket and provide your organization details. Support can:  
   - Confirm if a company account exists.  
   - Tell you who the Tenant Admin is.  
   - Help you if you should be a Tenant Admin but are not.  

### Get or request Tenant Admin access
- If you are already a Tenant Admin, you can add more admins. In Access Hub, go to **Admins** from the left navigation and select **Add tenant admin**.  
  For details, see [Veracity Access Hub guide](accesshub.md).  
- If you are not a Tenant Admin, ask the current Tenant Admin to add you.  
- If you should be a Tenant Admin but are not, open a support ticket and explain why.

### Collect the IDs you need
You need two IDs to connect your API with your company account:

- **App / API ID**: In My Projects, open your API resource, go to the **Settings** tab, and copy the value under **App / API ID**.  
- **Company Account ID**: In Access Hub, go to the homepage and look under **Details** for "Company Account ID". You can also copy it from the URL – the part after `tenant_id=`.  

### Add your API to Access Hub
1. Copy your **App / API ID** from My Projects. To find it, open your API resource, go to the **Settings** tab, and copy the value under **App / API ID**.  
2. Copy your **Company Account ID** from Access Hub. To find it, go to the homepage, open **Details**, and copy the **Company Account ID**, or copy it from the URL after `tenant_id=`.  
3. Open a support ticket and ask to link your API to your company account.  
4. When support links it, you will see your API under the **Applications** page in Access Hub.  

For details on managing applications, see [the Applications section in Veracity Access Hub guide](https://developer.veracity.com/docs/section/customerservices/accesshub#applications).  

### Manage users and grant test access
Once your API appears in Access Hub under **Applications**, you can:  

- Add or remove users by email.  
- Add or remove groups (if supported).  
- Add or remove application admins.  
- Toggle auto-assign subscription to automatically give new users in your company access.  

To test your API, add your test users here and assign the correct access level.  

For more details, see [the Users section in Veracity Access Hub guide](https://developer.veracity.com/docs/section/customerservices/accesshub#users).  

### If you can't manage users for applications
If you cannot add or remove users for your API in Access Hub, your company account may be using the Complex model. In that case, you need to handle access in your API as described in [non-tenant aware apps](#non-tenant-aware-apps). 

If you prefer to manage access through Access Hub, consult with your team and consider opening a support ticket to request a new company account with a different access management model or changing the current model to Fully managed or Hybrid.  

For details, see [Veracity Access Hub guide](https://developer.veracity.com/docs/section/customerservices/accesshub).  
  
## Non-tenant aware apps
If your API is not tenant-aware, you do not use Access Hub. Instead, you manage access directly in your application.  

- You still need to validate Veracity-issued tokens.  
- You identify the user by claims in the token, such as `userId`.  
- You store user roles and permissions in your own database.  
- On each request, after validating the token, you check if the user has permission to perform the action.  

Example:  
- Token includes `userId: abc123`.  
- Your app checks your database: is `abc123` in the "Admin" role?  
- If yes, allow access.  

This gives you full control over access without using Access Hub.
