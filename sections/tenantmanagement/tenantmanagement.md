--- 
author: Veracity 
description: Veracity Tenant Management for Developers
---

# Veracity Tenant Management for Developers

## Overview

Veracity Tenant Management (VTM) is the technology that powers Veracity Access Hub and Veracity MyServices. VTM handles access permissions for Veracity applications and the services connected to them. VTM follows standardized conventions and formats, responds to various events, and manages tenants, profiles, and groups to ensure smooth integration with other systems and services. VTM comes with an API.

Each tenant has three main entity types:

-   Tenant

    -   TenantService – An instance of a service or application within the parent tenant.

-   Profile (either a user or a service principal).

-   User Group – A group of users intended for managing access to applications.

Note that in end-user documentation, tenants are called company accounts.

Users may belong to multiple tenants. Veracity access levels and other attributes that are connected to a subscription come from the closest arrow to the service. In the sample below, that gives users a, b, c and e the same access level and attributes in their subscriptions, while user f has its own.

<figure>
	<img src="assets/image1.png"/>
</figure>

Applications that need more advanced permissions management should follow the same principles and replicate this in their own database.

### Tenant selector 

All applications that recognize tenants must present a tenant selector when the user accesses the application root (the users enter the application without having the tenant ID propagated through the URL).

Also, the application should allow switching between tenants.


<figure>
	<img src="assets/image2.png"/>
</figure>

After the normal login flow and policy check the application contacts VTM and requests the list of tenants where the user has a subscription to the service. This will confirm that the user has a subscription in one or more tenants and the application can decide if it is necessary to show the list.

If the list is empty, an error page should be shown. If there is one tenant, the user should be redirected to that tenant. And if there are two or more, the user needs to decide which tenant they are going to use the application on behalf of.

### Tying the application to the tenant

When a customer acquires an application from the Marketplace or through direct sales, the application gets installed in the customer's tenant. When installing the application, the service principals for that application are added to the tenant and granted the appropriate permissions. Only applications registered in Veracity for Developers can be installed in a tenant.

If the application uses the Veracity Domain Event system, application-specific initialization tasks can be executed automatically like installing a new instance of the application in a Kubernetes cluster.

### Granting access

Customers use Veracity Access Hub to manage access to their applications and decide on how much control they delegate to VTM. VTM offers three types of access control:

-   **Fully managed by Veracity** - Suitable for applications with role-based access control if the roles are application-wide (for example, reader, contributor, and so on). Admins can create user groups in VTM, assign certain access permissions to them, and then add users to those groups. Then, Veracity handles access control for the application.

-   **Hybrid access control** – Admins configure basic access permissions in Veracity and the details in the application.

-   **Complex access models** – The application handles access permissions, and Veracity shows the admins the applications, the users having access to them, and some other general information.

