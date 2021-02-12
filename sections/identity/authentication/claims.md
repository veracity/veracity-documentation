---
author: Veracity
description: Detailed description of the claims supported by Veracity IDP
---

# Claims
Claim name | Description | Comments
--- | --- | ---
sub | Veracity Id | <ul><li>Shall be used as the unique user identifier for all services on the Veracity platform</li><li>All lower case</li></ul>
aud | The identifier (client id) of the app that this token is issued for | <ul><li>For id tokens, the value is the client id of the app making the login request</li><li>For access tokens, the value matches the client id of the app for which you requested an access token (defined in the “scope” value of the login request)</li></ul>
mfa_required | Has the value “true” if multi-factor authentication (MFA) was requested for the login |
userId | Veracity Id | <ul><li>Do not use, use “sub” instead</li><li>Will be deprecated at some point, but information will be provided to services well in advance</li></ul>
given_name | First Name |
family_name | Surname |
name | Display Name |
dnvglAccountName | sAMAccountName/short username | <ul><li>Do not use -  will be deprecated</li><li>Lacks a value for federated users</li></ul>
myDnvglGuid | Veracity Id | <ul><li>Do not use, use “sub” instead</li><li>Will be deprecated at some point, but information will be provided to services well in advance</li></ul>
oid | Object ID | <ul><li>Do not use</li><li>“sub” claim (Veracity Id) shall be used as unique user identifier</li></ul>
email | E-mail address |
upn | Sign in name | <ul><li>Will be same as email address for all standard users (some legacy users may have a different value)</li></ul>
mfa_type | <div>Indicates whether multi-factor authentication (MFA) was part of the logon process:<ul><li>None – No MFA</li><li>Phone – MFA was completed using verification by SMS to user’s phone</li></ul></div> |
authenticatedBy | <div>Indicates which organization’s Identity Provider authenticated the user.<br/><br/>Currently it can contain the following values: <br/><ul><li>https://veracity.com – means user was authenticated by the Veracity IdP, i.e. the account is not federated, but a local account in the Veracity Identity store</li><li>https://dnv.com – means user was authenticated by DNV’s IdP (i.e. VERIT AD through ADFS farm fsint1.dnv.com, later Azure AD when logon page is switched to Azure AD B2C)</li><li>https://bp.com – means user was authenticated by BP’s Identity Provider (i.e. BP’s Azure AD tenant)</li><li>https://akersolutions.com – means user was authenticated by Aker Solutions’ Identity Provider (i.e. Aker Solutions’ Azure AD tenant)</li><li>https://pacificbasin.com – means user was authenticated by Pacific Basin’s Identity Provider (i.e. Pacific Basin’s ADFS farm)</li><li>https://fedtest.com – means user was authenticated by our federation test farm (using ADFS) </li></ul></div> |