---
author: Mariusz Klimek (DNV)
description: Configuring Client application in Veracity
---

[Previous - 2. Introduction to the Client Credentials flow](2-api-creation-in-veracity.md)

## Create a resource

<figure>
	<img src="assets/cc-client-step-1-create-a-new-resource.png"/>
	<figcaption>Create a new resource in a chosen resource group in Developer Portal on Veracity.</figcaption>
</figure>

## Pick resource type

<figure>
	<img src="assets/cc-client-step-2-pick-app-or-api.png"/>
	<figcaption>As the resource type pick App or API.</figcaption>
</figure>

## Pick localization

<figure>
	<img src="assets/cc-client-step-3-fill-in-resource-group.png"/>
	<figcaption>Select project and resource group of the resource to be created.</figcaption>
</figure>

## Configure your application

<figure>
	<img src="assets/cc-client-step-4-configure-your-client.png"/>
	<figcaption>Write the application name under **Application name**.</figcaption>
</figure>

For client application check Client Credentials.

## Advanced Tab

<figure>
	<img src="assets/cc-client-step-5-add-api-access.png"/>
	<figcaption>In the API Access section click Add API Access and from the dropbox that will appear select the API you just created.</figcaption>
</figure>

Press Next.

## Summary

Confirm the presented information for your application and click **Submit**.

Once finished, you will be redirected to your resource, where you can edit any data. 

<figure>
	<img src="assets/cc-client-step-6-summary.png"/>
	<figcaption>In the Settings tab you can find your API's ID under **App / Api ID**, and also **Subscriptions keys** and **Scopes**.</figcaption>
</figure>

From this part of the screen you should note:
- App ID under the field **App / Api ID**
- any client secret you create by pressing **Create client secret** button.

Remember to always protect this data and keep it confidential.

Next up, we will show you how to acquire an access token using MSAL in C#.

---

[Previous - 2. Creating an API in Veracity's Developer Portal](2-api-creation-in-veracity.md) --- [Next - 4. Acquiring access token using MSAL in C#](4-msal-access-token.md)