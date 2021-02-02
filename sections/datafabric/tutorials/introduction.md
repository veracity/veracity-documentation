---
author: Veracity
description: Description of introduction section
---

# Introduction

Veracity uses API Management. In order to get access, you will need to:
* Register at https://api-portal.veracity.com/
* Subscribe to the Veracity Platform API – Product, this will give you access to Data API and Provision API with a subscription id  

## Standard structure of API Call

### Header attributes
* **Ocp-Apim-Subscription-Key** - this header attribute is for API Management authentication. The value you can get from the API portal mentioned above.
* **Authorization** - this header attribute needs to contain the Bearer Token that is received through authorization process on Veracity  

### Example request
Call `GET` endpoint `users/me`, to get the current details of the current user.

Example:  
```
GET https://api.veracity.com/veracity/datafabric/data/api/1/users/me HTTP/1.1
Host: api.veracity.com
Ocp-Apim-Subscription-Key: {subscription-Key}
Authorization: Bearer {token}  
```
C# example:  
```cs
var httpClient = new System.Net.Http.HttpClient();

var request = new HttpRequestMessage(HttpMethod.Get, "https://api.veracity.com/veracity/datafabric/data/api/1/users/me");
request.Headers.Add("Ocp-Apim-Subscription-Key", "{Subscription-Key}");
request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", "{accessToken}");

var response = await httpClient.SendAsync(request);
```