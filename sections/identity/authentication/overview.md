---
author: Veracity
description: Gives an overview of the Veracity Identity services and related components.
---

# Overview of Veracity Identity Provider
Veracity Identity Provider (Veracity IDP) uses the industry standard OpenID Connect protocol built on top of [OAuth 2.0](https://auth0.com/docs/protocols/oidc) flows to authenticate users and generate a verifiable JSON Web Token with basic user information. Because of that, you can find multiple libraries online to help you add authentication to your application.

## Prerequisites
Before you can authenticate calls with Veracity IDP:
1. [Create a service in Veracity](../../developerexperience/introduction.md).
2. Optionally, to be in the production environment, [onboard your service](../../onboarding/onboarding.md).
3. Update your knowledge on user data protection and apply it in your application or service.

Note that the user data you access from Veracity IDP requires protection according to local and international laws. When you receive personal user data from Veracity IDP, you become responsible for securing it. Because of that:
* Request only the information that you need.
* If possible, avoid storing user data, and delete it when it is no longer necessary.
* Ensure that user data is handled securely inside your application or service.

## Authentication scenarios
There are two most common authentication scenarios:
* [Applications directly interacting with users](#apps-with-direct-interaction-with-users).
* [Applications without direct user interaction](#apps-without-direct-interaction-with-users) that perform operations based on requests from other applications (such as REST APIs).

How you intergrate with Veracity IDP depends on your authentication scenario.

### Apps with direct interaction with users

Applications that directly interact with users need to authenticate them before executing requests on their behalf. To authenticate users:
1. Redirect users to Veracity IDP login page to sign in. After a successful authentication, Veracity IDP sends a response to your application or service confirming the identity of the user.
2. Validate the response on your side.

Note that users are sent back to your application or service after a successful authentication.

<figure>
	<img src="assets/basic-oidc-authentication.png"/>
</figure>

### Apps without direct interaction with users
Some applications, like APIs, lack direct interaction with users, but need to perform actions on their behalf. Because of that, the requests they send must contain the information for authenticating the user such as an access token. For details, [go here](api.md)

<figure>
	<img src="assets/api-verification-sequence.png"/>
</figure>

## Additional authorization
Veracity IDP provides authentication for applications registered with the Veracity platform. However, it does not provide authorization except for giving access to other Veracity APIs.

If you need authorization, you will have to implement it in your application or service. You may use information retrieved from the Veracity IDP to identify the user and then look up permissions for that user within your database. The user identity token provides a claim called `userId` that can be used to uniquely identify the user.

## Parameters for user authentication

To authenticate API calls, you will need the following parameters from the Project Portal.
* `Client ID`
* `Reply URL`
* `Client secret` (only for web applications)

To get those parameters, [create a service in Veracity](../../developerexperience/introduction.md) or use an exisiting service.

To see the `Client ID` or `Client secret`:
* In the [Project Portal](https://developer.veracity.com/projects), select your app, service, or API. It may be grouped under a Resource Group.
* Select the "Settings" tab.

To configure the Reply URL:
* In the [Project Portal](https://developer.veracity.com/projects), select your app, service, or API. It may be grouped under a Resource Group.
* Select the "Configure" tab.

Below you can see other parametrs for authenticating API calls.

Parameter|Value
-|-
Tenant ID|`a68572e3-63ce-4bc1-acdc-b64943502e9d`
Policy|`B2C_1A_SignInWithADFSIdp`
Services API scope|`https://dnvglb2cprod.onmicrosoft.com/83054ebf-1d7b-43f5-82ad-b2bde84d7b75/user_impersonation`
Data Fabric API scope|`https://dnvglb2cprod.onmicrosoft.com/37c59c8d-cd9d-4cd5-b05a-e67f1650ee14/user_impersonation`

Note that, by  default, each API can call [Veracity MyServices API](https://developer.veracity.com/docs/section/identity/services-openapi). However, to call other [Veracity APIs](https://developer.veracity.com/api), you will need subscription keys for them. To get them, contact the [onboarding team](onboarding@veracity.com). 

## Meta data endpoint
You can get additional information from the metadata endpoint:

```
https://login.veracity.com/{tenantid}/v2.0/.well-known/openid-configuration?p={policy}
```

Before calling the endpoint, replace the placeholders with the following parameters.

Parameter|Value
-|-
Tenant ID|`a68572e3-63ce-4bc1-acdc-b64943502e9d`
Policy|`B2C_1A_SignInWithADFSIdp`