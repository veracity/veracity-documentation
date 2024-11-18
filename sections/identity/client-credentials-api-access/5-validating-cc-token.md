---
author: Mariusz Klimek (DNV)
description: Validating access token in your API in C#
---

# Validate access token in your API in C#

[Previous - 4. Acquiring access token using MSAL in C#](4-msal-access-token.md)

This tutorial will help you build a Client Credentials validator in your .NET 6 API. Note that all code samples are for C#.

First we need to declare a class that inherits from `AuthenticationSchemeOptions`:

```
using Microsoft.AspNetCore.Authentication;
using System.Security.Claims;

...

public class MyAuthenticationOptions : AuthenticationSchemeOptions
{
    public ClaimsIdentity Identity { get; set; } = default!;
}
```

Then we need to declare a class that inherits from `AuthenticationHandler`:

```
public class MyAuthenticationHandler : AuthenticationHandler<MyAuthenticationOptions>
{
    public MyAuthenticationHandler(
        IOptionsMonitor<MyAuthenticationOptions> options,
        ILoggerFactory logger,
        UrlEncoder encoder,
        ISystemClock clock) : base(options, logger, encoder, clock)
    {
    }
 
    protected override Task<AuthenticateResult> HandleAuthenticateAsync() 
        => Task.FromResult(Authenticate());
}
```

Next we will implement the `Authenticate()` method:

```
using Microsoft.AspNetCore.Authentication;

...

private AuthenticateResult Authenticate()
{
    try
    {
        // First we need to extract the Bearer token from the headers
        // (for logic check below to see the implementation of the 
        // ExtractBearerToken method)
        var rawToken = ExtractBearerToken(Request.Headers["authorization"]);
        if (string.IsNullOrWhiteSpace(rawToken))
            return AuthenticateResult.Fail("Authorization header not provided");

        // Next, we validate the token. For the purpose of clarity 
        // it was extracted to a separate method
        var tokenValidationResult = Validate(rawToken.Value);

        if (tokenValidationResult == null)
            return AuthenticateResult.Fail("Authorization failed: ");

        var ticket = new AuthenticationTicket(tokenValidationResult.Value, new AuthenticationProperties(), Scheme.Name);

        return AuthenticateResult.Success(ticket);
    }
    catch (Exception e)
    {
        return AuthenticateResult.Fail(e);
    }
}

// This method verifies that the Authorization header is properly formed
// and then extracts the token itself
private static string ExtractBearerToken(string authorizationHeader)
{
    if (string.IsNullOrWhiteSpace(authorizationHeader) || !authorizationHeader.StartsWith("Bearer "))
        return string.Empty;

    var bearerToken = authorizationHeader.Replace("Bearer ", string.Empty, StringComparison.OrdinalIgnoreCase);
    return bearerToken;
}
```

To validate the token we will use the Stardust NuGet package which is made by Veracity developers. The main logic for validating a token is within the Validate method which you can see below:

```
using Stardust.Aadb2c.AuthenticationFilter.Core;
using Stardust.Particles;

...

private ClaimsPrincipal? Validate(string rawToken)
{
    B2CGlobalConfiguration.ValidIssuer = configuration.Issuer;
    B2CGlobalConfiguration.Audience = configuration.Audience;
    B2CGlobalConfiguration.AadTenants = new[] { configuration.OpenIDConfiguration };
    B2CGlobalConfiguration.AllowClientCredentialsOverV2 = true;
    ConfigurationManagerHelper.SetValueOnKey("certificateRefresInterval", "30");
    ClaimsPrincipal authenticatedUser;

    try
    {
        authenticatedUser = TokenValidator.Validate(rawToken);

        return authenticatedUser;
    }
    catch (Exception ex)
    {
        // log exception

        return null;
    }
}
```

In this code we used an object named `configuration` in which we stored some values. This is where you can get them:

|Variable|Where to get it|
|--|--|
|Issuer|`https://login.microsoftonline.com/{tenant}/v2.0/;https://dnvglb2cprod.b2clogin.com/{tenant}/v2.0/;https://login.veracity.com/{tenant}/v2.0/`|
|Audience|`{appId}`. In the settings tab inside of Veracity Resource.|
|OpenIDConfiguration|`https://login.veracity.com/{tenant}/v2.0/.well-known/openid-configuration?p=B2C_1A_SignInWithADFSIdp`|

All these classes should now be declared in the `Program.cs` class. To make it more readable I suggest to create it as an extension method declated in a separate class:

```
internal static class AuthorizationExtensions
{
    const string AuthenticationDefaultScheme = "DefaultScheme";

    public static void SetupAuthorization(this WebApplicationBuilder builder)
    {
        builder.Services
            .AddAuthentication(options =>
            {
                options.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
                options.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
                options.DefaultScheme = JwtBearerDefaults.AuthenticationScheme;
            })
            .AddScheme<MyAuthenticationOptions, MyAuthenticationHandler>(JwtBearerDefaults.AuthenticationScheme, string.Empty, o => { });

        builder.Services.AddAuthorization(x =>
        {
            x.AddPolicy(
                AuthenticationDefaultScheme,
                policyBuilder => policyBuilder.RequireAuthenticatedUser());
        });
    }
}
```

And then simply using it:

```
builder.SetupAuthorization();
```

All of the above code will help you validate the Client Credentials token, but it will only test the validity of the token based on the provided data (issuer, audience, OpenIDConfiguration, etc.). At this point, **it's good to implement authorization and check what can the given appId do, and what it can't, as this is something that should be implemented on the side of your API**.

---

[Previous - 4. Acquiring access token using MSAL in C#](4-msal-access-token.md) --- [Next - 6. Summary](6-summary.md)
