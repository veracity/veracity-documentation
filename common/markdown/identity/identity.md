---
Title : "Identity"
Author: "Brede Børhaug"
Contributors: "Pawel Lehmann, Rachel Hassall, Jonas Syrstad"
---

## Overview  
The Veracity onboarding process has some mandatory and optional requirements for service providers. A key mandatory requirement is that the service provider integrates with our identity provider, enabling the Single Sign On (SSO) experience in Veracity. The Veracity cloud identity provider is Azure AD B2C. It is a highly available global service that scales to hundreds of millions of identities and is built on an enterprise-grade secure platform. Azure AD B2C keeps your applications, your business and your customers protected.

Your Veracity integration will be through Enterprise Accounts (using open standard protocol OpenID Connect). For the documentation on Azure AD B2C visit [Microsoft Azure](https://docs.microsoft.com/en-us/azure/active-directory-b2c/active-directory-b2c-overview).

## Common settings:
|Setting                |Value                                                                                |
|-----------------------|-------------------------------------------------------------------------------------|
|Tenant                 |`a68572e3-63ce-4bc1-acdc-b64943502e9d` or `dnvglb2cprod.onmicrosoft.com`             |
|B2C Metadata Endpoint  |`https://login.microsoftonline.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/.well-known/openid-configuration?p=B2C_1A_SignInWithADFSIdp`
|AadInstance            |`https://login.microsoftonline.com/tfp/{0}/{1}/v2.0/.well-known/openid-configuration`
|SignUpSignInPolicyId   |`B2C_1A_SignInWithADFSIdp`                                                             |
|ClientId               |Provided by Veracity in encrypted mail or in Veracity for Developers                 |
|ClientSecret           |Provided by Veracity in encrypted mail or in Veracity for Developers                 |

To be able to authenticate correclty and get a valid access token you will need to provide the correct scope as part of the configuration sent to Veracity upon authentication. The scopes differ for each service and should be:

Service|Scope
-|-
Services API|`https://dnvglb2cprod.onmicrosoft.com/83054ebf-1d7b-43f5-82ad-b2bde84d7b75/user_impersonation`
Data Fabric API|`https://dnvglb2cprod.onmicrosoft.com/37c59c8d-cd9d-4cd5-b05a-e67f1650ee14/user_impersonation`

You will also receive a serviceId, this id is the unique identifier for your application. This is primarily used with the [Services API](https://developer.veracity.com/doc/service-api) 


## Further reading
We are soon to publish new documentation for all product lines at Veracity. The old documentation with samlple code in this document are out of date and removed. Follow us at GitHub and developer.veracity.com for updates.
