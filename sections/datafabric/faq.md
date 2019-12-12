---
author: Veracity
description: Description of FAQ section
---

# Frequently Asked Questions

## How do I get the SAS key for my containers ?

To create a SAS key for your container from the My Data Section in Veracity web site, you need to navigate to your container you want to create the SAS key for.


**Note** : When you try to open your container, if you see the following warning "Your current access key has expired so we are unable to display the contents."


Then, click on "Request access". Once you click you will see the text "Your request has been received". Then click on Access and fill out the required fields. You will be in Share access tab.


**Note** : You can share a key with yourself or with other people.


Click on Share.

To view a SAS Key, navigate to User management tab in Access. Here you can get an overview for all keys for your container. You can see the keys you own by clicking on View key for any key.

## How to handle SAS key expired situation ?

By default SAS keys are created with a specified duration and that duration starts by redeeming the sharing/access and redeeming is done by clicking on the Access Key for the target key in User management. Once it is clicked, a SAS key is generated for the sharing/access and the key is expired after the specified duration time. The owner of the Access will lose his/her access to the container once the SAS key is expired.

On the other hand, when you create a Access share in Share access, there is an option called Set key as recurring. If this option is specified, the owner of the Access will be able to re-generate a new SAS key after the key generated previously is expired.

Selecting which duration when creating and Access Share is important for the recurring keys. If you set it as 6 months, even if you Revoke that Access, the last generated SAS key will keep Being valid for that duration.

## How to create container in my application ?

This can be achieved with and on-boarded application. You can use the client credentials flow. Your API/application can make the call as the application. Please see the Provisioning API reference for details.

## How to share access of my containers in my application ?

This can be achieved with and on-boarded application. You can use the client credentials flow. Your API/application can make the call as the application. Please see the Data API reference for details.

## How to get access token when I want to sync files with my container in my server without human login ?

You need to first on-board your application into Veracity. For that your application should be registered in AAD B2C v1(Client Credentials grant) with permissions to the Data/Provisioning APIs.

Once this is ready, you can make POST requests to the OAuth2 token endpoint of the tenant.

## How to deal with the case that I want to use DF as file storage, the web application can handle the file no matter who login to the application ?

This can be achieved with and on-boarded application. You can use the client credentials flow. Your API can make the call as the application. Internal Identity is managed by your App is not relevant in that case.
