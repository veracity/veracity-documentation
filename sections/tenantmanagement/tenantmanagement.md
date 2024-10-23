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

Customers can assign users different admin roles depending on how many permissions they want to grant them.

-   **User Admin** - A User Admin can add, approve, and remove users within a tenant.

-   **Group Admin** - A Group Admin can add or remove users from a group they manage within a tenant.

-   **Application Admin** - An Application Admin can view, add, and delete licenses for users and groups to the application. They can also change application settings such as automatic license assignment.

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

Veracity Services API version 4 is organized into the following groups of endpoints to focus on tenants, applications, groups, and users, with more granular control and additional functionalities.
* [Applications](#applications): Provides methods to interact with applications within a tenant. Supports retrieving applications, verifying user licenses, and managing user and group licenses.
* [Groups](#groups): Provides methods to manage groups and their members within a tenant. Supports retrieving groups, group members, and updating group properties.
* [Me](#me): Provides methods to retrieve information about the signed-in user, including their applications, groups, and tenants.
* [Tenants](#tenants): Provides methods to interact with tenants, including retrieving tenant details, and managing tenant administrators.
* [Users](#users):  Provides methods to manage users within a tenant, including retrieving user details, groups, and applications.



#### Updating with JsonPatch

Veracity suggests using the PATCH method (mutate) to change things through the API. Note that it is not always possible, though.

Ideally, querying data and adding and removing subscriptions to groups and profiles should be the only mutation you will need to do in Veracity Tenant Management.

See an example of using the PATCH method.

```json
[{"op":"replace","path":"/affiliationMode","value":"restricted"}]
```

##### Example of updates with JsonPatch

You can use JsonPatch to update data within the graph, such as adding, updating, or removing extension properties. See a sample scenario on how to do it.

You start with a payload with the following properties collection.

```json
"properties": [
        {
          "name": "vtmd2_allowedVessels",
          "value": ""
        }
      ]
```

Then, you can update the user to indicate the vessels which the user can see in the app and mark the new application user as seen by an admin.


```json
[
  {
    "value": {
      "Name": "vtmd2_allowedVessels",
      "Value": "7911545;7911533"
    },
    "path": "/properties/-",
    "op": "replace"
  },
  {
    "value": {
      "Name": "vtmd2_isSeen",
      "Value": "true"
    },
    "path": "/properties/-",
    "op": "add"
  }
]
```

This will result in the following properties:

```json
"properties": [
        {
          "name": "vtmd2_allowedVessels",
          "value": "7911545;7911533"
        },
        {
          "name": "vtmd2_isSeen",
          "value": "true"
        }
      ]
```

Then, you can remove the `allowedVessels` list and reset the `isSeen` flag. To do it, first remove the `vtmd2_allowedVessels` property by its index and then, do any other operations. Do these actions in this order, because when you do other operations, the elements can change, and the REMOVE method does not support removing by name.

You can do the same type of operations on any entity or relationship in the graph. See the example of a payload below.

```json
[
      "path": "/properties/0",
    "op": "remove"
  },
  {
    "value": {
      "Name": "vtmd2_isSeen",
      "Value": "false"
    },
    "path": "/properties/-",
    "op": "replace"
  }
]
```

This results in the following properties:

```json
 "properties": [
        {
          "name": "vtmd2_isSeen",
          "value": "false"
        }
      ]
```

Note that the NuGet packages provided by Veracity have helper methods to construct these queries and run them directly against the API.

```json
    user.MakeJsonPatch()
        .AddOrUpdateProperty("allowedVessels", "7911545;7911533")
        .AddOrUpdateProperty("isSeen", "true")
        .ExecutePatchUserAsync();
```

For more information about patching, go [here](https://jsonpatch.com/).

#### Applications

The **Applications** interface provides methods to interact with applications within a tenant. Use it to retrieve applications, verify user licenses, and manage user and group licenses.

##### Check applications installed in the tenant with support for OData query parameters
To check the applications installed in the tenant with support for OData query parameters, call the following endpoint with a GET method:
* `/tenants/{tenantId}/applications`

##### Check an application by its public ID
To check a specific application by its public ID, call the following endpoint with a GET method:
* `/tenants/{tenantId}/applications/{applicationId}`

##### Check direct users and groups with licenses for the application
To check all direct users and groups with licenses for an application, call the following endpoint with a GET method:
* `/tenants/{tenantId}/applications/{applicationId}/licenses`

##### Verify the user's license for the application
To verify if a user has a license for an application, call the following endpoint with a GET method:
* `/tenants/{tenantId}/applications/{applicationId}/licenses/{userId}`

##### Check all users
To check all users, including users inherited from groups, with deduplication support, call the following endpoint with a GET method:
* `/tenants/{tenantId}/applications/{applicationId}/users`
Note that you can disable deduplication to detect users with multiple paths to the application in the tenant.

##### Add a user or group license to the application
To add a user or group license to an application, call the following endpoint with a POST method:
* `/tenants/{tenantId}/applications/{applicationId}/licenses`

##### Set access level on the existing subscription
To set access level on the existing subscription, call the following endpoint with a PUT method:
* `/tenants/{tenantId}/applications/{applicationId}/licenses/{entityId}`
Note that you can use it only with applications which have access levels.

##### Update license details
To update license details using a JSON patch document, call the following endpoint with a PATCH method:
* `/tenants/{tenantId}/applications/{applicationId}/licenses/{entityId}`

##### Remove subscription
To remove a subscription, call the following endpoint with a DELETE method:
* `/tenants/{tenantId}/applications/{applicationId}/licenses/{entityId}`

##### Check all tenants
To check all tenants where the application is installed, call the following endpoint with a GET method:
* `/applications/{applicationId}/tenants`

##### Update application extension properties
To update application extension properties using a JSON patch document, call the following endpoint with a PATCH method:
* `/tenants/{tenantId}/applications/{applicationId}`

##### Check application administrators
To check all application administrators, call the following endpoint with a GET method:
* `/tenants/{tenantId}/applications/{applicationId}/administrators`

##### Add application administrator
To add a user as an application administrator, call the following endpoint with a POST method:
* `/tenants/{tenantId}/applications/{applicationId}/administrators/{userId}`

##### Remove application administrator
To remove an application administrator, call the following endpoint with a DELETE method:
* `/tenants/{tenantId}/applications/{applicationId}/administrators/{userId}`


#### Groups
The **Groups** interface provides methods to manage groups and their members within a tenant. Use it to retrieve groups andgroup members, and update group properties.

##### Get groups in tenant with support for OData query parameters
To check the groups in the tenant with support for OData query parameters, call the following endpoint with a GET method:
* `/tenants/{tenantId}/groups`

##### Check a group
To check a specific group by its ID, call the following endpoint with a GET method:
* `/tenants/{tenantId}/groups/{groupId}`

##### Check direct users and groups in a group
To check all direct users and groups within a group, call the following endpoint with a GET method: 
* `/tenants/{tenantId}/groups/{groupId}/members`

##### Get users
To check all users, including users inherited from groups, call the following endpoint with a GET method:
* `/tenants/{tenantId}/groups/{groupId}/members/exploded`

##### Update a member
To update member properties using a JSON patch document,  call the following endpoint with a PATCH method: 
* `/tenants/{tenantId}/groups/{groupId}/members/{memberId}`

##### Update a group
To update group properties using a JSON patch document, call the following endpoint with a PATCH method:
* `/tenants/{tenantId}/groups/{groupId}`

##### Check what groups a group is a part of
To list all the groups a specific group is a member of, call the following endpoint with a GET method: 
* `/tenants/{tenantId}/groups/{groupId}/memberOf`

##### Get applications group has a license for
To check all the applications licensed for the group, call the following endpoint with a GET method:
* `/tenants/{tenantId}/groups/{groupId}/applications`

#### Me
The **Me** interface provides methods to retrieve information about the logged-in user, including their applications, groups, and tenants.

##### Check details for logged-in user
To check the details for the logged-in user, call the following endpoint with a GET method:
* `/me`

##### Check all applications the user has access to
To check all the applications to which the user has access, call the following endpoint with a GET method:
* `/me/applications`

##### Check all applications in the tenant to which the user has access
To check all the applications in the tenant to which the user has access, call the following endpoint with a GET method:
* `/me/tenants/{tenantId}/applications`

##### Check groups to which the logged-in user belongs
To check all the groups to which the logged-in user belongs, call the following endpoint with a GET method:
* `/me/tenants/{tenantId}/groups`

##### Check all the tenants to which the logged-on user belongs
To check all the tenants to which the logged-on user belong, call the following endpoint with a GET method:
* `/me/tenants`

##### Check all tenants to which the logged-on user belongs and has access to a specific application
To check all the tenants the logged-on user is a member of and has access to a specific application, call the following endpoint with a GET method:
* `/me/applications/{applicationId}/tenants`

##### Verify Veracity user policies
To Verify Veracity user policies and return appropriate responses based on policy compliance, call the following endpoint with a POST method:
* `/me/applications/{applicationId}/.policy()`

It returns an empty 202 response if all policies are correct, and 406 with an error response with the URL to send the user to the correct the policy issue.

#### StatusService
To check information about the status of the service, call the following endpoint with a GET method:
* `/health`

You will get:
* A 200 OK response if all dependencies are correct.
* A 424 Failed Dependency response if there are some non-essential dependency failures. 
* A 500 Internal Server response when some essential dependencies are unreachable, or the service is down.

#### Tenants
The **Tenants** interface provides methods to interact with tenants, including retrieving tenant details and managing tenant administrators.

##### Get a tenant by ID
To check a tenant by its ID, call the following endpoint with a GET method:
* `/tenants/{tenantId}`

##### Check tenants linked to your service
To get a list of tenants linked to a specific service, call the following endpoint with a GET method:
* `/tenants`

##### Check admin details for the user by their ID
To check admin details for the user by their ID, call the following endpoint with a GET method:
* `/tenants/{tenantId}/admins/{userId}`

##### Get admins of the tenant
To checl all global and local admins of a tenant, call the following endpoint with a GET method:
* `/tenants/{tenantId}/admins`

#### Users
The **Users** interface provides methods to manage users within a tenant, including retrieving user details, groups, and applications.

##### Checka user by their email
To check a user by their email address, call the following endpoint with a GET method:
* `/tenants/{tenantId}/users/.email({email})`

##### Check user by their ID
To check a user by their ID, call the following endpoint with a GET method:
* `/users/{userId}`

#####  List users in a tenant
To get a list of users in a tenant with support for OData query parameters,  call the following endpoint with a GET method:
* `/tenants/{tenantId}/users`

##### Check user details in a tenant
To check the details of a user in a tenant, call the following endpoint with a GET method:
* `/tenants/{tenantId}/users/{userId}`

##### Check user's groups
To check the groups associated with a user, call the following endpoint with a GET method:
* `/tenants/{tenantId}/users/{userId}/groups`

##### Check user's applications
To check the applications associated with a user,call the following endpoint with a GET method:
* `/tenants/{tenantId}/users/{userId}/applications`

##### Check tenants to which the user belongs
To check the tenants a user is a member of, call the following endpoint with a GET method:
* `/users/{userId}/tenants`

##### Check full user details for a list of user IDs
To check full user details for a list of user IDs, call the following endpoint with a POST method:
* `/tenants/{tenantId}/users`

##### Update user extension properties
To update the extension properties for a user using a JSON patch document, call the following endpoint with a PATCH method:
* `/tenants/{tenantId}/users/{userId}`

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
