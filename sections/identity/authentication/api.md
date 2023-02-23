---
author: Veracity
description: Describes the required authentication mechanism for APIs provided with a bearer token
---

# Authentication for APIs

Each call to an API within the Veracity ecosystem should provide a relevant access token placed in the `Authorization header` of the request as a `Bearer token`.

Note that your API needs to handle authorization internally because Veracity Identity Provider (Veracity IDP) does not do that.

Your API should follow the process outlined below.
1. Receive the incoming request and extract the `Bearer` token from the `Authorization` header.
2. [Validate and decode the token](#validate-access-token).
3. Look up if the user has permission to perform the requested operation (for example, the API can access its database of users indexed by `userId` claim from the access token and retrieve additional information).
4. If the token is valid and the user has permission to do an action, perform the request and return a response.

For old APIs, see the [known security flaw](../whatsnew.md#api-security-flaw).

<figure>
	<img src="../assets/api-verification-sequence.png"/>
</figure>

## Validate access token
To validate the access token, your API needs additional information about OAuth configuration for Veracity IDP. You can get this information from the metadata endpoint:

```
https://login.veracity.com/{tenantid}/v2.0/.well-known/openid-configuration?p={policy}
```

Before calling the endpoint, replace the placeholders with the following parameters.

Parameter|Value
-|-
Tenant ID|`a68572e3-63ce-4bc1-acdc-b64943502e9d`
Policy|`B2C_1A_SignInWithADFSIdp`

Below you can see a sample response from the metadata endpoint.


```json
{
  "issuer": "https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/",
  "authorization_endpoint": "https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/oauth2/v2.0/authorize?p=b2c_1a_signinwithadfsidp",
  "token_endpoint": "https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/oauth2/v2.0/token?p=b2c_1a_signinwithadfsidp",
  "end_session_endpoint": "https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/oauth2/v2.0/logout?p=b2c_1a_signinwithadfsidp",
  "jwks_uri": "https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/discovery/v2.0/keys?p=b2c_1a_signinwithadfsidp",
  "response_modes_supported": [
    "query",
    "fragment",
    "form_post"
  ],
  "response_types_supported": [
    "code",
    "code id_token",
    "code token",
    "code id_token token",
    "id_token",
    "id_token token",
    "token",
    "token id_token"
  ],
  "scopes_supported": [
    "openid"
  ],
  "subject_types_supported": [
    "pairwise"
  ],
  "id_token_signing_alg_values_supported": [
    "RS256"
  ],
  "token_endpoint_auth_methods_supported": [
    "client_secret_post",
    "client_secret_basic"
  ],
  "claims_supported": [
    "dnvglAccountName",
    "myDnvglGuid",
    "userId",
    "oid",
    "name",
    "given_name",
    "family_name",
    "sub",
    "email",
    "upn",
    "mfaType",
    "mfa_required",
    "authenticatedBy",
    "iss",
    "iat",
    "exp",
    "aud",
    "acr",
    "nonce",
    "auth_time"
  ]
}
```

When validating the token:
1. Conform to [current best practice for OAuth token validation](https://auth0.com/docs/tokens/guides/access-token/validate-access-token#json-web-token-jwt-access-tokens).
2. Validate the token's signature using the relevant JSON Web Token key. For a list of public key signatures, see the `jwks_uri` endpoint in the metadata.
3. Optionally, [read more about validating the signature](https://learn.microsoft.com/en-us/azure/active-directory/develop/access-tokens#validating-the-signature).

This lets you confirm that the token:
* was issued by Veracity
* is not expired
* was signed by Veracity IDP

However, suppose any of the validation steps fail. In that case, your API must reject the token and return a `401 Unauthorized` response indicating to the calling code that the token is invalid and you will not handle the request.