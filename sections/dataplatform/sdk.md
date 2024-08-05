---
author: Veracity
description: This page lists available nuget packages
---

# Veracity SDKs
When using SDKs authentication is handled by providing Client id, secret and subscription key. 

## Event broker
### C# code example using Veracity IoT SDK
Use latest nuget package **Veracity.IoT.SDK.Client**


```cs
using Veracity.IoT.SDK.Client; 
 
string clientId = "[clientId]";
string clientSecret = "[clientSecret]";
string subscriptionKey = "[subscriptionKey]";
string baseUrl = "https://api.veracity.com/veracity/";
 
var tokenProvider = new ClientCredentialsTokenProvider(clientId, clientSecret);
var eventsClient = new VeracityIoTTimeSeriesClient(tokenProvider, baseUrl, subscriptionKey);  
 
//Replace as needed
var assetId = "555";
var assetIdIssuer = "imo";
var topic = "MC/Engines";
var eventType = "eventtype";
DateTime fromUtcDate = new DateTime(2000, 1, 1);
DateTime toUtcDate = DateTime.UtcNow;
var maxNumberOfItems = 10;
var offset = 0;
var result = await eventClient.Events.GetEvents(_tenantId,
assetId, assetIdIssuer, topic, eventType, fromUtcDate, toUtcDate, maxNumberOfItems, offset);
```