---
author: Veracity
description: Gives an overview of the Veracity Identity services and related components.
---

# Overview of the Veracity Identity Provider
The Veracity Identity Provider (Veracity IDP) uses the OpenID Connect protocol to authenticate users and generate a verifiable JSON Web Token containing basic user information.

If you need additional user information or want to execute some operations on user's behalf, you can request an access token that will give your application the access to core Veracity APIs (such as Services API).

## Protect user data

The user data you access from Veracity IDP requires protection according to local and international laws. When you receive personal user data from Veracity IDP, you become responsible for securing it. Because of that:
* Request only the information that you need.
* If possible, avoid storing user data, and delete it when it is no longer necessary.
* Ensure that user data is handled securely inside your application or service.

## Integrate with Veracity IDP
There are two most common authentication scenarios:
* Applications directly interacting with users.
* Applications without direct user interaction that perform operations based on requests from other applications (such as REST APIs).

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
