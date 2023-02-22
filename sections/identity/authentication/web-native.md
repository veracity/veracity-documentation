---
author: Veracity
description: Detailed description of how authentication with Veracity IDP works for a web apps.
---

# Authentication for Web and Native Applications
Authentication for web and native applications is similar and differs only in the parameters that are sent.

To authenticate a user:
1. Redirect the user to sign in to Veracity.
2. After the user sucessfully authenticates, await the validation response from Veracity IDP.
3. Validate the response.
4. Optionally, exchange an authorization code for an access token.
5. Optionally, validate the access token.

If you only need to authenticate the user with Veracity IDP and you will not call any Veracity APIs,  you can skip steps number four and five. 

<figure>
	<img src="../assets/basic-oidc-authentication.png"/>
</figure>

## To authenticate users

1. Go to the meta data URL in your browser: https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/.well-known/openid-configuration?p=B2C_1A_SignInWithADFSIdp
2. Copy the value for the `authorization_endpoint`.
3. For the authentication requests, specify and encode required parameters. For details, see [required parameters](#required-parameters) below.
4. Ensure that all parameters are URL encoded, so that they will remove any illegal values from the URL. For details, see [URL encoding](#url-encoding) below.
5. To authenticate users, redirect them to the `authorization endpoint`. The user will sign in to Veracity, and then Veracity IDP will issue a POST request to your specified `redirect_uri` with all the parameters requested in the `response_mode`. Below you can see a sample response.
  ```json
{
	state: "8ohxSOcjcvkB1JfS6yIJE",
	code: "eyJraWQiOiJhOXZ5SjJVX25SM3ZmakZubEpUQlFLbHhfUFF3UDhqU...",
	id_token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImVnR..."
}
```
6. Before you start using the `id_token` or `code`, [validate them](https://auth0.com/docs/secure/tokens/id-tokens/validate-id-tokens).
7. Optionally, after validating the `id_token`, you can use the `c_hash` claim from the from the `id_token` to validate the authorization code (`code`).

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

For help on finding `client_id` and `redirect_uri`, [go here](overview.md#parameters-for-user-authentication).

For `state`, note that this parameter is meant to contain data that will be returned to your application after the user is authenticated. You may encode in it anything you want. However, it is commonly used in place of a nonce to prevent cross-site scripting attacks. If you want to send actual data in this parameter, consider adding a nonce value that you validate once the request comes back.

For details on parameters, [go here](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow#request-an-authorization-code).

### URL encoding
Ensure that all parameters are URL encoded, so that when they are sent, all illegal characters are removed from the URL. With Node or JavaScript, you can do this using the `encodeURIComponent` function. (for details, [go here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)). 

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
1. For a web application, construct an HTTPS `POST` request from your server-side-code. For a native application, construct the request internally.
2. In the request, encode the parameters listed below as the `application/x-www-form-urlencoded` payload. For details,  ([go here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)).
3. Send the request to the `token_endpoint` URL that you have checked in the meta data endpoint before.

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

Below you can see an example of a sucessful request that has returned an access token. An access token allows making authorized requests on behalf of the user against the API endpoints defined in the `scope` parameter.

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

### Validate access token

After getting an access token, you should validate it.

You now need to validate the access token and as you did with the identity token earler and store it away safely within your application. 

You should also have received a refresh token (if you requested the scope `offline_access` earlier). This token can be used to ask for a new access token later should the current one expire. It cannot be used to access any services itself. 

Veracity does not directly disclose the lifetime for either the access token or refresh token as it may be changed without warning in response to security changes. Your application must know how to deal with both an expired access token and refresh token and prompt the user to log in once more if the latter expires.

## To send an API request

After getting an access token, you can send requests to the API specified in the `scope` parameter:
1. Construct an HTTPS request to the relevant endpoint.
2. In the request, add the access token in the `Authorization` header as a bearer token.
3. In the request, add your subscription key for the API.

Below you can see an example of a request to the `/my/profile` endpoint of the Services API.

```
GET https://api.veracity.com/Veracity/Services/V3/my/profile HTTP/1.1
Host: api.veracity.com
Ocp-Apim-Subscription-Key: [subscription-key]
Authorization: Bearer [token]
```

## Logging out
The logout process for a user involves two steps:

1. Clear all local session data for your application.
2. Redirect user to `https://www.veracity.com/auth/logout` in order to centrally log them out.

An authenticated user usually has an active session with your application. Such a session may contain access tokens and refresh tokens so that your application can query Veracity and other APIs as needed. Logging users out correctly is a vital part of a secure application as it will mitigate potential misuse of the access tokens the user has acquired. Access tokens issued by Veracity cannot normally be revoked thus you need to ensure that you are in complete control of the access token and that it never leaves your trusted application core. Once the user decides they are done with your service for the day and sign out you must also ensure the access and refresh tokens are deleted. This is done by clearing all session data upon logout.

In ExpressJS with Passport this is usually as easy as calling `request.logout()` and there are probably equivalent methods within your preferred library. Once a user starts the logout process this is the first thing you should do. Clearing session data (if done correctly) will delete any access and refresh tokens you acquired for the user earlier thus preventing access in the future. Once complete the user has been logged out from your system, but not from Veracity as a whole yet. In order log them out completely you need to also redirect them to the central logout endpoint on `https://www.veracity.com/auth/logout`. This will perform a Single-Sign-Out of all internal and other third-party services ensuring the session is properly terminated. After this the user is prompted to close their browser in order to clear any remaining session data. Only then is the user completely signed out.

**Note**: Veracity does not provide any mechanism for routing the user back to your application after being redirected to the Single-Sign-Out endpoint. This is by design in order to prompt them to close their browser to complete the sign-out process.
