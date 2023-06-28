---
author: Veracity
description: Veracity client credentials flow tokens documentation
---

# Veracity client credentials flow tokens documentation

In short: Client credentials flow tokens are used when you need to call Veracity API's without a user being present and you therefore are unable to get tokens with the code authorization flow. 

**Why would I want a client credentials flow token?**

Tokens from the client credentials flow are great if you have a use case where you absolutely are unable to retrieve a token for a logged in user. App-to-app calls are an example of this, or applications with multiple authentication options for the user. In these cases you will not have access to a user token from code authorization flow all of the time, but you&#39;d like to make calls towards your Veracity service anyways. Other cases are where you have a service which should administrate its own Data Fabric containers, e.g. a data container with ship data that should be updated independent of the logged in user. 

**How do I get one?**

Create an application in My Projects and choose "ClientCredentials" under the "Client application" section.

Some documentation here, for client credentials flow:

[https://github.com/AzureAD/azure-activedirectory-library-for-dotnet/wiki/Client-credential-flows](https://github.com/AzureAD/azure-activedirectory-library-for-dotnet/wiki/Client-credential-flows)

**Important informmation**

•	"resource" is used when calling this endpoint to get tokens: 
https://login.microsoftonline.com/dnvglb2cprod.onmicrosoft.com/oauth2/token

•	"scope" is used when calling these endpoints to get tokens: 
https://login.microsoftonline.com/dnvglb2cprod.onmicrosoft.com/oauth2/v2.0/token/.default
or
https://login.veracity.com/dnvglb2cprod.onmicrosoft.com/B2C_1A_SignInWIthADFSIdp/oauth2/v2.0/token/.default

Generally the scope determines which kind of token you want returned. You can combine multiple of the values:
•	scope=<client id value>/.default grants a token for the API registered with an ID with this value.
•	scope=openid grants and ID token. An ID token cannot be used to call API's. Not applicable when you want a client credentials token.
•	scope=offline_access grants a refresh token. Refresh tokens can be used to get new access tokens without having the user re-authenticate. Not applicable when you want a client credentials token.

**Some important parameters, in the form of a powershell script below which will yield a token:**


    $clientid = '<client ID>'
    $clientSecret = '<client secret>'
    $scope = 'https://dnvglb2cprod.onmicrosoft.com/<your app scope>/.default'
    $GrantType = "client_credentials"
    $Uri = "https://login.veracity.com/dnvglb2cprod.onmicrosoft.com/B2C_1A_SignInWIthADFSIdp/oauth2/v2.0/token"
 
 
    $Body = @{
       "grant_type" = $GrantType
       "client_id" = $clientid
       "scope" = $scope
       "client_secret" = $clientSecret
    }
 
    $token = Invoke-RestMethod -Uri $Uri -Method Post -Body $Body -ContentType "application/x-www-form-urlencoded"
    Write-Output $token.access_token

This token will contain the following information (the specific information below is test data): 

    {
     "iss": "https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/",
     "exp": 1673003685,
     "nbf": 1673000085,
     "aud": "14442a14-0313-4c93-8873-1a4faf8cdcf5",
     "sub": "3a758d22-dcf2-4dff-a8d5-9a5537d8f4a0",
     "mfaType": "none",
     "scp": "app.canUse",
     "azpacr": "1",
     "oid": "3a758d22-dcf2-4dff-a8d5-9a5537d8f4a0",
     "tid": "a68572e3-63ce-4bc1-acdc-b64943502e9d",
     "ver": "2.0",
     "azp": "34065879-a5b2-42a5-8990-79b9663a9ba0",
     "iat": 1673000085
    }



Access tokens can either be version 1.0 or version 2.0.
For services created before 2022 the tokens will be version 1.0, and the script below may be used.

You need full resource path (&quot;app ID URI&quot; in B2C lingo) to make this work:

ResourceURL for Veracity API service (this is the most commonly used one):

https://dnvglb2cprod.onmicrosoft.com/dfc0f96d-1c85-4334-a600-703a89a32a4c

ResourceURL for Veracity Data Fabric:

https://dnvglb2cprod.onmicrosoft.com/dfba9693-546d-4300-bcd7-d8d525bdff38


    $clientid = '<your client id / app id>'
    $clientSecret = '<your client secret>'
    $resource = '<the App ID URI of the API for which you want access token, example: https://dnvglb2cprod.onmicrosoft.com/dfc0f96d-1c85-4334-a600-703a89a32a4c if you want to obtain a token for Veracity Identity>'
    $GrantType = "client_credentials"
    $Uri = "https://login.microsoftonline.com/dnvglb2cprod.onmicrosoft.com/oauth2/token"


    $Body= @{

    "grant_type" = $GrantType
    "client_id" = $clientid
    "resource" = $resource
    "client_secret" = $clientSecret


    }

    $token = Invoke-RestMethod -Uri $Uri -Method Post -Body $Body -ContentType "application/x-www-form-urlencoded"
    Write-Output $token.access_token 

Documentation version 1.4

2023-06-26 AANDRES

Changelog: Edited powershell script to fix a typo. Rewrote major sections to represent new version 2 tokens.

Documentation version 1.3

2022-11-21 AANDRES

Changelog: Removed "Drawbacks?" section and updated "How do I get one?" section to reflect new self-service flow.

Documentation version 1.2

2021-09-17 AANDRES

Changelog: Removed hyperlinks in powershell script. Added some missing &quot;&quot; characters in the script. Added the word &quot;normal&quot; in the intro and emphasized that there is still a token that is obtained.

Documentation version 1.1

2021-04-22 AANDRES
