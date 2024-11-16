---
author: Mariusz Klimek (DNV)
description: Creating an API in Veracity Developer Portal
---

# Create an API in Veracity Developer Portal

[Previous - 1. Introduction to the Client Credentials flow](1-client-credentials-introduction.md)

## Create a new resource

<figure>
	<img src="assets/ccapi-step-1-create-a-new-resource.png"/>
	<figcaption>Create a new resource in a chosen resource group in Developer Portal on Veracity.</figcaption>
</figure>

## Pick resource type

<figure>
	<img src="assets/ccapi-step-2-pick-app-or-api.png"/>
	<figcaption>As the resource type pick App or API.</figcaption>
</figure>

## Pick localization

<figure>
	<img src="assets/ccapi-step-3-fill-in-resource-group.png"/>
	<figcaption>Select project and resource group where your API will be created.</figcaption>
</figure>

## Configure your API

<figure>
	<img src="assets/ccapi-step-4-configure-your-API.png"/>
	<figcaption>Next is the Configure step</figcaption>
</figure>

Write the API name under **Application name**.

For client application leave None.

Check the "This is an API" checkbox.

We suggest that you add a **my_scope** scope as we will use it further on.

## Advanced tab

<figure>
	<img src="assets/ccapi-step-5-advanced-tab.png"/>
	<figcaption>If you have created a client application earlier you can add them here. We will add them in the next step.</figcaption>
</figure>

## Summary

In the Summary tab, confirm the presented information for your API and click **Submit**.

Once finished, you will be redirected to your resource, where you can edit any data. 

<figure>
	<img src="assets/ccapi-summary-settings-tab.png"/>
	<figcaption>In the Settings tab you will find the data needed to configure your API</figcaption>
</figure>

 You can find your API's ID under **App / Api ID**, and also **Subscriptions keys** and **Scopes**.

Next up, we will configure a client application in Veracity that will call to this API.

---

[Previous - 1. Introduction to the Client Credentials flow](1-client-credentials-introduction.md) --- [Next - 3. Configuring Client application in Veracity](3-client-creation-in-veracity.md)