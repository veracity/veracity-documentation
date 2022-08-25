---
author: Veracity
description: Explains to a developer how to start using Veracity.
---

# How to start using Veracity?
If you are a developer, read this page to learn how to start using Veracity. 

The onboarding process for Veracity mixes meetings with the onboarding team and a self-service approach:
1. Someone from your company starts the onboarding process for customers. See how to do it [here](https://developer.veracity.com/docs/section/marketplace/productpresentation). A typical onboarding process results in
adding your company's app to the [Marketplace](https://store.veracity.com/) (see [Marketplace docs](https://developer.veracity.com/docs/section/marketplace/marketplace)) and using [Veracity Identity Provider](https://developer.veracity.com/docs/section/identity/identity) (Veracity IDP) for authentication. 
2. You [set up a non-production Veracity service](#project) and start working on it to comply with the [technical requirements](#requirements) for integrating with Veracity.
3. You ask the [onboarding team](mailto:onboarding@veracity.com) to provide you with application credentials for a "test" or "staging" Veracity application.
4. When your application meets [technical requirements](#technical-requirements), you contact the onboarding team to request a verification.
5. The onboarding team verifies if your application is ready for production.
6. After a successful verification, the onboarding team issues a new set of credentials for a production version of your application.
7. You use the production credentials to configure your production application.
8. You ask the [onboarding team](mailto:onboarding@veracity.com) for another verification.
9. After a successful verification, you receive client credentials for calling [Veracity APIs](https://developer.veracity.com/api) (including Veracity IDP).

Note that Veracity will cooperate with someone from your company on the commercial aspect of the onboarding when you go through the technical onboarding.

If you need assistance, contact the [onboarding team](mailto:onboarding@veracity.com). You can expect an answer within a few business days.

## API Explorer and GitHub
To see the specifications for APIs provided by Veracity, go [here](https://developer.veracity.com/api).

To see Veracity GitHub, go [here](https://github.com/veracity).

## <a name="project"></a>Project Portal
To start setting up your Veracity service, you need access to the Project Portal. To get it, [sign up](https://id.veracity.com/sign-up?return-url=https%3a%2f%2fdeveloper.veracity.com%2fauth%2flogin%3freturnTo%3d%2fdevEnrolled) for an account or [sign in](https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/oauth2/v2.0/authorize?p=b2c_1a_signinwithadfsidp&redirect_uri=https%3A%2F%2Fdeveloper.veracity.com%2Fauth%2Foidc%2Floginreturn&response_type=code&response_mode=form_post&client_id=3e6d5154-57c6-4fb2-a591-1f51b6c7739e&mfa_required=true&state=CUSTOMOVVnHKeZnaNhrB3VRj7KsCCA56dBjh9U%7B%22query%22%3A%7B%22returnTo%22%3A%22%2FdevEnrolled%22%2C%22p%22%3A%22B2C_1A_SignInWithADFSIdp%22%7D%7D&nonce=Dhgzqrv_YktA_BRvQCKJR3fkpVJaTFqP&scope=openid%20offline_access%20https%3A%2F%2Fdnvglb2cprod.onmicrosoft.com%2F83054ebf-1d7b-43f5-82ad-b2bde84d7b75%2Fuser_impersonation%20https%3A%2F%2Fdnvglb2cprod.onmicrosoft.com%2F83054ebf-1d7b-43f5-82ad-b2bde84d7b75%2Fmanage_appregistrations%20https%3A%2F%2Fdnvglb2cprod.onmicrosoft.com%2F83054ebf-1d7b-43f5-82ad-b2bde84d7b75%2Fuser_administration%20https%3A%2F%2Fdnvglb2cprod.onmicrosoft.com%2F83054ebf-1d7b-43f5-82ad-b2bde84d7b75%2Fmanage_services%20https%3A%2F%2Fdnvglb2cprod.onmicrosoft.com%2F83054ebf-1d7b-43f5-82ad-b2bde84d7b75%2Fresource_administration&x-client-SKU=passport-azure-ad&x-client-Ver=4.3.2) to your account.
In the [Project Portal](https://developer.veracity.com/projects), create the resources you need. For an overview, go [here](https://developer.veracity.com/docs/section/developerexperience/introduction). For a step-by-step guide, go [here](https://developer.veracity.com/docs/section/developerexperience/step-by-step-guide/getting-started).
Once you have created the resources you need, you will be able to get information for authenticating with Veracity IDP. 

To see the ID of your application, service, or API:
* In the [Project Portal](https://developer.veracity.com/projects), select your app, service, or API. It may be grouped under a Resource Group.
* Select the "Settings" tab.

If you need a client secret for your API, follow the same procedure as above.

To configure the Reply URLs:
* In the [Project Portal](https://developer.veracity.com/projects), select your app, service, or API. It may be grouped under a Resource Group.
* Select the "Configure" tab.

By default, your APIs have access to the [Veracity MyServices API](https://developer.veracity.com/docs/section/identity/services-openapi) used by Veracity Identity Provider. The scope is https://dnvglb2cprod.onmicrosoft.com/83054ebf-1d7b-43f5-82ad-b2bde84d7b75/user_impersonation.

If you need to call other [Veracity APIs](https://developer.veracity.com/api), you will need subscription keys for them. To get them, contact the [onboarding team](onboarding@veracity.com). 

## Technical requirements
If your company only needs a lead-generating site on Veracity, skip this section.
However, if you want to integrate your application with Veracity, you must meet the requirements described below. 

The Veracity platform is built on Microsoft Azure and uses Azure Active Directory B2C (OpenID Connect OAuth 2.0) for managing authentication with Veracity IDP. Because of that, the integration with Veracity will be easier for apps written in common languages and hosted on Azure, Amazon Web Services (AWS) or another large cloud platform.

**Technical requirements for integrating with Veracity:**
* [Sign-in button](#sign-in-button)
* [Sign-out](#sign-out-button)
* [Grant and remove subscriptions with API calls](#grant-and-remove-subscriptions-with-api-calls)
* [Consider authorization](#consider-authorization)
* [Unique user identifier](#unique-user-identifier)
* [Call the Policy API on every sign in](#call-the-policy-api-on-every-sign-in)
* [HTTPS & browser support](#https-and-browser-support)

**Test your application:**
* On internal company computers (for DNV, VERIT) and non-company computers.
* On internal company networks and external networks.

### Sign-in button
Your app should have a sign-in button integrated with [Veracity IDP](https://developer.veracity.com/docs/section/identity/identity). The Veracity IDP provides authentication and the [Single Sign On (SSO) experience](https://developer.veracity.com/docs/section/customerservices/sso). 

### Sign-out button
Your app should have a sign-out button that is easy to find. 
The sign-out button should clear relevant cookies and return the user to the Veracity sign-out endpoint: https://www.veracity.com/auth/logout. The endpoint sings out the user both from ADFS and Azure AD B2C.

If applicable, all local session info (including cookies) should be deleted when the user signs out.
Note that this applies to all Digital Services on Veracity.

### Grant and remove subscriptions with API calls
Veracity needs to know:
* Which Veracity users should have access to your app?
* What information on Veracity users does your app store?. Thanks to this, Veracity can stay compliant with the General Data Protection Regulation (GDPR).

Because of that, please stay in sync with Veracity. To do that, every time you add a Veracity user to your app, create a Service subscription for them.
If you delete or deactivate a user in your app's database, call a corresponding API endpoint to notify Veracity that we should revoke this user's access to your app. 

Veracity recommends creating an admin panel in your app for user management, so that non-technical admins can select buttons for actions that trigger API calls to Veracity.

To see Veracity MyServices endpoints for managing subscriptions, go [here](https://developer.veracity.com/docs/section/identity/services-openapi). Note that:
* The viewpoints "My" and "This" are available to you.
* The viewpoints "Directory" and "Options" are not available to you. 
* When you test API calls, you can do it in the browser for the "My" viewpoint. For the "This" viewpoint, use Postman or a similar tool.

### Consider authorization
Veracity provides user authentication but offers limited authorization options. 

If your application has a single access level, then you can assign service subscription to Veracity Users, and the users will have access to your app. To see the claims provided by Veracity IDP, go [here](https://developer.veracity.com/docs/section/identity/authentication/claims)

If your application is open to everyone (free), you might not need any authorization method. In this case, the onboarding team will help you decide on the authorization.

If your app has more than one user access level, you will need to control access on the side of your application. For example, your application may offer bronze, silver, and gold membership. In this case, when a user buys a membership, Veracity:
* Uses a service subscription to give the user access to your application.
* Informs your application which membership was bought by the user (bronze, silver, or gold).
After that, your application should use this information to give the user the access level that corresponds to their membership.

### Unique user identifier
Use the unique Veracity ID as a unique user identifier in your application. The Veracity ID is associated with the Veracity user account. Avoid using users' email addresses as unique identifiers because Veracity users can change their emails.

Also, if possible, avoid storing other information from the claim. Instead, you can retrieve it from the bearer token issued after the login. This approach should guarantee that you always have current profile information and avoid issues with syncing users.

### Call the Policy API on every sign in
Your app should call the Veracity Policy Service API when a user signs in. The API will:
* Check if the user has accepted the newest terms & conditions.
* Check if the user has a subscription for the given service on Veracity.

For details on the Policy API, go [here](https://developer.veracity.com/docs/section/identity/policy-service).

### HTTPS and browser support
Your application should use the HTTPS protocol and support the following browsers:
* Chrome
* Firefox
* Edge

However, you can choose not to support a browser and display a warning instead. In this case, when a user tries to access your service using an unsupported browser, they should see a warning that the app will not work properly and information what other browsers you support.