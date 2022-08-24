---
author: Veracity
description: This page explains how to authenticate and authorize API calls for Data Workbench.
---
# Authorization & authentication
Learn how to authorize and authenticate your API calls.

## Authorization

Authorise your API calls with [Veracity Identity Provider](https://developer.veracity.com/docs/section/identity/identity) using the OAuth 2.0 protocol and the Authorization code flow.

See the security scheme for OAuth 2.0 below.
```json
"OAuth2": {
        "type": "oauth2",
        "flows": {
          "authorizationCode": {
            "authorizationUrl": "https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/b2c_1a_signinwithadfsidp/oauth2/v2.0/authorize",
            "tokenUrl": "https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/oauth2/v2.0/token",
            "scopes": {
              "https://dnvglb2cprod.onmicrosoft.com/37c59c8d-cd9d-4cd5-b05a-e67f1650ee14"
            }
```

## Authentication
Authenticate your API calls with an API key and a bearer token (`tokenUrl`) placed in the header of your API call.

### API key
To get the API key:
1. In your Data Workbench workspace, select the **API Integrations** tab.
2. In the left sidebar, select a service account or [create a new service account](apiintegrations.md).
3. Find the **API key**, and copy it.

When you construct an API request, put the API key into an HTTP header `Ocp-Apim-Subscription-Key`.

### Bearer token
To get the bearer token, call the URL https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/oauth2/v2.0/token with the POST method.
Use the following request body:
* `client_id` - this is the Service account ID for your app.
* `client_secret` - this is the Service account secret for your app.
* `scope` - use the scope for Services API: https://dnvglb2cprod.onmicrosoft.com/83054ebf-1d7b-43f5-82ad-b2bde84d7b75/.default
* `grant_type` - client credentials

To get `client_id` and `client_secret`:
1. In your Data Workbench workspace, select the **API Integrations** tab.
2. In the left sidebar, select a service account or [create a new service account](apiintegrations.md).
3. Find and copy the values. The **Service account ID** is the `client_id`. The **Service account secret** is the `client_secret`.
