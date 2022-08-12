---
author: Veracity
description: This page explains how to authenticate and authorize API calls for Data Workbench.

# Authenticate and authorise calls
To authenticate API calls, you need:
* Service account secret – the secret used by an OAuth client to authenticate to Veracity. 
* Service account ID - an application (client) ID that uniquely identifies your app.
* API key – the Ocp-Apim-Subscription-Key key for calling the Veracity Platform API.

To find these values:
1. In your workspace, select the **API Integrations** tab.
2. In the left sidebar, select a service account or [create a new service account](apiintegrations.md).
3. Copy the values.

For the scope of your API calls, use the Data Fabric API scope https://dnvglb2cprod.onmicrosoft.com/37c59c8d-cd9d-4cd5-b05a-e67f1650ee14.

To authorise calls with [Veracity Identity Provider](https://developer.veracity.com/docs/section/identity/identity), use the URLs below:
* AuthorizationUrl: "https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/b2c_1a_signinwithadfsidp/oauth2/v2.0/authorize"
* TokenUrl: "https://login.veracity.com/a68572e3-63ce-4bc1-acdc-b64943502e9d/b2c_1a_signinwithadfsidp/oauth2/v2.0/token"

## Sample API request (draft)
Below you can see a sample API request.
