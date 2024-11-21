--- 
author: Veracity 
description: Veracity Tenant Management for Developers
---

# Veracity Tenant Management for Developers

## Overview

Veracity Tenant Management (VTM) is the technology that powers Veracity Access Hub and Veracity MyServices. VTM handles access permissions for Veracity applications and the services connected to them. VTM follows standardized conventions and formats, responds to various events, and manages tenants, profiles, and groups to ensure smooth integration with other systems and services. VTM comes with an API.

Each tenant has three main entity types:

-   Tenant

    -   Application – An instance of a service or application within the parent tenant.

-   Profile (either a user or a service principal).

-   Group – A group of users intended for managing access to applications.

Note that in end-user documentation, tenants are called company accounts.

Users may belong to multiple tenants. Veracity access levels and other attributes that are connected to a license come from the closest arrow to the service. In the sample below, that gives users a, b, c and e the same access level and attributes in their licenses, while user f has its own.

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

After the normal login flow and policy check the application contacts VTM and requests the list of tenants where the user has a license to the service. This will confirm that the user has a license in one or more tenants and the application can decide if it is necessary to show the list.

If the list is empty, an error page should be shown. If there is one tenant, the user should be redirected to that tenant. And if there are two or more, the user needs to decide which tenant they are going to use the application on behalf of.

### Tying the application to the tenant

When a customer acquires an application from the Marketplace or through direct sales, the application gets installed in the customer's tenant. When installing the application, the service principals for that application are added to the tenant and granted the appropriate permissions. Only applications registered in Veracity for Developers can be installed in a tenant.

If the application uses the Veracity Domain Event system, application-specific initialization tasks can be executed automatically like installing a new instance of the application in a Kubernetes cluster.

### Granting access

Customers use Veracity Access Hub to manage access to their applications and decide on how much control they delegate to VTM. VTM offers three types of access control:

-   **Fully managed by Veracity** - Suitable for applications with role-based access control if the roles are application-wide (for example, reader, contributor, and so on). Admins can create groups in VTM, assign certain access permissions to them, and then add users to those groups. Then, Veracity handles access control for the application.

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

-   Group – A collection of user profiles within a tenant that can be assigned access permissions to Resource Groups or other entities.

**Note that the user account ID** **is not the same as the user profile**. To use VTM, you need to look up user profiles (for example, from the API or the application database) and map users’ IDs to users’ profiles.

If possible, avoid making a full admin interface on your own. Use the Veracity Access Hub instead for adding users to the tenant, managing group membership and permissions, and so on.

## How the API works

The API surface includes multiple endpoints for managing tenants, profiles, groups, and other aspects of the system. Some endpoints follow the OData query format, while others support batch operations for improved efficiency.

Events generated by API calls and other sources are processed and communicated across the Tenant Management system. The API supports different payload types for various actions, such as create (POST), replace (PUT), mutate (PATCH), and delete (DELETE).

The API posts messages to the event store and immediately returns an HTTP 202 Accepted response. A transaction ID is sent back to the client in an HTTP header, allowing the client to check the processing state of the action.

For API specification, go to **API Explorer**.

### Eventual consistency of VTM

Note that VTM is eventual consistent system,  meaning that you may not immediately read what you have just written.

For example, when a user creates a new tenant in the API, MyServices and other services process the creation of a new tenant through the service bus.

Another example is when a new company is created in MyServices. Then, the message is passed by the service bus and a new tenant is created in Veracity Tenant Management.

**Note that** when the endpoint returns a 202 Accepted response for write operations in V4, it does not mean a successful data change. The 202 Accepted response informs that the solution has accepted the change. Then, it will process the change and update the data in the background. 

Once the change has been made, then on the service bus, the solution will publish an event informing whether the operation was successful or not. 

If your application does these write operations, it needs to integrate with the Veracity Service Bus and listen for these events to get the result of the call.
 
To get these messages, in Domain Events, configure that you want messages to the Tenant topic and use this connection to the service bus.

