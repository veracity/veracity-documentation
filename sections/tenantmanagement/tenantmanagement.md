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

### Veracity management modes

Customers use Veracity Access Hub to manage access to their applications and decide on how much control they delegate to VTM. VTM offers three types of access control:

* **Veracity-managed** - All user management is done in Veracity Access Hub, so there is no need to build your user management front-end. [See our Veracity managed example](#hot-seating-office-manager).
* **Hybrid** - This is for services with a well-defined lease privilege – meaning you can still manage most of your user access needs in Veracity Access Hub, but can also extend this to individual services for more granular control. [See our hybrid example](#health-and-safety-tracker).
* **Service-managed** - This one has no defined lease privilege – it is built on your own authorization policies and front-end interfaces, relying on Veracity Access Management’s robust back-end. This allows you to easily manage users, sharing other experiences between multiple services on the Veracity platform for a superior user experience. [See our service managed example](#mall-management-application).

To see sample scenarios for each kind of access control, go to [Sample use case scenarios](#use-case-scenarios).

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

VTM operates as an eventually consistent system. This means there might be a delay before the data you write becomes visible when you attempt to read it.

When a write endpoint returns a 202 Accepted response V4, it does not mean a successful data change. Even though the endpoint returns the new object, it does not mean that it has been persisted yet - the 202 Accepted response simply informs that the solution has accepted the change. Then, it will process the change and update the data in the background.

Once the change has been made, then, on the service bus, the solution will publish an event informing whether the operation was successful or not.

How does this affect your application?

Eventual consistency is only important for applications that are calling endpoints that change data. If your application does these write operations, it needs to integrate with the Veracity Service Bus and listen for these events to get the result of the call.

To get these messages, in Domain Events, configure that you want messages to the Tenant topic and use this connection to the Service Bus.


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

## Domain Events
For information about Veracity Tenant Management Domain Events, [see this document](https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/vtm/Veracity%20Tenant%20Management%20Events.pdf).

## Use case scenarios

We have prepared three sample use case scenarios of fictional applications created by a fictional SafeTech Solutions company to demonstrate what Veracity has to offer. The scenarios correspond to the [three Veracity managemenet modes](#veracity-management-modes).


### Why choose Veracity?

You have a vision for a service that can cater to the needs of multiple companies, teams, or projects - but the challenges of securely managing users, permissions, and access control can quickly become a roadblock, distracting you from your core innovation.

Veracity empowers you to streamline the development of secure, multi-tenant services. By providing a comprehensive set of tools and APIs, Veracity handles the complex backend work, allowing you to focus on crafting the unique features that will delight your customers.

With Veracity, you can:
* Easily create isolated, secure tenants for each of your customers.
* Have granular control over user licenses, roles, and permissions through a developer-friendly API.
* Leverage efficient data management features like JSON Patch and local data caching for optimal performance.
* Build resilient, responsive services with real-time domain events to keep your service in sync.
* Access comprehensive documentation, sample code, and a supportive developer community to accelerate your progress.

Veracity gives you the power to simplify development and deliver an unparalleled experience. See the examples below to learn more. 

### Download use cases
You can access our use cases in a PDF Format.
* [Hot Seating Office Manager](https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/vtm/Hot%20Seating%20Office%20Manager.pdf) (Veracity-managed)
* [Health And Safety Tracker](https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/vtm/Health%20And%20Safety%20Tracker.pdf) (hybrid)
* [Mall Management Application](https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/vtm/Mall%20Management%20Application.pdf) (service-managed)

### Listen to our podcasts
For those who prefer to listen, we have prepared podcasts discussing the applications of the fictional SafeTech Solutions company:
* [Health and Safety Tracker app](https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/vtm/VTMCaseStudy.wav)
* [Comparison of SafeTech Solutions apps](https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/vtm/ComparingSafeTechApps.wav)

### Hot Seating Office Manager (Veracity-managed)

SafeTech Solutions specializes in developing innovative software solutions for workplace management and efficiency. Their latest product, the Hot Seating Office Manager, leverages cutting-edge technology to ensure companies can manage seating arrangements, facilitate easy colleague location, and maintain up-to-date floor plans. SafeTech Solutions is committed to creating user-friendly and effective tools that enhance workplace productivity and improve overall employee collaboration.

**You can also view the Hot Seating Office Manager use case in [a PDF format ](https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/vtm/Hot%20Seating%20Office%20Manager.pdf)**.

#### Overview
The Hot Seating Office Manager is designed to manage seating arrangements in a dynamic office environment, integrating functionalities such as tracking available seats, locating colleagues, and managing floor plans. The service’s primary goal is to ensure an efficient and collaborative working environment.

Core Features and Functionalities
* Seat availability monitoring - Allows employees to check the availability of seats in real-time, ensuring they can find a workspace easily. 
* Colleague location - Employees can locate their colleagues within the office space, facilitating easy collaboration and interaction. 
* Floor plan management - Admins can upload and manage detailed floor plans, which are updated in real time to reflect current seating arrangements. 
* Notifications and alerts - Employees receive timely notifications and alerts regarding any updates or changes in seating arrangements.

#### Implementation Using Veracity Platform API
Running in Veracity-managed mode, The Hot Seating Office Manager uses the powerful Veracity Platform API.

##### User management 
Veracity Identity handles user identities, providing self-service signup, password reset, and other core identity management functions. As a redult, little to no admin is required once it is set up. 

##### 'Multi-Tenant' Service Management 
Hot Seat Office Manager supports multiple tenants – this means that multiple offices and departments can be managed centrally through the Veracity Access Hub. It is used to grant users access and set their roles. By leveraging the Access Hub, the product team does not need to spend time and effort on the user administration interface. See the [Veracity Access Hub documentation](https://developer.veracity.com/docs/section/customerservices/accesshub) for more details.

To manage tenants and their associated services, you can use the following endpoints.

##### User Session Establishment

Upon establishing a user session, check if the user has access to the service through one or more tenants. To do it, call the following endpoint using the GET method.
* `/me/applications/{applicationId}/tenants`

The user will see different pages when accessing the service depending on the response.
* If the response is an empty list, the user will be redirected to the unauthorized page. 
* If the response contains one tenant, the user will be redirected to the service using this tenant.
* If the response contains two or more tenants, the user will be redirected to the page where they can choose which tenant they want to work with. 

Note that the tenant ID can be passed in a cookie, URL query parameter or header value. 

##### Determine user roles and permissions
* **Get user license** - To get the user license, call the following endpoint using the GET method.
`/tenants/{tenantId}/applications/{applicationId}/licenses/{userId}`


The license object has an AccessLevel that is used to determine whether the user is a regular user who can book a seat for the day or if they are an admin who can upload new floor plans and manage existing ones, ensuring they are always up to date.

* **Upload and Manage Floor Plans** - Admins can upload new floor plans and manage existing ones, ensuring they are always up to date. 

#### Service responsibilities
The service stores all the floor plans and seat bookings in its own database, while Veracity handles users and permissions. This allows the product team to focus on the distinguishing features of the application while some of the security aspects are outsourced.

The maps are stored in a blob storage, while the seating arrangements and coordinates within the floor map are stored in an SQL database along with the bookings.

#### Conclusion
The Hot Seating Office Manager service exemplifies the practical use of the Veracity Platform API, creating a robust and efficient system for managing dynamic office environments. This fictional application demonstrates the versatility and power of the Veracity Platform API in addressing complex, real-world problems. 

Veracity cares about the privacy of the end-users. The service does not store user information other than a reference to the users so they can be shown on the map and searched for. 

### Health and Safety Tracker (hybrid)
SafeTech Solutions specializes in developing innovative software solutions for workplace safety and health management. 

Their flagship product, the Health and Safety Tracker, leverages cutting-edge technology to ensure that companies can
* Monitor employee health statuses.
* Manage safety compliance.
* Respond quickly to health and safety incidents. 

SafeTech Solutions is committed to creating user-friendly and effective tools that enhance workplace safety and improve employee well-being. 

How is the Veracity Platform leveraged in their products and services?

The Veracity Platform API, as described in the provided documentation, offers a comprehensive set of tools for managing services, users, groups, and permissions within a 'multi-tenant' environment. 

One practical service of this API is in the development and deployment of a Health and Safety Tracker for workplace service, which can significantly enhance the safety and well-being of employees by leveraging the robust capabilities of the Veracity Platform API. 


**You can also view the Health and Safety Tracker use case in [a PDF format](https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/vtm/Health%20And%20Safety%20Tracker.pdf) or listen about it [in our podcast](https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/vtm/VTMCaseStudy.wav)**.

#### Overview
The Health and Safety Tracker is designed to monitor and manage the health and safety conditions within a workplace.

Core features and functionalities 
* Employee health status monitoring - Service employees can report their health status, which management can monitor in real-time. 
* Safety compliance tracking - The service tracks safety compliance across different departments, ensuring that all safety protocols are being followed. 
* Incident reporting and management - Employees can report safety incidents, and the service facilitates the management and resolution of these incidents. 
* Notifications and alerts - Service notifications and alerts are sent to employees and management regarding any health and safety updates or incidents. 

#### Implementation Using Veracity Platform API 
The implementation of the Health and Safety Tracker leverages various endpoints and functionalities provided by the Veracity Platform. See some key aspects of the implementation below.

##### User Identity

Veracity Identity handles user identities, providing self-service signup, password reset, and other core identity management functions.

##### Multi-Tenant Service Management

The service supports multiple tenants, each representing a different workplace or department. 

To grant users access to the service and set their roles, use Veracity Access Hub. The tenant administrators or the service administrators in the customer organization add users by assigning them direct licenses, which are inherited through groups or added automatically. See the [Veracity Access Hub documentation](https://developer.veracity.com/docs/section/customerservices/accesshub) for more details.

You can use the following endpoints to manage tenants and their associated services.

##### Upon establishing a user session

To check if the user has access to the service through one or more tenants, call the following endpoint using the GET method.
* `/me/applications/{applicationId}/tenants`

The user will see different pages when accessing the service depending on the response.
* If the response is an empty list, the user will be redirected to the unauthorized page. 
* If the response contains one tenant, the user will be redirected to the service using this tenant.
* If the response contains two or more tenants, the user will be redirected to the page where they can choose which tenant they want to work with. 

Note that the tenant ID can be passed in a cookie, URL query parameter or header value. 

##### To determine the user’s role in the service instance

You can determine the user's role by getting the user license object. To do it, call the following endpoint using the GET method.
* `/tenants/{tenantId}/applications/{applicationId}/licenses/{userId}`

All tenant objects contain extension properties that servicea can use to store service-specific information. In this case, look for these two
properties:
* `demo_caseTypeHandler` - It contains a space-separated list of case type names of which the user is a handler.
* `demo_caseRegionHandler` - It contains the region identifier for which the user is handling cases.

If a user has both these properties, it means that they are a case handler. Otherwise, they are a regular user and can only report cases.

##### To determine if the user can assign other case handlers

To find the service administrator within the tenant, call the following endpoint using the GET method.
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

#### Conclusion
The Health and Safety Tracker application exemplifies the practical use of the Veracity Platform API in creating a robust and efficient system for managing workplace safety. By leveraging the multi-tenant capabilities, user and group management, and detailed permission settings provided by the API, the application ensures a safe and compliant working environment. This fictional application demonstrates the versatility and power of the Veracity Platform API in addressing complex, real-world problems.

In this example, we care about the privacy of the end-users, and the application never stores any user information unless the user reports a case. In that case, we need to store enough information to comply with regulations. The same goes for the ones handling cases.

### Mall Management Application (service-managed)
SafeTech Solutions, renowned for developing innovative software solutions, has introduced a multi-tenant shopping mall management service. This service is designed to keep track of all employees and health and safety managers for all shops renting space in the mall. 

**You can also view the Mall Management Application use case in [a PDF format](https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/vtm/Mall%20Management%20Application.pdf)**.

#### Overview
It allows each store manager to manage their own employees (including health and safety managers), while enabling all employees to check in and out of work. The service ensures efficient crisis management by the mall administration and integrates seamlessly with EPOS systems to provide real-time data on employee presence in a user-friendly manner. Each mall gets its own virtual ‘tenant’, and store managers can manage their store within the mall’s tenant. 

Core features and functionalities:
* Employee and manager tracking - Real-time record of all employees and health and safety managers, enhancing efficiency and safety.
* Check-in and check-out system - Tracks attendance and manages work shifts effectively, with real-time updates. 
* Managerial control for store managers - Store managers can update employee details and ensure health and safety compliance, maintaining coordination with mall administration.
* EPOS system integration - Efficient tracking of employee presence, reducing administrative overhead and enhancing operational efficiency.
* Health and safety compliance - Monitors compliance, reports incidents, and ensures safety protocols are followed, with prompt notifications and alerts.
* Notifications and alerts - FireBase is used for real-time push notifications for employees, ensuring smooth and efficient crisis response

#### Implementation Using Veracity Platform API 

See the implementation below.

##### User Identity
Veracity Identity handles user identities, providing self-service signup, password reset, and other core identity management functions.

##### Multi-Tenant Service Management

The service supports multiple tenants, representing different stores within the mall.

Use the following endpoints to manage tenants and their associated services.

##### Upon establishing a user session

To check if the user has access to the service through one or more tenants, call the following endpoint using the GET method:
* `/me/applications/{applicationId}/tenants`

The user will see different pages when accessing the service depending on the response.
* If the response is an empty list, the user will be redirected to the unauthorized page. 
* If the response contains one tenant, the user will be redirected to the service using this tenant.
* If the response contains two or more tenants, the user will be redirected to the page where they can choose which tenant they want to work with. 

Note that the tenant ID can be passed in a cookie, URL query parameter or header value. 

##### To determine user roles and permissions

To get the user license, call the following endpoint using the GET method:
* `/tenants/{tenantId}/applications/{applicationId}/licenses/{userId}`

The license object has an AccessLevel that is used to determine whether the user is a regular user who can check in and out or an admin who can manage employees and health and safety compliance.

Store managers are added to the system and granted user admin and application admin roles within the Veractiy Tenant Management system through the API. The storeId is added to the extension properties of the license.

Then, the store manager can add and remove users from their own store. When adding a new user to the store, the storeId is saved in the extension properties. The app also saves a flag indicating if the user is a health and safety responsible for the store.

The MallManager application stores info on the license for the mall administration, marking this person as the store’s primary contact. To check this info, call the following endpoint using the PATCH method:
* `tenants/{tenantId}/applications/{applicationId}/licenses/{entityId}`

The service does not need to save any personal information about the users, only a reference that can be used to resolve this when needed. 

#### Conclusion
The shopping mall management service by SafeTech Solutions is a robust and efficient system designed to enhance workplace management and safety. By leveraging the multi-tenant capabilities, user and group management, and detailed permission settings provided by the Veracity Platform API, the service ensures a well-coordinated and safe working environment. 

This fictional service demonstrates the versatility and power of the Veracity Platform API in addressing complex, real-world problems, and showcases SafeTech Solutions' commitment to creating user-friendly and effective tools that improve overall security and collaboration within the workplace.