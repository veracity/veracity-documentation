---
author: Veracity
description: Describes Multi Factor Authentication with Veracity Identity
---

# Multi-Factor Authentication (MFA)

## Types of Multi-Factor Authentication offered by Veracity

### Service-initiated MFA
A service can invoke MFA for all users of its service or for certain functions within its service. This is accomplished by sending the following parameter in the login request:

**NOTE! Due to a bug that has not been solved yet, the value of mfa_required must be in lower case (_true_)**

*mfa_required=true*

If only certain functions within a service shall invoke MFA, then the service can upon usage of the function redirect the user to Veracity login adding the mentioned parameter. If MFA shall only be invoked for certain users of a service (such as admin users), then after a successful standard login, the service can redirect the user back to Veracity login adding the mentioned parameter, and MFA will then be invoked.

Example of logon request invoking MFA:

<code style="overflow-wrap: break-word">
https://login.veracity.com/dnvglb2cprod.onmicrosoft.com/oauth2/v2.0/authorize?p=B2C_1A_SignInWithADFSIdp&client_id=58d531de-c4f6-4fce-b792-4a1edfe32e2d&nonce=defaultNonce&redirect_uri=https%3A%2F%2Fjwt.ms&scope=openid&response_type=id_token<strong>&mfa_required=true</strong>
</code>


### User-initiated MFA
A user can choose to always use MFA for any service they use in Veracity. This can be done on the **Security** page in the user’s profile ref. _link to end user doc_.


## Invoking MFA on user authentication
When MFA is invoked, it will by default only be invoked once during the lifetime of the user’s session. The session lifetime for Veracity login is set to 8 hours but will be terminated if user closes the browser. This means that if the user has already done MFA previously in the session, e.g. a service requested it, he will by default not be prompted again if he navigates to a new service that also requires MFA.

A service can decide to force MFA even if it has already been done earlier in the session by sending the parameters *&mfa_required=true&prompt=login* in the login request. User will then be asked both to log in and do MFA.

## Verifying that MFA has been done
In order to verify that MFA has been completed in the session, you can look for the following claims:

Claim name | Description
--- | ---
mfa | <div>Indicates whether multi-factor authentication (MFA) was part of the logon process:<ul><li>true/false</li></ul></div>
mfaMethod | <div>Indicates what type of multi-factor authentication (MFA) was done:<ul><li>none – No MFA</li><li>totp – MFA was completed using Veracity's MFA solution with verification by code from user's authenticator app</li><li>phone – MFA was completed using Veracity's MFA solution with verification by SMS or call to user's phone</li><li>federatedIdp - Only relevant for SSO-based users that log in to Veracity with an account in their own company. This value means that MFA is invoked in the user's own company and Veracity will by design not prompt for MFA again. </li></ul></div>
mfaType | <div>Legacy - indicates whether multi-factor authentication (MFA) was part of the logon process:<ul><li>none – No MFA</li><li>phone – MFA was completed using Veracity's MFA solution (either TOTP or SMS/Call).</li><li>federatedIdp - Only relevant for SSO-based users that log in to Veracity with an account in their own company. This value means that MFA is invoked in the user's own company and Veracity will by design not prompt for MFA again. </li><li>DO NOT USE. Use "mfa" and "mfaMethod" instead. Will be deprecated at some point, but information will be provided to services well in advance.</li></ul>