To see sample scenarios for each kind of access control, go to [Sample use case scenarios](#use-case-scenarios).

### Admin roles
Customers can assign different admin roles depending on how many permissions they want to grant.
-   **User Admin** - A User Admin can add, approve, and remove users within a tenant.

-   **Group Admin** - A Group Admin can add or remove users from a group they administer within a tenant.

-   **Application Admin** - An Application Admin can view, add, and delete liceses for users and groups to the application. They can also change setting for the application such as automatic license assignment.

## VTM terminology and tips

-   User account – A representation of the user as an identity.

-   User profile - A representation of the user in an application. One user can have at least as many profiles as the applications they have access to. If a profile is related to a company account, the company account ID is “baked into” the profile.

-   Tenant – An account for a specific company. In interface and documentation for admins, it is called a company account. Admins and the account owner can add users. Tenants can contain groups. A tenant is also a practical grouping of user profiles.

-   User group – A collection of user profiles within a tenant that can be assigned access permissions to Resource Groups or other entities.

**Note that the user account ID** **is not the same as the user profile**. To use VTM, you need to look up user profiles (for example, from the API or the application database) and map users’ IDs to users’ profiles.

If possible, avoid making a full admin interface on your own. Use the Veracity Access Hub instead for adding users to the tenant, managing group membership and permissions, and so on.

## How the API works

The API surface includes multiple endpoints for managing tenants, profiles, groups, and other aspects of the system. Some endpoints follow the OData query format, while others support batch operations for improved efficiency.

Events generated by API calls and other sources are processed and communicated across the Tenant Management system. The API supports different payload types for various actions, such as create (POST), replace (PUT), mutate (PATCH), and delete (DELETE).

The API posts messages to the event store and immediately returns an HTTP 202 Accepted response. A transaction ID is sent back to the client in an HTTP header, allowing the client to check the processing state of the action.

**Note that** VTM is eventual consistent system meaning that you may not immediately read what you have just written.

For example, when a user creates a new tenant in the API, MyServices and other services process the creation of a new tenant through the service bus.

Another example is when a new company is created in MyServices. Then, the message is passed by the service bus and a new tenant is created in Veracity Tenant Management.

For API specification, go to [Swagger UI.](https://tenantmanagement-jhzsxkv2oanng-devtest.azurewebsites.net/swagger/index.html)

### How to use the API

For authentication and authorization of your API calls, follow [these instructions](https://developer.veracity.com/docs/section/identity/authentication/web-native#get-an-access-token-for-the-user).

Veracity suggests using the PATCH method (mutate) to change things through the API. Note that it is not always possible, though.

Ideally, querying data and adding and removing subscriptions to groups and profiles should be the only mutation you will need to do in Veracity Tenant Management.

#### To check for violated policies for the signed in user and service subscription status

To check for violated polices for the signed in user and the subscription status to specified service, call the following endpoint with a GET method:

```json
 GET
 https://api.veracity.com/Veracity/Services/V3/my/policies/\[serviceid\]/validate()  
 Host: api.veracity.com  
 Ocp-Apim-Subscription-Key: \[subscription-key\]  
 Authorization: Bearer \[token\]
 ```

If the signed in user doesn’t violate any policy and has a subscription to the service, you will get a 204 OK response.

If they user doesn’t have a valid subscription, you will get a 406 Not Acceptable response:

```json
{  
"url":"https://servicestest.veracity.com",  
 "violatedPolicies":\["Subscription"\],  
 "SubscriptionMissing":true,  
 "message":"No subscription found",  
 "information":null,  
 "subCode":0,  
 "supportCode":"\[generated\_id\]"  
 }
 ```

If the user has other policies that are violated, like not accepting terms and conditions, you will get a 406 Not Acceptable response and the user should be redirected to the returned URL:

```json
 {  
 "url":"\[url\]/terms-of-use?mode=accept&redirect-url=&id=\[serviceid\]",  
 "violatedPolicies":\["Terms needs acceptance"\],  
 "SubscriptionMissing":null,  
 "message":"Terms need acceptance",  
 "information":"please accept policy \[serviceid\]",  
 "subCode":3,  
 "supportCode":"\[generated\_id\]"  
 }
 ```

#### To check subscription to a service

To check if a user has a subscription (flow) to a specified service, call the following endpoint with a GET method:

 https://api.veracity.com/Veracity/Services/V3/this/services/\[serviceid\]/subscribers/\[userid\] HTTP/1.1

 Host: api.veracity.com  
 Ocp-Apim-Subscription-Key: \[subscription-key\]  
 Authorization: Bearer \[token\]

If the user has a subscription to the specified service, you will get a
200 OK response:

```json
 {  
 "state": "Subscribing",  
 "identity": "/directory/users/\[userid\]",  
 "email": "\[useremail\]",  
 "activated": true,  
 "name": "\[username\]",  
 "id": "\[userid\]"  
 }
 ```

If the user doesn’t have a subscription to the specified service, you will get a 404 Not Found response:

```json
 {  
 "message":"Service subscription not found. with id =
 \[userid\]:\[serviceid\] not found",  
 "information":"Type: System.Security.Claims.ClaimsIdentity, Identity:
 \[generated\_id\], , Claim: \[generated\_id\]",  
 "subCode":0,  
 "supportCode":"\[generated\_id\]"  
 }
 ```

#### To add a user to a service

To add a user to a service, call the following endpoint with a PUT method:

```json
 PUT
 https://api.veracity.com/Veracity/Services/V3/this/services/\[serviceid\]/subscribers/\[userid\]
 HTTP/1.1  
 Host: api.veracity.com  
 Ocp-Apim-Subscription-Key: \[subscription-key\]  
 Authorization: Bearer \[token\]
 ```

If the call is successful, you will get a 204 OK response.

#### To remove a user from a service

To remove a user from a service, call the following endpoint with a PUT method:

```json
 DELETE
 https://api.veracity.com/Veracity/Services/V3/this/services/\[serviceid\]/subscribers/\[userid\]
 HTTP/1.1  
 Host: api.veracity.com  
 Ocp-Apim-Subscription-Key: \[subscription-key\]  
 Authorization: Bearer \[token\]
 ```

If the call is successful, you will get a 204 OK response.

#### To get information on the signed in user

To information on the signed in user, call the following endpoint with a GET method:

```json
 GET https://api.veracity.com/Veracity/Services/V3/my/profile
 HTTP/1.1  
 Host: api.veracity.com  
 Ocp-Apim-Subscription-Key: \[subscription-key\]  
 Authorization: Bearer \[token\]
 ```

Below is sample information you might get from this request:

```json
 {  
 "profilePageUrl": "https://mytest.dnvgl.com/EditProfile",  
 "messagesUrl": "/my/messages",  
 "identity": "/my/profile",  
 "servicesUrl": "/my/services?page=0&pageSize=10",  
 "companiesUrl": "/my/companies",  
 "name": "Spersrud, Arild",  
 "email": "john.brown@dnv.com",  
 "id": "6d0766d9-46fe-44e0-aea0-43803ee8707d",  
 "company": {  
 "identity":
 "/directory/companies/4558b6b9-6144-461b-83ac-f22c3a139edb",  
 "name": "111111111",  
 "id": "4778b6b9-6199-461b-83ac-f22c3a139edb"  
 },  
 "#companies": 19,  
 "verifiedEmail": true,  
 "phone": "+47 45018303",  
 "verifiedPhone": true,  
 "firstName": "John",  
 "lastName": "Brown",  
 "countryCode": "NO",  
 "managedAccount": false,  
 "activated": true  
 }
 ```

## Service Bus

The Service Bus documentation will be made available shortly.

## Use case scenarios

Below we present sample use case scenarios for VTM. The scenarios correspond to the [three types of access control](https://dnv.sharepoint.com/:w:/r/teams/VeracityIdentityTrustNetwork/Shared%20Documents/Tenant%20Management/Documentation/Veracity%20Access%20Hub%20Guide.docx?d=w8e4cd5772cbf4cefabd1a87f630f90f8&csf=1&web=1&e=ekpFBB&nav=eyJoIjoiMjc5ODE1ODkzIn0) that Veracity Tenant Management offers.

### Simple calculator (fully managed by Veracity)

The user needs a license for this service but it doesn’t require more authorization. The application relies on normal Veracity sign-in flow with an additional subscription check.

All users can do everything in the service meaning there are no roles with varying permissions.

#### APIs used

|Name|URL|
|--------|-----------|
|Policy|https://api.veracity.com/Veracity/Services/V3/my/policies/%7bserviceId%7d/validate()|
|Subscription details|https://api.veracity.com/veracity/vtm/v1/tenant/%7btenantId%7d/services/%7bserviced%7d/subscribers/%7bprofileId%7d|


#### Business case

An example of such an application might be an analysis tool that lets you run offline operational scenarios for your compressor to optimise your machine’s configuration an quantify the effect of changing gas compositions such as adding Biogas, LNG, and Hydrogen.

### Seating tracker for hot seating workplaces (complex access model)

In this example, we have a:

-   Multi-tenant application. When the user accesses the application’s root, if you follow [Veracity Tenant Selector guidelines](https://dnv.sharepoint.com/:w:/r/teams/VeracityIdentityTrustNetwork/Shared%20Documents/Tenant%20Management/Documentation/Veracity%20Tenant%20Management%20for%20Developers.docx?d=wca837b6c59844fd59ae5b187ed93cb3b&csf=1&web=1&e=gVEF38&nav=eyJoIjoiNjI5OTExMzY4In0), you can make an API call to check which tenants the user has access to. Then, if they only belong to one, you take them there directly and if they belong to multiple tenants, you ask them to choose to which tenant they want to sign in.   Note that, instead of using APIs to get the tenant, you can use a local copy synchronized through Veracity Service Bus.

-   Support for access levels and permissions based on roles.

-   User management tasks are delegated to Veracity.

Note that:

-   You can check to which tenant(s) user belongs with API calls.

-   You can check user permissions through API calls.

-   You can delegate user management to Veracity APIs.

Thanks to this, you can focus on the functional requirements of the application you are building.

The application allows admins to manage floor plans by uploading “maps” and configuring seating locations. Normal users can register their desk for the day in the tool. It is a multi-tenant SaaS application.

#### APIs used

|Name|URL|
|--------|-----------|
|Policy|https://api.veracity.com/Veracity/Services/V3/my/policies/%7bserviceId%7d/validate()|
|Service tenants|https://api.veracity.com/veracity/vtm/v1/me/services/%7bserviceId%7d/tenants|
|Access level|https://api.veracity.com/veracity/vtm/v1/tenant/%7btenantId%7d/services/%7bserviced%7d/subscribers/%7bprofileId%7d|
|Profile picture|https://api.veracity.com/veracity/services/v3/my/picture|
|Profile picture for user|https://api.veracity.com/veracity/services/v3/this/services/%7bserviceId%7d/subscribers/%7buserId%7d/picture|
|All users|https://api.veracity.com/veracity/vtm/v1/tenant/%7btenantId%7d/services/%7bserviced%7d/subscribers/exploded|


Note that if the application needs to store a local copy, it must be able to provide the same results as the API (access level).

#### Business case

An example of such an application might be a data service that provides on-demand information for solar power plants. Users have access to data from different sites (multi-tenant structure), authentication and authorization is handled by calling Veracity APIs and the same is true for checking user permissions in the application (for example, engineers can automate site-screening and feasibility analysis, but external consultants can only read some data).

### Health and safety tracker application (hybrid access model)

The application is used for risk management and as a health and safety tracker. All users can register incidents and risks, and then the application assigns them to the ‘Case responsible’ based on some criteria (for example, case type or geographical region).

This application has a well-defined least privilege but requires more detailed permissions for the ‘Case responsible’ granting permissions to objects not modeled in the VTM data structure.

#### APIs used

|Name|URL|
|--------|-----------|
|Policy|https://api.veracity.com/Veracity/Services/V3/my/policies/%7bserviceId%7d/validate()|
|Service tenants|https://api.veracity.com/veracity/vtm/v1/me/services/%7bserviceId%7d/tenants|
|Access level|https://api.veracity.com/veracity/vtm/v1/tenant/%7btenantId%7d/services/%7bserviced%7d/subscribers/%7bprofileId%7d|
|Profile picture|https://api.veracity.com/veracity/services/v3/my/picture|
|Profile picture for user|https://api.veracity.com/veracity/services/v3/this/services/%7bserviceId%7d/subscribers/%7buserId%7d/picture|
|All users|https://api.veracity.com/veracity/vtm/v1/tenant/%7btenantId%7d/services/%7bserviced%7d/subscribers/exploded|
|Add subscription|https://api.veracity.com/veracity/vtm/v1/tenant/%7btenantId%7b/services/%7bid%7d/subscribers/%7bentityId%7d?memberType=%7bprofile|
|Get groups|https://api.veracity.com/veracity/vtm/v1/tenant/%7btenantId%7d/groups?$filter=isBuiltIn%20eq%20false|
|Get direct group members|https://api.veracity.com/veracity/vtm/v1/tenant/%7btenantId%7d/groups/%7bgroupId%7d/members|
|Get all group members|https://api.veracity.com/veracity/vtm/v1/tenant/%7btenantId%7d/groups/%7bgroupId%7d/members/exploded|



In this scenario, the application will receive the basic permissions from Veracity and all these users will have a clear least privilege defined as being allowed to report new incidents and see the status of cases they have reported. The tenant admin or application access admins can assign additional permissions to individual users or groups in the application. The application can, if required for performance or resiliency reasons, keep a local copy of the tenant structure that is relevant.

Additional permissions are then assigned to userGroups or individual profiles. In the permission configuration table/storage, each permission must tell if it is a group or profile that is assigned the permission.

### App with complex authorization and no clear least privilege defined (Data Workbench)

An example of such an application is [Data Workbench](https://store.veracity.com/data-workbench).

This is an application with no clear least privilege defined and cannot use the Veracity subscription model directly. However, to get update notifications from Veracity Identity and other Veracity components, the application needs to register a subscription for all users that are granted access to the application.

#### APIs used

|Name|URL|
|--------|-----------|
|Policy|https://api.veracity.com/Veracity/Services/V3/my/policies/%7bserviceId%7d/validate()|
|Service tenants|https://api.veracity.com/veracity/vtm/v1/me/services/%7bserviceId%7d/tenants|
|Access level|https://api.veracity.com/veracity/vtm/v1/tenant/%7btenantId%7d/services/%7bserviced%7d/subscribers/%7bprofileId%7d|
|Profile picture|https://api.veracity.com/veracity/services/v3/my/picture|
|Profile picture for user|https://api.veracity.com/veracity/services/v3/this/services/%7bserviceId%7d/subscribers/%7buserId%7d/picture|
|All users|https://api.veracity.com/veracity/vtm/v1/tenant/%7btenantId%7d/services/%7bserviced%7d/subscribers/exploded|
|Add subscription|https://api.veracity.com/veracity/vtm/v1/tenant/%7btenantId%7b/services/%7bid%7d/subscribers/%7bentityId%7d?memberType=%7bprofile|
|Get groups|https://api.veracity.com/veracity/vtm/v1/tenant/%7btenantId%7d/groups?$filter=isBuiltIn%20eq%20false|
|Get direct group members|https://api.veracity.com/veracity/vtm/v1/tenant/%7btenantId%7d/groups/%7bgroupId%7d/members|
|Get all group members|https://api.veracity.com/veracity/vtm/v1/tenant/%7btenantId%7d/groups/%7bgroupId%7d/members/exploded|


In the application, the tenant admin or application access admins can assign additional permissions to individual users or groups. The application can, if required for performance or resiliency reasons, keep a local copy of the tenant structure that is relevant.

Permissions are assigned to userGroups or individual profiles. In the permissions configuration table/storage each permission must tell if it is a group or profile that is assigned the permission. When a user/group is assigned permission, the application needs to ensure that the user/group has a subscription to the technical service in Veracity.
