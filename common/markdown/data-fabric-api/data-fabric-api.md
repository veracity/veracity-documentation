---
Title : "Data Fabric API"
Author: "Brede Børhaug"
Contributors: "Rachel Hassall, Thomas Rudfoss"
---

## Overview
Veracity's Application Programming Interfaces (APIs) enable data providers and consumers to interact with Veracity programmatically. There are 3 main Veracity APIs: 

- Data API - The Veracity Data API is an API where developers and applications can get information on data containers, get the key to a data container, or share a key with other Veracity Platform users.
- Provisioning API - The Veracity Provision API is an API that enables developers and applications to create data containers. 
- Metadata API - The Veracity Metadata API is an API that can both get and post information on data containers. The API enables you to add meta data to the containers both to visually represent the data containers in the portal, and make it easier to search in the data catalogue.

## Authentication

Authentication is performed through OAuth2 bearer tokens. To learn how to set up Azure AD B2C, go [here](https://developer.veracity.com/doc/identity).

## End-points

### Data API

This API provides end-points for managing access and 


```url
https://api.veracity.com/veracity/datafabric/data/api/[end-point]
```

|End-point|Path|Method|Description|
|:---------|:-------|:--:|:----------|
|KeyTemplates_&#8203;GetStorage&#8203;KeyTemplate|`/keytemplates`|`GET`|Get all supported key templates for generating access keys.|
|ProviderAccess|`/resources/{resourceId}/accesses`|`GET`, `POST`|Get list of providers with access to a given storage item or grant access.|
|FetchKeyFor&#8203;StorageContainer|`/resources/{resourceId}/keys`|`GET`|Get a SAS key to access a storage item shared with you.|
|GetAllResources|`/resources`|`GET`|Get a list of all resources you can claim keys for.|
|Users|`/users/{userId}`|`GET`|Get information about a user.|

For all requests to this end-point you need to provide the `Ocp-Apim-Subscription-Key` header. It must contain your subscription key found in your profile.

#### `/keytemplates`

Response format:
```
[
  {
    id: UUID,
    name: string,
    totalHours: int32,
    isSystemKey: boolean,
    description: string,
    attribute1: boolean,
    attribute2: boolean,
    attribute3: boolean,
    attribute4: boolean,
    ...
  }
]
```

#### `/resources/{resourceId}/accesses`

When reading this end-point using `GET` you must provide a page number as well as a page size as query parameters to this request.

The `{resourceId}` parameter must be the UUID of the resource.

E.g.:
```url
/this/services?pageNo=1&pageSize=15
```

Request format:
```
{
  userId: UUID,
  accessKeyTemplateId: UUID, see /keytemplates end-point
}
```

The following request body types are supported:

- `application/json`
- `text/json`
- `application/xml`
- `text/xml`
- `application/x-www-form-urlencoded`

Response format:
```
{
  results: [
    {
      providerEmail: string,
      userId: UUID,
      ownerId: UUID,
      accessSharingId: UUID,
      keyCreated: boolean,
      autoRefreshed: boolean,
      keyCreatedTimeUTC: string,
      keyExpiryTimeUTC: string,
      resourceType: string,
      accessHours: int32,
      accessKeyTemplateId: UUID,
      attribute1: boolean,
      attribute2: boolean,
      attribute3: boolean,
      attribute4: boolean,
      resourceId: UUID
    },
    ...
  ],
  page: 0,
  resultsPerPage: 0,
  totalPages: 0,
  totalResults: 0
}
```

#### `/resources/{resourceId}/keys`

This request requires an `accessSharingId` query parameter defining the id of the key you want to return:

```url
https://api.veracity.com/veracity/datafabric/data/api/resources/{resourceId}/keys?accessSharingId={accessSharingId}
```

Response format:

```
{
  sasKey: string,
  sasuRi: string,
  fullKey: string,
  sasKeyExpiryTimeUTC: string,
  isKeyExpired: boolean,
  autoRefreshed: boolean
}
```

#### `/resources`

This end-point also provides two optional `boolean` query parameters `shared` and `owned` to return shared or owned resources. By default only owned resources are returned:

```url
https://api.veracity.com/veracity/datafabric/data/api/resources?shared=false&owned=true
```

Response format:

```
{
  ownedResources: [
    {
      resourceId: UUID,
      resourceName: string,
      resourceUrl: string,
      lastModifiedUTC: string,
      ownerId: UUID,
      consumerName: string,
      resourceType: string,
      resourceRegion: string
    }
  ],
  sharedResources: [
    {
      storageItem: {
        resourceId: UUID,
        resourceName: string,
        resourceUrl: string,
        lastModifiedUTC: string,
        ownerId: UUID,
        consumerName: string,
        resourceType: string,
        resourceRegion: string
      },
      accessDescription: string,
      accessKeyCreated: boolean,
      accessKeyEndDateUTC: string,
      accessKeyTemplateId: UUID,
      accessSharingId: UUID,
      autoRefreshed: boolean
    }
  ]
}
```

#### `/users/{userId}`

This end-point requires either a `{userId}` or the literal `me`. The former returns information about the specific user while the latter returns information about the current user.

Response format:

```
{
  userId: UUID,
  companyId: UUID,
  role: string
}
```

### Provisioning API

This API provides an end-point for provisioning new Azure Blob Containers. The base url for requests is:

```url
https://api.veracity.com/veracity/datafabric/data/api/[end-point]
```

|End-point|Path|Method|Description|
|:--------|:---|:-----:|:----------|
|Container|`/container`|`POST`|Provisions a new blob storage container|

|HTTP Status|Name|Description|
|:----------|:---|:----------|
|200|OK|Your request was processed correctly. View content for response.|
|400|Bad Request|The view-point/action exists, but the way you formatted the request was incorrect. Check `http verb`, `headers` or `body`.|
|401|Unauthorized|You do not have permission to access the end-point.|
|403|Forbidden|The requester has insufficient permissions to perform the action or authorization information is missing from the request. Check that you provide a valid OAuth2 `Authorization` header.|
|404|Not Found|The requested end-point was not found or is not known.|
|409|Conflict|The request cannot be completed as it conflicts with an existing resource.|
|500|Internal Server Error|Something went wrong on the server when processing your request. Try to include the `x-supportcode` header content if you wish to submit a support request.|
|502|Bad Gateway|The request was not processed correctly by a dependent service of the API.|

#### Response format

The API supports formatting the response body according to the mime type provided in your requests `Accept` header. Currently the following mime types are supported:

- `application/json`
- `text/json`
- `application/xml`
- `text/xml`

#### `/container`

The provision api supports `POST` requests that provision new Azure Blob Storage containers on the Veracity platform.

You need to provide the `Ocp-Apim-Subscription-Key` header on all requests using this end-point. It must contain your subscription key found in your profile.

An HTTP response of type `202 Accepted` means the request was accepted and is currently processing. It may take up to 15 minutes for a container to be completed.

An HTTP response of type `409 Conflict` means that there already exists a blob container using the same short name. Please choose another.

Request body format (* required):
```
{
  storageLocation: string ["Unknown"|"NorthEurope"|"EastUs1"],
  requestCode: string, A unique string is needed to track each provision request, if you use the same code more than twice in a given timespan the second request is rejected
  containerShortName: string, 5-32 character short name
  title: string,
  description: string,
  icon: {
    id: string,
    backgroundColor: string (Hex color)
  },
  tags: [
    {
      title: string,
      type: string
    }
  ]
}
```

The following request body types are supported:

- `application/json`
- `text/json`
- `application/xml`
- `text/xml`
- `application/x-www-form-urlencoded`

### Metadata API

This API defines two primary end-points from which you can access metadata information. The base url for requests is:

```url
https://api.veracity.com/veracity/datafabric/data/api/[end-point]

e.g.:
https://api.veracity.com/veracity/datafabric/data/api/global-tags
```

These are:

|End-point|Path|Description|
|:---------|:-------|:----------|
|Resources|`/resources`|Manage metadata for resources that you own or are shared with you.|
|Global-tags|`/global-tags`|Manage global tags.|

The response status code describes whether the request succeeded or not. Currently the following status codes may be returned

|HTTP Status|Name|Description|
|:----------|:---|:----------|
|200|OK|Your request was processed correctly. View content for response.|
|400|Bad Request|The view-point/action exists, but the way you formatted the request was incorrect. Check `http verb`, `headers` or `body`.|
|401|Unauthorized|You do not have permission to access the end-point.|
|403|Forbidden|The requester has insufficient permissions to perform the action or authorization information is missing from the request. Check that you provide a valid OAuth2 `Authorization` header.|
|404|Not Found|The requested end-point was not found or is not known.|
|409|Conflict|The resource you requested is stale or an older version. [TODO not clear what this means]|
|500|Internal Server Error|Something went wrong on the server when processing your request. Try to include the `x-supportcode` header content if you wish to submit a support request.|

The response type for all end-points that return data will be JSON (`application/json`).

#### Resources

This end-point can be used to manage metadata for resources that you own or have access to.

|Action|Method|Description|
|:-----|:----:|:----------|
|`/resources`|`GET`, `POST`|Get metadata about all resources you have access to or update metadatada about a specific resource.|
|`/resources/{id}`|`GET`|Get metadata about a specific resource.|
|`/global-tags`|`GET`, `POST`|Get all global tags or create new global tags.|
|`/global-tags/{id}`|`PUT`, `DELETE`|Update or delete specific tags.|

##### `/resources`

Using `GET` will return information about all resources you currently have access to

Using `POST` along with body data updates metadata about a specific resource.

Request format (* required):
```
{
  resourceId:	string *($uuid) Resource Id
  title:	string * Resource title
  description:	string * Resource description
  icon:	Icon{
    id:	string * Pick ID from the Icons id list below
    backgroundColor:	string * default: 'Blue' The background color of the svg icon (choose from list below).
  }
  tags:	[Tag{
    title:	string *
    tag title.
    type:	string *
    default: personal
    Tag type Enum: [ global, personal ]
  }] *
}

Icons: 
  Automatic_Information_Display,
  Dangerous_Cargo,
  Fairplay,
  Operational_Vessel_Data,
  Statistics_Of_Accidents,
  Wave,
  Wind

Colors: 
  { name: 'Cyan', hex: ‘#009fda’ },
  { name: 'Green', hex: ‘#36842d’ },
  { name: 'Blue', hex: ‘#003591’ },
  { name: 'Violet', hex: ‘#6e5091’ },
  { name: 'Red', hex: ‘#c4262e’ },
  { name: 'Orange', hex: ‘#e98300’ },
  { name: 'Yellow', hex: ‘#fecb00’ },
  { name: 'Grey', hex: ‘#988f86’ }
```

Response format `application/json`:

```
[
  ResourceMetadata{
    resourceUrl:	string ($url)
    resourceRegion:	string
    keyExpired:	boolean
    resourceId:	string *($uuid)
    Resource Id

    isOwner:	boolean
    keyAvailable:	boolean
    autoRefreshed:	boolean
    ownerId:	string ($uuid)
    title:	string *
    Resource title

    tags:	[...]*
    icon:	Icon{
      id:	string *
      backgroundColor:	string *
    }
    activeKey:	boolean
    resourceName:	string
    description:	string *
    Resource description

    lastModified:	string ($dateTime)
  },
  ...
]
```

##### `/resources/{resourceId}`

Returns information on the specific resource. To update a resource with information use `POST` the endpoint `/resources` with a body containing the changes as well as the id of the resource you wish to update.

Response format `application/json`:

```
ResourceMetadata{
  resourceUrl:	string ($url)
  resourceRegion:	string
  keyExpired:	boolean
  resourceId:	string *($uuid)
  Resource Id

  isOwner:	boolean
  keyAvailable:	boolean
  autoRefreshed:	boolean
  ownerId:	string ($uuid)
  title:	string *
  Resource title

  tags:	[...]*
  icon:	Icon{
    id:	string *
    backgroundColor:	string *
  }
  activeKey:	boolean
  resourceName:	string
  description:	string *
  Resource description

  lastModified:	string ($dateTime)
}
```

##### `/global-tags`

Using `GET` will return all global tags.

Using `POST` along with body data adds a new tag. The id of the tag is automatically generated.

Request format (* required):
```
{
  title:	string *
}
```

Response format `application/json`:

```
[
  {
    id:	string ($uuid)
    title:  string
  }
]
```

##### `/global-tags/{globalTagId}`

Using `PUT` updates a specific tag

Using `DELETE` removes a specific tag

Request format (* required):
```
{
  title:	string *
}
```

#### Global tags



## Tutorial
Veracity uses API Management. In order to get access, you will need to:
- Register at [https://api-portal.veracity.com/](https://api-portal.veracity.com/)
- Subscribe to the Veracity Platform API – Product, this will give you access to our DataAPI and ProvisionAPI with a subscription ID

NB! The endpoint URLs might be changed/refactored during public preview period to further enhance the developer experience. We will try to inform users of the API before such changes take place.

### Standard structure of API Call

#### Call header:
- **Ocp-Apim-Subscription-Key** - this header attribute is for API Management authentication
- **Authorization** - this header attribute needs to contain the Bearer Token that is received through authorization on Veracity

#### Query parameters:
Depending on end-point

#### Authorization snippet (for developers)
You need to authorize Veracity with code and copy the Bearer Token to your requests (which we will provide more info on later). Swagger UI can be used for now. The Bearer Token is usually valid for one hour, after that you need to request a new one.

It's best practice to always get a new token before a request. 

```ps
curl -v -X GET "https://api.dnvgl.com/platform/Mydata/api/resources?shared={boolean}&owned={boolean}"
-H "Ocp-Apim-Subscription-Key: {subscription key}"
-H "Authorization: Bearer {token}"
```

### Azure Active Directory (AD) B2C
To acquire the Bearer Token needed for API requests it is possible to authenticate with the code below. It's important to register any new app in the Azure Active Directory as a Native App. 
This App ID, together with the tenant name from Azure AD will be used to obtain an authentication key.

The below code in .NET shows how to programmatically get the Bearer Key. This code is also available [here](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-veracity-api/veracity-api-net).

Firstly, input data is required:

```ps
Tenant - tenant name from Azure Portal (Active Directory)
ClientId - Application ID from your Native app registration
PolicySignUpSignIn - sign in policy created during app registration
ApiScopes - scopes available for given api
```
For user identification we use the class PublicClientApplication which is available in the namespace Microsoft.Identity.Client.
You can include it as a NuGet package, currently in preview mode.
```csharp
public static PublicClientApplication PublicClientApp { get; } =
  new PublicClientApplication(ClientId, Authority, TokenCacheHelper.GetUserCache());
```


The Authority field is the following URL, where {tenant} and {policy} are replaced with proper values from the app registration.:
```
"https://login.microsoftonline.com/tfp/{tenant}/{policy}/oauth2/v2.0/authorize";
```

To sign in, the AcquireTokenAsync method from PublicClientApplication is used.
```csharp
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

### Data API
The Veracity Data Platform DataAPI is an API where developers and applications can get information on data containers and get their key to a data container or share a key with another Veracity Data Platform user.

Implementations:
- [.NET implementation](#net-implementation)


#### .NET implementation
The below sample assumes that the user has a Subscription Key from the Veracity Portal and a Bearer Key. For now the Bearer Key can be obtained from Swagger UI, as described in the previous section. You also need to know the URI to the Data API service.

We are going to access the Data API service via http requests and in our implementation we will use HttpClient from System.Net.Http.
Below each GET and POST request implementation available in the API is described.

##### GET current user

Based on Subscription Key and Bearer Key you can ask DataApi service for current user data.

```csharp
public async Task<Tuple<string, User>> RequestCurrentUser()
{
  var uri = $"{_baseDataApiUrl}users/me?";

  var response = await _httpClient.GetAsync(uri);
  var responseContent = await response.Content.ReadAsStringAsync();
  return response.IsSuccessStatusCode
    ? new Tuple<string, User>("", JsonConvert.DeserializeObject<User>(responseContent))
    : new Tuple<string, User>(responseContent, null);
}
```

Notice the URL that was additionally to the base address provided by user has an additional path to users.
As a result of the method you get a tuple containing a string message and an object model deserialized from the Json response.
The string message is empty if the operation was successful. If the operation failed, there is an error message. The Json object model for the User is represented by the below class.

```csharp
public class User
{
  public string UserId { get; set; }
  public string CompanyId { get; set; }
  public string Role { get; set; }
}
```
In this way we can get the ID for the current user used in other API requests. We also receive a company ID that the user is assigned to, as well as the role of the current user.

##### GET user

If you have the user ID you can ask the Data API service for other information about that user.

```csharp
public async Task<Tuple<string, User>> RequestUser(string userId)
{
  var uri = $"{_baseDataApiUrl}users/{userId}";

  var response = await _httpClient.GetAsync(uri);
  var responseContent = await response.Content.ReadAsStringAsync();
  return response.IsSuccessStatusCode
    ? new Tuple<string, User>("", JsonConvert.DeserializeObject<User>(responseContent))
    : new Tuple<string, User>(responseContent, null);
}
```

As a result from this method you get a tuple containing a string message and an object model deserialized from the Json response.
The string message is empty if the operation was successful. If the operation failed, there is an error message. The response Json is similar to that of the previous example.

##### GET company
If you have the company ID you can ask the Data API for other information about the corresponding company.

```csharp
public async Task<Tuple<string, Company>> RequestCompany(string companyId)
{
  var uri = $"{_baseDataApiUrl}companies/{companyId}";

  var response = await _httpClient.GetAsync(uri);
  var responseContent = await response.Content.ReadAsStringAsync();
  return response.IsSuccessStatusCode
    ? new Tuple<string, Company>("", JsonConvert.DeserializeObject<Company>(responseContent))
    : new Tuple<string, Company>(responseContent, null);
}
```

As a result from this method you get a tuple containing a string message and an object model deserialized from the Json response.
The string message is empty if the operation was successful. If the operation failed, there is an error message. The resulting object model from the Json response is as below.

```csharp
public class Company
{
  public string CompanyId { get; set; }
  public string AzureId { get; set; }
}
```

##### GET Key Templates
This method returns the template for different types of key that you can generate. Blob Storage is the only storage type supported at the moment.
Supported access types for Blob Storage are as follows:
1. Write key
2. Read and list key
3. Read, write and list key
4. Read, write, delete and list key

```csharp
public async Task<Tuple<string, List<StorageKeyTemplate>>> RequestStorageKeyTemplates()
{
  var uri = $"{_baseDataApiUrl}keytemplates";

  var response = await _httpClient.GetAsync(uri);
  var responseContent = await response.Content.ReadAsStringAsync();
  return response.IsSuccessStatusCode
    ? new Tuple<string, List<StorageKeyTemplate>>("", JsonConvert.DeserializeObject<List<StorageKeyTemplate>>(responseContent))
    : new Tuple<string, List<StorageKeyTemplate>>(responseContent, null);
}
```

From the method you get a tuple containing a string message and an object model deserialized from the Json response.
The string message is empty if the operation was successful. If the operation failed, there is an error message.
The resulting Json is represented by an object model, like below.

```csharp
public class StorageKeyTemplate
{
  public string Id { get; set; }
  public string Name { get; set; }
  public int TotalHours { get; set; }
  public bool IsSystemKey { get; set; }
  public string Description { get; set; }
  public bool Attribute1 { get; set; }
  public bool Attribute2 { get; set; }
  public bool Attribute3 { get; set; }
  public bool Attribute4 { get; set; }
}
```

From the description property you know what the rights of the key template are.

##### GET Resources
Every user has the possibility to store their data in resources within the Veracity platform. Use this API request to list the resources that are owned or shared by the user.

```csharp
public async Task<Tuple<string, Resources>> RequestAllResources(bool shared, bool owned)
{
  var queryString = HttpUtility.ParseQueryString(string.Empty);
  queryString["shared"] = shared.ToString();
  queryString["owned"] = owned.ToString();

  var uri = $"{_baseDataApiUrl}resources?{queryString}";

  var response = await _httpClient.GetAsync(uri);
  var responseContent = await response.Content.ReadAsStringAsync();
  return response.IsSuccessStatusCode
    ? new Tuple<string, Resources>("", JsonConvert.DeserializeObject<Resources>(responseContent))
    : new Tuple<string, Resources>(responseContent, null);
}
```

The input parameters are two bool properties in which you can specify if you want to list owned or shared resources.
The result from this method is a tuple containing a string message and an object model deserialized from the Json response. The string message is empty if the operation was successful. If the operation failed, there is an error message.
Successful output from the method consists of two collections of resources in an object model like below.

```csharp
public class Resources
{
  public List<Resource> OwnedResources { get; set; }
  public List<SharedResource> SharedResources { get; set; }
}
public class Resource
{
  public string ResourceId { get; set; }
  public string ResourceName { get; set; }
  public string ResourceUrl { get; set; }
  public string LastModifiedUTC { get; set; }
  public string OwnerId { get; set; }
  public string ConsumerName { get; set; }
  public string ResourceType { get; set; }
}
public class SharedResource
{
  public Resource StorageItem { get; set; }
  public string AccessDescription { get; set; }
  public bool AccessKeyCreated { get; set; }
  public string AccessKeyEndDateUTC { get; set; }
  public string AccessKeyTemplateId { get; set; }
  public string AccessSharingId { get; set; }
  public bool AutoRefreshed { get; set; }
}
```

##### GET Accesses for resource

With this query you can get all accesses provided for a given resource.

```csharp
public async Task<Tuple<string, Accesses>> RequestAccesses(string resourceId, int pageNo, int pageSize)
{
  var queryString = HttpUtility.ParseQueryString(string.Empty);
  queryString["pageNo"] = pageNo.ToString();
  queryString["pageSize"] = pageSize.ToString();

  var uri = $"{_baseDataApiUrl}resources/{resourceId}/accesses?" + queryString;

  var response = await _httpClient.GetAsync(uri);
  var responseContent = await response.Content.ReadAsStringAsync();
  return response.IsSuccessStatusCode
    ? new Tuple<string, Accesses>("", JsonConvert.DeserializeObject<Accesses>(responseContent))
    : new Tuple<string, Accesses>(responseContent, null);
}
```

As input arguments, next to the resourceId that you are interested in, specify the page number and page size (if you expect to have a lot of results).
As a result of the method you get a tuple containing a string message and an object model deserialized from the Json response.
A string message is empty if the operation was successful. If the operation failed, there is an error message.
The resulting Json is like below.

```csharp
public class Accesses
{
  public List<Access> Results { get; set; }
  public int Page { get; set; }
  public int ResultsPerPage { get; set; }
  public int TotalPages { get; set; }
  public int TotalResults { get; set; }
}
public class Access
{
  public string ProviderEmail { get; set; }
  public string UserId { get; set; }
  public string OwnerId { get; set; }
  public string AccessSharingId { get; set; }
  public bool KeyCreated { get; set; }
  public bool AutoRefreshed { get; set; }
  public string KeyCreatedTimeUTC { get; set; }
  public string KeyExpiryTimeUTC { get; set; }
  public string ResourceType { get; set; }
  public int AccessHours { get; set; }
  public string AccessKeyTemplateId { get; set; }
  public bool Attribute1 { get; set; }
  public bool Attribute2 { get; set; }
  public bool Attribute3 { get; set; }
  public bool Attribute4 { get; set; }
  public string ResourceId { get; set; }
}
```

##### POST Share Access

If you want to share access to a specific resource with other users you can use this post request.

```csharp
public async Task<Tuple<string, ShareAccessResponse>> ShareAccess(string resourceId, bool autoRefreshed,
  string userToShareId, string shareTemplateId)
{
  var uri = $"{_baseDataApiUrl}resources/{resourceId}/accesses?autoRefreshed={autoRefreshed}";
  var body = JsonConvert.SerializeObject(new { UserId = userToShareId, AccessKeyTemplateId = shareTemplateId });

  var response = await _httpClient.PostAsync(uri, new StringContent(body, Encoding.UTF8, "application/json"));
  var responseContent = await response.Content.ReadAsStringAsync();
  return response.IsSuccessStatusCode
    ? new Tuple<string, ShareAccessResponse>("", JsonConvert.DeserializeObject<ShareAccessResponse>(responseContent))
    : new Tuple<string, ShareAccessResponse>(responseContent, null);
}
```

It's important to note that in addition to the defined URL, you need to send Json content with the resource ID that you want to share and the user id of whom you want to share the resource with. Also needed is the shared template id describing what access type the user will have to your resource.
The shared template ID can be obtained by executing the RequestStorageKeyTemplates method and choosing the key that fits best to your needs. As a result of the method we get a tuple containing a string message and an object model deserialized from the Json response. The string message is empty if the operation was successful. If the operation failed, there is an error message.
As result we get the access sharing ID.

```csharp
public class ShareAccessResponse
{
  public string AccessSharingId { get; set; }
}
```

##### GET Fetch Key for storage container

To get access to a storage container you need to get a SAS token. You can execute the below method giving access using the sharing id from the previous step as an input parameter.

```csharp
public async Task<Tuple<string, SasData>> FetchKeyForStorageContainer(string resourceId, string accessSharingId)
{
  var uri = $"{_baseDataApiUrl}resources/{resourceId}/keys?accessSharingId={accessSharingId}";

  var response = await _httpClient.GetAsync(uri);
  var responseContent = await response.Content.ReadAsStringAsync();
  return response.IsSuccessStatusCode
    ? new Tuple<string, SasData>("", JsonConvert.DeserializeObject<SasData>(responseContent))
    : new Tuple<string, SasData>(responseContent, null);
} 
```

As a result of the method we get a tuple containing a string message and an object model deserialized from the Json response. The string message is empty if the operation was successful. If the operation failed, there is an error message.
The resulting Json is like below.

```csharp
public class SasData
{
  public string SasKey { get; set; }
  public string SasUri { get; set; }
  public string FillKey { get; set; }
  public string SasKeyExpiryTimeUTC { get; set; }
  public bool IsKeyExpired { get; set; }
  public bool AutoRefreshed { get; set; }
}
```

The object model contains the SAS URI and SAS key that give us access to a specified resource.


### Provision API
The Veracity Data Platform ProvisioningAPI is an API where developers and applications can create data containers.

Implementations:
- [.NET implementation](#provisionapi-net-implementation)


#### ProvisionAPI .NET implementation
The below sample assumes that the user has a Subscription Key from the Veracity Portal, as well as a Bearer Key. For now, the Bearer Key can be obtained from the Swagger UI. User must also know the URI to Data API service.

We are going to access the Provision API service via http requests and in our implementation we will use HttpClient from System.Net.Http.

##### POST ProvisionContainer
Whilst having a Subscription Key and a Bearer Key for authentication, the user is able to provision a data container.
You are required to choose a storage location from these available options:
1. Unknown,
2. NorthEurope,
3. EastUs1

You can also specify the container name, but this parameter is optional.

```csharp
public async Task<string> ProvisionContainer(StorageLocations storageLocation, string containerShortName = null)
{
  var queryString = HttpUtility.ParseQueryString(string.Empty);
  if(!string.IsNullOrEmpty(containerShortName))
    queryString["containerShortName"] = containerShortName;

  var requestCode = Guid.NewGuid().ToString();

  var uri = $"{_baseProvisioningApiUrl}container?storageLocation={storageLocation}&requestCode={requestCode}&{queryString}";
  var body = JsonConvert.SerializeObject(new { StorageLocation = storageLocation.ToString(), RequestCode = requestCode, ContainerShortName = containerShortName });

  var response = await _httpClient.PostAsync(uri, new StringContent(body, Encoding.UTF8, "application/json"));
  var responseContent = await response.Content.ReadAsStringAsync();
  return response.IsSuccessStatusCode ? response.ReasonPhrase : responseContent;
}
```

It is important that in addition to the URL parameters, the user needs to create a Json with these same parameters and send this Json request.
As a result, we expect to get string information about the success or failure of our operation.
The provisioning of the container can take up to 10 minutes, this means there is a time delay needed between requesting a container and performing operations on that container.

### Metadata API




## GitHub  
Follow our open projects related to Veracity data fabric API on https://github.com/veracity

## Stack Overflow
Stack Overflow is the largest, most trusted online community for developers to learn and share their programming knowledge. The Veracity developer team monitor Stack Overflow forum posts that include the tag Veracity Platform.

[Visit Stack Overflow](https://stackoverflow.com/questions/tagged/veracity+platform?mode=all)
