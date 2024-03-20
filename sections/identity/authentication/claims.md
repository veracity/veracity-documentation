---
author: Veracity
description: Description of the claims suppored by Veracity Identity Provider.
---

# Claims
Claim name | Description | Comments
--- | --- | ---
sub | Veracity Id | <ul><li>Shall be used as the unique user identifier for all services on the Veracity platform</li><li>All lower case</li></ul>
aud | The identifier (client id) of the app that this token is issued for | <ul><li>For id tokens, the value is the client id of the app making the login request</li><li>For access tokens, the value matches the client id of the app for which you requested an access token (defined in the "scope" value of the login request)</li></ul>
mfa_required | Has the value "true" if multi-factor authentication (MFA) was requested for the login |
given_name | First Name |
family_name | Surname |
name | Display Name |
email | E-mail address |
upn | Sign in name | <ul><li>Will be same as email address for all standard users (some legacy users may have a different value)</li></ul>
mfa | <div>Indicates whether multi-factor authentication (MFA) was part of the logon process (true/false)</li></ul></div> |
mfaMethod | <div>Indicates what type of multi-factor authentication (MFA) was done:<ul><li>none – No MFA</li><li>totp – MFA was completed using Veracity's MFA solution with verification by code from user's authenticator app</li><li>phone – MFA was completed using Veracity's MFA solution with verification by SMS or call to user's phone</li><li>federatedIdp - Only relevant for SSO-based users that log in to Veracity with an account in their own company. This value means that MFA is invoked in the user's own company and Veracity will by design not prompt for MFA again.</li></ul></div> |
authenticatedBy | Indicates which organization's Identity Provider authenticated the user. |

## Obsolete claims - To be deprecated
Claim name | Description | Comments
--- | --- | ---
mfaType | <div>Legacy - indicates whether multi-factor authentication (MFA) was part of the logon process:<ul><li>none – No MFA</li><li>phone – MFA was completed using Veracity's MFA solution (either TOTP or SMS/Call)</li><li>federatedIdp - Only relevant for SSO-based users that log in to Veracity with an account in their own company. This value means that MFA is invoked in the user's own company and Veracity will by design not prompt for MFA again.</li></ul></div> | <ul><li>This claims supports implementations of MFA that was done before TOTP was introduced.</li><li>Do not use, use "mfa" and "mfaMethod" instead.</li><li>Will be deprecated at some point, but information will be provided to services well in advance.</li></ul> |
myDnvglGuid | Veracity Id | <ul><li>Do not use, use "sub" instead.</li><li>Will be deprecated at some point, but information will be provided to services well in advance.</li></ul>
userId | Veracity Id | <ul><li>Do not use, use "sub" instead.</li><li>Will be deprecated at some point, but information will be provided to services well in advance.</li></ul>
dnvglAccountName | sAMAccountName/short username | <ul><li>Do not use -  will be deprecated.</li><li>Lacks a value for federated users.</li></ul>
myDnvglGuid | Veracity Id | <ul><li>Do not use, use "sub" instead.</li><li>Will be deprecated at some point, but information will be provided to services well in advance.</li></ul>
oid | Object ID | <ul><li>Do not use.</li><li>"sub" claim (Veracity Id) shall be used as unique user identifier.</li></ul>
