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

#### Web application
Below code is based on default VisualStudio template for web application and Microsoft tutorial available [here](https://docs.microsoft.com/en-us/azure/active-directory-b2c/active-directory-b2c-devquickstarts-web-dotnet-susi)

Data required to perform authentication:
```xml
    <add key="ida:Tenant" value="Tenant name from Azure Portal (Active Directory)"/>
    <add key="ida:ClientId" value="Application ID from your Native app registration" />
    <add key="ida:ClientSecret" value="secrec created during app registration" />
    <add key="ida:AadInstance" value="base authority url" />
    <add key="ida:RedirectUri" value="redirect url to go after successfull authentication" />
    <add key="ida:SignUpSignInPolicyId" value="sign in policy created during app registration" />
```

All above values are to be sent in web.config file.

To compile and run sample you need to install following NuGet packages:
- Microsoft.Owin.Security.OpenIdConnect
- Microsoft.Owin.Security.Cookies
- Microsoft.Owin.Host.SystemWeb

OWIN is a middleware that defines a standard interface between .NET web servers and web applications.

In the root directory of the project there is class called Startup.cs. Its used by OWIN at startup.
```csharp
using Microsoft.Owin;
using Owin;

[assembly: OwinStartup(typeof(aad_b2c_web_net.Startup))]

namespace aad_b2c_web_net
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
```
In App_Start directory there is second part of above partial class, defining ConfigureAuth method.
It basically setup cookie authentication, policies, error and notification handling. For more details see Microsoft guide [here](https://docs.microsoft.com/en-us/azure/active-directory-b2c/active-directory-b2c-devquickstarts-web-dotnet-susi).

In Account controller, to sign in and out use below code:
```csharp
public void SignUpSignIn()
{
    // Use the default policy to process the sign up / sign in flow
    if (!Request.IsAuthenticated)
    {
        HttpContext.GetOwinContext().Authentication.Challenge();
        return;
    }
    Response.Redirect("/");
}
public void SignOut()
{
    // To sign out the user, you should issue an OpenIDConnect sign out request.
    if (Request.IsAuthenticated)
    {
        IEnumerable<AuthenticationDescription> authTypes = HttpContext.GetOwinContext().Authentication.GetAuthenticationTypes();
        HttpContext.GetOwinContext().Authentication.SignOut(authTypes.Select(t => t.AuthenticationType).ToArray());
        Request.GetOwinContext().Authentication.GetAuthenticationTypes();
    }
}
```

There is also Claims View and Controller accessible only when user is authenticated. Otherwise it will redirect to sign in page.
To achieve that simple attribute is added in controller:
```csharp
[Authorize]
public ActionResult Claims()
{
    var displayName =
        ClaimsPrincipal.Current.FindFirst(ClaimsPrincipal.Current.Identities.First().NameClaimType);
    ViewBag.DisplayName = displayName != null ? displayName.Value : string.Empty;
    return View();
}
```