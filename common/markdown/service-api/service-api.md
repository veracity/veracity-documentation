---
Title: Service API
Author: "Brede Børhaug"
---

# Overview 

The Service API provides a consistent interface for accessing data about the user and the Veracity platform in general. At its heart it is a REST service built up of "view-points" where you can read, write and update information. Authentication is handled through Azure B2C OAuth 2.

## Authentication

Authentication is performed through OAuth2 bearer tokens.

## View-points

The API defines three primary view-points from which you can access more detailed information. The base url for requests is:

***[TODO NOT VERIFIED FINAL URLS]***
```url
https://myapiv3.dnvgl.com/[view-point]

e.g.:
https://myapiv3.dnvgl.com/my/profile
```

These are:

|View-point|Path|Description|
|:---------|:-------|:----------|
|Discover|`/discover`|Information about different masterdata and resources with in myDNVGL. The main categories are: Services, Users and companies.|
|My|`/my`|Provides information about the currently logged in user.|
|This|`/this`|Provides information from the service or applications point of view, its capabilities and metadata.|

The view-points themselves do not provide information directly, instead you interact with them through defined **actions**. An action is just a string that you append to the end of the view-point path in order to perform a request. The actions follow normal usage of HTTP verbs with some minor exceptions.

### Responses

Each response provides all or most of these headers:

|Header|Type|Description|
|:-----|:--:|:----------|
|x-supportcode|GUID|Provides a unified way of correlating log entries accross all system components.|
|x-serviceversion|string|The api build number.|
|x-timer|int|The time spent on the server producing the response in milliseconds. [TODO is this correct?]|
|x-region|string|The Azure service region serving the request.|
|x-principal|-|The user the request was executed on behalf of.|
|x-view-point|string|The name of the current view-point.|
|x-actor|GUID|The user id of the actor/service account. [TODO describe better]|

The response status code describes whether the request succeeded or not. Currently the following status codes may be returned

|HTTP Status|Name|Description|
|:----------|:---|:----------|
|200|OK|Your request was processed correctly. View content for response.|
|204|No Content|Your request was processed correctly and no content was returned.|
|300|Ambiguous|Your request could point to multiple resources. You should augment it with additional identifying information.|
|400|Bad Request|The view-point/action exists, but the way you formatted the request was incorrect. Check `http verb`, `headers` or `body`.|
|403|Forbidden|The requester has insufficient permissions to perform the action or authorization information is missing from the request. Check that you provide a valid OAuth2 `Authorization` header.|
|404|Not Found|The requested resource/view-point/action was not found or is not known.|
|500|Internal Server Error|Something went wrong on the server when processing your request. Try to include the `x-supportcode` header content if you wish to submit a support request.|
|501|Not Implemented|The view-point or action is not currently implemented, but may be in the future.|

#### Response format

The API supports formatting the response body according to the mime type provided in your requests `Accept` header. Currently the following mime types are supported:

- `application/json`
- `text/json`
- `application/xml`
- `text/xml`

### Discover

The primary purpose of the **Discover** view-point is to provide information about your "surroundings". Using it you can get information about companies, services and users in the system. [TODO correct?]

#### Actions

The following actions are supported on the `/discover` view-point. Parameters in urls are indicated by `{}` and should be replaced when using the action.

|Action|Method|Description|
|:-----|:----:|:----------|
|`/discover/companies/{id}`|`GET`|Get details about a specific company.|
|`/discover/companies/{id}/users`|`GET`|Get users affiliated with a specific company.|
|`/discover/services/{id}`|`GET`|Get details about a specific service.|
|`/discover/services/{id}/users`|`GET`|Get users subscribed with a specific service.|
|`/discover/users/email?email={email}`|`GET`|Get information about all users associated with a specific email address.|
|`/discover/users/{id}`|`GET`|Get the full profile for a specific user.|
|`/discover/users`|`POST`|Get full profile information for multiple users.|
|`/discover/users/{id}/companies`|`GET`|Get companies the user is affiliated to.|
|`/discover/users/{id}/services`|`GET`|Get services the user is subscribed to.|
|`/discover/users/{userid}/services/{serviceid}`|`GET`|Get the role a specific user has with regard to a specific service [TODO correct?]|

#### `/discover/companies/{id}`

Response format:

