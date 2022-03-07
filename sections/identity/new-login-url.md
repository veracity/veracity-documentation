---
author: Veracity
description: Transition to new login URL in B2C
---

# Transition to new login URL in B2C

## UPDATE MARCH 7 2022
* There is now a hard stop date from Microsoft (ref. <https://azure.microsoft.com/en-us/updates/update-apps-using-azure-ad-b2c-to-new-redirect-b2clogincom/>). This means that if you have not changed to login.veracity.com within <span style="color:red;font-weight:bolder;">**August 31st, 2022**</span>, login to your service will no longer work!

## UPDATE JUNE 24 2021
* July 1st 2021 is fast approaching and as we informed earlier this year, we will not be able to guarantee authentication of the old login url after this date. We strongly urge you to update this NOW.
## Background
MS will deprecate the use of login.microsoftonline.com for Azure AD B2C tenants.

## What does this mean: 
* All services in Veracity trusting B2C PROD (the dnvglb2cprod tenant) must change from login.microsoftonline.com to **login.veracity.com**
* When this is changed, all issued tokens will get a new issuer value: 
  * Old: "iss": "https://login.microsoftonline.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/", 
  * New: "iss": "https://**login.veracity.com**/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/",
* This means that if your service involves APIs, you need to make sure that your API can support this new issuer before the client apps that call the API are updated
* **Note! Change to login.veracity.com must only be made after March 15th.**

## Deadline
<span style="color:red;font-weight:bolder;">**July 1st, 2021**</span><br/>
We have switched to a new logon page using Azure AD B2C, and users of services still using login.microsoftonline.com will get a secondary logon prompt if they navigate between services that have changed and those that have not. 

## Changes required in different scenarios:
### Apps using Client Credentials grant type
If your app is using Client Credentials grant type (used for service-to-service scenarios where no user login happens), you must continue to use login.microsoftonline.com.

### Apps using the Veracity .net package
If your app is using the the Veracity .net package for handling authentication, [update according to the documentation found here](https://github.com/veracity/Veracity-Identity-and-Services-Api).
### If you are not using the Veracity .net package
If your app is NOT using the veracity .net package, you can find more documentation [here](https://developer.veracity.com/docs/section/identity/authentication/web-native).

## Need help?
If you have questions or need help, [use this form to contact support](https://services.veracity.com/form/SupportAnonymous).
