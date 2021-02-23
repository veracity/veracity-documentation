---
author: Veracity
description: Transition to new login URL in B2C
---

# New Login Url
## Background
MS will deprecate the use of login.microsoftonline.com for Azure AD B2C tenants.

## What does this mean: 
* All services in Veracity trusting B2C PROD (the dnvglb2cprod tenant) must change from login.microsoftonline.com to login.veracity.com 
* When this is changed, all issued tokens will get a new issuer value: 
  * Old: "iss": "https://login.microsoftonline.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/", 
  * New: "iss": "https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/",
* This means that if your service involves APIs, you need to make sure that your API can support this new issuer before the client apps that call the API are updated
* **Note! Change to login.veracity.com must only be made after March 15th.**

## Deadline
<span style="color:red;">**July 1st, 2021**</span><br/><br/>
Note that in order to keep SSO for your service, we recommend that you make this change before April 10th. On this date, we will switch to a new logon page using Azure AD B2C, and users of services still using login.microsoftonline.com will get a secondary logon prompt if they navigate between services that have changed and those that have not. 

## Additional information:
Note that the above change should only be made for regular Azure AD B2C apps where users log in. If you use apps with Client Credentials grant type (used for service-to-service scenarios), these apps must continue to use login.microsoftonline.com. 

## Changes required in different scenarios:
### Apps using Client Credentials grant type
If your app is using Client Credentials grant type (used for service-to-service scenarios where no user login happens), you must continue to use login.microsoftonline.com.

### Apps using the Veracity .net package
If your app is using the the Veraciy .net package for handling authentication, [update according to the documentation found here](https://github.com/veracity/Veracity-Identity-and-Services-Api).

## Need help?
If you have questions or need help, [use this form to contact support](https://services.veracity.com/form/SupportAnonymous).