For more information, see the [Service Bus documentation](https://github.com/veracity/veracity-documentation/blob/VTM-docs/sections/servicebus/servicebus.md).


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

Ideally, querying data and adding and removing licenses to groups and profiles should be the only mutation you will need to do in Veracity Tenant Management.

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
  {
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

```c#
    user.MakeJsonPatch()
        .AddOrUpdateProperty("allowedVessels", "7911545;7911533")
        .AddOrUpdateProperty("isSeen", "true")
        .ExecutePatchUserAsync();
```

For more information about patching, go [here](https://jsonpatch.com/).

#### Applications

The **Applications** interface provides methods to interact with applications within a tenant. Use it to retrieve applications, verify user licenses, and manage user and group licenses.

##### Check applications installed in the tenant with support for OData query parameters
To check the applications installed in the tenant with support for OData query parameters, call the following endpoint using the GET method:
* `/tenants/{tenantId}/applications`

##### Check an application by its public ID
To check a specific application by its public ID, call the following endpoint using the GET method:
* `/tenants/{tenantId}/applications/{applicationId}`

##### Check direct users and groups with licenses for the application
To check all direct users and groups with licenses for an application, call the following endpoint using the GET method:
* `/tenants/{tenantId}/applications/{applicationId}/licenses`

##### Verify the user's license for the application
To verify if a user has a license for an application, call the following endpoint using the GET method:
* `/tenants/{tenantId}/applications/{applicationId}/licenses/{userId}`

##### Check all users
To check all users, including users inherited from groups, with deduplication support, call the following endpoint using the GET method:
* `/tenants/{tenantId}/applications/{applicationId}/users`
Note that you can disable deduplication to detect users with multiple paths to the application in the tenant.

##### Add a user or group license to the application
To add a user or group license to an application, call the following endpoint with a POST method:
* `/tenants/{tenantId}/applications/{applicationId}/licenses`

##### Set access level on the existing license
To set access level on the existing license, call the following endpoint using the PUT method:
* `/tenants/{tenantId}/applications/{applicationId}/licenses/{entityId}`
Note that you can use it only with applications which have access levels.

##### Update license details
To update license details using a JSON patch document, call the following endpoint using the PATCH method:
* `/tenants/{tenantId}/applications/{applicationId}/licenses/{entityId}`

##### Remove license
To remove a license, call the following endpoint using the DELETE method:
* `/tenants/{tenantId}/applications/{applicationId}/licenses/{entityId}`

##### Check all tenants
To check all tenants where the application is installed, call the following endpoint using the GET method:
* `/applications/{applicationId}/tenants`

##### Update application extension properties
To update application extension properties using a JSON patch document, call the following endpoint using the PATCH method:
* `/tenants/{tenantId}/applications/{applicationId}`

##### Check application administrators
To check all application administrators, call the following endpoint using the GET method:
* `/tenants/{tenantId}/applications/{applicationId}/administrators`

##### Add application administrator
To add a user as an application administrator, call the following endpoint with a POST method:
* `/tenants/{tenantId}/applications/{applicationId}/administrators/{userId}`

##### Remove application administrator
To remove an application administrator, call the following endpoint using the DELETE method:
* `/tenants/{tenantId}/applications/{applicationId}/administrators/{userId}`


#### Groups
The **Groups** interface provides methods to manage groups and their members within a tenant. Use it to retrieve groups andgroup members, and update group properties.

##### Get groups in tenant with support for OData query parameters
To check the groups in the tenant with support for OData query parameters, call the following endpoint using the GET method:
* `/tenants/{tenantId}/groups`

##### Check a group
To check a specific group by its ID, call the following endpoint using the GET method:
* `/tenants/{tenantId}/groups/{groupId}`

##### Check direct users and groups in a group
To check all direct users and groups within a group, call the following endpoint using the GET method: 
* `/tenants/{tenantId}/groups/{groupId}/members`

##### Get users
To check all users, including users inherited from groups, call the following endpoint using the GET method:
* `/tenants/{tenantId}/groups/{groupId}/members/exploded`

##### Update a member
To update member properties using a JSON patch document,  call the following endpoint using the PATCH method: 
* `/tenants/{tenantId}/groups/{groupId}/members/{memberId}`

##### Update a group
To update group properties using a JSON patch document, call the following endpoint using the PATCH method:
* `/tenants/{tenantId}/groups/{groupId}`

##### Check what groups a group is a part of
To list all the groups a specific group is a member of, call the following endpoint using the GET method: 
* `/tenants/{tenantId}/groups/{groupId}/memberOf`

##### Get applications group has a license for
To check all the applications licensed for the group, call the following endpoint using the GET method:
* `/tenants/{tenantId}/groups/{groupId}/applications`

#### Me
The **Me** interface provides methods to retrieve information about the logged-in user, including their applications, groups, and tenants.

##### Check details for logged-in user
To check the details for the logged-in user, call the following endpoint using the GET method:
* `/me`

##### Check all applications the user has access to
To check all the applications to which the user has access, call the following endpoint using the GET method:
* `/me/applications`

##### Check all applications in the tenant to which the user has access
To check all the applications in the tenant to which the user has access, call the following endpoint using the GET method:
* `/me/tenants/{tenantId}/applications`

##### Check groups to which the logged-in user belongs
To check all the groups to which the logged-in user belongs, call the following endpoint using the GET method:
* `/me/tenants/{tenantId}/groups`

##### Check all the tenants to which the logged-on user belongs
To check all the tenants to which the logged-on user belong, call the following endpoint using the GET method:
* `/me/tenants`

##### Check all tenants to which the logged-on user belongs and has access to a specific application
To check all the tenants the logged-on user is a member of and has access to a specific application, call the following endpoint using the GET method:
* `/me/applications/{applicationId}/tenants`

##### Verify Veracity user policies
To Verify Veracity user policies and return appropriate responses based on policy compliance, call the following endpoint with a POST method:
* `/me/applications/{applicationId}/.policy()`

It returns an empty 202 response if all policies are correct, and 406 with an error response with the URL to send the user to the correct the policy issue.

#### StatusService
To check information about the status of the service, call the following endpoint using the GET method:
* `/health`

You will get:
* A 200 OK response if all dependencies are correct.
* A 424 Failed Dependency response if there are some non-essential dependency failures. 
* A 500 Internal Server response when some essential dependencies are unreachable, or the service is down.

#### Tenants
The **Tenants** interface provides methods to interact with tenants, including retrieving tenant details and managing tenant administrators.

##### Get a tenant by ID
To check a tenant by its ID, call the following endpoint using the GET method:
* `/tenants/{tenantId}`

##### Check tenants linked to your service
To get a list of tenants linked to a specific service, call the following endpoint using the GET method:
* `/tenants`

##### Check admin details for the user by their ID
To check admin details for the user by their ID, call the following endpoint using the GET method:
* `/tenants/{tenantId}/admins/{userId}`

##### Get admins of the tenant
To checl all global and local admins of a tenant, call the following endpoint using the GET method:
* `/tenants/{tenantId}/admins`

#### Users
The **Users** interface provides methods to manage users within a tenant, including retrieving user details, groups, and applications.

##### Checka user by their email
To check a user by their email address, call the following endpoint using the GET method:
* `/tenants/{tenantId}/users/.email({email})`

##### Check user by their ID
To check a user by their ID, call the following endpoint using the GET method:
* `/users/{userId}`

#####  List users in a tenant
To get a list of users in a tenant with support for OData query parameters,  call the following endpoint using the GET method:
* `/tenants/{tenantId}/users`

##### Check user details in a tenant
To check the details of a user in a tenant, call the following endpoint using the GET method:
* `/tenants/{tenantId}/users/{userId}`

##### Check user's groups
To check the groups associated with a user, call the following endpoint using the GET method:
* `/tenants/{tenantId}/users/{userId}/groups`

##### Check user's applications
To check the applications associated with a user,call the following endpoint using the GET method:
* `/tenants/{tenantId}/users/{userId}/applications`

##### Check tenants to which the user belongs
To check the tenants a user is a member of, call the following endpoint using the GET method:
* `/users/{userId}/tenants`

##### Check full user details for a list of user IDs
To check full user details for a list of user IDs, call the following endpoint with a POST method:
* `/tenants/{tenantId}/users`

##### Update user extension properties
To update the extension properties for a user using a JSON patch document, call the following endpoint using the PATCH method:
* `/tenants/{tenantId}/users/{userId}`

## Service Bus

The Service Bus documentation will be made available shortly.

## Use case scenarios

The Veracity Platform API offers comprehensive tools for managing applications, users, groups, and permissions within a multi-tenant environment. See some practical applications below.

### Health and Safety Tracker

The Health and Safety Tracker monitors and manages workplace health and safety conditions. It keeps track of safety compliance, sends notifications and alerts, allows reporting health status and safety incidents, and monitors and manages them.

It uses various endpoints and functionalities provided by the Veracity Platform API. See some key aspects of the implementation below.

#### User Identity

Veracity Identity handles user identities, providing self-service signup, password reset, and other core identity management functions.

#### Multi-Tenant Application Management

The application supports multiple tenants, each representing a different workplace or department. 

To grant users access to the application and set their roles, use Veracity Access Hub. The tenant administrators or the application administrators in the customer organization add users by assigning them direct licenses, which are inherited through groups or added automatically. See the [Veracity Access Hub documentation](https://developer.veracity.com/docs/section/customerservices/accesshub) for more details.

Also, you can use the following endpoints to manage tenants and their associated applications.

##### To check if the user has access to the application

To check if the user has access to the application through one or more tenants, call the following endpoint using the GET method:
* `/me/applications/{applicationId}/tenants`

Depending on the response, the user will see different pages when accessing the application.
* If the response is an empty list, the user will be redirected to the unauthorized page. 
* If the response contains one tenant, the user will be redirected to the application using this tenant
* If the response contains two or more tenants, the user will be redirected to the page where they can choose which tenant they want to work with. 

Note that the tenant ID can be passed in a cookie, URL query parameter or a header value. 

##### To determine the user’s role in the application

You can determine the role of the user by getting their license. To do it, call the following endpoint using the GET method
* `/tenants/{tenantId}/applications/{applicationId}/licenses/{userId}`


All tenant objects contain extension properties that applications can use to store application specific information. In this case, look for these two
properties:
* `demo_caseTypeHandler` - It contains a space-separated list of case type names of which the user is a handler.
* `demo_caseRegionHandler` - It contains the region identifier for which the user is handling cases.

If a user has both these properties, it means that they are a case handler. Otherwise, they are a regular user and can only report cases.

##### To determine if the user can assign other case handlers

To find the application administrator within the tenant, call the following endpoint using the GET method:
* `/tenants/{tenantId}/applications/{applicationId}/administrators`

If the logged-in user is on the list of administrators, the administration menu will be displayed.

##### To assign a user as a case handler for ‘physical security’ in the EMEA region

To assign a user as a case handler for ‘physical security’ in the EMEA region, call the following endpoint using the PATCH method.
* `/tenants/{tenantId}/applications/{applicationId}/licenses/{userId}`


Also, use the following request body.
```json
[
    {
        "value": {
            "Name": "demo_caseTypeHandler",
            "Value": "physical_security"
        },
        "path": "/properties/-",
        "op": "add"
    },
    {
        "value": {
            "Name": "demo_caseRegionHandler",
            "Value": "EMEA"
        },
        "path": "/properties/-",
        "op": "add"
    }
]
```

##### To assign an application admin role to a user

You can assign an application administrator role to a user by calling the following endpoint using the POST method.
* `/tenants/{tenantId}/applications/{applicationId}/administrators/{userId}`

##### To remove an application admin role from a user

You can remove an application administrator role from a user by calling the following endpoint using the DELETE method.
* `/tenants/{tenantId}/applications/{applicationId}/administrators/{userId}`

##### To find users to assign them admin or case handler roles

To search for users in the tenant, call the following endpoint using the GET method:
* `/tenants/{tenantId}/users`

You can also search for users who are already users of the application by calling the following endpoint using the GET method:
* `/tenants/{tenantId}/applications/{applicationId}/users`

Both these endpoints support odata queries.
Example odata query: 
* `[GET tenants/be0c84cb-7a4a-4114-aa17-9c0224b084cf/users?$filter=name eq 'Normann, Ola'&$top=1&$skip=0]`


Note that in this example user groups can also be made case handlers. However, you can assign administrator roles only to single users.

### Hot Seating Office Manager Application

The Hot Seating Office Manager application optimizes seating arrangements in a dynamic office environment. It helps track available seats, locate colleagues, and manage floor plans, ensuring an efficient and collaborative workspace.

It uses various endpoints and functionalities provided by the Veracity Platform API. See some key aspects of the implementation below.

#### User Identity

Veracity Identity handles user identities, providing self-service signup, password reset, and other core identity management functions.

#### Multi-Tenant Application Management

The application supports multiple tenants, each representing a different workplace or department. 

To grant users access to the application and set their roles, use Veracity Access Hub. The tenant administrators or the application administrators in the customer organization add users by assigning them direct licenses, which are inherited through groups or added automatically. See the [Veracity Access Hub documentation](https://developer.veracity.com/docs/section/customerservices/accesshub) for more details.

Also, you can use the following endpoints to manage tenants and their associated applications.

##### To check if the user has access to the application

To check if the user has access to the application through one or more tenants, call the following endpoint using the GET method:
* `/me/applications/{applicationId}/tenants`


Depending on the response, the user will see different pages when accessing the application.
* If the response is an empty list, the user will be redirected to the unauthorized page. 
* If the response contains one tenant, the user will be redirected to the application using this tenant
* If the response contains two or more tenants, the user will be redirected to the page where they can choose which tenant they want to work with. 

Note that the tenant ID can be passed in a cookie, URL query parameter or a header value. 

##### To determine user roles and permissions
To get the user license, call the following endpoint using the GET method:
* `/tenants/{tenantId}/applications/{applicationId}/licenses/{userId}`

The license object has an AccessLevel that is used to determine whether the user is a regular user who can book a seat for the day or if they are an admin can upload new floor plans and manage existing ones, ensuring they are always up to date.

#### Application responsibilities
The application stores all the floor plans and seat bookings in its own database while users and permissions are handled by Veracity. This allows the product team to focus on the distinguishing features of the application while some of the security aspects are outsourced.

The maps are stored in a blob storage while the seating arrangements and coordinates within the floor map is stored in a SQL database along with the bookings.

### Shopping Mall Management Application

The application is designed to manage employees and health and safety managers for all shops in a mall. It allows store managers to oversee their staff and ensures efficient crisis management by the mall administration. The application integrates with POS systems to provide real-time data on employee presence. Its core functionalities include:
* Employee and Manager Tracking: Real-time record-keeping of all employees and health and safety managers.
* Check-in and Check-out System: Easy tracking of attendance and work shifts.
* Managerial Control for Store Managers: Autonomy for store managers to manage their staff and ensure compliance.
* POS System Integration: Efficient tracking of employee presence.
* Health and Safety Compliance: Monitoring and reporting of health and safety compliance.
* Notifications and Alerts: Real-time push notifications for safety incidents using Firebase.


#### Multi-Tenant Application Management

The application supports multiple tenants, each representing a different workplace or department. 

To grant users access to the application and set their roles, use Veracity Access Hub. The tenant administrators or the application administrators in the customer organization add users by assigning them direct licenses, which are inherited through groups or added automatically. See the [Veracity Access Hub documentation](https://developer.veracity.com/docs/section/customerservices/accesshub) for more details.

Also, you can use the following endpoints to manage tenants and their associated applications.

##### To check if the user has access to the application

To check if the user has access to the application through one or more tenants, call the following endpoint using the GET method:
* `/me/applications/{applicationId}/tenants`


Depending on the response, the user will see different pages when accessing the application.
* If the response is an empty list, the user will be redirected to the unauthorized page. 
* If the response contains one tenant, the user will be redirected to the application using this tenant
* If the response contains two or more tenants, the user will be redirected to the page where they can choose which tenant they want to work with. 

Note that the tenant ID can be passed in a cookie, URL query parameter or a header value. 

##### To determine user roles and permissions

To get the user license, call the following endpoint using the GET method:
* `/tenants/{tenantId}/applications/{applicationId}/licenses/{userId}`


The license object has an AccessLevel that is used to that determine whether the user is a regular user who can check in and out or an admin who can manage employees and health and safety compliance.


Store managers are added to the system and granted user admin and application admin roles within the Veractiy Tenant Management system through the API. The storeId is added to the extension properties of the license.


Then, the store manager can add and remove users from their own store. When adding a new user to the store, the storeId is saved in the extension properties. The app also saves a flag indicating if the user is a health and safety responsible for the store.

The application stores info on the license for the mall administration, marking this person as the store’s primary contact. To check this info, call the following endpoint using the PATCH method:
* `tenants/{tenantId}/applications/{applicationId}/licenses/{entityId}`
