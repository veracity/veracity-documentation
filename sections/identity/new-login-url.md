---
author: Veracity
description: Transition to new login URL in B2C
---

# New Login Url
Microsoft will deprecate the use of login.microsoftonline.com for Azure AD B2C tenants Dec 4th, 2020. All services in Veracity trusting B2C PROD (the dnvglb2cprod tenant) must change from login.microsoftonline.com to login.veracity.com. When this is changed, all issued tokens will get a new issuer value: 
Old: "iss": "https://login.microsoftonline.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/", 
New: "iss": "https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/", 

## What does this mean for me?
All services in Veracity trusting B2C PROD (the dnvglb2cprod tenant) must change from login.microsoftonline.com to "dnvglb2cprod.b2clogin.com" 
When this is changed, all issued tokens will get a new issuer value: 
* Old: "iss": "https://login.microsoftonline.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/", 
* New:"iss": "https://dnvglb2cprod.b2clogin.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/", 
This means that if your service involves APIs, you need to make sure that your API can support this new issuer before the client apps that call the API are updated 
All Veracity Platform APIs will support the new issuer from Oct 12th, 2020 

## Deadline
In order to keep Single Sign On (SSO) for your service, you need to perform the above change before Nov 15st, 2020 
After this date we plan to change to a new logon page using Azure AD B2C, and services still using login.microsoftonline.com will see issues after this change. 

## Changes required in different scenarios:
### Apps using Client Credentials grant type
If your app is using Client Credentials grant type (used for service-to-service scenarios where no user login happens), you must continue to use login.microsoftonline.com.

### Apps using the Veracity .net package
If your app is using the the Veraciy .net package for handling authentication, [update according to the documentation found here](https://github.com/veracity/Veracity-Identity-and-Services-Api).

### Apps using the NPM package @veracity/node-auth
If your app is using the NPM pacakge @veracity/node-auth, you must update it to version `1.0.7` or greater, or version `2.0.7` or greater.

## Need help?
If you have questions or need help, [use this form to contact support](https://services.veracity.com/form/SupportAnonymous).
