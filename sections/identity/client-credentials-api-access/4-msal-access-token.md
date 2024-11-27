---
author: Mariusz Klimek (DNV)
description: Acquiring access token using MSAL in C#
---

# Getting an access token

[Previous - 3. Configuring Client application in Veracity](3-client-creation-in-veracity.md)

In this chapter we will acquire an access token for your client application.

The following examples are written in .NET.

In order to acquire a client credentials token in your .NET application, first you need to make sure you have the following NuGet package added to your dependencies:

```
Microsoft.Identity.Client
```

To acquire an access token you can use the following snippet:

```
using Microsoft.Identity.Client;

...

await ConfidentialClientApplicationBuilder.Create(clientId)
    .WithClientSecret(clientSecret)
	.WithAuthority(authority)
    .Build()
    .AcquireTokenForClient(scopes)
    .ExecuteAsync();
```

Where the used variables are:

|Variable|Where to get it|
|--|--|
|clientId|In the Settings tab inside of your client application in developer.veracity.com|
|clientSecret|In the Settings tab inside of your client application in developer.veracity.com. You can generate more than one, but it can be saved by you only on creation.|
|authority|`https://login.veracity.com/tfp/a68572e3-63ce-4bc1-acdc-b64943502e9d/B2C_1A_SignInWithADFSIdp/v2.0`|
|scopes|`https://dnvglb2cprod.onmicrosoft.com/{API_ID}/.default`, where you replace `{API_ID}` with the `App / Api ID` from your API's Settings tab in developer.veracity.com. Although we set up a `my_scope` scope, in order to get the token we still write `.default`|

The following code returns an object of `Task<AuthenticationResult>`. AuthenticationResult has a property of AccessToken which will serve as the token you will send to your API.

Remember, just because your `appId` is registered in Veracity, doesn't mean these are the only steps that require your attention. Make sure, your API validates each request, its appId and the permissions you want to grant it. 

Next up, we will validate the token we just acquired.

---

[Previous - 3. Configuring Client application in Veracity](3-client-creation-in-veracity.md) --- [Next - 5. Validating a Client Credentials Token](5-validating-cc-token.md)
