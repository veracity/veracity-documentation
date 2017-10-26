---
Title : "Identity"
Author: "Brede Børhaug"
Contributors: "Pawel Lehmann, Rachel Hassall"
---

## Overview 
The Veracity onboarding process has some mandatory and optional requirements for service providers. A key mandatory requirement is that the service provider integrates with our identity provider, enabling the Single Sign On (SSO) experience in Veracity. The Veracity cloud identity provider is Azure AD B2C. It is a highly available global service that scales to hundreds of millions of identities and is built on an enterprise-grade secure platform. Azure AD B2C keeps your applications, your business and your customers protected.

Your Veracity integration will be through Enterprise Accounts (using open standard protocol OpenID Connect). For the documentation on Azure AD B2C visit [Microsoft Azure](https://docs.microsoft.com/en-us/azure/active-directory-b2c/active-directory-b2c-overview).

Tutorials:
- [Web Apps](#web-aps)
    - [ASP.NET](#asp.net-implementation)
    - [nodeJs - pending review]()
- [Mobile and desktop Apps](#mobile-and-desktop-apps)
    - [.NET implementation](#net-implementation)
    


## Tutorial
The verrcity-quickstart-samples on [GitHub](https://www.github.com/Veracity) hold the complete running samples for these tutorials. Please feel free to clone or fork the repository, and get started using them. In the tutorial we will follow the code step-by-step, so that you will be able to do the integration in a clean app, or  include it into your existing applications.


### Web Apps
The first section of the tutorial will focus on Web Apps. 



#### ASP.NET implementation
This part of the tutorial will demonstrate how to add authentification to a MVC .NET application. The code in this tutorial is based on the default VisualStudio template for web application and the Microsoft tutorial available [here](https://docs.microsoft.com/en-us/azure/active-directory-b2c/active-directory-b2c-devquickstarts-web-dotnet-susi). You can find our [veracity-quickstart-sample](https://github.com/veracity/) for .NET on our Github repo [here](https://github.com/veracity/veracity-quickstart-samples).


For the rest of the tutorial on ASP.NET implementation, we will assume that the application has already been created, and does not contain any form of setup for AD B2C authentification. First, we will need to add some NuGet packages. 

```xml
Install-Package Microsoft.Owin.Security.OpenIdConnect -Version 4.0.0-alpha1
Install-Package Microsoft.Owin.Security.Cookies -Version 4.0.0-alpha1
Install-Package Microsoft.Owin.Host.SystemWeb -Version 4.0.0-alpha1
Update-package Microsoft.IdentityModel.Protocol.Extensions
```

The package “Microsoft.Owin.Security.OpenIdConnect” contains the middleware used to protect web apps with OpenId Connect, this package contains the logic for the heavy lifting needed when our MVC App talks with Azure B2C tenant to request tokens and validate them.

The package “Microsoft.IdentityModel.Protocol.Extension” contains classes which represent OpenID Connect constants and messages and lastly the package “Microsoft.Owin.Security.Cookies” will be used to create a cookie based session after obtaining a valid token from our Azure AD B2C tenant. This cookie will be sent from the browser to the server with each subsequent request and gets validated by the cookie middleware.

From the package install we also added some new keys to the web.config that need the correct information. This information will be provided when you register your application with Veracity.

```xml
<add key="ida:Tenant" value="Tenant name from Azure Portal (Active Directory)"/>
<add key="ida:ClientId" value="Application ID from your Native app registration" />
<add key="ida:ClientSecret" value="secrec created during app registration" />
<add key="ida:AadInstance" value="base authority url" />
<add key="ida:RedirectUri" value="redirect url to go after successfull authentication" />
<add key="ida:SignUpSignInPolicyId" value="sign in policy created during app registration" />
```

Since we assume a default MVC (Model View Controller) template structure, there will not be any "Startup" class located at the root directory of your application. We need to configure the OWIN OpenID Connect middleware at the start of our Web App, you will create a new class located at the root, named “Startup”. In the newly created class, we add the following:

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

Your IDE may complain that the ConfigureAuth does not exist, but you can ignore that for now as we will configure the authentication middleware. Open the file App_Start\Startup.Auth.cs and implement the ConfigureAuth(...) method. If Startup.Auth.cs does not exist you can go ahead and create it. The parameters you provide in OpenIdConnectAuthenticationOptions serve as coordinates for your app to communicate with Azure AD B2C. If you do not specify certain parameters, it will use the default value. For example, we do not specify the ResponseType in the sample, so the default value code id_token will be used in each outgoing request to Azure AD B2C. Note that we need to set up cookie authentication, the OpenID Connect middleware uses cookies to maintain user sessions, amongst other things.


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

In OpenIdConnectAuthenticationOptions above, we define a set of callback functions for specific notifications that are received by the OpenID Connect middleware. These behaviours are defined using an OpenIdConnectAuthenticationNotifications object and stored into the Notifications variable. In our sample, we define three different callbacks depending on the event.

Now we need to configure out Web App to invoke the policies we created. We do this by adding a new controller named “AccountController”, you can add it and paste the code below:

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

Your app is now properly configured to communicate with Azure AD B2C by using the OpenID Connect authentication protocol. OWIN manages the details of crafting authentication messages, validating tokens from Azure AD B2C, and maintaining user sessions. All that remains is to initiate each user's flow.

When a user selects Sign up/Sign in or Sign Out in the web app, the associated action is invoked in Controllers\AccountController.cs.

When you authenticate users by using OpenID Connect, Azure AD B2C returns an ID token to the app that contains claims. You can access user claims in your controllers via the ClaimsPrincipal.Current security principal object. If you would like to get the name of the logged in user and return that to the view, you can do the following:

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

### Mobile and Desktop Apps
In this section of the tutorial we will be focussing on mobile and desktop Apps. 


#### .NET Implementation
This sample demonstrates a .Net WPF application calling a web API that is secured using Azure AD. The .Net application uses the Active Directory Authentication Library (ADAL) to obtain a JWT access token through the OAuth 2.0 protocol. The access token is sent to the web API to authenticate the user.

The tutorial is based on the [Azure Samlples](https://github.com/Azure-Samples/active-directory-dotnet-native-desktop/).


For more information about how the protocols work in this scenario and other scenarios, see [Authentication Scenarios for Azure AD](http://go.microsoft.com/fwlink/?LinkId=394414) at Microsoft.

In order to develop this code you may need to set up your computer to trust the IIS Express SSL certificate. 


When integrating towards our Azure AD B2C tenant, you will need the following information provided by the Veracity team, as part of the onboarding process:

```xml
Tenant - tenant name from Azure Portal (Active Directory)
ClientId - Application ID from your Native app registration
PolicySignUpSignIn - sign in policy created during app registration
ApiScopes - scopes available for given api
```

For user identification we will use the class PublicClientApplication available in namespace Microsoft.Identity.Client. For this reason, you'll need to install the package like this:

```xml
Install-Package Microsoft.Identity.Client -Version 1.1.0-preview
```

Please note that the package is currently in preview state, but you will be able to use it.


Firstly, we need to create a TokenCasheHelper class in the root directory. Create the file and add the following code:

```csharp
using System.IO;
using Microsoft.Identity.Client;

namespace azure_ad_b2c
{
  /// <summary>
  /// Class taken from sample from Microsoft available here:
  /// https://azure.microsoft.com/en-us/resources/samples/active-directory-b2c-dotnet-desktop/
  /// </summary>
  static class TokenCacheHelper
  {
    /// <summary>
    /// Path to the token cache
    /// </summary>
    public static string CacheFilePath = System.Reflection.Assembly.GetExecutingAssembly().Location + "msalcache.txt";
    private static readonly object FileLock = new object();
    private static TokenCache _usertokenCache;
    /// <summary>
    /// Get the user token cache
    /// </summary>
    /// <returns></returns>
    public static TokenCache GetUserCache()
    {
      if (_usertokenCache != null) return _usertokenCache;
      _usertokenCache = new TokenCache();
      _usertokenCache.SetBeforeAccess(BeforeAccessNotification);
      _usertokenCache.SetAfterAccess(AfterAccessNotification);
      return _usertokenCache;
    }
    public static void BeforeAccessNotification(TokenCacheNotificationArgs args)
    {
      lock (FileLock)
      {
        args.TokenCache.Deserialize(File.Exists(CacheFilePath)
          ? File.ReadAllBytes(CacheFilePath)
          : null);
      }
    }
    public static void AfterAccessNotification(TokenCacheNotificationArgs args)
    {
      // if the access operation resulted in a cache update
      if (args.TokenCache.HasStateChanged)
      {
        lock (FileLock)
        {
          // reflect changesgs in the persistent store
          File.WriteAllBytes(CacheFilePath, args.TokenCache.Serialize());
          // once the write operationtakes place restore the HasStateChanged bit to filse
          args.TokenCache.HasStateChanged = false;
        }
      }
    }
  }
}
```

Then go into the program.cs file and add the following:


Then we go into the program.cs file and add the following:

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Identity.Client;

namespace azure_ad_b2c
{
  public class Program
  {
    /// <summary>
    /// Active Directory Tenent where app is registered
    /// </summary>
    private const string Tenant = "<tenant name goes here - format: <some name>.onmicrosoft.com>";
    /// <summary>
    /// Id of registered app. App needs to be registered in tenant.
    /// </summary>
    private const string ClientId = "< id from registered app goes here>";
    /// <summary>
    /// Policy for authentication
    /// </summary>
    public static string PolicySignUpSignIn = "< signup policy goes here >";
    /// <summary>
    /// List of scopes for tenant
    /// openid and offline_access added by default, no need to repeat
    /// </summary>
    public static string[] ApiScopes =
    {
      "< api scope goes here >"
    };
    /// <summary>
    /// Template url where authentication will take place. 
    /// {tenant} and {policy} to be replaced by proper values
    /// </summary>
    private static string BaseAuthority =
      "https://login.microsoftonline.com/tfp/{tenant}/{policy}/oauth2/v2.0/authorize";
    /// <summary>
    /// Propert url where authentication will take place.
    /// </summary>
    public static string Authority =
      BaseAuthority.Replace("{tenant}", Tenant).Replace("{policy}", PolicySignUpSignIn);
    /// <summary>
    /// Identity object performing authentication and recieving access token
    /// </summary>
    public static PublicClientApplication PublicClientApp { get; } =
      new PublicClientApplication(ClientId, Authority, TokenCacheHelper.GetUserCache());
    /// <summary>
    /// Main method. Executes sign in and shows result.
    /// </summary>
    /// <param name="args"></param>
    static void Main(string[] args)
    {
      var authResult = SignIn();
      authResult.Wait();
      DisplayBasicTokenInfo(authResult.Result);
      Console.ReadLine();
    }
    /// <summary>
    /// Tries to connect to Authority with given Scopes and Policies.
    /// Results with separate dialog where user needs to specify credentials.
    /// </summary>
    /// <returns>Authentication result containing access token</returns>
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
    /// <summary>
    /// Small summary of authentication result object
    /// </summary>
    /// <param name="authResult"></param>
    private static void DisplayBasicTokenInfo(AuthenticationResult authResult)
    {
      if (authResult == null) return;
      Console.WriteLine("Autorization token info: ");
      Console.WriteLine($"Name: {authResult.User.Name}");
      Console.WriteLine($"Token Expires: {authResult.ExpiresOn.ToLocalTime()}");
      Console.WriteLine($"Access Token: {authResult.AccessToken}");
    }
    /// <summary>
    /// Finds users according to given policy
    /// </summary>
    /// <param name="users"></param>
    /// <param name="policy"></param>
    /// <returns></returns>
    private static IUser GetUserByPolicy(IEnumerable<IUser> users, string policy)
    {
      foreach (var user in users)
      {
        string userIdentifier = Base64UrlDecode(user.Identifier.Split('.')[0]);
        if (userIdentifier.EndsWith(policy.ToLower())) return user;
      }
      return null;
    }
    /// <summary>
    /// Decodes url
    /// </summary>
    /// <param name="s"></param>
    /// <returns></returns>
    private static string Base64UrlDecode(string s)
    {
      s = s.Replace('-', '+').Replace('_', '/');
      s = s.PadRight(s.Length + (4 - s.Length % 4) % 4, '=');
      var byteArray = Convert.FromBase64String(s);
      var decoded = Encoding.UTF8.GetString(byteArray, 0, byteArray.Count());
      return decoded;
    }
  }
}
```

In the Program-.cs, we see that the AcquireTokenAsync method from PublicClientApplication is used to sign in.

```csharp
public static async Task<AuthenticationResult> SignIn()
```

The AuthenticationResult object contains the AccessToken property where the Bearer Key is stored. This can then be used to, for example, call the Veracity Data Fabric API's.

## GitHub  
Follow our open projects related to identity on https://github.com/veracity


## Stack Overflow
Stack Overflow is the largest, most trusted online community for developers to learn, share their programming knowledge. The Veracity developer team monitor Stack Overflow forum posts that include the tag Veracity Platform.

[Visit Stack Overflow](https://stackoverflow.com/questions/tagged/veracity+platform?mode=all)