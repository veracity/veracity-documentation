---
author: Veracity
description: This page explains how to authenticate API calls for Data Workbench.
---
# Authentication
Authenticate your API calls with an API key and a bearer token (`tokenUrl`) placed in the header of your API call.

## API key
To get the API key:
1. In your Data Workbench workspace, select the **API Integrations** tab.
2. In the left sidebar, select a service account or [create a new service account](apiintegrations.md).
3. Find the **API key**, and copy it.

When you construct an API request, put the API key into an HTTP header `Ocp-Apim-Subscription-Key`.

## Bearer token
To get the bearer token, call the URL https://login.microsoftonline.com/dnvglb2cprod.onmicrosoft.com/oauth2/token with the POST method.
Use the following request body:
* `client_id` - this is the Service account ID for your app.
* `client_secret` - this is the Service account secret for your app.
* `resource` - use the scope for Services API: https://dnvglb2cprod.onmicrosoft.com/83054ebf-1d7b-43f5-82ad-b2bde84d7b75
* `grant_type` - client_credentials

<figure>
	<img src="assets/requestbody.png"/>
	<figcaption>An application with direct user interaction can redirect the user to the login page to authenticate them.</figcaption>
</figure>

To get `client_id` and `client_secret`:
1. In your Data Workbench workspace, select the **API Integrations** tab.
2. In the left sidebar, select a service account or [create a new service account](apiintegrations.md).
3. Find and copy the values. The **Service account ID** is the `client_id`. The **Service account secret** is the `client_secret`.
