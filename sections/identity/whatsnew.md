---
author: Veracity
description: Public changelog with important announcments.
---

# Latest news
This page contains latest news about Veracity Identity Provider and its [changelog](#changelog).
## Rotation of the Veracity Identity Token Signing Key
Last updated: 18 August 2022

According to security best practice, we will implement a new rotation scheme for the key used to sign the tokens issued by the Veracity Identity provider (Azure AD B2C/login.veracity.com) as follows:
- The new key will be published to the metadata (https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/discovery/v2.0/keys?p=b2c_1a_signinwithadfsidp) **one month before it gets activated**. This will allow the services to pick up the new key.
- Once the new key is activated, tokens will be issued using the new key.
- A new key will be published **every 6 months**.

We do not expect this to cause issue for services as they should already handle such rotation in accordance with best practice, however, the very first time we activate a new key, we will only make it active for 1 day. When it expires, the old (the key used today) will be used again. This will allow services to detect potential issues, but get them working again (at the latest) the next day.

The first key will be:
- Published to metadata:**6 September 2022**
- Set active: **11 October 2022**
- Expired: **12 October 2022**

If all goes well, we will start the 6 month rotation scheme as follows:
- Published to metadata: **18 October 2022**
- Set active: **22 November 2022**
- Expired:After **~6 months**

## Transition to new login URL in B2C
Last updated: 18 August 2022

Microsoft will deprecate the use of login.microsoftonline.com for Azure AD B2C tenants on 31 August 2022([source](https://azure.microsoft.com/en-us/updates/update-apps-using-azure-ad-b2c-to-new-redirect-b2clogincom/)). Because of that, Veracity advises you to **change your login URL to login.veracity.com by 31 August 2022**. If you do not do this, the login to your application will stop working.

After changing the login URL, all issued tokens will get a new issuer value (**login.veracity.com**). See an example of a new token: `iss`: "https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/"
If your service contains APIs, first make sure that your API supports the new issuer value. Then, you can update client apps that call your APIs.

### Exceptions
In some scenarios, you should take a different approach than described above.
* Are your apps using Client Credentials grant type?
This grant type is used for service-to-service scenarios where no user login happens. If your apps use it, continue using login.microsoftonline.com.
* Are your apps using the Veracity .net package?
If this is how your apps authenticate, [consult this documentation](https://github.com/veracity/Veracity-Identity-and-Services-Api) and update accordingly. 
* Are your apps not using the Veracity .net package?
If your app is NOT using the veracity .net package, you can find more documentation [here](https://developer.veracity.com/docs/section/identity/authentication/web-native).

### Need help?
If you have questions or need help, [use this form to contact support](https://services.veracity.com/form/SupportAnonymous).

## API Security flaw
Last updated: 18 August 2022

### Audience
The below is important information for all developers of an API using the Veracity Identity Provider, Azure AD B2C.

### The problem
Microsoft's implementation of OAuth 2.0 has a security flaw that you have to be aware of if you are responsible for an API:

- **Any client application (registered in _any_ Azure AD tenant, incl. non DNV-owned tenants) is able to get an access (bearer) token for any other API registered in Azure AD B2C without any permissions granted between the two.**

This can be done by requesting an access token using the OAuth2.0 grant type "Client Credentials".
It is possible to disable the possibility to issue access tokens for an API requested through the "Client Credentials" grant type. However, until now, the default configuration that has been used for APIs, both when creating them manually and through the Veracity Developer Portal, have not implemented this restriction. This will shortly be fixed in the Veracity Developer Portal, however, already existing APIs need to be manually managed.
This document explains how to set up your API with access restrictions to mitigate the OAuth 2.0 security flaw in Azure AD B2C. If you have any questions, please register it here: [https://support.veracity.com/](https://support.veracity.com/)

### What needs to be done 

#### API apps that only support access tokens generated on behalf of a logged-on user

If your API is only accepting calls made on behalf of a logged-on user (i.e. the client application that requested the access token used one of the user-based OAuth 2.0 flows such as Authorization Code flow), we can disable the possibility to issue access tokens for an API requested through the "Client Credentials" grant type. Register a request on [https://mygss.dnv.com](https://mygss.dnv.com) with the following information:

_Please send to IAM team:_

_Please enable "Assignment required" on my Veracity API app: \<Client ID of your API app\>_


#### API apps that support access tokens generated with "Client Credentials" grant type
The simplest method is to enable a restriction so that only client apps that are specifically granted permissions are allowed to get an access token using the "Client Credentials" grant type. This must be requested from support at the moment, but will soon be supported in the Developer Portal for API apps registered there.
Register a request on [https://mygss.dnv.com](https://mygss.dnv.com) with the following information:

_Please send to IAM team:_

_Please configure the following for my Veracity API app \<Client ID of API app\>:_

_1.	Add appRole_ 

_2.	Implement "Assignment required"_

_3.	Grant the following client apps access to the role:_

- _\<list of Client IDs for client apps\>_


Alternatively, you can use one of the two methods described below, but these require code changes to your API.

##### Access control lists

You can implement code in your API that specifically checks whether the caller is allowed to call you. You will then have to maintain (for example in a database) a list of callers that are allowed to call.
If your API will accept access tokens generated using the OAuth2.0 Client Credentials grant type (used in a server-to-server scenario where you do not have any logged-on users), this is one of two methods you can use to protect your API (the other one is listed below: "Application permissions").

There are different claims specifying the caller app depending on how your API was created. If it was created through the Veracity Developer portal, it will look like the following where the caller Client ID is identified by the **azp** claim:

```json

{
  "aud": "984bcd86-8d37-4cad-b77a-9f487a4b820b",
  "iss": "https://login.microsoftonline.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0",
  "iat": 1642086103,
  "nbf": 1642086103,
  "exp": 1642090003,
  "aio": "E2ZgYHBc+vTxEdYDHw4mehm5XFAvAQA=",
  "azp": "965cee6f-5a13-4ef6-a53a-c976ea2d06b6",
  "azpacr": "1",
  "oid": "1895cd34-e475-433a-9a21-1487b4dad841",
  "rh": "0.ASIA43KFps5jwUus3LZJQ1AunW_uXJYTWvZOpTrJduotBrYkAAA.",
  "sub": "1895cd34-e475-433a-9a21-1487b4dad841",
  "tid": "a68572e3-63ce-4bc1-acdc-b64943502e9d",
  "uti": "5NF1BPfmZkeybvuFGpzuAA",
  "ver": "2.0"
}
```

If your API app was created manually requesting it to be used specifically with "Client Credentials", it might look like the below where the caller Client ID is identified by the **appid** claim:

```json
{
  "aud": "https://dnvglb2cprod.onmicrosoft.com/dfc0f96d-1c85-4334-a600-703a89a32a4c",
  "iss": "https://sts.windows.net/a68572e3-63ce-4bc1-acdc-b64943502e9d/",
  "iat": 1642085326,
  "nbf": 1642085326,
  "exp": 1642089226,
  "aio": "E2ZgYAiX+ZPuWnxmU6fpIis35RX6AA==",
  "appid": "965cee6f-5a13-4ef6-a53a-c976ea2d06b6",
  "appidacr": "1",
  "idp": "https://sts.windows.net/a68572e3-63ce-4bc1-acdc-b64943502e9d/",
  "oid": "1895cd34-e475-433a-9a21-1487b4dad841",
  "rh": "0.ASIA43KFps5jwUus3LZJQ1AunW_uXJYTWvZOpTrJduotBrYkAAA.",
  "sub": "1895cd34-e475-433a-9a21-1487b4dad841",
  "tid": "a68572e3-63ce-4bc1-acdc-b64943502e9d",
  "uti": "F5jrRzklA02Aa3DK7ngFAQ",
  "ver": "1.0"
}
```

For an access token generated on behalf of a logged-on user, the **azp** claim will be the claim to look for if you want to use the "Access control lists" method also in this scenario:
```json
{
  "iss": "https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0/",
  "exp": 1642082239,
  "nbf": 1642078639,
  "aud": "83054ebf-1d7b-43f5-82ad-b2bde84d7b75",
  "mfa_required": "true",
  "myDnvglGuid": "47B5CC98-F524-4864-BD0E-6E6562E34DC5",
  "dnvglAccountName": "FIRSTLA",
  "oid": "7b183823-cc38-426b-a78b-422605f61988",
  "name": "Firstname Lastname",
  "email": [
    "firstname.lastname@veracity.com"
  ],
  "upn": "firstname.lastname@veracity.com",
  "authenticatedBy": "https://veracity.com",
  "userId": "47B5CC98-F524-4864-BD0E-6E6562E34DC5",
  "sub": "47b5cc98-f524-4864-bd0e-6e6562e34dc5",
  "given_name": "Firstname",
  "family_name": "Lastname",
  "mfaType": "phone",
  "nonce": "mkrtest",
  "scp": "user_impersonation",
  "azp": "3374885a-39e2-48e3-97e9-b3781ea57cd4",
  "ver": "1.0",
  "iat": 1642078639
}
```
More information from Microsoft:

[https://docs.microsoft.com/en-us/azure/active-directory-b2c/application-types#daemonsserver-side-applications](https://docs.microsoft.com/en-us/azure/active-directory-b2c/application-types#daemonsserver-side-applications)
[https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-client-creds-grant-flow#access-control-lists](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-client-creds-grant-flow#access-control-lists)

##### Application permissions
If you want to be able to differentiate what different callers are allowed to request from your API, you can use **appRoles** in the configuration of your API (done on the app registration for the API in Azure AD B2C).

Then in the code of your API you can check for a claim called **roles**. If that claim is present, you can be sure that the caller app has specifically been granted access to your API in Azure AD B2C. All other apps that have not been granted this access will not be able to get this claim in the access token.

This is how an access token with such a **roles** claim could look like:
```json
{
  "aud": "984bcd86-8d37-4cad-b77a-9f487a4b820b",
  "iss": "https://login.microsoftonline.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/v2.0",
  "iat": 1642146052,
  "nbf": 1642146052,
  "exp": 1642149952,
  "aio": "E2ZgYCg/NaPFXNT7uKiX/ioHISMFAA==",
  "azp": "965cee6f-5a13-4ef6-a53a-c976ea2d06b6",
  "azpacr": "1",
  "oid": "1895cd34-e475-433a-9a21-1487b4dad841",
  "rh": "0.ASIA43KFps5jwUus3LZJQ1AunW_uXJYTWvZOpTrJduotBrYkAAA.",
  "roles": [
    "Vessel.Write"
  ],
  "sub": "1895cd34-e475-433a-9a21-1487b4dad841",
  "tid": "a68572e3-63ce-4bc1-acdc-b64943502e9d",
  "uti": "nSZjMzmjRUikwlwQHSYNAQ",
  "ver": "2.0"
}
```
We can specify different roles and the role names can be anything. To follow MS' use of it, you may choose a format of the type
- **object.permissiontype** (e.g. All.Full, User.Read, Vessel.Write, etc.)

and client apps can be granted access to different roles. The **roles** claim will only contain the roles that a client app has been granted access to.

We plan to support self-service creation of appRoles using Veracity Developer portal in the future. Until that is in place you need to request for this through https://mygss.dnv.com. You should specify the following in the request:

- Client ID of your API
- The name of the appRoles you want
- Which Client ID shall be given access to which role
- Also mention that the request should go to the IAM team to make sure it gets routed the correct way.

More information from MS:

[https://docs.microsoft.com/en-us/azure/active-directory-b2c/application-types#daemonsserver-side-applications](https://docs.microsoft.com/en-us/azure/active-directory-b2c/application-types#daemonsserver-side-applications)
[https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-client-creds-grant-flow#application-permissions](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-client-creds-grant-flow#application-permissions)


## <a name="changelog"></a>Changelog
This section contains a public and cumulative changelog for Veracity Identity.