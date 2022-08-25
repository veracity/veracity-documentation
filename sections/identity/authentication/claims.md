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
mfa_type | <div>Indicates whether multi-factor authentication (MFA) was part of the logon process:<ul><li>none – No MFA</li><li>phone – MFA was completed using Veracity's MFA solution with verification by SMS or call to user's phone</li><li>federatedIdp - Only relevant for federated users, means that MFA was completed by the federated Identity Provider</li></ul></div> |
authenticatedBy | Indicates which organization's Identity Provider authenticated the user. |

## Obsolete claims - To be deprecated
Claim name | Description | Comments
--- | --- | ---
userId | Veracity Id | <ul><li>Do not use, use "sub" instead</li><li>Will be deprecated at some point, but information will be provided to services well in advance</li></ul>
dnvglAccountName | sAMAccountName/short username | <ul><li>Do not use -  will be deprecated</li><li>Lacks a value for federated users</li></ul>
myDnvglGuid | Veracity Id | <ul><li>Do not use, use "sub" instead</li><li>Will be deprecated at some point, but information will be provided to services well in advance</li></ul>
oid | Object ID | <ul><li>Do not use</li><li>"sub" claim (Veracity Id) shall be used as unique user identifier</li></ul>
