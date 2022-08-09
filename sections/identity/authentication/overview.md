---
author: Veracity
description: Gives an overview of the Veracity Identity services and related components.
---

# Overview of the Veracity Identity Provider
The Veracity Identity Provider allows applications to securely authenticate users as well as verify that they are who they claim to be. Authentication is performed using the OpenID Connect protocol and will result in a verifiable JSON Web Token containing some basic information about the user. During the OpenID Connect operation you may also ask for an access token that will give the application access to core Veracity APIs (such as the Services API) which in turn can provide additional user information or allow your applcation to execute operations on the users behalf.

When working with user information it is vitally important to always adhere to security best practices and principles. The data your application is able to access is personal to the user and you should therefore only request information you absolutely need, never store it unnecessarily and in general ensure it is properly handled in all stages of your application. The Veracity IDP ensures the users data is protected at rest and compliant with industry standards. But as soon as your application retrieves any of this information you are responsible for it. Always check local and international laws regarding working with user identifiable information.

## Veracity IDP integration
Integrating with the Veracity IDP is handled differently depending on what you are building, but in general it boils down to two primary use cases:

- Applications that directly interact with the user. This includes web applications and native applications where the user will log in and perform operations.
- Applications that perform operations based on requests from other applications. These include services like REST APIs that do not directly interact with users, but receives requests from other applications.

Applications that directly interact with users need to perform an authentication step before they can execute requests on behalf of the user. This authentication step entails redirecting the user to the Veracity IDP login page and returning them back once they have successfully been verified as users in Veracity. The technical details of how the login is performed is not something your application needs to worry about. Simply direct the user to the Veracity IDP and it will handle the rest. Successful responses from the Veracity IDP means you can trust the user is who they claim to be (provided you validate the reponse).

<figure>
	<img src="assets/basic-oidc-authentication.png"/>
	<figcaption>An application with direct user interaction can redirect the user to the login page to authenticate them.</figcaption>
</figure>

APIs and other services that are not intended to interact directly with users and instead are ment to service requests coming from others such as a web application or native application do not need to authenticate the user in the same way. They will still need to vet the user as an authenticated user however and validate that they have sufficient permissions to perform the action they are requesting. Since such an API has no direct interactions it cannot redirect the user to a login page or similar in order to verify who they are so the code calling the API must provide information that allows you to be sure the user is who they claim to be.

<figure>
	<img src="assets/api-verification-sequence.png"/>
	<figcaption>A application receiving calls from another will have to validate the incomming request as well as the access token provided to ensure the user is who they claim to be.</figcaption>
</figure>

To get more details on how to perform authentication see the technical implementation guidelines in the Authentication sub-section.

## Additional authorization
The Veracity IDP provides authentication for any application registered with the platform. This allows your application to verify that the user logging in is who they claim to be. *Authorization* on the other hand is not handled by the Veracity IDP except for access to other Veracity APIs such as Services or Data Fabric. If you need authorization services you will have to implement this for your own application yourself. You may use information retrieved from the Veracity IDP to identify the user and then look up permissions for that user within your own database based on that. The user identity token provides a claim called `userId` that can be used to uniquely identify the specific user.