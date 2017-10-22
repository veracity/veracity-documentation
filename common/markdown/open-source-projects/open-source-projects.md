---
Title : "Open Source Projects"
---
# Overview 

Veracity embrace open source. Veracity utilize open source in the development of the platform, and we feel it is correct to contribute back. We both contribute directly in open source projects, but also share whatever useful code we create on [GitHub](https://www.github.com/Veracity). 

There are two main categories of content. First there are [veracity-quickstart-samples](https://github.com/veracity/veracity-quickstart-samples) that are supporting code for how to work with veracity. These are shared under [apache 2.0](https://github.com/veracity/veracity-quickstart-samples/blob/master/LICENSE) license. 

Second there are projects that we develop that we believe users may find useful, even if it may not be a direct link to how to interact with Veracity. One such project is the [Machine Learning Automation](https://github.com/veracity/veracity-machinelearning-automation) project that we will address further in this document.

Veracity will accept contributions to all content we publish on [GitHub](https://www.github.com/veracity), and you may find the [CONTRIBUTING.md](https://github.com/veracity/veracity-quickstart-samples/blob/master/CONTRIBUTING.md) file useful. With respect to contributions, we accept both small changes and larger contributions like complete quickstart samples, if they are evaluated as a fit to Veracity. All pull requests are evaluated by a developer from the Veracity Developer.


Links to content

- [Machine Learning automation](#machine-learning-automation)


# Machine Learning automation
When considering data quality, we deal a lot with the concept of Machine Learning. Thanks to advanced algorithms we can go through data, test it againstseveral metrics and provide different data transformations. Additionally, we can draw conclusions not visible at first glance.

Microsoft provides a platform called Azure Machine Learning. Undeniable advantage of AML is that it exists in Azure environment so it is put as close to the data as possible in Veracity. Further it provides easy to use API for managing this data. In this solution, we provide code samples on how to automate parts of Machine Learning workflow. In particular we focus on consuming and retraining AML Web Service with usage of Azure Functions. The following code description applies to the .NET implementation, as it is the base platform used for the tool.

## Implementation and usage
The solution contains several projects, covering functionalities like consuming AML Web Service and retraining AML Web Service. Further, there is sample Azure Function code showing how to use retraining code in a specific scenario. The tutorial assumes that AML Web Service with retraining experiment is already setup and deployed to Azure. For information on how to deploy the AML, visit the [Analytics](https://developer.veracity.com/doc/analytics) documentattion. For additional information about how to create retraining experiment and publish in Azure, you may also have a look [here](https://docs.microsoft.com/en-us/azure/machine-learning/machine-learning-retrain-models-programmatically).

Source code described in detail below is available on [GitHub](https://github.com/veracity/veracity-machinelearning-automation).

### Consuming AML Web Service
One of the standard operations executed while working with Machine Learning is asking Web Service via REST API for predictions given some input data. At this stage model is already trained and will expect only particular set of input data.
Here we will focus on how to send data and receive predictions in real-time. 

There is also possible to consume Web Service in batch mode. This will be covered when describing retraining algorithm as it uses this approach.

The WebServiceConsumer class is the one responsible for sending the scoring request and receiving predictions from AML Web Service. To setup it correctly we need to set two properties via the constructor:
```csharp
public WebServiceConsumer(string webServiceUrl, string apiKey)
{
    ServiceUrl = webServiceUrl;
    ApiKey = apiKey;
}
```
All this data is available from AML Studio. API Key is available directly after choosing the right Web Service. ServiceUrl is available after choosing what kind of request we want to make.

As mentioned in the introduction, there are two possibilities. Single request-response action, and batch mode. 
In the following example, we use url for single request-response action.

Main method for communication with Web Service is shown below:
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

We then use the HttpClient from System.Net.Http to send request and retrieve response. Note that original service url should be extended with
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
The structure of the request can also be found in AML Studio, after choosing proper Web Service and proper action. In this case, single request-response action. As we can see, we can have several inputs as its represented as dictionary. Single input needs to provide name and a structure called StringTable.
```csharp
public class StringTable
{
    public string[] ColumnNames { get; set; }
    public string[,] Values { get; set; }
}
```
This structure contains a one-dimensional array of type string, for column names and a two-dimensional array of type string for values. Each dimension needs to have same number of values as number of columns.

As output, we receive JSON string formatted like the input structure, with the difference that there are to additional values containing the predictions.

### Retraining AML Azure Function
When working with Machine Learning, you will find the need to update the Machine Learning model from time to time. The operation is called retraining, and can be executed via Web Service REST API.

Code for how to do the retraining is available [here](https://github.com/veracity/veracity-machinelearning-automation/tree/master/MachineLearningRetrain). The code include all steps needed to retrain the Model.

There are two main classes to be concerned about.
- [WebServiceRetrainer](#Web-Service-Retrainer-class)
- [WebServiceUpdater](#Web-Service-Updater-class)

#### Web Service Retrainer class
Just like in WebServiceConsumer we need to provide two properties via the constructor when initializing class.
```csharp
public WebServiceRetrainer(string serviceUrl, string apiKey)
{
    ServiceJobsUrl = serviceUrl;
    ApiKey = apiKey;
}
```
The parameters are both available from AML Studio. The API Key is available directly after choosing the correct Web Service, and the ServiceUrl is available after choosing batch mode.

As we are using batch mode, we need to create a special kind of request message, that we will send to Web Service later.

The message we need is created in the method PrepareRequest.
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
Our request message contains the collection of inputs and corresponding output data. Input is a location where data for retraining is stored. We need to provide a Data Connection String to Azure Storage Account. 

As an output from retraining, we get an .ilearner file. It’s our new retrained model. We need to store it somewhere and later update our predictive model using WebServiceUpdater class. We can use the same Azure Storage Account but it’s not required, so we need to specify it. We need to provide container and blob name information to the storage.

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
Once the request is sent correctly, we receive a Job ID created for our request. Next step is to execute that job.
We do that by sending:
```csharp
response = await client.PostAsync(ServiceJobsUrl + "/" + jobId + "/start?api-version=2.0", null);
```

Now we have started the training process. As this is not simple request-response action we will not get the result immediately. 
The last line of Retrain method is about monitoring how this job evaluates and what is the progress. 

In the MonitorProgress method we have a loop which asks WebService for the status on our job.

After the job is completed, we receive location of our .ilearner file. The file will be used by WebServiceUpdater to update the predictive model.
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



#### Web Service Updater class
When initializing the updater class, we need to provide WebService url and Api key
        public WebServiceUpdater(string serviceEndPointUrl, string endpointApiKey)
        {
            ServiceEndpointUrl = serviceEndPointUrl;
            EndpointApiKey = endpointApiKey;
        }

Web Service url needs to point to the Web Service with the predictive model. Note that the api key is not taken from default Web Service endpoint. We need to create special endpoint used only for the updates. More about adding new endpoint and updating trainer model you can find [here](https://docs.microsoft.com/en-us/azure/machine-learning/machine-learning-retrain-a-classic-web-service).

The UpdateModel method is the method that takes the .ilearner file we created while retraining, and is used to update the predictive model. As input to the method we pass a collection of AzureBlobDataReference objects.
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

Now, using HttpClient from System.Net.Http we send PATCH request.
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

After successful response, we have new retrained and updated predictive model.
