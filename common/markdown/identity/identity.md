---
Title : "Identity"
---
# Overview 
Review state added



# Tutorial


## Azure AD B2C
Azure AD B2C is a cloud identity management solution for your web and mobile applications. It is a highly available global service that scales to hundreds of millions of identities. Built on an enterprise-grade secure platform, Azure AD B2C keeps applications, business, and customers protected.

Below code describes how to connect to Azure AD B2C and get authentication token used later to request Veracity Data Fabric API. Important is to register new app in Azure Active Directory in accordence with the application you create. This process is part of the Veracity service onboarding. Contact Veracity support for additional details.


### .NET implementation
When your application is registered with Azure AD B2C tenant, you will recieve some information, among others the app ID together with tenant, and we will use that to obtain authentication key. Code is available [here](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-identity/azure-ad-b2c/azure-ad-b2c-net).


#### Native App

Data required to continue with below code:
```
Tenant - tenant name from Azure Portal (Active Directory)
ClientId - Application ID from your Native app registration
PolicySignUpSignIn - sign in policy created during app registration
ApiScopes - scopes available for given api
```
For user identification we use class PublicClientApplication available in namespace Microsoft.Identity.Client.
You can include it as NuGet package, currently in preview mode.
```csharp
public static PublicClientApplication PublicClientApp { get; } =
    new PublicClientApplication(ClientId, Authority, TokenCacheHelper.GetUserCache());
```

Authority is an url:
```
"https://login.microsoftonline.com/tfp/{tenant}/{policy}/oauth2/v2.0/authorize";
```
where tenant and policy are replaced with proper values from app registration.

To sign in, AcquireTokenAsync method from PublicClientApplication is used.
```csharp
public static async Task<AuthenticationResult> SignIn()
{
    try
    {
        return await PublicClientApp.AcquireTokenAsync(ApiScopes,
            GetUserByPolicy(PublicClientApp.Users, PolicySignUpSignIn), UIBehavior.SelectAccount, string.Empty,
            null, Authority);
    }
    catch (Exception ex)
    {
        Console.WriteLine(
            $"Users:{string.Join(",", PublicClientApp.Users.Select(u => u.Identifier))}{Environment.NewLine}Error Acquiring Token:{Environment.NewLine}{ex}");
        return null;
    }
}
```

AuthenticationResult object contains AccessToken property where Bearer Key is stored.
