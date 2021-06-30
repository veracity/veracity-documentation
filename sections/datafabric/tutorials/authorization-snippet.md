---
author: Veracity
description: Description of authorization section
---

# Authorization snippet

The Bearer Token is usually valid for one hour, after that you need to request a new one.

It's best practice to check the expire date of the token and get a new token before it expires a request.

## Application (AAD B2C)

Make sure your AAD B2C application is onboarded and added to Data Fabric before you proceed with this guide.

Information you need to acquire before you start :

* ClientId - Application ID from your Native app registration
* ClientSecret - Application secret
* Full Data Fabric Resource url
* AAD Tenant id - Azure AD Tenant Id

To get a access token:

Example Http request:  
```
POST https://login.microsoftonline.com/{tenantId/oauth2/token
Content-Type: application/x-www-form-urlencoded
grant_type=client_credentials&resource={Full Data fabric resource url}f&client_id={ClientId}&client_secret={ClientSecret}  
```
Note: Remember to url encode the form content

### Example C#

This example requires:
* [Newtonsoft.Json](https://www.nuget.org/packages/Newtonsoft.Json/)

Aad Token class:  
```cs
public class Token
{
    [JsonProperty("token_type")]
    public string TokenType { get; set; }

    [JsonProperty("expires_in")]
    public string ExpiresIn { get; set; }

    [JsonProperty("ext_expires_in")]
    public string ExtExpiresIn { get; set; }

    [JsonProperty("expires_on")]
    public string ExpiresOn { get; set; }

    [JsonProperty("not_before")]
    public string NotBefore { get; set; }

    [JsonProperty("resource")]
    public string Resource { get; set; }

    [JsonProperty("access_token")]
    public string AccessToken { get; set; }
}
```
Retrieve the access token:  
```cs
var clientId = "{clientId}";
var clientSecret = "{clientSecret}";
var tokenEndpoint = "https://login.microsoftonline.com/{tenantId}/oauth2/token";
var resource = "{Data fabric resource url}";

using (var client = new System.Net.Http.HttpClient())
{
    var content =
        new StringContent(
            $"grant_type=client_credentials&client_id={clientId}&resource={resource}&client_secret={HttpUtility.UrlEncode(clientSecret)}",
            Encoding.UTF8, "application/x-www-form-urlencoded");

    var response = await client.PostAsync(tokenEndpoint, content);
    var result = JsonConvert.DeserializeObject<Token>(await response.Content.ReadAsStringAsync());

    var accessToken = result.AccessToken;
}
```
## User

To acquire the Bearer Token needed for the API requests it is possible to authenticate with the code below. It's important to register any new app in the Azure Active Directory as a Native App. This App ID, together with the tenant name from Azure AD will be used to obtain an authentication key.

The below code in .NET shows how to programmatically get the Bearer Key. This code is also available here.

Firstly, input data is required:
* Tenant - tenant name from Azure Portal (Active Directory)
* ClientId - Application ID from your Native app registration
* PolicySignUpSignIn - sign in policy created during app registration
* ApiScopes - scopes available for given api  

For user identification we use the class PublicClientApplication which is available in the namespace [Microsoft.Identity.Client](https://www.nuget.org/packages/Microsoft.Identity.Client). You can include it as a NuGet package, currently in preview mode.  
```cs
public static PublicClientApplication PublicClientApp { get; } = new PublicClientApplication(ClientId, Authority, TokenCacheHelper.GetUserCache());
```
The Authority field is the following URL, where {tenant} and {policy} are replaced with proper values from the app registration.:  

    "https://login.microsoftonline.com/tfp/{tenant}/{policy}/oauth2/v2.0/authorize";

To sign in, the AcquireTokenAsync method from PublicClientApplication is used.  
```cs
public static async Task<AuthenticationResult> SignIn()
{
    try
    {
        var authResult = await PublicClientApp.AcquireTokenAsync(ApiScopes,
        GetUserByPolicy(PublicClientApp.Users, PolicySignUpSignIn), UIBehavior.SelectAccount, string.Empty,
        null, Authority);

        DisplayBasicTokenInfo(authResult);
        return authResult;
    }
    catch (Exception ex)
    {
        Console.WriteLine(
        $"Users:{string.Join(",", PublicClientApp.Users.Select(u => u.Identifier))}{Environment.NewLine}Error Acquiring Token:{Environment.NewLine}{ex}");
        return null;
    }
}  
```

The AuthenticationResult object contains the property AccessToken, which is where the Bearer Key is stored.

This key is to be used in the following code samples to properly authenticate API requests.

