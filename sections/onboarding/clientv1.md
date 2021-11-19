---
author: Veracity
description: Veracity V1 client documentation
---

# Veracity V1 client documentation

In short: The V1 client is a client which can make API calls towards Veracity without a normal user token.

**What is it?**

V1 clients are different from regular clients. They do not require a normal user token to access Veracity service API endpoints, they only require the client ID and client secret. They are also the only clients able to access Veracity Data Fabric without a user token.

V1 clients use tokens obtained with the client credentials flow, whereas regular clients use the code authorization flow.

**Why would I want a V1 client?**

V1 clients are great if you have a use case where you absolutely are unable to retrieve a token for a logged in user. App-to-app calls are an example of this, or applications with multiple authentication options for the user. In these cases you will not have access to a user token all of the time, but you&#39;d like to make calls towards your Veracity service anyways. Other cases are where you have a service which should administrate its own Data Fabric containers, e.g. a data container with ship data that should be updated independent of the logged in user. Only V1 clients can access the Data Fabric API without a user token.

**How do I get one?**

V1 clients are only created in instances where you cannot retrieve a user token or if you need to have a Data Fabric container which is directly administrated by the service. Please speak to the Veracity onboarding manager ([onboarding@veracity.com](mailto:onboarding@veracity.com)) to request a V1 client. Please state your use case and for which service the client should have rights. You will receive an encrypted set of credentials on email.

**Drawbacks?**

V1 clients are inherently more unsafe because they do not require a user token. Compromised V1 credentials are more dangerous than compromised credentials for a regular application. The V1 client only requires the client ID and secret to have the ability to call API endpoints or create/edit/delete Data Fabric containers. This means that if a hostile party gets hold of your V1 credentials they can do great damage.

**How do I use the V1 client?**

Some documentation here, for client credentials flow:

[https://github.com/AzureAD/azure-activedirectory-library-for-dotnet/wiki/Client-credential-flows](https://github.com/AzureAD/azure-activedirectory-library-for-dotnet/wiki/Client-credential-flows)

Need full resource path (&quot;app ID URI&quot; in B2C lingo) to make this work:

ResourceURL for Veracity API service (this is the most commonly used one):

https://dnvglb2cprod.onmicrosoft.com/dfc0f96d-1c85-4334-a600-703a89a32a4c

ResourceURL for Veracity Data Fabric:

https://dnvglb2cprod.onmicrosoft.com/dfba9693-546d-4300-bcd7-d8d525bdff38

**Some important parameters, in the form of a powershell script below:**

    $clientid = '<your client id / app id>'
    $clientSecret = '<your client secret>'
    $resource = '<the App ID URI of the API for which you want access token, example: https://dnvglb2cprod.onmicrosoft.com/dfc0f96d-1c85-4334-a600-703a89a32a4c if you want to obtain a token for Veracity Identity>'
    $GrantType = "client_credentials"
    $Uri = ”https://login.microsoftonline.com/dnvglb2cprod.onmicrosoft.com/oauth2/token”


    $Body= @{

    "grant_type" = $GrantType
    "client_id" = $clientid
    "resource" = $resource
    "client_secret" = $clientSecret


    }

    $token = Invoke-RestMethod -Uri $Uri -Method Post -Body $Body -ContentType "application/x-www-form-urlencoded"
    Write-Output $token.access_token 


Documentation version 1.2

2021-09-17 AANDRES

Changelog: Removed hyperlinks in powershell script. Added some missing &quot;&quot; characters in the script. Added the word &quot;normal&quot; in the intro and emphasized that there is still a token that is obtained.

Documentation version 1.1

2021-04-22 AANDRES
