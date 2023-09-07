---
author: Mariusz Klimek (DNV)
description: Acquiring access token using MSAL in C#
---

[Previous - 3. Configuring Client application in Veracity](3-client-creation-in-veracity.md)

In order to acquire a client credentials token in your .NET application, first you need to make sure you have the following NuGet package added to your dependencies:

```
Microsoft.Identity.Client
```

To acquire an access token you can use the following snippet:

```
using Microsoft.Identity.Client;

...

await ConfidentialClientApplicationBuilder.Create(appId)
    .WithClientSecret(clientSecret)
    .WithB2CAuthority(instance)
    .Build()
    .AcquireTokenForClient(scopes)
    .ExecuteAsync();
```

Where the used variables are:

|Variable|Where to get it|
|--|--|
|appId|In the settings tab inside of Veracity Resource|
|clientSecret|In the settings tab inside of Veracity Resource. You can generate more than one, but it can be saved by you only on creation. |
|instance|Is composed of: `https://dnvglb2cprod.b2clogin.com/tfp/{tenant}/b2c_1a_signinwithadfsidp/` remember to replace `{tenant}` with the proper value.|
|scopes|`https://dnvglb2cprod.onmicrosoft.com/{appId}/.default`, where you replace `{appId}` with the mentioned before appId from Veracity Developer Portal|

The following code returns an object of `Task<AuthenticationResult>`. AuthenticationResult has a property of AccessToken which will serve as the token you will send to your API.

Remember, just because your `appId` is registered in Veracity, does it mean these are the only steps that require your attention. Make sure, your API validates each request, its appId and the permissions you want to grant it. 

Next up, we will validate the token we just acquired.

---

[Previous - 3. Configuring Client application in Veracity](3-client-creation-in-veracity.md) --- [Next - 5. Validating a Client Credentials Token](5-validating-cc-token.md)
