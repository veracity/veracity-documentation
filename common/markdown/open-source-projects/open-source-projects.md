# Overview 

This guide will describe in details Veracity open source projects. Each of them is small piece of code providing useful functionality within Veracity platform. To proceed, you need to have Azure subscription.

Links to content

- [Markdown parser tool](#markdown-parser-tool)
- [Machine Learning automation](#machine-learning-automation)

# Markdown parser tool
When preparing documentation, we base on GitHub and markdown files (.md) where we put all documentation data. With that approach, we can easily maintain the data and have full control over the workflow. On the other hand, it’s not convenient for external users to go through repository when looking at documentation.
That's why there is a tool which can easily translate .md format to HTML syntax consumed by web browser. 
Thanks to this translation and extraction of additional metadata we can provide user friendly and intuitive documentation which is easy to read and navigate.
The following code description applies to the .NET implementation as it is the base platform used for that tool.

## Implementation and usage
Markdown parser tool is designed as a fully automatic module that is executed every time Documentation repository on GitHub is updated. So, there is no need for user input other than adding or updating documentation.
To achieve that goal, we need to setup and deploy a service that will be able to track repository changes and execute appropriately providing a piece of data which can be easily interpreted by web browser at the end.
Instead of setting up whole service with all infrastructure and management concerns we decided to use completely serverless approach called Azure Functions. It’s a solution for running pieces of code in the cloud where we pay only for the time the code runs and trust Azure to scale as needed.
Source code is available [here](https://github.com/veracity/MarkdownParser).

### Markdown parser Azure Function
Azure Functions among many great functionalities provides templates to get started with key scenarios. One of scenarios is called GitHub webhook.
This template executes our "piece of code" every time event occur in GitHub repositories. Its perfect scenario for us. We wait with our Azure Function until a user makes a change in repository, then GitHub sends an event with data about the change and thanks to webhook Azure executes our Function. And we pay only for that execution, not for idle time between repository updates.
More details about Azure Functions and other templates can be found [here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview)


Every Function contains a method called Run. This is an entry point executed by trigger from GitHub webhook:
```csharp
public static async Task<HttpResponseMessage> Run([HttpTrigger(WebHookType = "github")] HttpRequestMessage req,
    Binder binder, TraceWriter log)
{
	log.Info("C# HTTP trigger function processed a request.");
	dynamic data = await req.Content.ReadAsAsync<object>();
	var result = await ProcessCommitAsync(data, binder, log);
	return result
    ? req.CreateResponse(HttpStatusCode.OK)
    : req.CreateErrorResponse(HttpStatusCode.NoContent, "error.");
}
```

Inside the method we can distinguish three parts. 
- Read input request - handled by Azure Function, asynchronous reading of data
- Process request - extract needed data from request, process it in Markdown parser
- Return HTTP response based on status from Markdown parser

### Preparing request for parser

To read input request properly we need to know data structure of the request. As the data comes from GitHub, there we can find how sample webhook payload looks like.
Here is [link](https://developer.github.com/v3/activity/events/types/#pushevent) to GitHub documentation and below small description of key points.

When listening for push event, we expect to get information about current commit. Especially we are interested in what files are added/updated/deleted. If any of them will be .md file, we need to process it.

Sample payload for push event:
```json
{
  "head_commit": {
    "id": "0d1a26e67d8f5eaf1f6ba5c57fc3c7d91ac0fd1c",
  },
  "repository": {
    "id": 35129377,
    "default_branch": "master"
  }
}
```
```json
{
  "head_commit": {
    "id": "0d1a26e67d8f5eaf1f6ba5c57fc3c7d91ac0fd1c",
  },
  "repository": {
    "id": 35129377,
    "default_branch": "master"
  }
}
```

Processing method in our Azure Function:

```csharp
private static async Task<bool> ProcessCommitAsync(dynamic data, Binder binder, TraceWriter log)
{
    var repositoryId = (long) data.repository.id;
    var branch = (string) data.repository.default_branch;
    var commitId = (string) data.head_commit.id;
    var mdFiles = await GetAllMdFilesTask("MarkdownParser", repositoryId, branch, commitId, log);
    var jsonFiles = PrepareJsonData(mdFiles, log);
    return await WriteJsonFilesToFileShareTask(jsonFiles, log);
}
```

As you can see we expect data like repository id and branch name for accessing correct place in Git repository. Also, we expect commit id.
All of this are needed to get .md files included in commit that triggered this webhook event.

### Ask GitHub API for changes in commit

Having above data we are ready to ask GitHub API for data that we are interested in. To achieve that we use a wrapper called [Octokit](https://github.com/octokit/octokit.net) available as NuGet package.

```csharp
public static async Task<List<Tuple<string, string>>> GetAllMdFilesTask(string appName, long repositoryId,
    string branchName, string commitId, TraceWriter log)
{
	.
	.
	var github = new Octokit.GitHubClient(new Octokit.ProductHeaderValue(appName));
	var commit = await github.Repository.Commit.Get(repositoryId, commitId);
	foreach (var file in commit.Files)
	{
	 // if file is md, read its content and put in result collection.
	}
}
```
You can see that as return object we expect collection of Tuples where Item1 in tuple is md file name and Item2 is md file content.

appName in this case is "MarkdownParser" which is name of our repository.

The code inside foreach loop checks if file has status set to "modified" or "added", in that case reads the content of that file with:
```csharp
var contents =
    await github.Repository.Content.GetAllContentsByRef(repositoryId, file.Filename,
        branchName);
```

And adds it to return collection. If file has status other than "modified" or "added" its considered as deleted. So, there is no way to read its content.
But we need to track those changes also, so we put entry in return collection as well. Just with empty string as content.

With data prepared like this we can execute core code of Markdown parser.

### Markdown parser core

In Markdown parser code, we are interested only in md file content. Input collection of Tuples in method PrepareJsonData is used only for creating similar output.
With a difference that output Tuple Item1 is name of produced json file and Item2 is json content.
When input tuple item2 is empty (because file was deleted), output tuple Item2 will also we empty but still there will be entry in output collection.
```csharp
public static List<Tuple<string, string>> PrepareJsonData(List<Tuple<string, string>> mdFiles,
    TraceWriter log)
{
	.
	.
	foreach (var mdFile in mdFiles)
	{
		var mdParser = new MarkdownParser.MarkdownParser();
		var jsonText = mdParser.CreateJson(mdFile.Item2);
		jsonList.Add(new Tuple<string, string>($"{mdFile.Item1}.json", jsonText));
	}
	.
	.
}
```

As a result for JSON serialization we expect object of type MarkdownData.

```csharp
public class MarkdownData
{
    public string Title { get; set; } = string.Empty; // to be used later
    public string HtmlString { get; set; }
    public List<Header> HeaderData { get; set; }
}
```
HtmlString is a properly formatted HTML web page created based on .md input.
HeaderData is a metadata extracted from .md input defining tree structure of headers. Its used for menu creation.

For pure HTML generation [Markdig](https://github.com/lunet-io/markdig) library is used. As one of middle steps it produces nice object model which is used by us for Headers tree structure generation.

The Markdig library is used as follows:
```csharp
using (var writer = new StringWriter())
{
    var builder = new MarkdownPipelineBuilder();
    builder.UseAutoIdentifiers();
    builder.UseFigures();
    builder.UseCustomCodeBlockExtension();
    document = Markdown.ToHtml(mdFileContent, writer, builder.Build());
    htmlString = writer.ToString();
}
```
UseAutoIdentifiers enables adding ids for headers. 

UseFigures enables usage of Figures statements.

UseCustomCodeBlockExtension is an extension written by us to replace default html code blob renderer with our own. 
This approach gives great possibilities for html syntax modifications for specified part of .md files, in this case parts with code samples.

As Markdig object model does not provide hierarchical object grouping like tree model, when extracting Headers there was need to write custom code.
```csharp
private void CreateTree(IEnumerable<HeadingBlock> headingBlocks, HeaderData root)
{
	// loop heading blocks and put them in hierarhical tree.
}
```

Markdig object model provides a collection of header objects of type HeadingBlock. They are all on the same level but in .md files we can deal with nested headers like:
```csharp
# 1. Main Header
	## 1.1. Nested Header
		### 1.1.1. Nested Header of Nested Header
# 2. Second Main Header
```
And so on.

So, in CreateTree method we look at every header and try to assign it to proper branch of our Header Tree structure.

### JSON serialization

When Markdown Data object is prepared, we need to serialize it into JSON format. We use standard JSON serialization library from [Newtonsoft](https://www.newtonsoft.com/json)

Here is the usage:
```csharp
private string ConvertToJson(MarkdownData data)
{
    return JsonConvert.SerializeObject(data, Formatting.Indented, new JsonSerializerSettings
    {
        ReferenceLoopHandling = ReferenceLoopHandling.Serialize,
        PreserveReferencesHandling = PreserveReferencesHandling.None
    });
}
```

In ProcessCommitAsync method there is one more step to do:
```csharp
return await WriteJsonFilesToFileShareTask(jsonFiles, log);
```

We need to store our new json files somewhere. We decided to choose Azure File Shares. There is a FileShare created only for this data.

The core of method is like this:
```csharp
var storageAccount = CloudStorageAccount.Parse(GetEnvironmentVariable("AzureWebJobsStorage"));
var fileClient = storageAccount.CreateCloudFileClient();
var share = fileClient.GetShareReference(GetEnvironmentVariable("OutputFileShareName"));

foreach (var json in jsonData)
{
    var sourceFile = share.GetRootDirectoryReference().GetFileReference(json.Item1);
    if (string.IsNullOrEmpty(json.Item2)) // when content is empty we should delete blob.
    {
        if (sourceFile.Exists())
            await sourceFile.DeleteAsync();
    }
    else
    {
        sourceFile.Properties.ContentType = "application/json; charset=utf-8";
        sourceFile.UploadText(json.Item2, Encoding.UTF8);
    }
}
```

There is also solution based on Azure Blobs which is not used but can be easly switched on.
```csharp
foreach (var json in jsonData)
{
    if (string.IsNullOrEmpty(json.Item2)) // when content is empty we should delete blob.
    {
        var blob =
            await binder.BindAsync<CloudBlockBlob>(new BlobAttribute($"json-container/{json.Item1}"));
        blob.Delete();
    }
    else
    {
        var blob =
            await binder.BindAsync<CloudBlockBlob>(new BlobAttribute($"json-container/{json.Item1}"));
        blob.Properties.ContentType = "application/json; charset=utf-8";
        blob.UploadText(json.Item2, Encoding.UTF8);
    }
}
```

You can see that if there is no content in Tuple Item2 file is considered as deleted so we delete it from container as well.
And if content is resent, we write it to blob names from Tuple Item1.

You can see here a "binder" object. It comes from the very start from "Run" method. And it's used for [imperative bindings](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-csharp#imperative-bindings).
Very short, Azure Functions in general use declarative bindings. So you define inputs and outputs when defining Function itself.
Here we don't have this possibility because we don't know blob name at this point. 
For more details about imperative binding click [here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-csharp#imperative-bindings).


# Machine Learning automation
When considering data quality, we deal a lot with concept of Machine Learning. Thanks to advanced algorithms we can go through user data, test it against a number of metrics and provide different data transformations. Additionally, we can draw conclusions not visible at first glance.
Microsoft provides a platform called Azure Machine Learning. Undeniable advantage of AML is that it exists in Azure environment so it is put as close to user data as possible. And it provides easy to use API for managing this data.
In this solution, we are trying to provide code samples about how we can automate parts of Machine Learning workflow.
In particular we are focusing on consuming and retraining AML Web Service with usage of Azure Functions. 
The following code description applies to the .NET implementation as it is the base platform used for that tool.

## Implementation and usage
Solution contains several projects covering functionalities like consuming AML Web Service and retraining AML Web Service. Additionally, there is sample Azure Function code showing how to use retraining code in specific scenario. 
There is an assumption that AML Web Service with retraining experiment is already setup and published. More information about how to create retraining experiment and publish in Azure, please have a look [here](https://docs.microsoft.com/en-us/azure/machine-learning/machine-learning-retrain-models-programmatically).

Source code described in detail below is available [here](https://github.com/veracity/veracity-machinelearning-automation).

### Consuming AML Web Service
One of the standard operations executed while working with Machine Learning is asking Web Service via REST API for predictions giving some input data. At this stage model is already trained and will expect only particular set of input data.
Here we will focus on how to send data and receive predictions in real-time. 

There is also possible to consume Web Service in batch mode. This will be covered when describing retraining algorithm as it uses this approach.

WebServiceConsumer class is the one responsible for sending the scoring request and receiving predictions from AML Web Service. To setup it correctly we need to set two properties via constructor:
```csharp
public WebServiceConsumer(string webServiceUrl, string apiKey)
{
    ServiceUrl = webServiceUrl;
    ApiKey = apiKey;
}
```
All this data is available from AML Studio. API Key is available directly after choosing right Web Service, ServiceUrl is available after choosing what kind of request we want to make.
As mentioned in introduction there are two possibilities. Single request-response action and batch mode. 
In this example, we use url for single request-response action.

Main method for communication with Web Service is like below:
```csharp
public async Task<Tuple<string, string>> RequestScore(Request scoreRequest)
{
    using (var client = new HttpClient())
    {
        client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", ApiKey);
        var response = await client.PostAsJsonAsync(ServiceUrl + "/execute?api-version=2.0&details=true", scoreRequest);
        if (response.IsSuccessStatusCode)
            return new Tuple<string, string>("Request executed successfully.", await response.Content.ReadAsStringAsync());
        return new Tuple<string, string>(await GetFailedResponse(response), null);
    }
}
```

We use here HttpClient from System.Net.Http to send request and retrieve response. Note that original service url should be extended with
```csharp
"/execute?api-version=2.0&details=true"
```
Api key is used for authorization and set as default request header:
```csharp
client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", ApiKey);
```
Our input data is represented here as Request class.
```csharp
_scoreRequest = new Request
{
    Inputs = new Dictionary<string, StringTable>
    {
        {
            "input1",
            new StringTable
            {
                ColumnNames = new[]
                {
                    "col1", "col2"
                },
                Values = new[,]
                {
                    {
                        "0", "value"
                    },
                    {
                        "0", "value"
                    }
                }
            }
        }
    },
    GlobalParameters = new Dictionary<string, string>()
};
```
Structure of the request can be found also in AML Studio after choosing proper Web Service and proper action. In this case, single request-response action.
As we can see, we can have several inputs as its represented as dictionary. Single input needs to provide name and a structure called StringTable.
```csharp
public class StringTable
{
    public string[] ColumnNames { get; set; }
    public string[,] Values { get; set; }
}
```
This structure contains one dimensional array of string for column names and two-dimensional array of strings for values. Each dimension needs to have same number of values as number of columns.

As output, we receive JSON string formatted like input structure with this difference that additionally to values in array we receive also predictions.

### Retraining AML Azure Function
When working with Machine Learning, just next to standard usage its required time to time to update Machine Learning model. The operation is called retraining and can be executed via Web Service REST API.
Code available [here](https://github.com/veracity/veracity-machinelearning-automation/tree/master/MachineLearningRetrain) provides a usage sample of how step by step we can retrain our Model.
There are two main classes
- [WebServiceRetrainer](#Web-Service-Retrainer-class)
- [WebServiceUpdater](#Web-Service-Updater-class)

#### Web Service Retrainer class
Just like in WebServiceConsumer we need to provide two properties via constructor when initializing class.
```csharp
public WebServiceRetrainer(string serviceUrl, string apiKey)
{
    ServiceJobsUrl = serviceUrl;
    ApiKey = apiKey;
}
```
All this data is available from AML Studio. API Key is available directly after choosing right Web Service, ServiceUrl is available after choosing batch mode.
As we are using batch mode, we need to create special kind of request message that will send to Web Service later.
Message for our purpose is created in method PrepareRequest.
```csharp
private BatchExecutionRequest PrepareRequest(AzureStorageData inputdata, AzureStorageData outputData)
{
    return new BatchExecutionRequest
    {
        Inputs = new Dictionary<string, AzureBlobDataReference>
        {
            {
                "input2",
                new AzureBlobDataReference
                {
                    ConnectionString = inputdata.DataConnectionString,
                    RelativeLocation = $"{inputdata.ContainerName}/{inputdata.BlobName}"
                }
            },
        },
        Outputs = new Dictionary<string, AzureBlobDataReference>
        {
            {
                "output2",
                new AzureBlobDataReference
                {
                    ConnectionString = outputData.DataConnectionString,
                    RelativeLocation = $"{outputData.ContainerName}/{outputData.BlobName}"
                }
            }
        },
        GlobalParameters = new Dictionary<string, string>()
    };
}
```
Our request message contains corresponding collections of input and output data. Input is a location where data for retraining is stored. We need to provide Data Connection String to Azure Storage Account, container and blob name.
As output from retraining we get .ilearner file. It’s our new retrained model. We need to store it somewhere and later update our predictive model using WebServiceUpdater class.
We can use the same Azure Storage Account but it’s not required so we need to specify it here as well. We need to provide container and blob name.

With request data prepared like this we can use HttpClient from System.Net.Http and send it via REST API
```csharp
public async Task<Tuple<string, IEnumerable<AzureBlobDataReference>>> Retrain(AzureStorageData inputStorageData, AzureStorageData outputStorageData)
{
    var request = PrepareRequest(inputStorageData, outputStorageData);
    using (var client = new HttpClient())
    {
        client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", ApiKey);
        // submit
        var response = await client.PostAsJsonAsync(ServiceJobsUrl + "?api-version=2.0", request);
        if (!response.IsSuccessStatusCode)
            return new Tuple<string, IEnumerable<AzureBlobDataReference>>(await Utilities.GetFailedResponse(response), null);
                
        var jobId = await response.Content.ReadAsAsync<string>();
        var jobLocation = ServiceJobsUrl + "/" + jobId + "?api-version=2.0";

        // if submitted correctly, start retraining job
        response = await client.PostAsync(ServiceJobsUrl + "/" + jobId + "/start?api-version=2.0", null);
        if (!response.IsSuccessStatusCode)
            return new Tuple<string, IEnumerable<AzureBlobDataReference>>(await Utilities.GetFailedResponse(response), null);

        return await MonitorProgress(client, jobId, jobLocation);
    }
}
```
For HttpClient we need to provide authentication header:
```csharp
client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", ApiKey);
```
Once the request is sent correctly we receive a Job ID created for our request. Next step is to execute that job.
We do that by sending:
```csharp
response = await client.PostAsync(ServiceJobsUrl + "/" + jobId + "/start?api-version=2.0", null);
```

Now job starts. As this is not simple request-response action we will not get the result immediately. 
The last line of Retrain method is about monitoring how this job evaluates and what is the progress. 

In MonitorProgress method we have a loop which asks WebService for our job and based on response status, prepares result if finished, prepares error message if faulted or just waits and repeats if job is still in progress.


After job is completed we receive location of our .ilearner file.
```csharp
public class AzureBlobDataReference
{
    // Storage connection string used for regular blobs. It has the following format:
    // DefaultEndpointsProtocol=https;AccountName=ACCOUNT_NAME;AccountKey=ACCOUNT_KEY
    // It's not used for shared access signature blobs.
    public string ConnectionString { get; set; }

    // Relative uri for the blob, used for regular blobs as well as shared access 
    // signature blobs.
    public string RelativeLocation { get; set; }

    // Base url, only used for shared access signature blobs.
    public string BaseLocation { get; set; }

    // Shared access signature, only used for shared access signature blobs.
    public string SasBlobToken { get; set; }
}
```

This file will be used by WebServiceUpdater to update our predictive model.

#### Web Service Updater class
When initializing updater class, we need to provide WebService url and Api key
        public WebServiceUpdater(string serviceEndPointUrl, string endpointApiKey)
        {
            ServiceEndpointUrl = serviceEndPointUrl;
            EndpointApiKey = endpointApiKey;
        }

Web Service url needs to point to Web Service with predictive model.
Note that api key is not taken from default Web Service endpoint. We need to create special endpoint used only for updates.
More about adding new endpoint and updating trainer model you can find [here](https://docs.microsoft.com/en-us/azure/machine-learning/machine-learning-retrain-a-classic-web-service).

UpdateModel method is the one that takes .ilearner file created while retraining and updates predictive model.
As input to the method we pass collection of AzureBlobDataReference objects
```csharp
public class AzureBlobDataReference
{
    // Storage connection string used for regular blobs. It has the following format:
    // DefaultEndpointsProtocol=https;AccountName=ACCOUNT_NAME;AccountKey=ACCOUNT_KEY
    // It's not used for shared access signature blobs.
    public string ConnectionString { get; set; }

    // Relative uri for the blob, used for regular blobs as well as shared access 
    // signature blobs.
    public string RelativeLocation { get; set; }

    // Base url, only used for shared access signature blobs.
    public string BaseLocation { get; set; }

    // Shared access signature, only used for shared access signature blobs.
    public string SasBlobToken { get; set; }
}
```
This class contains information where .ilearner file is stored.

And then, using HttpClient from System.Net.Http we send PATCH request.
```csharp
using (var client = new HttpClient())
{
    client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", EndpointApiKey);

    using (var request = new HttpRequestMessage(new HttpMethod("PATCH"), ServiceEndpointUrl))
    {
        request.Content = new StringContent(JsonConvert.SerializeObject(resourceLocations),
            Encoding.UTF8, "application/json");
        var response = await client.SendAsync(request);

        if (!response.IsSuccessStatusCode)
            results.Add(await Utilities.GetFailedResponse(response));
        else
            results.Add($"Web Service updated successfully with {reference.RelativeLocation}");
    }
}
```

We need to remember to provide proper authentication header value just like for WebServiceConsumer and WebServiceRetrainer classes.

After successful response we have new retrained and updated predictive model.
