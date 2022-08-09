---
author: Veracity
description: A general description of the Veracity Identity Service plus useful resources.
---

# Overview
Veracity Identity is the Identity Provider (IDP) for the Veracity Platform. It provides a secure authentication mechansim for 1st and 3rd party services as well as authorization for 1st parties. The service is built upon Microsoft Azure B2C and uses common industry standards such as **OpenID Connect** and **Authorization code flow** to authenticate users.
The Veracity IDP provides authentication for any application registered with the platform. This allows your application to verify that the user logging in is who they claim to be. 

## Benefits
The Veracity Identity Provider (IDP) also provides federation services other industry leading companies in order to allow single-sign-on for users accross the sector. Using the Veracity IDP allows you not only to securely authenticate your own users, but you can also instantly provide access to users of other companies federated with Veracity.

This documentation contains information about how the Veracity IDP works, how to integrate with it and some general information about the underlying protocols used. You can read more about the core protocols on the Azure documentation pages [here](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-app-types).

## Quick navigation
If you want to jump straight into implementation you can:
* Go to a detailed tutorial for [Creating a NodeJS app with Veracity](nodejs-webapp-ts/1-introduction.md).
* See our useful libraries on our [Veracity GitHub page](https://github.com/veracity).

## Support
If you are a customer with Veracity and are having issues with authentication you can email support at [support@veracity.com](mailto:support@veracity.com)

## Veracity IDP metadata endpoint
To obtain information about the configuration of the implementation of the OAuth 2.0 in Veracity, call the metadata endpoint:
https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/.well-known/openid-configuration?p=B2C_1A_SignInWithADFSIdp

This endpoint returns useful information for configuring authentication with Veracity IDP.

## Parameters for authentication
Tenant ID a68572e3-63ce-4bc1-acdc-b64943502e9d

Policy B2C_1A_SignInWithADFSIdp

The API used by Veracity IDP is called Services API. It's scope is https://dnvglb2cprod.onmicrosoft.com/83054ebf-1d7b-43f5-82ad-b2bde84d7b75/user_impersonation

The scope for the Data Fabric API is https://dnvglb2cprod.onmicrosoft.com/37c59c8d-cd9d-4cd5-b05a-e67f1650ee14/user_impersonation

## Claims
Claim name | Description | Comments
--- | --- | ---
sub | Veracity Id | <ul><li>Shall be used as the unique user identifier for all services on the Veracity platform</li><li>All lower case</li></ul>
aud | The identifier (client id) of the app that this token is issued for | <ul><li>For id tokens, the value is the client id of the app making the login request</li><li>For access tokens, the value matches the client id of the app for which you requested an access token (defined in the “scope” value of the login request)</li></ul>
mfa_required | Has the value “true” if multi-factor authentication (MFA) was requested for the login |
given_name | First Name |
family_name | Surname |
name | Display Name |
email | E-mail address |
upn | Sign in name | <ul><li>Will be same as email address for all standard users (some legacy users may have a different value)</li></ul>
mfa_type | <div>Indicates whether multi-factor authentication (MFA) was part of the logon process:<ul><li>none – No MFA</li><li>phone – MFA was completed using Veracity's MFA solution with verification by SMS or call to user’s phone</li><li>federatedIdp - Only relevant for federated users, means that MFA was completed by the federated Identity Provider</li></ul></div> |
authenticatedBy | Indicates which organization’s Identity Provider authenticated the user. |

## Obsolete claims - To be deprecated
Claim name | Description | Comments
--- | --- | ---
userId | Veracity Id | <ul><li>Do not use, use “sub” instead</li><li>Will be deprecated at some point, but information will be provided to services well in advance</li></ul>
dnvglAccountName | sAMAccountName/short username | <ul><li>Do not use -  will be deprecated</li><li>Lacks a value for federated users</li></ul>
myDnvglGuid | Veracity Id | <ul><li>Do not use, use “sub” instead</li><li>Will be deprecated at some point, but information will be provided to services well in advance</li></ul>
oid | Object ID | <ul><li>Do not use</li><li>“sub” claim (Veracity Id) shall be used as unique user identifier</li></ul>