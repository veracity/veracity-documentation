---
Title : "Open Source Projects"
---
# Overview 

This guide will describe in details Veracity open source projects. Each of them is small piece of code providing useful functionality within Veracity platform. To proceed, you need to have Azure subscription.

Links to content

- [Machine Learning automation](#machine-learning-automation)


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
