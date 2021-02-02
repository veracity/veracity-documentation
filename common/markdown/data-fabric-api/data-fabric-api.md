---
Title : "Data Fabric API"
Author: "Brede Børhaug"
Contributors: "Rachel Hassall, Thomas Rudfoss"
---

## Overview
Veracity's Application Programming Interfaces (APIs) enable data providers and consumers to interact with Veracity programmatically. There are 3 main Veracity APIs:

- **Data API**: The Veracity Data API provides developers and applications to get information on data containers they have access to, retrieve keys for the data containers, or share access to other Veracity Platform users.
- **Provisioning API**: The Veracity Provision API enables developers and applications to create, update and delete data containers.
- **Service API**: The Service API provides a consistent interface for accessing data about the user, as well as the Veracity platform in general, [click here for more information](https://developer.veracity.com/doc/service-api)


## Authentication
Authentication is performed through OAuth2 bearer tokens. To learn how to set up Azure AD B2C, go [here](https://developer.veracity.com/doc/identity).

## API usage
For all requests you need to provide the `Ocp-Apim-Subscription-Key` header. It must contain your subscription key found in your [profile](https://api-portal.veracity.com/developer).

All request also requires an Authorization token, a guide on how to acquire the token can be found [here](https://developer.veracity.com/doc/identity)

The following request body types are supported on all requests:

- `application/json`
- `text/json`
- `application/xml`
- `text/xml`

Example http request:

```http request
GET https://api.veracity.com/veracity/datafabric/data/api/1/users/me HTTP/1.1
Host: api.veracity.com
Content-Type: application/json
Ocp-Apim-Subscription-Key: {subscription-Key}
Authorization: Bearer {token}
```

## End-points

### Data API

This API provides end-points for managing access and:

```url
https://api.veracity.com/veracity/datafabric/data/api/1/[end-point]
```

| Action | Path | Method | Description |
|:---------|:---------|:-------|:---------|
| V1.0 Access       | `/resources/{resourceId}/accesses`                | `GET`     | Retrieves a list of Providers that have access to a specified resource. |
| V1.0 Access       | `/resources/{resourceId}/accesses`                | `POST`    | Share access to another user for the specified resource. |
| V1.0 Access       | `/resources/{resourceId}/accesses/{accessId}`     | `PUT`     | Revoke an users ability to refresh keys on a resource |
| V1.0 Access       | `/resources/{resourceId}/accesses/{accessId}/key` | `PUT`     | Fetch a SAS key to access the storage item shared with you |
| V1.0 Application  | `/application`                                    | `GET`     | Returns information about the current application |
| V1.0 Application  | `/application`                                    | `POST`    | Add a new application to Veracity data fabric. |
| V1.0 Application  | `/application/{applicationId}`                    | `GET`     | Gets information about an application in Veracity data fabric. |
| V1.0 Application  | `/application/{applicationId}`                    | `PUT`     | Update role of a application on Veracity data fabric. |
| V1.0 DataStewards | `/resources/{resourceId}/datastewards`            | `GET`     | Retrieve a list of data stewards for the resource |
| V1.0 DataStewards | `/resources/{resourceId}/owner`                   | `PUT`     | Transfer the ownership of the Azure resource to a specified user |
| V1.0 DataStewards | `/resources/{resourceId}/datastewards/{userId}`   | `DELETE`  | Delete a data stewards |
| V1.0 DataStewards | `/resources/{resourceId}/datastewards/{userId}`   | `POST`    | Delegate the rights to use the Azure resource to another Veracity user. |
| V1.0 KeyTemplates | `/keytemplates`                                   | `GET`     | Returns the templates for the different types of keys you can generate |
| V1.0 Ledger       | `/resource/{resourceId}/ledger`                   | `GET`     | Returns a list of ledger records |
| V1.0 Resources    | `/resources`                                      | `GET`     | Fetches all storage resources that you can claim keys for |
| V1.0 Resources    | `/resources/{resourceId}`                         | `GET`     | Returns a single resource |
| V1.0 Tags         | `/tags`                                           | `GET`     | Retrive metadata tags in Veracity |
| V1.0 Tags         | `/tags`                                           | `POST`    | Inserts tags and returns the inserted new inserted tags with ID's  |
| V1.0 Users        | `/users/me`                                       | `GET`     | Returns information about the current user  |
| V1.0 Users        | `/users/{userId}`                                 | `GET`     | Gets information about an user |
| V1.0 Groups       | `/groups`                                         | `GET`     | Returns all the groups that you have created. |
| V1.0 Groups       | `/groups`                                         | `POST`    | Create a grouping for a set of resources. | 
| V1.0 Groups       | `/groups/{id}`                                    | `GET`     | Returns the group with the given id. |
| V1.0 Groups       | `/groups/{id}`                                    | `PUT`     | Update the group with the given id. |
| V1.0 Groups       | `/groups/{id}`                                    | `DELETE`  | Deletes the group with the given id. |


#### V1.0 Access

##### GET /resources/{resourceId}/accesses

Get a list of users / applications with access (keys) to the specified resource.

Endpoint will list your own accesses.

The endpoint will return a list active and expired accesses.

Need to be owner or data steward of container to see access of other users/applications in the results.

_Note the variable keyCreatedTimeUTC is the time the SAS key generated is valid from, this is set one hour in the past from the time created this to avoid azure time skew issues._

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/resources/{resourceId}/accesses

`With query parameters:`

https://api.veracity.com/veracity/datafabric/data/api/1/resources/{resourceId}/accesses?pageNo=1&pageSize=200

 **Input**

`Parameters`

| Parameter | Parameter Type | Data Type | required | Description |
|:----------|:--------------|:----------|:---------|:----------|
| resourceId | path | string | required | Azure resource |
| pageNo | query | int32 | optional | Page number. Defaults to 1 |
| pageSize | query | int32 | optional | Number of results per page. Defaults to 50. If this is a negative number, all results will be fetched |


 **Return**

`Response code: 200 OK:`
```
{
  "results": [
    {
      "userId": UUID
      "ownerId": UUID
      "grantedById": UUID
      "accessSharingId": UUID
      "keyCreated": boolean
      "autoRefreshed": boolean
      "keyCreatedTimeUTC": string
      "keyExpiryTimeUTC": string
      "resourceType": string
      "accessHours": int32
      "accessKeyTemplateId": UUID
      "attribute1": boolean
      "attribute2": boolean
      "attribute3": boolean
      "attribute4": boolean
      "resourceId": UUID
      "ipRange": {
        "startIp": string
        "endIp": string
      }
    }
  ],
  "page": int32
  "resultsPerPage": int32
  "totalPages": int32
  "totalResults": int32
}
```

##### POST /resources/{resourceId}/accesses

Share access to another user for a resource.

You can also share with yourself by providing your own user/application id.

Value for "accessKeyTemplateId"(In JSON payload) can be found [here](#GETkeytemplates)

The endpoint returns a "accessSharingId" this is can be used to claim the SAS key. To do this, see (PUT /resources/{resourceId}/accesses/{accessId}/key).

The autoRefreshed parameter allows the other user/application to fetch a new SAS key when the old has expired.

_note: autoRefreshed is required_

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/resources/{resourceId}/accesses?autoRefreshed=true

 **Input**

`Parameters`

| Parameter | Parameter Type | Data Type | required | Description |
|:----------|:--------------|:----------|:---------|:----------|
| resourceId | path  | string | required | Azure resource|
| autoRefreshed | query  | boolean | required | Should a renewed key be issued to the shared party after it expires |

`JSON payload`
```
{
  "userId": UUID #The other user/applications id.
  "accessKeyTemplateId": UUID #See GET /keytemplates for value
  "ipRange": { #This is optional
    "startIp": string
    "endIp": string
  }
}
```

 **Return**

`Response code: 200 OK:`

```
{
  "accessSharingId": UUID
}
```

##### PUT /resources/{resourceId}/accesses/{accessId}
 Revoke the ability to fetch new keys on a resource when the old one expires.

_Note: needs to be owner or data steward to revoke_

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/resources/{resourceId}/accesses/{accessId}

 **Input**

`Parameters`

| Parameter | Parameter Type | Data Type | required | Description |
|:----------|:--------------|:----------|:---------|:----------|
| resourceId | path  | string | required | Azure resource|
| accessId | path  | string | required | Access ID| 

 **Return**

`Response code: 200 OK`

##### PUT /resources/{resourceId}/accesses/{accessId}/key
Fetch the SAS key to a resource shared with you

To find the accessId use (GET /resources/{resourceId}/accesses), if you are unsure about the resource id, see (GET /resources)

The SAS key is used to gain access to a container, [read more](https://developer.veracity.com/doc/data-fabric-ingest).

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/resources/{resourceId}/accesses/{accessId}/key

 **Input**

`Parameters`

| Parameter |Parameter Type	| Data Type | required |Description|
|:---------|:---------|:-------|:--:|:----------|
| resourceId | path  | string | required | Azure resource|
| accessId | path  | string | required | Access ID|

**Return**

`Response code: 200 OK:`

```
{
  "sasKey": string
  "sasuRi": string
  "fullKey": string
  "sasKeyExpiryTimeUTC": string
  "isKeyExpired": boolean
  "autoRefreshed": boolean
  "ipRange": {
    "startIp": string
    "endIp": string
  }
}
```


#### V1.0 Application

##### GET /application

Returns information about the current logged (based on the Bearer token) in application.

Use [this](https://developer.veracity.com/doc/service-api#directory) to check company information

Returns a 404 Not Found if a user tries to run the endpoint

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/application

 **Input**

 None

 **Return**

`Response code: 200 OK:`

```
{
  "id": UUID
  "companyId": UUID
  "role": string
}
```

##### GET /application/{applicationId}

Gets information about an application in Veracity data fabric.

Use [this](https://developer.veracity.com/doc/service-api#directory) to check company information

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/application/{applicationId}

 **Input**

`Parameters`

| Parameter | Parameter Type | Data Type | required | Description |
|:----------|:--------------|:----------|:---------|:----------|
| applicationId | path  | string | required | AAD B2C Application Id |

**Return**

`Response code: 200 OK:`

```
{
  "id": UUID
  "companyId": UUID
  "role": string
}
```

#### V1.0 DataStewards

##### GET /resources/{resourceId}/datastewards

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/resources/{resourceId}/datastewards

Retrieve a list of data stewards for the resource

_Note: Need to be owner or data steward to perform this action_

 **Input**

`Parameters`

| Parameter | Parameter Type | Data Type | required | Description |
|:----------|:--------------|:----------|:---------|:----------|
| resourceId | path  | string | required | The Id of the resource |

 **Return**

`Response code: 200 OK:`

```
[
  {
    "grantedBy": UUID
    "userId": UUID
    "resourceId": UUID
  }
]
```

##### PUT /resources/{resourceId}/owner
Transfer the ownership of the Azure resource to a different user/application

The other user/application needs to have the role Data Manager.

_Note: Needs to be owner of the container to perform this_

_Returns the Azure resource with updated OwnerId field._

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/resources/{resourceId}/owner

**Input**

`Parameters`

| Parameter | Parameter Type | Data Type | required | Description |
|:----------|:--------------|:----------|:---------|:----------|
| resourceId | path  | string | required | The Id of the resource |
| userId | path  | string | required | The Id of the user with role of Data Manager that ownership will be transfered to. |

**Return**

`Response code: 200 OK:`

```
{
  "resourceId": UUID
  "resourceName": string
  "resourceUrl": string
  "lastModifiedUTC": string
  "ownerId": UUID
  "resourceType": string
  "resourceRegion": string
  "mayContainPersonalData": boolean
  "metadata": {
    "title": string
    "description": string
    "icon": {
      "id": string
      "backgroundColor": string
    },
    "tags": [
      {
        "id": UUID
        "title": string
      }
    ]
  }
}
```

##### DELETE /resources/{resourceId}/datastewards/{userId}

This endpoint allows you to remove a data steward.

All accesses shared by the data steward will still be active.

_The user must be the owner of the resource to be able to delete datastewards_

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/resources/{resourceId}/datastewards/{userId}

 **Input**

`Parameters`

| Parameter | Parameter Type | Data Type | required | Description |
|:----------|:--------------|:----------|:---------|:----------|
| resourceId | path  | string | required | The Id of the resource |
| userId | path  | string | required | The Id of the data steward who will be removed. |
 **Return**

`Response code: 200 OK`

##### POST /resources/{resourceId}/datastewards/{userId}

Add a new data steward.

A data steward has the possibilities to share keys(access) to the container on your behalf.

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/resources/{resourceId}/datastewards/{userId}

 **Input**

`Parameters`

| Parameter | Parameter Type | Data Type | required | Description |
|:----------|:--------------|:----------|:---------|:----------|
| resourceId | path  | string | required | The Id of the resource |
| userId | path  | string | required |A Data Steward user Id |

 **Return**

`Response code: 200 OK:`

```
{
  "grantedBy": UUID
  "userId": UUID
  "resourceId": UUID
}
```

#### V1.0 KeyTemplates

##### GET /keytemplates

Returns the template for the different types of keys you can generate. Blob Storage is the only storage type supported at the moment.

Supported access types for the Blob Storage types are as follows:
```
1. Write key
2. Read and list key
3. Read, write and list key
4. Read, write, delete and list key
```

For Each access type there are key templates that lasts 1 h, 8 h, 1 month, 2 months, 3 months, 4 months, 5 months and 6 months.

Note : "IsSystemKey" field in the result data is not relevant for the functionality currently supported. Please ignore that field.

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/keytemplates

**Input**
None
**Return**
Response Class (Status 200):
```
[
  {
    "id": UUID
    "name": string
    "totalHours": int32
    "isSystemKey": boolean
    "description": string
    "attribute1": boolean
    "attribute2": boolean
    "attribute3": boolean
    "attribute4": boolean
  }
]
```

#### V1.0 Ledger

##### GET /resource/{resourceId}/ledger

Endpoint returns a list of ledger records.

A ledger record is any action done to a container, ex; creating/reading/deleting a file, sharing/claiming a key and more.

Some of the content in the ledger might take some time before it shows up in this endpoint

The endpoint returns the last 200 entries, upto 14 days in the past.

_Note: You can only get the ledger for a container you are owner for_

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/resource/{resourceId}/ledger

 **Input**

`Parameters`

| Parameter | Parameter Type | Data Type | required | Description |
|:----------|:--------------|:----------|:---------|:----------|
| resourceId | path  | string | required | The Id of the resource |

 **Return**

Response Class (Status 200):
```
[
  {
    "entityId": string #The user/application id who did the action
    "entityType": [user, application]
    "companyId": string
    "containerName": string
    "dateOfEvent": string
    "category": string
    "ledgerSubCategory": string
    "description": string
    "region": string
    "affectedEntityId": string
    "affectedEntityType": string
    "affectedCompanyId": string
    "fileName": string #Only if there is a file operation
    "ipAddress": string #Only when there is a unknown user
  }
]
```

#### V1.0 Resources

##### GET /resources

Returns a list of all resources you have a relationship with.

The list contains resources you are data steward for, these resources are marked by accessLevel : dataSteward

The list contains resources you can claim keys for, these resources are marked by keyStatus : available

List of all key statuses:

```
 ['noKeys', 'expired', 'available', 'active']
```
List of all access levels:
```
['owner', 'dataSteward', 'consumer']
```

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/resources

 **Input**

_None_

**Return**

```
[
  {
    "id": UUID
    "reference": string
    "url": string
    "lastModifiedUTC": string
    "ownerId": UUID
    "accessLevel":  ['owner', 'dataSteward', 'consumer']
    "region": string
    "keyStatus": ['noKeys', 'expired', 'available', 'active']
    "mayContainPersonalData": boolean,
    "metadata": {
      "title": string
      "description": string
      "icon": {
        "id": string
        "backgroundColor": string
      },
      "tags": [
        {
          "id": UUID
          "title": string
        }
      ]
    }
  }
]
```

##### GET /resources/{resourceId}

Returns a single resource.

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/resources/{resourceId}

**Input**

`Parameters`

| Parameter | Parameter Type | Data Type | required | Description |
|:----------|:--------------|:----------|:---------|:----------|
| resourceId | path  | string | required | The Id of the resource |

 **Return**

```
{
    "id": UUID
    "reference": string
    "url": string
    "lastModifiedUTC": string
    "ownerId": UUID
    "accessLevel":  ['owner', 'dataSteward', 'consumer']
    "region": string
    "keyStatus": ['noKeys', 'expired', 'available', 'active']
    "mayContainPersonalData": boolean,
    "metadata": {
      "title": string
      "description": string
      "icon": {
        "id": string
        "backgroundColor": string
      },
      "tags": [
        {
          "id": UUID
          "title": string
        }
      ]
    }
  }
  ```

#### V1.0 Tags

##### GET /tags

Retrieve the metadata tags in Data fabric
Default returns approved and non deleted tags.

Use Query parameters to include non approved and deleted _(needs to be DataAdmin to perform this action)_

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/tags

 **Input**

`Parameters`

| Parameter | Parameter Type | Data Type | required | Description |
|:----------|:--------------|:----------|:---------|:----------|
| includeDeleted | query  | string | required | The Id of the resource |
| includeNonVeracityApproved | query  | string | required | The Id of the resource |

 **Return**

```
[
  {
    "id": UUID
    "title": string
  }
]
```

##### POST /tags

Insert new tags to Data Fabric, this is also automatically done when you use the Provision APIs endpoints.

The endpoint returns the inserted tags with a Id.

Tags with the same name will get the same Id

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/tags

**Input**

`JSON payload`

```
[
  {
    "title": string
  }
]
```

**Return**
```
[
  {
    "id": UUID
    "title": string
  }
]
```

#### V1.0 Users

##### GET /users/me

Returns information about the current (based on the Bearer token) logged in user.

Use [this](https://developer.veracity.com/doc/service-api#directory) to check company information

Returns a 404 Not Found if a application tries to run the endpoint

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/users/me

**Return**
```
{
  "userId": UUID
  "companyId": UUID
  "role": string
}
```

##### GET /users/{userId}

Gets information about an user

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/users/{userId}

**Input**

`Parameters`

| Parameter |Parameter Type	| Data Type | required |Description|
|:---------|:---------|:-------|:--:|:----------|
| userId | path  | string | required | My DNV GL Id |

**Return**
```
{
  "userId": UUID
  "companyId": UUID
  "role": string
}
```


#### V1.0 Groups
##### POST /groups
Creates a group for a set of container. A group is a group of resources, as the name indicates, a way to order a set of resources together.

Creating a group with resources that belong to an existing group will move them to this newly created group.

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/groups

**Input**

`Parameters`

| Parameter     | Parameter Type	| Data Type                     | Required    | Description            | 
|:--------------|:----------------|:------------------------------|:------------|:-----------------------|
| input         | Body            | GroupCreationInputParameters  | Yes         | Input parameters       |


`GroupCreationInputParameters`
```
{
  "title": "string" # Required title for the group
  "description": "string" # Optional description for the group
  "resourceIds": [ # Required, list of resource IDs
    "00000000-0000-0000-0000-000000000000"
  ],
  "sortingOrder": 0 # Floating point, optional (default 0), can be used to order groups relative to eachother
}
```

**Return**

`Response code: 201 Created`
```
{
  "id": "00000000-0000-0000-0000-000000000000",
  "title": "string",
  "description": "string",
  "resourceIds": [
    "00000000-0000-0000-0000-000000000000"
  ],
  "sortingOrder": 0.0
}
```
`Response code: 400 Bad Request` Resource ID not found.

##### GET /groups
Retrieves the list of groups for the user.

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/groups

**Return**

`Response code: 200 OK`
```
[
  {
    "id": "00000000-0000-0000-0000-000000000000",
    "title": "string",
    "description": "string",
    "resourceIds": [
      "00000000-0000-0000-0000-000000000000"
    ],
    "sortingOrder": 0
  }
]
```

##### GET /groups/{Id}
Retrieves the group with the given id.

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/groups/{Id}

**Input**

`Parameters`

| Parameter     | Parameter Type	| Data Type     | Required    | Description    | 
|:--------------|:----------------|:--------------|:------------|:---------------|
| Id            | Path            | Guid          | Yes         | Group Id       | 



**Return**

`Response code: 200 OK`
```
{
  "id": "00000000-0000-0000-0000-000000000000",
  "title": "string",
  "description": "string",
  "resourceIds": [
    "00000000-0000-0000-0000-000000000000"
  ],
  "sortingOrder": 0.0
}
```
`Response code: 404 Not Found` Group with given ID not found.

##### PUT /groups/{Id}
Updates the given group. In order to remove a resource, omit it from the request resources array. In order to add a resource, add it to the request resources array.

Note that adding a resource that belongs to another Group will move it to this group.

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/groups/{Id}

**Input**

`Parameters`

| Parameter     | Parameter Type	| Data Type                     | Required    | Description            | 
|:--------------|:----------------|:------------------------------|:------------|:-----------------------|
| Id            | Path            | Guid                          | Yes         | Id of the group        |
| input         | Body            | GroupCreationInputParameters  | Yes         | Input parameters       |

`GroupCreationInputParameters`
```
{
  "title": "string",
  "description": "string",
  "resourceIds": [
    "00000000-0000-0000-0000-000000000000"
  ],
  "sortingOrder": 0
}
```

**Return**

`Response code: 200 OK` Group successfully updated.
`Response code: 400 Bad Request` Resource Id(s) not found.
`Response code: 404 Not Found ` Group not found.

##### DELETE /groups/{Id}
Deletes the given group. Does not delete resources, just removes them from the group.

**Url**

https://api.veracity.com/veracity/datafabric/data/api/1/groups/{Id}

**Input**

`Parameters`

| Parameter     | Parameter Type	| Data Type     | Required    | Description    | 
|:--------------|:----------------|:--------------|:------------|:---------------|
| Id            | Path            | Guid          | Yes         | Group Id       | 

**Return**

`Response code: 204 No Content` Successfully deleted group.
`Response code: 404 Not Found` Group not found.






### Provisioning API

This API provides end-points for managing access and:

```url
https://api.veracity.com/veracity/datafabric/provisioning/api/1/[end-point]
```

| Action | Path | Method | Description |
|:---------|:---------|:-------|:----------|
|V1.0 Container | `/container` | `POST` | Provision a blob storage container, requires a short name and storage container. |
|V1.0 Container | `/container/{id}/metadata` | `PATCH` | Update container metadata. |
|V1.0 Container | `/container{id}` | `DELETE` | Delete a azure storage container |
|V1.0 Regions | `/regions` | `GET` | Get all supported regions |


#### V1.0 Container

##### POST /container

An HTTP response of type 202 Accepted means the request was accepted and is currently processing. It may take up to 15 minutes for a container to be completed.

An HTTP response of type 409 Conflict means that there already exists a blob container using the same short name. Please choose another.

A valid location can be found by using the GET /regions endpoint

**Url**

https://api.veracity.com/veracity/datafabric/provisioning/api/1/container

**Input**

`JSON payload`

```
{
  "storageLocation": string #A valid location can be found by using the GET /regions endpoint
  "containerShortName": string
  "mayContainPersonalData": boolean
  "title": string #
  "description": string #Max length is 500
  "icon": { #optional, this is used the Veracity frontend
    "id": string
    "backgroundColor": string
  },
  "tags": [ #optional, this is used the Veracity frontend
    {
      "title": string
    }
  ]
}
```


**Return**
`Response code: 202 OK`

A 202 means the storage container will be created.

##### PATCH /container/{id}/metadata

JSON [Patch](https://tools.ietf.org/html/rfc6902) defines a JSON document structure for expressing a sequence of operations to apply to a JavaScript Object Notation (JSON) document; it is suitable for use with the HTTP PATCH method.

The "application/json-patch+json" media type is used to identify such patch documents.

Example in this case:

```json
{
  "value": "My new container name",
  "path": "Title",
  "op": "replace"
}
```
This operation would replace the title

A other example for update of tags (NOTE: remember to update the list of tags with all the tags) 

```json
{
  "value": [ { "Title" :"First tag" }, { "Title" : "Second tag" }],
  "path": "Tags",
  "op": "replace"
}
```
 This operation would replace the tags

The metadata is used by the veracity frontend

**Url**

https://api.veracity.com/veracity/datafabric/provisioning/api/1/container/{id}/metadata

**Input**

`Parameters`

| Parameter | Parameter Type | Data Type | required | Description |
|:----------|:--------------|:----------|:---------|:----------|
| id | path  | string | required | The Id of the resource |


`JSON payload`

```
{
  "value": object #value of change
  "path": string #The path
  "op": "replace"
}
```

**Return**

```
{
    "id": UUID
    "reference": string
    "url": string
    "lastModifiedUTC": string
    "ownerId": UUID
    "accessLevel":  ['owner', 'dataSteward', 'consumer']
    "region": string
    "keyStatus": ['noKeys', 'expired', 'available', 'active']
    "mayContainPersonalData": boolean,
    "metadata": {
      "title": string
      "description": string
      "icon": {
        "id": string
        "backgroundColor": string
      },
      "tags": [
        {
          "id": UUID
          "title": string
        }
      ]
    }
  }
```

##### DELETE /container/{id}

Delete the azure container.
You need to be the owner of the resource to be able to delete the container.
What happens when the container is deleted:

- All active keys will stop working.
- All content on the container will be deleted and this action is not reversible

**Url**

https://api.veracity.com/veracity/datafabric/provisioning/api/1/container/{id}

**Input**

`Parameters`

| Parameter | Parameter Type | Data Type | required | Description |
|:----------|:--------------|:----------|:---------|:----------|
| id | path  | string | required | The Id of the resource |

#### V1.0 Regions

##### POST /regions
A list of active regions supported by veracity

**Url**

https://api.veracity.com/veracity/datafabric/provisioning/api/1/regions

**Input**

_None_

**Return**
`Response code: 200 OK`

```
[
  {
    "shortName": string
    "fullName": string
    "location": string
    "azureName": string #This is the name you should use as input when creating a new storage container
    "displayName": string
    "groupName": string
  }
]
```

## Tutorial
Veracity uses API Management. In order to get access, you will need to:

- Register at [https://api-portal.veracity.com/](https://api-portal.veracity.com/)
- Subscribe to the Veracity Platform API – Product, this will give you access to our DataAPI and ProvisionAPI with a subscription ID

### Standard structure of API Call

#### Call header:

- **Ocp-Apim-Subscription-Key** - this header attribute is for API Management authentication
- **Authorization** - this header attribute needs to contain the Bearer Token that is received through authorization on Veracity

Example:

```http request
GET https://api.veracity.com/veracity/datafabric/data/api/1/users/me HTTP/1.1
Host: api.veracity.com
Ocp-Apim-Subscription-Key: {subscription-Key}
Authorization: Bearer {token}
```

C# example:

```cs
var httpClient = new System.Net.Http.HttpClient();
var request = new HttpRequestMessage(httpMethod, "https://api.veracity.com/veracity/datafabric/data/api/1/users/me");
request.Headers.Add("Ocp-Apim-Subscription-Key", "{Subscription-Key}");
request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", "{accessToken}");

var response = await httpClient.SendAsync(request);
```

### Authorization snippet

The Bearer Token is usually valid for one hour, after that you need to request a new one.

It's best practice to check the expire date of the token and get a new token before it expires a request.

##### Application (AAD B2C)

Make sure your AAD B2C application is onboarded and added to Data Fabric before you proceed with this guide.

Information you need to acquire before you start :

```ps
ClientId - Application ID from your Native app registration
ClientSecret - Application secret
Full Data Fabric Resource url
AAD Tenant id - Azure AD Tenant Id
```
To get a access token:

Example Http request:

```http request
POST https://login.microsoftonline.com/{tenantId/oauth2/token
Content-Type: application/x-www-form-urlencoded
grant_type=client_credentials&resource={Full Data fabric resource url}f&client_id={ClientId}&client_secret={ClientSecret}
```

_Note: Remember to url encode the form content_

Example C#

This example requires:
- [Newtonsoft.Json](https://www.nuget.org/packages/Newtonsoft.Json/)

Aad Token class:

```cs
public class Token
{
    [JsonProperty("token_type")]
    public string TokenType { get; set; }

    [JsonProperty("expires_in")]
    public string ExpiresIn { get; set; }

    [JsonProperty("ext_expires_in")]
    public string ExtExpiresIn { get; set; }

    [JsonProperty("expires_on")]
    public string ExpiresOn { get; set; }

    [JsonProperty("not_before")]
    public string NotBefore { get; set; }

    [JsonProperty("resource")]
    public string Resource { get; set; }

    [JsonProperty("access_token")]
    public string AccessToken { get; set; }
}
```

Retrieve the access token:

```cs
var clientId = "{clientId}";
var clientSecret = "{clientSecret";
var tokenEndpoint = "https://login.microsoftonline.com/{tenantId}/oauth2/token";
var resource = "{Data fabric resource url}";

using (var client = new System.Net.Http.HttpClient())
{
    var content =
        new StringContent(
            $"grant_type=client_credentials&client_id={clientId}&resource={resource}&client_secret={HttpUtility.UrlEncode(clientSecret)}",
            Encoding.UTF8, "application/x-www-form-urlencoded");

    var response = await client.PostAsync(tokenEndpoint, content);
    var result = JsonConvert.DeserializeObject<Token>(await response.Content.ReadAsStringAsync());

    var accessToken = result.AccessToken;
}
```

##### User

To acquire the Bearer Token needed for the API requests it is possible to authenticate with the code below. It's important to register any new app in the Azure Active Directory as a Native App.
This App ID, together with the tenant name from Azure AD will be used to obtain an authentication key.

The below code in .NET shows how to programmatically get the Bearer Key. This code is also available [here](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-veracity-api/veracity-api-net).

Firstly, input data is required:

```ps
Tenant - tenant name from Azure Portal (Active Directory)
ClientId - Application ID from your Native app registration
PolicySignUpSignIn - sign in policy created during app registration
ApiScopes - scopes available for given api
```

For user identification we use the class PublicClientApplication which is available in the namespace [Microsoft.Identity.Client](https://www.nuget.org/packages/Microsoft.Identity.Client).
You can include it as a NuGet package, currently in preview mode.

```cs
public static PublicClientApplication PublicClientApp { get; } = new PublicClientApplication(ClientId, Authority, TokenCacheHelper.GetUserCache());
```

The Authority field is the following URL, where {tenant} and {policy} are replaced with proper values from the app registration.:

```url
"https://login.microsoftonline.com/tfp/{tenant}/{policy}/oauth2/v2.0/authorize";
```

To sign in, the AcquireTokenAsync method from PublicClientApplication is used.

```cs
public static async Task<AuthenticationResult> SignIn()
{
  try
  {
    var authResult = await PublicClientApp.AcquireTokenAsync(ApiScopes,
      GetUserByPolicy(PublicClientApp.Users, PolicySignUpSignIn), UIBehavior.SelectAccount, string.Empty,
      null, Authority);

    DisplayBasicTokenInfo(authResult);
    return authResult;
  }
  catch (Exception ex)
  {
    Console.WriteLine(
      $"Users:{string.Join(",", PublicClientApp.Users.Select(u => u.Identifier))}{Environment.NewLine}Error Acquiring Token:{Environment.NewLine}{ex}");
    return null;
  }
}
```

The AuthenticationResult object contains the property AccessToken, which is where the Bearer Key is stored.

This key is to be used in the following code samples to properly authenticate API requests.

### Data fabric Quick start

This is a quick start on how to use the Data Fabrics API.

This guide will cover this:
1st scenario:

- Authenticate
- Create container
- Create a key for your self
- Push Data to your new container
- Share key to a other user.

2nd scenario:

- Find Resource
- Claim key and read content


The Veracity Data Platform DataAPI is an API where developers and applications can get information on data containers and get their key to a data container or share a key with another Veracity Data Platform user.

Implementations:
- [.NET implementation](#net-implementation)


#### .NET implementation
The below sample assumes that the user has a Subscription Key from the Veracity Portal.

We are going to access the Data API service via http requests and in our implementation we will use a custom HttpClient based on from System.Net.Http.

This example requires:
- [Newtonsoft.Json](https://www.nuget.org/packages/Newtonsoft.Json/)
- [WindowsAzure.Storage](https://www.nuget.org/packages/WindowsAzure.Storage/9.3.2)

We will also reuse the authentication code (for application) from [here](#Authorization-snippet)

To make communication with the Data fabric apis, we have created a sample helper to use:
```cs
public class DataFabricClient
{

    public async Task<T> Handle<T>(HttpMethod httpMethod, string uri, object content = null)
    {
        //Same TokenProvider from previous step (from Authorization snippet)
        //Recommended to add caching of token.
        var tokenProvider = new TokenProvider();
        var token = await tokenProvider.GetToken();

        //Set your subscription key, best practice is to not hard code it. So remember to get it from app settings or other places
        var subscriptionKey = "{subscriptionKey}";

        //Best practice from microsoft is to have a global httpclient registered in dependency config(Lifestyle: Singleton).
        var httpClient = new System.Net.Http.HttpClient();

        //We add the subscription key to the header
        httpClient.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", subscriptionKey);

        var request = new HttpRequestMessage(httpMethod, uri);
        request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", token.AccessToken);

        //If we have content we want to be apart of the request, we want to Serialize it to json
        if (content != null)
        {
            var jsonContent = new StringContent(JsonConvert.SerializeObject(content), Encoding.UTF8, "application/json");
            request.Content = jsonContent;
        }

        var response = await httpClient.SendAsync(request);

        // This will throw an exception if it's an unexpected response (not 2xx series codes)
        response.EnsureSuccessStatusCode();

        return JsonConvert.DeserializeObject<T>(await response.Content.ReadAsStringAsync());
    }
}
```
This client gets the bearer token(from the TokenProvider provided in the first example).

To view all classes/models used, see [here](#models)
##### 1st scenario:

A prerequisite for this scenario is an already registered AAD application  (you can also use [User authentication](#User))

I will recommend you create a new blank Console program, to follow the examples

This fist scenario will cover:

- Authenticate (with an application)
- Create container
- Create a key for your self
- Push Data to your new container
- Share key to another user.

###### Authenticate (with an application)

The code below will authenticate the application and return a instance of "Token". The token will contain "AccessToken", this accesstoken can later be used to do authenticated calls to the Data fabric apis.

Replace the values of:

- {clientId}
- {clientSecret}
- {Data fabric resource url}
- {tenantId}

With values provided from developer portal.

```cs
public class TokenProvider {
  /// <summary>
  /// Object based on https://tools.ietf.org/html/rfc6750
  /// </summary>
  public class Token
  {
      [JsonProperty("token_type")]
      public string TokenType { get; set; }

      [JsonProperty("expires_in")]
      public string ExpiresIn { get; set; }

      [JsonProperty("ext_expires_in")]
      public string ExtExpiresIn { get; set; }

      [JsonProperty("expires_on")]
      public string ExpiresOn { get; set; }

      [JsonProperty("not_before")]
      public string NotBefore { get; set; }

      [JsonProperty("resource")]
      public string Resource { get; set; }

      [JsonProperty("access_token")]
      public string AccessToken { get; set; }
  }

  /// <summary>
  /// Returns a access token.
  /// Throws exception if the request is invalid
  /// </summary>
  /// <returns></returns>
  public async Task<Token> GetToken()
  {
      string clientId = "{clientId}";
      string clientSecret = "{clientSecret}";
      string tokenEndpoint = "https://login.microsoftonline.com/{tenantId}/oauth2/token";
      string resource = "{Data fabric resource url}";


      using (var client = new System.Net.Http.HttpClient())
      {
          var content =
              new StringContent(
                  $"grant_type=client_credentials&client_id={clientId}&resource={resource}&client_secret={HttpUtility.UrlEncode(clientSecret)}",
                  Encoding.UTF8, "application/x-www-form-urlencoded");

          var response = await client.PostAsync(tokenEndpoint, content);

          response.EnsureSuccessStatusCode();//This will throw an exception, so it should be handled

          var result = JsonConvert.DeserializeObject<Token>(await response.Content.ReadAsStringAsync());
          return result;
      }
  }
}
```

###### Create container

This will show you how to create a new container in data fabric.

The "StorageLocation" can be found by using the "GET /api/1/regions" endpoint, by default the North Europe(northeurope) and East Us(eastus) regions are active.

Container creation can take up to 2 min. So you should add some retry logic if the container does not appear the first time.

```cs
var client = new DataFabricClient();

var provisionApiBaseUrl = "{provisionApiBaseUrl}";
var dataApiBaseUrl = "{dataApiBaseUrl}";

var containerInput = new ContainerInput()
{
    ContainerShortName = "firstcontainer",
    StorageLocation = "northeurope",
    MayContainPersonalData = false
};

//Retrieve your user/application information, just to test if your setup is working
var identity = await client.Handle<Identity>(HttpMethod.Get, $"{dataApiBaseUrl}/api/1/application");

if (identity.Role != "DataFabricManager")
    throw new Exception("You do not have the correct rights to provision a new container");

//If all is okay, we can provision a container
await client.Handle<string>(HttpMethod.Post, $"{provisionApiBaseUrl}/api/1/container", containerInput);

//This operation might take up to 2 min, so we wait 30 sec before we continue
Thread.Sleep(30000);

//Retrieve all your resources
var containers = await client.Handle<List<Resource>>(HttpMethod.Get, $"{dataApiBaseUrl}/api/1/resources");

//Find your new container
var container = containers
      .OrderByDescending(resource => resource.LastModifiedUTC) // Order by Date so you are sure to get the last container you created
      .FirstOrDefault(resource => resource.Reference.StartsWith(containerInput.ContainerShortName));

if (container != null)
{
    //You have your container, you can now do more logic here
}

//If there is no container, you should retry retrieve the containers, and check again
```

###### Create a key for your self

After your container is created, it's time to give yourself access to the container.

Replace the {resourceId} with container id from last step

To see what each attribute of a key template is, read more [here](#GET/keytemplates)

This will create a "AccessSharingId" the id will later be used to fetch the SAS token.

```cs
var client = new DataFabricClient();

var dataApiBaseUrl = "{dataApiBaseUrl}";

var resourceId = "{resourceId}";

//retrieve your user/application information, just to test if your setup is working
var identity = await client.Handle<Identity>(HttpMethod.Get, $"{dataApiBaseUrl}/api/1/application");

//Find the key template you want to create a key with
var keyTemplates = await client.Handle<List<KeyTemplate>>(HttpMethod.Get, $"{dataApiBaseUrl}/api/1/keytemplates");

//Find the first key template with all access (See documentation on key template endpoint to see what each attribute is):
var keytemplate = keyTemplates.FirstOrDefault(template =>
      template.Attribute1 && template.Attribute2 && template.Attribute3 && template.Attribute4);

if (keytemplate == null)
    throw new Exception("No Key template found");

var keyInput = new SharingResourceInputData
{
    AccessKeyTemplateId = keytemplate.Id, // Use the id of the key template we found
    UserId = identity.Id // Share it with your own Id
};

//This will create a "AccessSharingId" this id can be used to fetch the key
var accessSharing = await client.Handle<ShareResourceVM>(HttpMethod.Post,
    $"{dataApiBaseUrl}/api/1/resources/{resourceId}/accesses?autoRefreshed=true", keyInput);

if (accessSharing == null)
    throw new Exception("Could not share key");

//You have now created a accessSharing
```

###### Push Data to your new container

Now it's time to get your SAS token and use it!

[For more information on SAS tokens](https://docs.microsoft.com/en-us/azure/storage/common/storage-dotnet-shared-access-signature-part-1)

Use the accessSharingId you retrieved from the last step and replace {accessSharingId}.

```cs
var client = new DataFabricClient();

var dataApiBaseUrl = "{dataApiBaseUrl}";

var resourceId = "{resourceId}";
var accessSharingId = "{accessSharingId}";

//Retrieve your user/application information, just to test if your setup is working
var identity = await client.Handle<Identity>(HttpMethod.Get, $"{dataApiBaseUrl}/api/1/application");

//Get your SAS token from data fabric by using your accessSharingId from the last step
var key = await client.Handle<SASToken>(HttpMethod.Put,
    $"{dataApiBaseUrl}/api/1/resources/{resourceId}/accesses/{accessSharingId}/key");

if (key == null)
    throw new Exception("Could not claim key");

//Use your claimed SAS Key (fullKey) to access the container
var container = new CloudBlobContainer(new Uri(key.FullKey));

//Get the blob reference
var blob = container.GetBlockBlobReference("first_folder/first_file.txt");

//The library will automatically create the file for you.
await blob.UploadTextAsync("Hello Container! \n This is my first data");

//You have now uploaded a simple text to your container
```

###### Share key to another user.

It's time to share your amazing container with other people.

For simplicity we use the same keytemplateId as the last time.

```cs
var client = new DataFabricClient();

var dataApiBaseUrl = "{dataApiBaseUrl}";

var resourceId = "{resourceId}";
var otherUserId = "{otherUserId}";

var keytemplateId = "{keytemplateId}";
//Retrieve your user/application information, just to test if your setup is working
var identity = await client.Handle<Identity>(HttpMethod.Get, $"{dataApiBaseUrl}/api/1/application");

var keyInput = new SharingResourceInputData
{
    AccessKeyTemplateId = Guid.Parse(keytemplateId), // Use the id of the key template we found before
    UserId = Guid.Parse(otherUserId)// Share it with the other user id
};

var accessSharing = await client.Handle<ShareResourceVM>(HttpMethod.Post,
    $"{dataApiBaseUrl}/api/1/resources/{resourceId}/accesses?autoRefreshed=true", keyInput);

//You have now shared access to your container
```

##### 2nd scenario:

This seccond scenario will continue and build upon the steps from the first scenario.

This scenario  will cover:

- Find Resource
- Claim key and read content

###### Find Resource

It's now time to find out if someone (or you) has given you access to their container.

```cs
var client = new DataFabricClient();

var dataApiBaseUrl = "{dataApiBaseUrl}";

//Retrieve your user/application information, just to test if your setup is working
var identity = await client.Handle<Identity>(HttpMethod.Get, $"{dataApiBaseUrl}/api/1/application");

//Retrieve all your resources
var containers = await client.Handle<List<Resource>>(HttpMethod.Get, $"{dataApiBaseUrl}/api/1/resources");

//Find an resource where you have an key available
var resource = containers
    .FirstOrDefault(r =>
        r.KeyStatus == KeyStatus.Available);

if (resource == null)
    throw new Exception("Found no resource where you could claim key");
```

###### Claim key and read content

```cs
var client = new DataFabricClient();

var dataApiBaseUrl = "{dataApiBaseUrl}";

var resourceId = "{resourceId}";

//Retrieve your user/application information, just to test if your setup is working
var identity = await client.Handle<Identity>(HttpMethod.Get, $"{dataApiBaseUrl}/api/1/application");

//Make sure the resource exist
var container = await client.Handle<Resource>(HttpMethod.Get, $"{dataApiBaseUrl}/api/1/resources/{resourceId}");
if (container == null)
    throw new Exception("Can't find/access resource");

//Find your accessSharingId on the container
var accesses = await client.Handle<ProviderAccessResult>(HttpMethod.Get, $"{dataApiBaseUrl}/api/1/resources/{resourceId}/accesses");

var access = accesses.Results.FirstOrDefault(a =>
    a.Attribute1 && a.Attribute2 && a.Attribute3 && a.Attribute4);

if (access == null)
    throw new Exception("No valid access for this scenario");

//Get your SAS token from data fabric
var key = await client.Handle<SASToken>(HttpMethod.Put,
    $"{dataApiBaseUrl}/api/1/resources/{resourceId}/accesses/{access.AccessSharingId}/key");

//You can now use key.FullKey to access the container 
var storageContainer = new CloudBlobContainer(new Uri(key.FullKey));

//Get the blob reference
var blob = storageContainer.GetBlockBlobReference("first_folder/first_file.txt");

//Check if the file exist
if (await blob.ExistsAsync())
{
    using (var stream = await blob.OpenReadAsync())
    {
        var reader = new StreamReader(stream);

        //read the content of the blob
        var content = await reader.ReadToEndAsync();
    }
}
```
##### Models

All the models used in the quick guide
```cs
public class ProviderAccessResult
{
    [JsonProperty("results")]
    public List<ProviderAccess> Results { get; set; }
}

public class ProviderAccess
{
    [JsonProperty("accessSharingId")]
    public Guid AccessSharingId { get; set; }

    [JsonProperty("attribute1")]
    public bool Attribute1 { get; set; }

    [JsonProperty("attribute2")]
    public bool Attribute2 { get; set; }

    [JsonProperty("attribute3")]
    public bool Attribute3 { get; set; }

    [JsonProperty("attribute4")]
    public bool Attribute4 { get; set; }
}


public class SASToken
{
    public string SASKey { get; set; }
    public string SASURi { get; set; }

    public string FullKey => SASURi + SASKey;

    public DateTime SASKeyExpiryTimeUTC { get; set; }
    public bool IsKeyExpired { get; set; }

    public bool AutoRefreshed { get; set; }
}

public class SharingResourceInputData
{
    public Guid UserId { get; set; }
    public Guid AccessKeyTemplateId { get; set; }
}

public class ShareResourceVM
{
    /// <summary>
    /// Sharing id for the container
    /// </summary>
    public Guid AccessSharingId { get; set; }
}

public class KeyTemplate
{
    public Guid Id { get; set; }
    public byte AccessType { get; set; }
    public string Name { get; set; }
    public short TotalHours { get; set; }
    public bool IsSystemKey { get; set; }
    public string Description { get; set; }
    public bool Attribute1 { get; set; }
    public bool Attribute2 { get; set; }
    public bool Attribute3 { get; set; }
    public bool Attribute4 { get; set; }
    public bool Deleted { get; set; }
}

public class Resource
{
    /// <summary>
    /// Container ID
    /// </summary>
    public Guid Id { get; set; }

    /// <summary>
    /// The name of the container in Azure. 
    /// <example>
    /// my-container5e1b021a-d3dc-4cdd-ba1e-7399db38ecf4
    /// </example>
    /// </summary>
    public string Reference { get; set; }

    /// <summary>
    /// The full container url in Azure. 
    /// <example>
    /// https://ne1dnvgltstgcus0000f.blob.core.windows.net/my-container5e1b021a-d3dc-4cdd-ba1e-7399db38ecf4
    /// </example>
    /// </summary>
    public string Url { get; set; }

    public DateTime LastModifiedUTC { get; set; }
    public Guid OwnerId { get; set; }
    public AccessLevel AccessLevel { get; set; }


    /// <summary>
    /// Which region the resource was created in. Valid values: "USA" | "Europe"
    /// </summary>
    public string Region { get; set; }

    /// <summary>
    /// <see cref="KeyStatus"/>
    /// </summary>
    public KeyStatus KeyStatus { get; set; }

}

/// <summary>
/// Shows information about what type of keys are available for that resource
/// </summary>
public enum KeyStatus
{
    NoKeys = 0,
    Expired = 1,
    Available = 2,
    Active = 3
}

/// <summary>
/// Access level for container
/// </summary>
public enum AccessLevel
{
    Owner = 2,
    DataSteward = 1,
    Consumer = 0
}


public class Identity
{
    public Guid Id { get; set; }
    public Guid CompanyId { get; set; }
    public string Role { get; set; }
}

public class ContainerInput
{
    /// <summary>
    /// The Location which a storage container will be provisioned. Containers can only be created in supported regions
    /// </summary>

    public string StorageLocation { get; set; }

    /// <summary>
    /// 5-32 character short name used to distinguish between storage containers. The name needs to be lowercase and alphanumeric. The full name of the container will comprise of this shortname plus a unique Guid genarated by the system. Note - storage containers can not be renamed
    /// </summary>
    public string ContainerShortName { get; set; }

    /// <summary>
    /// Indicates whether the user has accepted that the container will not contain personal data. Required to be true for a user to upload a container
    /// </summary>
    public bool MayContainPersonalData { get; set; }
}
```

## GitHub  
Follow our open projects related to Veracity data fabric API on https://github.com/veracity

## Stack Overflow
Stack Overflow is the largest, most trusted online community for developers to learn and share their programming knowledge. The Veracity developer team monitor Stack Overflow forum posts that include the tag Veracity Platform.

[Visit Stack Overflow](https://stackoverflow.com/questions/tagged/veracity+platform?mode=all)

## Frequently Asked Questions

###### How do I get the SAS key for my containers ?
To create a SAS key for your container from the My
Data Section in [Veracity web
site](https://data.veracity.com/containers),  you need to navigate to your
container you want to create the SAS key for. 

 
-----------------------------------------------------------
**Note** : When you try to open your container, if you see the following warning "Your current access key has expired so we are unable to display the contents."  

-----------------------------------------------------------

Then, click on "Request access". Once you click you will see the text "Your request has been received". Then click on Access and fill out the required fields. You will be in Share access tab.

-----------------------------------------------------------
**Note**  : You can share a key with yourself or with other people.

-----------------------------------------------------------


 Click on Share.

To view a SAS Key, navigate to User management tab in Access. Here you can get an overview for all keys for your container.
You can see the keys you own by clicking on View key for any key.

###### How to handle SAS key expired situation ?
By default SAS keys are created with a specified duration and that duration starts by redeeming the sharing/access and redeeming is done by clicking on the Access Key for the target key in User management. Once it is clicked, a SAS key is generated for the sharing/access and the key is expired after the specified duration time. The owner of the Access will lose his/her access to the container once the SAS key is expired.

On the other hand, when you create a Access share in Share access,  there is an option called Set key as recurring.  If this option is specified, the owner of the Access will be able to re-generate a new SAS key after the key generated previously is expired.

Selecting which duration when creating and Access Share is important for the recurring keys. If you set it as 6 months, even if you Revoke that Access, the last generated SAS key will keep
Being valid for that duration.

###### How to create container in my application ?
This can be achieved with and on-boarded application. You can use the client credentials flow. Your API/application can make the call as the application. Please see the Provisioning API reference for details.

###### How to share access of my containers in my application ?
This can be achieved with and on-boarded application. You can use the client credentials flow. Your API/application can make the call as the application. Please see the Data API reference for details.


###### How to get access token when I want to sync files with my container in my server without human login ?
You need to first on-board your application into Veracity.
For that your application should be registered in AAD B2C v1(Client Credentials grant) with permissions to the Data/Provisioning APIs.

Once this is ready, you can make POST requests to the OAuth2 token endpoint of the tenant.

###### How to deal with the case that I want to use DF as file storage, the web application can handle the file no matter who login to the application ?
This can be achieved with and on-boarded application. You can use the client credentials flow. Your API can make the call as the application. Internal Identity is managed by your App is not relevant in that case.