```
CompanyInfo {
  name (string, optional),
  url (string, optional),
  usersUrl (string, optional),
  addressLines (Array[string], optional),
  id (string, optional),
  city (string, optional),
  country (string, optional),
  countryCode (string, optional),
  zipCode (string, optional),
  #employee (integer, optional),
  domains (string, optional),
  email (string, optional),
  #requests (integer, optional)
}
```

#### `/discover/companies/{id}/users`

This action returns a paged result. You must provide a page number as well as a page size as query parameters to this request.

E.g.:
```url
/discover/companies/{id}/users?page=1&pageSize=15
```

Response format:

```
[
  {
    identity (string, optional, read only): The relative path to the resource details ,
    email (string, optional),
    name (string, optional),
    id (string, optional)
  },
  ...
]
```

#### `/discover/services/{id}`

Response format:

```
ServiceInfo {
  name (string, optional),
  shortDescription (string, optional),
  description (string, optional),
  apiAudience (string, optional),
  category (string, optional),
  public (boolean, optional),
  id (string, optional),
  inherited (boolean, optional),
  selfSubscribe (boolean, optional),
  serviceOwner (string, optional),
  termsOfUse (string, optional),
  lastUpdated (string, optional),
  parentUrl (string, optional, read only),
  parentId (string, optional),
  childrenUrl (string, optional, read only),
  servicerUrl (string, optional)
}
```

#### `/discover/services/{id}/users`

This action returns a paged result. You must provide a page number as well as a page size as query parameters to this request.

E.g.:
```url
/discover/services/{id}/users?page=1&pageSize=15
```

Response format:

```
[
  {
    identity (string, optional, read only): The relative path to the resource details ,
    email (string, optional),
    name (string, optional),
    id (string, optional)
  },
  ...
]
```

#### `/discover/users/email?email={email}`

Response format:

```
[
  {
    identity (string, optional, read only): The relative path to the resource details ,
    email (string, optional),
    name (string, optional),
    id (string, optional)
  },
  ...
]
```

#### `/discover/users/{id}`

Response format:

```
UserInfo {
  name (string, optional): Contains the users formatted name: {lastName}, {firstName}. the id token contains the discrete values in the givenName and surname claims. ,
  email (string, optional): The users registered email address. if verifiedEmail is true this can be used to contact the user. ,
  id (string, optional),
  company (CompanyReference, optional): Contains the default company affiliation if any. ,
  verifiedEmail (boolean, optional): true if email is verified by the user; otherwise, false. ,
  language (string, optional): Contains the perfered language for the user. If your service support multi-language use this. ,
  identity (string, optional): The relative path to the resource details ,
  servicesUrl (string, optional, read only): Gets the relative url to the users service lits ,
  companiesUrl (string, optional, read only): Gets the relative url to the users companies lits ,
  firstName (string, optional),
  lastName (string, optional)
}
CompanyReference {
  identity (string, optional, read only): The relative path to the resource details ,
  name (string, optional),
  id (string, optional),
  description (string, optional)
}
```

#### `/discover/users`

The body of this request should be a list of user IDs. Example:

```json
[
  "eacf14df-5f5c-482c-9a12-d1444b69ae82",
  "325d5051-b68e-486b-bbf1-25416cb5035d"
]
```

The following request body types are supported:

- `application/json`
- `text/json`
- `application/xml`
- `text/xml`
- `application/x-www-form-urlencoded`

Remember to set the `Content-Type` header of your request to `application/json`.

Response format:

```
[
  {
    name (string, optional): Contains the users formatted name: {lastName}, {firstName}. the id token contains the discrete values in the givenName and surname claims. ,
    email (string, optional): The users registered email address. if verifiedEmail is true this can be used to contact the user. ,
    id (string, optional),
    company (CompanyReference, optional): Contains the default company affiliation if any. ,
    verifiedEmail (boolean, optional): true if email is verified by the user; otherwise, false. ,
    language (string, optional): Contains the perfered language for the user. If your service support multi-language use this. ,
    identity (string, optional): The relative path to the resource details ,
    servicesUrl (string, optional, read only): Gets the relative url to the users service lits ,
    companiesUrl (string, optional, read only): Gets the relative url to the users companies lits ,
    firstName (string, optional),
    lastName (string, optional)
  },
  ...
]

CompanyReference {
  identity (string, optional, read only): The relative path to the resource details ,
  name (string, optional),
  id (string, optional),
  description (string, optional)
}
```

#### `/discover/users/{id}/companies`

Response format:

```
[
  {
    identity (string, optional, read only): The relative path to the resource details ,
    name (string, optional),
    id (string, optional),
    description (string, optional)
  },
  ...
]
```

