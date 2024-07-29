---
author: Veracity
description: How to publish an API to Veracity API Explorer.
---

# Project and resource overview

Veracity API Explorer lets you browse APIs that use the Veracity ecosystem. This document explains how to publish your API in Veracity API Explorer.

Note that Veracity API Explorer replaced Veracity API Portal which was deprecated by Microsoft. They offer the same functionalities with one exception: you can't test endpoints from Veracity API Explorer.


## Prerequisites

If you are not a Veracity customer yet, [follow the onboarding process](https://developer.veracity.com/docs/section/onboarding/onboarding).

If you are a Veracity customer with a project and resource group published to production (Developer Portal > My projects), you can add your API product there and when you finish configuration, it will show in Veracity API Explorer (assuming you set the visibility to public; otherwise, if you set it to private, you can share a link to give people access). 

If you don't want to reuse a resource group published to production or don't have one, follow the instructions in this document to publish your API product to the test or staging environment. Then, test if it works correctly, and if it does, contact the [onboarding team](mailto:onboarding@veracity.com) with a request to publish your resource group to production.

## Types of APIs
There are two types of APIs:
* Public APIs - Show in API Explorer. 
* Private (unlisted) APIs - Don't show in API Explorer. To access them, you need to get a direct URL, for example, from the API owner.

* As an API provider, you decide whether to make your API public or private.

## Make API public or private
If you already published an API product on Developer Portal and connected API specification to it, you can change if its public or private API. To do so:
1. On Developer Portal, go to My Projects.
2. Go to the resource group where you placed the API product.
3. Open the API product.
4. On the **Configure** tab, find the toggle **Is public?**
5. To make this a public API, turn the toggle on. Alternatively, to make this a private API, ensure that the toggle is turned off.

## To publish an API
1. Publish an API product.
2. Consider customizing the advanced settings for the API product.
3. Publish API specifications and connect them to an API product.

1. Note that:
* You do those steps on the Developer Portal in My projects (access it from the top navigation menu).
* If you need more help, check the [general instructions for publishing resources](https://developer.veracity.com/docs/section/developerexperience/introduction).

## To publish an API product
1. Go to Developer Portal.
2. Go to **My projects**.
3. Create a new project or reuse an existing project.
4. Open a project and **Create new resource group**. Alternatively, reuse an existing resource group.
5. In the Resource group, select **New Resource**.
6. Select resource type **API Product** and select **Next**.
7. On the **Structure** step, select a project and a resource to which you want to assign the API Product.
8. On the **Configure** step: 			
  8.1 Name the API product.
  8.2 Decide if it requires subscription approval.
  8.3 Decide if this API should be public. If so, toggle on **Is public**. 
  8.4 Add a description to your API. 
9. On the **Advanced** step, decide whether to Enable throttling and **Enable CORS**.
10. On the **Summary** step, check if everything is correct and either select **Back** to correct mistakes or **Submit** to publish your API Product.

### To customize advanced settings for API product
Consider customizing advanced settings for your API product. If you make any changes, at the bottom of this page, select **Submit** to save them.

In the **Throttling** section, you can limit the number of allowed calls to your API.  To do so:

1.	Under **Counter Key**, select if you want to check the number of calls from an **API Address** or from a **Subscription Key**.
2.	Under **Calls**, enter a number that will be the limit for how many calls can be made to the API.
3.	Under **Renewal** period in seconds, set the time in which the calls cannot exceed the number you set in Calls.
4.	Under **Increment condition**, decide if only successful calls to your API count against the call limit (**Success**) or if all calls, including failed ones, are counted (**Any**).

In the **CORS** section, which stands for Cross-Origin Resource Sharing:
1.	Under **Allowed origin**, enter the domains (and subdomains) from which your API will allow requests. For exampe, `https://veracity.com`. 
2.	Under **Allowed methods**, you can select which types of HTTP methods (GET, POST, PUT, and so on) can be used in the API requests to your API product.

## To publish API specifications
1.	Go to Developer Portal.
2.	Go to **My projects**.
3.	Reuse the project and resource group where you placed the API Product to which you want to connect this API specification.
4.	In the resource group, select **New Resource**.
5.	Select resource type **API Specification** and select **Next**.
6.	On the **Structure** step, select a project and a resource to which you want to assign the API Specification. Use the same project and resource group as for the API Product.
7.	On the **Configure** step: 
a.	Name the API Specification.
b.	Decide if it requires subscription to access it.
c.	Under **API Products**, select the product(s) to which this specification should be assigned.
d.	Under **Upload type**, select the type of the API specification file that you will upload.
e.	Under **API Specification**, paste API specification. This can be a Swagger or Openapi link, a Swagger json, or Openapi yaml or json file, depending on the Upload type you selected.
f.	Under **API Suffix**, enter API suffix that will be used in full URL. 
g.	Optionally, under **Version**, enter the version of this API specification.
8.	On the **Summary** step, check if everything is correct and either select **Back** to correct mistakes or **Submit** to publish your API Specification.

## To show API Product in API Explorer
Your API Product must meet the following conditions to show in Veracity API Explorer.
* Be a public API. To check this setting, open the API Product on the Configure tab and ensure that the **Is public?** toggle is on.
* Have at least one **API Specification** assigned to it. When you open an API Product and go to the Settings tab, look under **API Specification** to see all API specifications assigned to it.
* Be in a resource group that was approved to the production environment. If you are unsure whether your resource group is in production or need to publish a new group, contact the [onboarding team](mailto:onboarding@veracity.com). If you are new to Veracity, [read about the onboarding process](https://developer.veracity.com/docs/section/onboarding/onboarding).

## To share access to a private API
Share the URL to your API. The URL structure is:
https://developer.veracity.com/docs/section/api-explorer/{API Product ID}/apis/provider/{API-Specifications-ID}

To get API Product ID:

1. On Developer Portal, go to My Projects.
2. Find your API Product and open it.
3. Go to the **Settings** tab and copy **API Product ID**.

To get API Specification ID:

1. On Developer Portal, go to My Projects.
2. Find your API Specifications and open them.
3. Go to the **Settings** tab and copy **API Specification ID**.