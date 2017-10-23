---
Title : "Identity"
---
# Overview 
When onboarding as a service provider there are some mandatory and some optional requirements. A key mandatory requirement for onboarding Veracity is the the service provider integrates with our identity provider, enable the Single Sign On (SSO) experience in Veracity. Veracity cloud identity provider is Azure AD B2C. It is a highly available global service that scales to hundreds of millions of identities. Built on an enterprise-grade secure platform, Azure AD B2C keeps your applications, your business, and your customers protected.

Your integration towards Veracity will be towards and Enterprise Accounts (using open standard protocol OpenID Connect). For the documentation on Azure AD B2C visit [Microsoft Azure](https://docs.microsoft.com/en-us/azure/active-directory-b2c/active-directory-b2c-overview).

Tutorials:
- [Web Apps](#web-aps)
    - [ASP.NET](#aspnet-implementation)
    - [nodeJs - pending review]()
- [Mobile and desktop Apps](#mobile-and-desktop-apps)
    - [.NET implementation](#net-implementation)
    


# Tutorial

## Web Apps

### ASP.NET implementation
This part of the tutorial will demonstrate how to add authentification to a MVC .NET application. The code in this tutorial is based on the default VisualStudio template for web application and Microsoft tutorial available [here](https://docs.microsoft.com/en-us/azure/active-directory-b2c/active-directory-b2c-devquickstarts-web-dotnet-susi)

We will assume that the application is already created, and do not contain any form of setup for AD B2C authentification. First we will need to add some nuget packages. 

```xml
Install-Package Microsoft.Owin.Security.OpenIdConnect -Version 4.0.0-alpha1
Install-Package Microsoft.Owin.Security.Cookies -Version 4.0.0-alpha1
Install-Package Microsoft.Owin.Host.SystemWeb -Version 4.0.0-alpha1
Update-package Microsoft.IdentityModel.Protocol.Extensions
```
The package “Microsoft.Owin.Security.OpenIdConnect” contains the middleware used to protect web apps with OpenId Connect, this package contains the logic for the heavy lifting happens when our MVC App will talk with Azure B2C tenant to request tokens and validate them.

The package “Microsoft.IdentityModel.Protocol.Extension” contains classes which represent OpenID Connect constants and messages, lastly the package “Microsoft.Owin.Security.Cookies” will be used to create a cookie based session after obtaining a valid token from our Azure AD B2C tenant. This cookie will be sent from the browser to the server with each subsequent request and get validate by the cookie middleware.

From the package install we also got some new keys added to the web.config that needs the correct information. This information will be provided when you register your application with Veracity.
```xml
    <add key="ida:Tenant" value="Tenant name from Azure Portal (Active Directory)"/>
    <add key="ida:ClientId" value="Application ID from your Native app registration" />
    <add key="ida:ClientSecret" value="secrec created during app registration" />
    <add key="ida:AadInstance" value="base authority url" />
    <add key="ida:RedirectUri" value="redirect url to go after successfull authentication" />
    <add key="ida:SignUpSignInPolicyId" value="sign in policy created during app registration" />
```

Since we assume a default MVC template structure, there will not be any "Startup" class located at the root directory of your application. We need to configure the OWIN OpenID Connect middleware at the start of our Web App. To fix this you will create a new class located at the root, named “Startup”. In the newly cleated class, we add the following.


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
Your IDE may complaine that the ConfigureAuth does not exist, but ignore that for now. We will fix that now. We will configure the authentication middelware, and you do that in the following way. Open the file App_Start\Startup.Auth.cs and implement the ConfigureAuth(...) method. If Startup.Auth.cs does not exist you just create it. The parameters you provide in OpenIdConnectAuthenticationOptions serve as coordinates for your app to communicate with Azure AD B2C. If you do not specify certain parameters, it will use the default value. For example, we do not specify the ResponseType in the sample, so the default value code id_token will be used in each outgoing request to Azure AD B2C. Note also that we need to set up cookie authentication. The OpenID Connect middleware uses cookies to maintain user sessions, among other things.

```csharp
using Microsoft.Identity.Client;
using Microsoft.Owin.Security;
using Microsoft.Owin.Security.Cookies;
using Microsoft.Owin.Security.OpenIdConnect;
using Microsoft.Owin.Security.Notifications;
using Owin;
using System;
using System.Configuration;
using System.Threading.Tasks;
using System.Web;
using System.IdentityModel.Claims;
using aad_b2c_web_net.Models;
using Microsoft.IdentityModel.Protocols.OpenIdConnect;
using Microsoft.IdentityModel.Tokens;

namespace aad_b2c_web_net
{
    /// <summary>
    /// Based on Microsoft tutorial:
    /// https://docs.microsoft.com/en-us/azure/active-directory-b2c/active-directory-b2c-devquickstarts-web-dotnet-susi
    /// </summary>
    public partial class Startup
    {
        // App config settings
        public static string ClientId = ConfigurationManager.AppSettings["ida:ClientId"];
        public static string ClientSecret = ConfigurationManager.AppSettings["ida:ClientSecret"];
        public static string AadInstance = ConfigurationManager.AppSettings["ida:AadInstance"];
        public static string Tenant = ConfigurationManager.AppSettings["ida:Tenant"];
        public static string RedirectUri = ConfigurationManager.AppSettings["ida:RedirectUri"];

        // B2C policy identifiers
        public static string SignUpSignInPolicyId = ConfigurationManager.AppSettings["ida:SignUpSignInPolicyId"];
        public static string DefaultPolicy = SignUpSignInPolicyId;

        // API Scopes
        public static string ApiIdentifier = ConfigurationManager.AppSettings["api:ApiIdentifier"];
        public static string ReadTasksScope = ApiIdentifier + ConfigurationManager.AppSettings["api:ReadScope"];
        public static string WriteTasksScope = ApiIdentifier + ConfigurationManager.AppSettings["api:WriteScope"];
        public static string[] Scopes = { ReadTasksScope, WriteTasksScope };

        // OWIN auth middleware constants
        public const string ObjectIdElement = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier";

        // Authorities
        public static string Authority = String.Format(AadInstance, Tenant, DefaultPolicy);

        /*
        * Configure the OWIN middleware 
        */
        public void ConfigureAuth(IAppBuilder app)
        {
            app.SetDefaultSignInAsAuthenticationType(CookieAuthenticationDefaults.AuthenticationType);

            app.UseCookieAuthentication(new CookieAuthenticationOptions());

            app.UseOpenIdConnectAuthentication(
                new OpenIdConnectAuthenticationOptions
                {
                    // Generate the metadata address using the tenant and policy information
                    MetadataAddress = String.Format(AadInstance, Tenant, DefaultPolicy),

                    // These are standard OpenID Connect parameters, with values pulled from web.config
                    ClientId = ClientId,
                    RedirectUri = RedirectUri,
                    PostLogoutRedirectUri = RedirectUri,

                    // Specify the callbacks for each type of notifications
                    Notifications = new OpenIdConnectAuthenticationNotifications
                    {
                        RedirectToIdentityProvider = OnRedirectToIdentityProvider,
                        AuthorizationCodeReceived = OnAuthorizationCodeReceived,
                        AuthenticationFailed = OnAuthenticationFailed,
                    },

                    // Specify the claims to validate
                    TokenValidationParameters = new TokenValidationParameters
                    {
                        NameClaimType = "name"
                    },

                    // Specify the scope by appending all of the scopes requested into one string (separated by a blank space)
                    Scope = $"openid profile offline_access {ReadTasksScope} {WriteTasksScope}"
                }
            );
        }

        /*
         *  On each call to Azure AD B2C, check if a policy (e.g. the profile edit or password reset policy) has been specified in the OWIN context.
         *  If so, use that policy when making the call. Also, don't request a code (since it won't be needed).
         */
        private Task OnRedirectToIdentityProvider(RedirectToIdentityProviderNotification<OpenIdConnectMessage, OpenIdConnectAuthenticationOptions> notification)
        {
            var policy = notification.OwinContext.Get<string>("Policy");

            if (!string.IsNullOrEmpty(policy) && !policy.Equals(DefaultPolicy))
            {
                notification.ProtocolMessage.Scope = OpenIdConnectScope.OpenId;
                notification.ProtocolMessage.ResponseType = OpenIdConnectResponseType.IdToken;
                notification.ProtocolMessage.IssuerAddress = notification.ProtocolMessage.IssuerAddress.ToLower().Replace(DefaultPolicy.ToLower(), policy.ToLower());
            }

            return Task.FromResult(0);
        }

        /*
         * Catch any failures received by the authentication middleware and handle appropriately
         */
        private Task OnAuthenticationFailed(AuthenticationFailedNotification<OpenIdConnectMessage, OpenIdConnectAuthenticationOptions> notification)
        {
            notification.HandleResponse();

            // Handle the error code that Azure AD B2C throws when trying to reset a password from the login page 
            // because password reset is not supported by a "sign-up or sign-in policy"
            if (notification.ProtocolMessage.ErrorDescription != null && notification.ProtocolMessage.ErrorDescription.Contains("AADB2C90118"))
            {
                // If the user clicked the reset password link, redirect to the reset password route
                notification.Response.Redirect("/Account/ResetPassword");
            }
            else if (notification.Exception.Message == "access_denied")
            {
                notification.Response.Redirect("/");
            }
            else
            {
                notification.Response.Redirect("/Home/Error?message=" + notification.Exception.Message);
            }

            return Task.FromResult(0);
        }


        /*
         * Callback function when an authorization code is received 
         */
        private async Task OnAuthorizationCodeReceived(AuthorizationCodeReceivedNotification notification)
        {
            // Extract the code from the response notification
            var code = notification.Code;
            var signedInUserId = notification.AuthenticationTicket.Identity.FindFirst(ClaimTypes.NameIdentifier).Value;
            var userTokenCache = new MSALSessionCache(signedInUserId,
                    notification.OwinContext.Environment["System.Web.HttpContextBase"] as HttpContextBase)
                .GetMsalCacheInstance();
            var cca = new ConfidentialClientApplication(ClientId, Authority, RedirectUri,
                new ClientCredential(ClientSecret), userTokenCache, null);
            var result = await cca.AcquireTokenByAuthorizationCodeAsync(code, Scopes);
        }
    }
}
```
In OpenIdConnectAuthenticationOptions above, we define a set of callback functions for specific notifications that are received by the OpenID Connect middleware. These behaviors are defined using a OpenIdConnectAuthenticationNotifications object and stored into the Notifications variable. In our sample, we define three different callbacks depending on the event.

Now we need to configure out Web App to invoke the policies we created. We do this by adding a new controller named “AccountController”, so add it and paste the code below:

```csharp
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using Microsoft.Owin.Security;

namespace aad_b2c_web_net.Controllers
{
    /// <summary>
    /// Based on Microsoft tutorial:
    /// https://docs.microsoft.com/en-us/azure/active-directory-b2c/active-directory-b2c-devquickstarts-web-dotnet-susi
    /// </summary>
    public class AccountController : Controller
    {
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
    }
}
```

Your app is now properly configured to communicate with Azure AD B2C by using the OpenID Connect authentication protocol. OWIN manages the details of crafting authentication messages, validating tokens from Azure AD B2C, and maintaining user session. All that remains is to initiate each user's flow.

When a user selects Sign up/Sign in, or Sign Out in the web app, the associated action is invoked in Controllers\AccountController.cs:

When you authenticate users by using OpenID Connect, Azure AD B2C returns an ID token to the app that contains claims. You can access user claims in your controllers via the ClaimsPrincipal.Current security principal object. If you e.g would like to get the name of the loged in user and return that to the view, you can do the following:

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
Happy coding.

## Mobile and Desktop Apps
### .NET Implementation

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

