---
author: Mariusz Klimek (DNV)
description: Creating an API in Veracity's Developer Portal
---

[Previous - 1. Introduction to the Client Credentials flow](1-client-credentials-introduction.md)

## Create a new resource

<figure>
	<img src="assets/ccapi-step-1-create-a-new-resource.png"/>
	<figcaption>Create a new resource in a chosen resource group in Developer Potal on Veracity.</figcaption>
</figure>

## Pick resource type

<figure>
	<img src="assets/ccapi-step-2-pick-app-or-api.png"/>
	<figcaption>As the resource type pick App or API.</figcaption>
</figure>

## Pick localization

<figure>
	<img src="assets/ccapi-step-3-fill-in-resource-group.png"/>
	<figcaption>Select project and resource group of the resource to be created.</figcaption>
</figure>

## Configure your API

<figure>
	<img src="assets/ccapi-step-4-configure-your-API.png"/>
	<figcaption></figcaption>
</figure>

Write the API name under **Application name**.

For client application leave None.

Check the "This is an API" checkbox.

If you need to, add scopes.

## Advances tab

<figure>
	<img src="assets/ccapi-step-5-advanced-tab.png"/>
	<figcaption>If you have created a client application earlier you can add them here.</figcaption>
</figure>

## Summary

In the Summary tab, confirm the presented information for your API and click **Submit**.

Once finished, you will be redirected to your resource, where you can edit any data. In the Settings tab you can find your API's ID under **App / Api ID**, and also **Subscriptions keys** and **Scopes**.

<figure>
	<img src="assets/ccapi-summary-settings-tab.png"/>
	<figcaption></figcaption>
</figure>

Next up, we will configure a client application that will call to this API.

---

[Previous - 1. Introduction to the Client Credentials flow](1-client-credentials-introduction.md) --- [Next - 3. Configuring Client application in Veracity](3-client-creation-in-veracity.md)