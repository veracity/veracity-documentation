---
author: Veracity
description: Description of quick start section
---

# Data fabric Quick start

This is a quick start on how to use the Data Fabrics API. This guide will cover two scenario's:

1. [Scenario 1 - Creation and sharing](#scenario-1---creation-and-sharing)
    - [Create container](#create-container)
    - [Create a key for your self](#create-a-key-for-your-self)
    - [Push Data to your new container](#push-data-to-your-new-container)
    - [Share key to another user.](#share-key-to-another-user)
1. [Scenario 2 - Read data from container](#scenario-2---read-data-from-container)
    - [Find Resource](#find-resource)
    - [Claim key and read content](#claim-key-and-read-content)

Models used in the demo's:
- [Models](#models)


The Veracity Data Platform uses to APIs:
- **Data API**
  - Get information on containers, get access keys to containers and share access to other Veracity users.
- **Provisioning API**
  - Provision new containers and update the meta data of a container.


## .NET implementation

The below sample assumes that the user has a Subscription Key from the Veracity Portal.

We are going to access the Data API service via http requests and in our implementation we will use a custom HttpClient based on from System.Net.Http.

This example requires:
* [Newtonsoft.Json](https://www.nuget.org/packages/Newtonsoft.Json/)
* [WindowsAzure.Storage](https://www.nuget.org/packages/WindowsAzure.Storage/9.3.2)

We will also reuse the authentication code (for application) from [here](https://developer.veracity.com/doc/data-fabric-api#Authorization-snippet)

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

To view all classes/models used, see here

## Scenario 1 - Creation and sharing

A prerequisite for this scenario is an already registered AAD application (you can also [use User authentication](https://developer.veracity.com/doc/data-fabric-api#User))

I will recommend you create a new blank Console program, to follow the examples

This fist scenario will cover:
* Authenticate (with an application)
* Create container
* Create a key for your self
* Push Data to your new container
* Share key to another user.

Authenticate (with an application)

The code below will authenticate the application and return a instance of "Token". The token will contain "AccessToken", this access token can later be used to do authenticated calls to the Data fabric apis.

Replace the values of:
* {clientId}
* {clientSecret}
* {Data fabric resource url}
* {tenantId}

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
### Create container

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

### Create a key for your self

After your container is created, it's time to give yourself access to the container.

Replace the {resourceId} with container id from last step

To see what each attribute of a key template is, read more here

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

### Push Data to your new container

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
### Share key to another user.

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

## Scenario 2 - Read data from container

This seccond scenario will continue and build upon the steps from the first scenario.

This scenario will cover:
* Find Resource
* Claim key and read content

### Find Resource

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
### Claim key and read content
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

### Models

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