#### `/discover/users/{id}/services`

Response format:

```
[
  {
    identity (string, optional, read only): The relative path to the resource details ,
    name (string, optional),
    id (string, optional),
    description (string, optional)
  },
  ...
]
```

#### `/discover/users/{userid}/services/{serviceid}`

Response format:

```
SubscriptionDetails {
  service (ServiceReference, optional),
  user (UserReference, optional),
  role (RoleReference, optional)
}
ServiceReference {
  identity (string, optional, read only): The relative path to the resource details ,
  name (string, optional),
  id (string, optional),
  description (string, optional)
}
UserReference {
  identity (string, optional, read only): The relative path to the resource details ,
  email (string, optional),
  name (string, optional),
  id (string, optional)
}
RoleReference {
  identity (string, optional, read only): The relative path to the resource details ,
  type (string, optional),
  name (string, optional),
  id (string, optional)
}
```

### My

The `/my` view-point provides information from the point of view of the currently logged in user.

#### Actions

The following actions are supported on the `/my` view-point. Parameters in urls are indicated by `{}` and should be replaced when using the action. 

|Action|Method|Description|
|:-----|:----:|:----------|
|`/my/profile`|`GET`|Get the profile of the currently logged in user.|
|`/my/messages/count`|`GET`|Get the number of unread messages of the currently logged in user.|
|`/my/messages`|`GET`|Get all messages for the currently logged in user.|
|`/my/companies`|`GET`|Get companies the currently logged in user is affiliated with.|
|`/my/policies/{serviceId}/validate()`|`GET`|Validates all myDNVGL policies for a specific service and returns a list of the policies that need validation. [TODO |
|`/my/policies/validate()`|`GET`|Validates all myDNVGL policies and returns a list of the policies that need validation.|
|`/my/services`|`GET`|Get all services the user is subscribed to.|

#### `/my/profile`

Response format:

```
MyUserInfo {
  profilePageUrl (string, optional, read only),
  messagesUrl (string, optional, read only),
  identity (string, optional),
  servicesUrl (string, optional, read only): Gets the relative url to the users service lits ,
  companiesUrl (string, optional, read only): Gets the relative url to the users companies lits ,
  name (string, optional): Contains the users formatted name: {lastName}, {firstName}. the id token contains the discrete values in the givenName and surname claims. ,
  email (string, optional): The users registered email address. if verifiedEmail is true this can be used to contact the user. ,
  id (string, optional),
  company (CompanyReference, optional): Contains the default company affiliation if any. ,
  verifiedEmail (boolean, optional): true if email is verified by the user; otherwise, false. ,
  language (string, optional): Contains the perfered language for the user. If your service support multi-language use this. ,
  firstName (string, optional),
  lastName (string, optional)
}
CompanyReference {
  identity (string, optional, read only): The relative path to the resource details ,
  name (string, optional),
  id (string, optional),
  description (string, optional)
}
```

#### `/my/messages/count`

Response format:

```
Int32
```

#### `/my/messages`

Response format:

```
[
  {
    identity (string, optional, read only): The relative path to the resource details ,
    name (string, optional),
    id (string, optional),
    description (string, optional)
  }
]
```

#### `/my/companies`

Response format:

```
[
  {
    identity (string, optional, read only): The relative path to the resource details ,
    name (string, optional),
    id (string, optional),
    description (string, optional)
  }
]
```

#### `/my/policies/{serviceId}/validate()`

Response format:

[TODO missing response format information in (https://myapiv3test.dnvgl.com/swagger/ui/index#!/My/My_MyServices)]

#### `/my/policies/validate()`

Response format:

[TODO missing response format information in (https://myapiv3test.dnvgl.com/swagger/ui/index#!/My/My_MyServices)]

#### `/my/services`

Response format:

```
[
  {
    serviceUrl (string, optional): the location of the application. ,
    identity (string, optional, read only): The relative path to the resource details ,
    name (string, optional),
    id (string, optional),
    description (string, optional)
  }
]
```

### This

`/this` is the service/applications point of view and provides information from the context of a service or application. Authenticate using a service account before using these actions.

|Action|Method|Description|
|:-----|:----:|:----------|
|`/this/services`|`GET`|Get all services the service principal has access to.|
|`/this/subscribers`|`GET`|Get all users currently subscribed to this service.|
|`/this/services/{serviceId}/subscribers`|`GET`|Get all users currently subscribed to a specific service the current service account is associated with.|
|`/this/subscribers/{userId}`|`PUT`, `DELETE`|Add or remove service subscriptions for a specifc user.|
|`/this/services/{serviceId}/subscribers/{userId}`|`PUT`, `DELETE`|Add or remove service subscriptions for a specifc user.|
|`/this/user`|`POST`|Create a user in myDNVGL|
|`/this/users`|`POST`|Create multiple users in myDNVGL|

#### `/this/services`

This action returns a paged result. You must provide a page number as well as a page size as query parameters to this request.

E.g.:
```url
/this/services?page=1&pageSize=15
```

Response format:

```
[
  {
    identity (string, optional, read only): The relative path to the resource details ,
    name (string, optional),
    id (string, optional),
    description (string, optional)
  }
]
```

#### `/this/subscribers`

**warning**: This action may return `300 Ambiguous` if the service account you are authenticated with is linked to multiple services.

This action returns a paged result. You must provide a page number as well as a page size as query parameters to this request.

E.g.:
```url
/this/subscribers?page=1&pageSize=15
```

Response format:

```
[
  {
    identity (string, optional, read only): The relative path to the resource details ,
    email (string, optional),
    name (string, optional),
    id (string, optional)
  }
]
```

#### `/this/services/{serviceId}/subscribers`

This action returns a paged result. You must provide a page number as well as a page size as query parameters to this request.

E.g.:
```url
/this/services/{serviceId}/subscribers?page=1&pageSize=15
```

Response format:

```
[
  {
    identity (string, optional, read only): The relative path to the resource details ,
    email (string, optional),
    name (string, optional),
    id (string, optional)
  }
]
```

#### `/this/subscribers/{userId}`

**warning**: This action may return `300 Ambiguous` if the service account you are authenticated with is linked to multiple services.

Adds or removes subscribers to the service. Add by using the HTTP verb `PUT` and remove by using `DELETE`.

The `PUT` request must provide a body of the following format:

```
SubscriptionOptions {
  role (string, optional)
}
```

The following request body types are supported:

- `application/json`
- `text/json`
- `application/xml`
- `text/xml`
- `application/x-www-form-urlencoded`

#### `/this/services/{serviceId}/subscribers/{userId}`

Adds or removes subscribers to the service. Add by using the HTTP verb `PUT` and remove by using `DELETE`.

The `PUT` request must provide a body of the following format:

```
SubscriptionOptions {
  role (string, optional)
}
```

The following request body types are supported:

- `application/json`
- `text/json`
- `application/xml`
- `text/xml`
- `application/x-www-form-urlencoded`

#### `/this/user`

Request format:
```
UserRegistration {
  firstName (string, optional),
  lastName (string, optional),
  email (string, optional),
  options (RegistrationOptions, optional): Specify additional creation controll options, this is not mandatory
}

RegistrationOptions {
  sendMail (boolean, optional): Set this to false to take responsibillity of sending the registration email to the user. ,
  createSubscription (boolean, optional): Make the service create a default subscription for the newly created user ,
  serviceId (string, optional): The service id to create subscription for ,
  role (string, optional): Specify the accessLevel/role the user should have with the new subscription. Optional
}
```

The following request body types are supported:

- `application/json`
- `text/json`
- `application/xml`
- `text/xml`
- `application/x-www-form-urlencoded`

#### `/this/users`

Request format:
```
[
  UserRegistration {
    firstName (string, optional),
    lastName (string, optional),
    email (string, optional),
    options (RegistrationOptions, optional): Specify additional creation controll options, this is not mandatory
  }
]

RegistrationOptions {
  sendMail (boolean, optional): Set this to false to take responsibillity of sending the registration email to the user. ,
  createSubscription (boolean, optional): Make the service create a default subscription for the newly created user ,
  serviceId (string, optional): The service id to create subscription for ,
  role (string, optional): Specify the accessLevel/role the user should have with the new subscription. Optional
}
```

The following request body types are supported:

- `application/json`
- `text/json`
- `application/xml`
- `text/xml`
- `application/x-www-form-urlencoded`

## GitHub  
Follow our open projects related to Veracity Services API on https://github.com/veracity

## Stack Overflow
Stack Overflow is the largest, most trusted online community for developers to learn, share their programming knowledge. The Veracity developer team monitor Stack Overflow forumposts that include the tag Veracity Platform.

[Visit Stack Overflow](https://stackoverflow.com/questions/tagged/veracity+platform?mode=all)
