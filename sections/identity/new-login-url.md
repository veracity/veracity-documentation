---
author: Veracity
description: Transition to new login URL in B2C
---

# New Login Url
Microsoft will deprecate the use of login.microsoftonline.com for Azure AD B2C tenants Dec 4th, 2020. All services in Veracity trusting B2C PROD (the dnvglb2cprod tenant) must change from login.microsoftonline.com to login.veracity.com. When this is changed, all issued tokens will get a new issuer value: 
Old: "iss": "https://login.microsoftonline.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/", 
New:"iss": "https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/", 

## What does this mean for me?
### Apps using Client Credentials grant type
If your app is using Client Credentials grant type (used for service-to-service scenarios where no user login happens), you must continue to use login.microsoftonline.com.

### Apps using the .net Veracity package - WIP
If your app is using the the .net package for handling authentication, you must update your config in the following way

### Apps using npm package @veracity/node-auth
If your app is using the NPM pacakge @veracity/node-auth, you must update it to either version `1.0.7` or `2.0.7`.

### Other scenarios - WIP
If your app is using another way of authenticating, you must make sure that you update the login URL to: 
