---
author: Veracity
description: Describes Multi Factor Authentication with Veracity Identity
---

# Multi-Factor Authentication (MFA)
*Note!* Currently only phone-based MFA (SMS or call) is supported. Support for push notification to Microsoft’s Authenticator app will be supported as soon as Microsoft supports it for their Azure AD B2C tenants.

## Types of Multi-Factor Authentication offered by Veracity

### Service-specific MFA
A service can invoke MFA for all users of its service or for certain functions within its service. This is accomplished by sending the following parameter in the login request:

*mfa_required=true*

If only certain functions within a service shall invoke MFA, then the service can upon usage of the function redirect the user to Veracity login adding the mentioned parameter. If MFA shall only be invoked for certain users of a service (such as admin users), then after a successful standard login, the service can redirect the user back to Veracity login adding the mentioned parameter, and MFA will then be invoked.

Example of logon request invoking MFA:

```url
https://login.veracity.com/dnvglb2cprod.onmicrosoft.com/oauth2/v2.0/authorize?p=B2C\_1A\_SignInWithADFSIdp&client\_id=842ec61b-26cf-4adf-adfb-e05dac4d4eee&nonce=defaultNonce&redirect\_uri=https%3A%2F%2Fjwt.ms&scope=openid&response\_type=id\_token&mfa\_required=true
```

### User-initiated MFA
A user can choose to always use MFA for any service they use in Veracity. This can be done by toggling the following option in the user’s profile:

<figure>
	<img src="assets/user-initiated-mfa.png" alt="Toggle mfa"/>
</figure>

## Invoking MFA on user authentication
When MFA is invoked, it will by default only be invoked once during the lifetime of the user’s session. The session lifetime for B2C is set to 8 hours but will be terminated if user closes the browser. This means that if the user has already done MFA previously in the session, e.g. a service requested it, he will by default not be prompted again if he navigates to a new service that also requires MFA.
A service can decide to force MFA even if it has already been done earlier in the session by sending the parameters *\_mfa\_required=true&prompt=login\_* in the login request. User will then be asked both to log in and do MFA.

## Verifying that MFA has been done
In order to verify that MFA has been completed in the session, you can look for the claim *mfaType* which should have the value *phone*. If no MFA has been done, it has the value *none*.
If it is a federated user (federated user means that user logs in to Veracity with an account in their own company), and MFA is invoked on federated company side, MFA will not be prompted again on Veracity side. The claim *mfaType* will then have the value *federatedIdP*.