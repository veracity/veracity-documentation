# Overview
This Veracity API's enable data providers and consumers to interact with veracity programatically.  

# API Reference
- Some reference...


# Tutorial
Veracity uses API Management. In order to get access, you will need to do the following two steps:
- You need to register at [https://api-portal.dnvgl.com/](https://api-portal.dnvgl.com/)
- Subscribe to the Veracity Platform API – Product, this will give you access to our DataAPI and ProvisionAPI with a subscription ID

NB! The endpoint URLs might be changed/refactored during private preview period to further enhance the developer experience. We will try to inform users of the API before such changes take place.


## Standard structure of API Call

### Call header:
- **Ocp-Apim-Subscription-Key** - this header attribute is for authentication to API Management
- **Authorization** this header attribute needs to contain the Bearer Token gotten through atuhorization on Veracity

### Query parameters:
Depeding on end-point

### Authorization snippet (for developer)
You need to authorize to Veracity with code and copy the Bearer Token to your requests (we will provide later). Swagger UI can be used for now. Bearer token is usually valid for one hour, after that you need to request a new.

Best practice to always get a new token before a request. 

```
curl -v -X GET "https://api.dnvgl.com/platform/Mydata/api/resources?shared={boolean}&owned={boolean}"
-H "Ocp-Apim-Subscription-Key: {subscription key}"
-H "Authorization: Bearer {token}"
```


## Data API
The Veracity Data Platform DataAPI is an API where developers and applications can get information on data containers, get their key to a data container or share a key with another Veracity Data Platform user.

Implementations:
- [.NET implementation](#net-implementation)


### .NET implementation
Below sample assumes that user have Subscription Key from Veracity Portal and Bearer Key. As for now Bearer Key can be obtained from Swagger UI.
User also needs to know Uri to Data Api service.

We are going to access Data Api service via http requests and in implementation we will use HttpClient from System.Net.Http.
Below each GET and POST request implementation available in API is described.

#### GET current user
Based on Subscription Key and Bearer Key we can ask DataApi service for current user data.
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
Notice Url that additionally to base address provided by user has additional path to users.
As a result from method we get Tuple containing string message and Object Model deserialized from Json response.
String message is empty if operation is successful. If operation failed, there is error message.
Json object model for User is represented by below class.
```csharp
public class User
{
    public string UserId { get; set; }
    public string CompanyId { get; set; }
    public string Role { get; set; }
}
```
So in that way we can get ID for the current user used in other Api requests. We recieve also company ID that user is assigned to and Role of the current user.

#### GET user
If we have user ID we can ask Data Api service for other info about that user.
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
As a result from method we get Tuple containing string message and Object Model deserialized from Json response.
String message is empty if operation is successful. If operation failed, there is error message.
Response Json is similar to one in previous example.

#### GET company
If we have company ID we can ask Data Api for other info about that company.
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
As a result from method we get Tuple containing string message and Object Model deserialized from Json response.
String message is empty if operation is successful. If operation failed, there is error message.
Result object model from Json response is like below.
```csharp
public class Company
{
    public string CompanyId { get; set; }
    public string AzureId { get; set; }
}
```
#### GET Key Templates
Returns the template for the different types of keys you can generate. Blob Storage is the only storage type supported at the moment.
Supported access types for the Blob Storage types are as follows:
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
As a result from method we get Tuple containing string message and Object Model deserialized from Json response.
String message is empty if operation is successful. If operation failed, there is error message.
Result Json is represented by object model like below.
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
From the description property we are able to know what kind of right this key template provides.

#### GET Resources
Every user has possibility to store his data in resources within Veracity platform. To list resources that are owned or shared by the user this Api request is to be used.
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
As input parameters we have two bool properties. We can specify if want to list only owned resources or maybe shared resources as well.
As a result from method we get Tuple containing string message and Object Model deserialized from Json response.
String message is empty if operation is successful. If operation failed, there is error message.
Successful output from method are two collections of resources, in object model like below.
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
#### GET Accesses for resource
With this query we can get all accesses provided for given resource.
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
As input arguments, next to resourceId that we are interested in, we specify also page number and page size if we expect to have a lot of results.
As a result from method we get Tuple containing string message and Object Model deserialized from Json response.
String message is empty if operation is successful. If operation failed, there is error message.
Result Json is like below.
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
#### POST Share Access
If we want to share access to specific resource with other user we can use this POST request.
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
Important here is that adiitionally to defined Url we need to send Json content with resource id that we want to share, user id that we want to share resource with and share template id saying what access type user will have to your resource.
Share template id you can obtain executing RequestStorageKeyTemplates method and choosing one that fits best.
As a result from method we get Tuple containing string message and Object Model deserialized from Json response.
String message is empty if operation is successful. If operation failed, there is error message.
As result we get access sharing id.
```csharp
public class ShareAccessResponse
{
    public string AccessSharingId { get; set; }
}
```
#### GET Fetch Key for storage container
To get access to storage container, so get SAS token we execute below method giving access shaing id from previous step as input parameter.
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
As a result from method we get Tuple containing string message and Object Model deserialized from Json response.
String message is empty if operation is successful. If operation failed, there is error message.
Result Json is like below.
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
Object model contains SAS uri and SAS key that gives us access to specified resource.

## Provision API

## Metadata API


# Pattern & Practices 
In this section we will give theoretical and practical recommendations on how to best develop, design and implement your service 
 
# References 

# GitHub  
Follow our open projects related to veracity API on https://github.com/veracity

# Stack Overflow
Stack Overflow is the largest, most trusted online community for developers to learn, share​ ​their programming ​knowledge. The Veracity developer team monitor Stack Overflow forumposts that include the tag Veracity
 
[Visit Stack Oerflow](https://stackoverflow.com/questions/tagged/veracity?mode=all)


 
# Video 
Some text

 
# Resources  
In this section we have added resources that may provide you with additional learning.  


 
# FAQ 
Some text 
 
# Price model 
Some text
 
