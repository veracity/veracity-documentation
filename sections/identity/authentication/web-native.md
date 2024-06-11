---
author: Veracity
description: Detailed description of how authentication with Veracity IDP works for web apps.
---

# Authentication for Web and Native Applications
Authentication for web and native applications is similar and differs only in the parameters that are sent.

To authenticate a user:
1. Redirect the user to sign in to Veracity.
2. After the user successfully authenticates, await the validation response from Veracity IDP.
3. Validate the response.
4. Optionally, exchange an authorization code for an access token.
5. Optionally, validate the access token.

If you only need to authenticate the user with Veracity IDP and you will not call any Veracity APIs,  you can skip steps number four and five. 

<figure>
	<img src="../assets/basic-oidc-authentication.png"/>
</figure>

## To authenticate users

1. Go to the metadata URL in your browser: https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/.well-known/openid-configuration?p=B2C_1A_SignInWithADFSIdp
2. Copy the value for the `authorization_endpoint`.
3. For authentication requests, specify and encode the required parameters. For details, see [the required parameters](#required-parameters) below.
4. Ensure that all parameters are URL encoded so that they will remove any illegal values from the URL. For details, see [the URL encoding](#url-encoding) below.
5. To authenticate users, redirect them to the `authorization endpoint`. The user will sign in to Veracity, and then Veracity IDP will issue a POST request to your specified `redirect_uri` with all the parameters requested in the `response_mode`. Below you can see a sample response.
  ```json
{
	state: "8ohxSOcjcvkB1JfS6yIJE",
	code: "eyJraWQiOiJhOXZ5SjJVX25SM3ZmakZubEpUQlFLbHhfUFF3UDhqU...",
	id_token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImVnR..."
}
```
6. Before you start using the `id_token` or `code`, [validate them](https://auth0.com/docs/secure/tokens/id-tokens/validate-id-tokens).
7. Optionally, after validating the `id_token`, you can use the `c_hash` claim from the `id_token` to validate the authorization code (`code`).

### Required parameters
Your authentication requests to Veracity IDP need to provide the following parameters.

Parameter|Value
-|-
`client_id`|`[from the Project Portal]`
`scope`|`openid offline_access [plus one of the service scope claims]`
`redirect_uri`|`[Reply URL the Project Portal]`
`state`*|State data you wish the endpoint to send back to you once the user is authenticated.
`response_type`|`code id_token` (if you do not need an access token, skip `code`)
`response_mode`|`form_post`

For help finding `client_id` and `redirect_uri`, [go here](overview.md).

For `state`, note that this parameter is meant to contain data that will be returned to your application after the user is authenticated. You may encode in it anything you want. However, it is commonly used instead of a nonce to prevent cross-site scripting attacks. If you want to send actual data in this parameter, consider adding a nonce value that you validate once the request returns.

For details on parameters, [go here](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow#request-an-authorization-code).

### URL encoding
Ensure that all parameters are URL encoded so that when they are sent, all illegal characters are removed from the URL. You can do this using the `encodeURIComponent` function with Node or JavaScript (for details, [go here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)).

Below you can see an example of a complete encoded URL. Line breaks were added for clarity. This request authenticates the user and returns an authorization code that can be exchanged for an access token with [Veracity MyServices API](../services-openapi.yaml).

```url
https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/oauth2/v2.0/authorize

?p=b2c_1a_signinwithadfsidp
&client_id=6731de76-14a6-49ae-97bc-6eba6914391e
&response_type=code%20id_token
&response_mode=form_post
&redirect_uri=http%3A%2F%2Flocalhost%2Fmyapp%2Fauth-return
&state=uaweghlibuysdahewkbaskjdg
&scope=openid%20offline_access%20https%3A%2F%2Fdnvglb2cprod.onmicrosoft.com%2F83054ebf-1d7b-43f5-82ad-b2bde84d7b75%2Fuser_impersonation
```

## Get an access token for the user

To get an access token for a user:
1. For a web application, construct an HTTPS `POST` request from your server-side code. For a native application, construct the request internally.
2. In the request, encode the parameters listed below as the `application/x-www-form-urlencoded` payload. For details,  ([go here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)).
3. Send the request to the `token_endpoint` URL that you have checked in the metadata endpoint before.

In your request, provide the following parameters required by Veracity IDP. For details on sending parameters to the token endpoint, [go here](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow#request-an-access-token).

Parameter|Value
-|- 
`client_id`|`[from Project Portal]`
`grant_type`|`authorization_code`
`scope`|The same scope string you used with the authentication request.
`code`|The authorization code from the authentication request.
`redirect_uri`|`[Reply URL from Project Portal]`
`client_secret`*|`[from Project Portal; needed only for web apps]`


\* Provide the **client secret** only for web applications, and do not disclose it to anyone except for Veracity IDP.

Below you can see an example of a successful request that has returned an access token. An access token allows making authorized requests on behalf of the user against the API endpoints defined in the `scope` parameter.

```json
{
	"access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSU...",
	"id_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1Ni...",
	"token_type": "Bearer",
	"not_before": "1569076697",
	"expires_in": "3600",
	"expires_on": "1569080297",
	"resource": "83054ebf-1d7b-43f5-82ad-b2bde84d7b75",
	"id_token_expires_in": "3600",
	"profile_info": "eyJ2ZXIiOiIxLjAiLCJ0aWQiOiJhNjg1N...",
	"refresh_token": "eyJraWQiOiJhOXZ5SjJVX25SM3ZmakZu...",
	"refresh_token_expires_in": "1209600"
}
```

### To validate an access token

After getting an access token:
* [Validate the token](https://auth0.com/docs/secure/tokens/access-tokens/validate-access-tokens).
* Store it safely within your application.

### To refresh an access token
If you requested the scope `offline_access`, you would also have a refresh token that can be used to get a new access token after the current one expires. 

Note that:
* Veracity does not directly disclose the lifetime of the access token or refresh token.
* Veracity can change the access and refresh tokens without warning as a response to security changes. 
* Your application needs to be able to handle expiring access and refresh tokens. If the refresh token expires, prompt the user to sign in again.

## To send an API request with an access token

After getting an access token, you can send requests to the API specified in the `scope` parameter:
1. Construct an HTTPS request for the relevant endpoint.
2. In the request, add the access token in the `Authorization` header as a bearer token.
3. In the request, add your subscription key for the API.

Below is an example of a request to the `/my/profile` endpoint of the Services API.

```
GET https://api.veracity.com/Veracity/Services/V3/my/profile HTTP/1.1
Host: api.veracity.com
Ocp-Apim-Subscription-Key: [subscription-key]
Authorization: Bearer [token]
```

## To sign out the user

An authenticated user usually has an active session with your application containing access and refresh tokens to query Veracity IDP and other APIs. Given that those tokens usually cannot be revoked, ensure that:
* The tokens stay within your trusted application core.
* The user is correctly signed out.

To sign out the user:
1. Clear all local session data for your application. In ExpressJS with Passport, you can call `request.logout()` or use an equivalent method within your preferred library. This deletes any access and refreshes tokens that you got for the user.
2. To centrally sign out the user, redirect them to `https://www.veracity.com/auth/logout`. This clears any  remaining session data. 

Note that Veracity does not provide any mechanism for routing the user back to your application after being redirected to the Single-Sign-Out endpoint. This is by design to prompt them to close their browser to complete the sign-out process.

## Redirecting users back to your service after reset password or create account

When users try to access a service that is integrated with the Veracity platform, the user is redirected to the Veracity login page. If the user needs to reset the password or create an account, the user will jump out of the login flow. If you want users to be redirected back to your service after they have reset the password or created an account, you can add the following parameter to the login request:

&appUrl=\<the URL you want the user to be redirected back to\>

Example of logon request:

https://login.veracity.com/dnvglb2cprod.onmicrosoft.com/oauth2/v2.0/authorize?p=B2C_1A_SignInWithADFSIdp&client_id=58d531de-c4f6-4fce-b792-4a1edfe32e2d&nonce=defaultNonce&redirect_uri=https%3A%2F%2Fjwt.ms&scope=openid&response_type=code+id_token&appUrl=https://myservice.com

**NOTE!**
The value of the appUrl parameter must be registered as a “Service URL” on a resource type veracity.service in Veracity Developer.
