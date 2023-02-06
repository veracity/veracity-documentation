---
author: Benedikte Kallåk
description: This section describes the different endpoints of the IoT Api
---

# Use api from applications
Only users that has access to an asset as well as given permission to datachannel-datasets can access iot data from this asset.

## C# SDK
Veracity IOT SDK can be used to connect to API from .NET application. Veracity IOT SDK is based on .Net Standard and availabale as Nuget packages.

- [model](https://www.nuget.org/packages/Veracity.IoT.SDK.Models/): Veracity.IOT.SDK.Models: models used for data ingest and output of data queries
- [client](https://www.nuget.org/packages/Veracity.IoT.SDK.Client/): Veracity.IOT.SDK.Client: To create HTTTP client to access API. Includes Veracity.IOT.SDK.Models
- [extentions](https://www.nuget.org/packages/Veracity.IoT.SDK.Client.Extensions/): Veracity.IOT.SDK.Client.Extensions: For dependency injections. Includes Veracity.IOT.SDK.Models and Veracity.IOT.SDK.Client

### Token provider and Veracity ioT Http client


   ```cs
          //Get token
            ClientCredentialsTokenProvider tokenProvider = new Veracity.IoT.SDK.Client.ClientCredentialsTokenProvider(Environment.GetEnvironmentVariable("ClientId"), Environment.GetEnvironmentVariable("ClientSecret") );
            string baseUrl = "https://api.veracity.com/veracity/";
            var veracityIoTTimeSeriesClient = new Veracity.IoT.SDK.Client.VeracityIoTTimeSeriesClient(tokenProvider, baseUrl , Environment.GetEnvironmentVariable("SubscriptionKey"));
      
       ```
 
 When VeracityIoTTimeSeriesClient is instantiated you can call any of the methods provided (and token is automatiocally refreshed for you):
 Methods are grouped into categories:
  - .Assets: methods for accessing assets yu have access to
  - .Ingest.Events: Methods for ingesting events
  - .Query.Events:  Methods for querying events
  - .Query.Sensors: Methods for querying sensors
  
### Ingest event example

In this example an event described in object payload will be ingested
```cs
            ClientCredentialsTokenProvider tokenProvider = new Veracity.IoT.SDK.Client.ClientCredentialsTokenProvider(Environment.GetEnvironmentVariable("ClientId"), Environment.GetEnvironmentVariable("ClientSecret") );
            string baseUrl = "https://api.veracity.com/veracity/";
            var veracityIoTTimeSeriesClient = new Veracity.IoT.SDK.Client.VeracityIoTTimeSeriesClient(tokenProvider, baseUrl , Environment.GetEnvironmentVariable("SubscriptionKey"));
            
			string imoNr = "1234";
            string eventType = "SystemAlarmTest";
            string dataChannelId = "TestTagId";
            string dataChannelSchema = "MC";
            string assetIdSchema = "imo";
            string json = JsonConvert.SerializeObject(payload);
            var result = await veracityIoTTimeSeriesClient.Ingest.Events.AddEventByTemplate(payload, imoNr, eventType, assetIdSchema, dataChannelSchema, dataChannelId);

```

### Use HTTP client directly
You can call the apis directly from code without using our SDK.

```cs

            var baseUrl = https://api-test.veracity.com/veracity/;
            var httpClient = new HttpClient();
            httpClient.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", Environment.GetEnvironmentVariable("SubscriptionKey"));
            httpClient.BaseAddress = new Uri(baseUrl);
            httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);

```

Then build relative url and call POST or GET 

Get token using Microsoft.Identity.Client

 tenant: "dnvglb2cprod.onmicrosoft.com"
 scope:  "https://dnvglb2cprod.onmicrosoft.com/29a8760a-d13a-41ce-998e-0a00c3d948d5/.default"
 loginUrl: "https://login.microsoftonline.com"
 authority: = "https://login.microsoftonline.com/dnvglb2cprod.onmicrosoft.com"
 
 ```cs
  public async Task<string> GetAccessToken()
        {
            var clientApplication = ConfidentialClientApplicationBuilder
                .Create(_clientId)
                .WithClientSecret(_clientSecret)
                .WithAuthority(_authority)
                .Build();

            var authenticationResult = await clientApplication.AcquireTokenForClient(new[] { _scope }).ExecuteAsync();
            var token = authenticationResult.AccessToken;
            return token;
        }
```

## Python SDK
SDK for Python: [Python](https://github.com/veracity/Python-Sample-to-Connect-to-Veracity-Service)






