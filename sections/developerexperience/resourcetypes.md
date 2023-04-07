---
author: Veracity
description: Learn about different resorce types offered by Veracity.
---

# Resource types

You can use different resource types that Veracity has prepared for you.

## Veracity Service

## App or API

## API product
This is a package of one or more APIs that are bundled together and offered as a single product. This package includes documentation, support, and any other resources necessary to help developers integrate the APIs into their applications.

### To create an API product
1. Either from **My projects**, an existing project, or a resource group, select **Create new resource**.
2. Select **API Product** and then, at the bottom of the resource list, select **Next**. This will open a configuration wizard.
3. On the **Structure** step, select under which project and resource group your want to put your API product.
4. On the **Configure** step:

	4.1 Enter the name of your product.

	4.2 Under **Require subscription approval**, toggle it to **False** to automatically approve new subscriptions or **True** to require manual approval from administrators.

	4.3 Under **Is public**, toggle **False** to make the API product accessible only by a direct link or **True** to make it visible in Veracity API Explorer.

5. Under **Description**, add a description for your API product.
6. On the **Advanced** step, you can enable API throttling and CORS.
	
	6.1 To **Enable throttling**, toggle **Yes**. Then, select a counter key (Veracity recommends using subscription key for your API), enter the number of allowed calls, enter the renewal period in seconds (the period of time in which the calls cannot exceed the call limit), and the incremenent condition (what counts as an API call).
	
	6.2 To **Enable CORS**, toggle **Yes**. Then, enter the allowed origins and the allowed methods.
	
7. On the **Advanced** step, you can set password expiration policy and toggle acccess levels.
	
	7.1 To force users to change their passwords after certain time has passed, toggle **Set password expiration policy**. Then, select when to make the password expiration check and after what time users' passwords expire. 
	
	Note that this settings are not applied to federated users.
	
	7.2 To add access levels to your application, toggle **Access levels** and add at least two roles for your application. You can assign access levels to users and check the "role" property of a subscribed user through Veracity Services API. 
	
	Note that you should avoid adding access levels to an application that is in production because this will revert your subscribers to the "not subscribed" status before you could assign them new access roles.

	Note that deleting or renaming an access level is not supported (the change will have no effect), so if you started using access levels, avoid disabling them.

8. On the **Summary** step, check the summary of your API product. If anything needs to be corrected, select **Back** to go to the previous step. When you are ready to submit your application, select **Submit**.


### To edit API product
1. Go to the project and resource group where the key is grouped.
2. Select the name of the API product resource. This will open the edit menu.

In the edit menu, you can:
* In the **Configure** tab, change the API product's name, enable or disable subscription approval, make the API public or private, and change its description.
* In the **Advanced** tab, configure API throttling and CORS.
* In the **Settings** tab, see API Product ID and API specification.

## Veracity JWT Key
This resource type is used for creating JWT keys and for token validation.


### To create a Veracity JWT key
1. Either from **My projects**, an existing project, or a resource group, select **Create new resource**.
2. Select **Veracity JWT key** and then, at the bottom of the resource list, select **Next**. This will open a configuration wizard.
3. On the **Structure** step, select under which project and resource group your want to put your JWT key.
4. On the **Configure** step, enter the name and description for your JWK key.
5. On the **Advanced** step, select **New claim** and add a claim. For a list of Veracity Identity claims, go [here](../identity/authentication/claims.md).
6. On the **Advanced** step, check if everything is correct, and select **Submit**.

### To update an JWT key
1. Go to the project and resource group where the key is grouped.
2. Select the name of the JWK resource. This will open the update menu.

In the update menu, you can:
* In the **Configure** tab, change the key's name, description, and manage claims it contains. 
* In the **Clients** tab, manage clients, including setting expiration date for the JWT token or revoking the token. 
* In the **Settings** tab, copy the public key.

## Veracity API clients

This resource is used for creating Veracity API clients.

### To create a Veracity API client
1. Either from **My projects**, an existing project, or a resource group, select **Create new resource**.
2. Select **Veracity API client key** and then, at the bottom of the resource list, select **Next**. This will open a configuration wizard.
3. On the **Structure** step, select under which project and resource group your want to put your client.
4. On the **Configure** step:
	4.1 Enter the resource name.
	4.2 If the client requires a subscription key, tick the tickbox **Need Subscription Key** and select the API for which it a subscription key. 
	4.3 If the client should use an access token,  tick the tickbox **Will Use Access Token** and select a JWK key.
	4.4 Add any **Claims** that you need and then select the **Submit**. For a list of Veracity Identity claims, go [here](../identity/authentication/claims.md).
5. On the **Settings** step, 

## Domain Event Management

This resource is used for managing the Veracity Common Domain Infrastructure.

### To create Domain Event Management
1. Either from **My projects**, an existing project, or a resource group, select **Create new resource**.
2. Select **Domain Event Management** and then, at the bottom of the resource list, select **Next**. This will open a configuration wizard.
3. On the **Structure** step, select under which project and resource group your want to put your Domain Event Management key.
4. On the **Configure** step, enter the name and description for your Domain Event Management.
5. On the **Advanced** step, 
6. On the **Summary** step, check if everything is correct, and select **Submit**.
