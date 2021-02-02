---
Title : "Open Source Projects"
Author: "Brede Børhaug"
Contributors: "Pawel Lehmann, Rachel Hassall"
---
## Overview 

Veracity embraces open source. Veracity utilizes open source in the development of the platform, and we feel it is correct to contribute back. We contribute both directly in open source projects, but also share whatever useful code we create on [GitHub](https://www.github.com/Veracity). 

There are two main categories of content. Firstly, there are [veracity-quickstart-samples](https://github.com/veracity/veracity-quickstart-samples) that consist of supporting code for how to work with veracity. These are shared under [apache 2.0](https://github.com/veracity/veracity-quickstart-samples/blob/master/LICENSE) license. 

Secondly, there are projects that we develop that we believe users may find useful, even if it may not be directly linked to how to interact with Veracity. One such project is the [Machine Learning Automation](https://github.com/veracity/veracity-machinelearning-automation) project that we will address further on in this document.

Veracity will accept contributions to all content we publish on [GitHub](https://www.github.com/veracity), and you may find the [contributing.md](https://github.com/veracity/veracity-quickstart-samples/blob/master/CONTRIBUTING.md) file useful. With respect to contributions, we accept both small changes and larger contributions, like complete quickstart samples, if they are evaluated as a fit to Veracity. All pull requests are evaluated by a developer from the Veracity Development group.


Links to content:

- [Machine Learning automation](#machine-learning-automation)


## Machine Learning automation
When considering data quality, we deal a lot with the concept of Machine Learning. Thanks to advanced algorithms we can go through data, test it against several metrics and provide different data transformations. Additionally, we can draw conclusions not visible at first glance.

Microsoft provides a platform called Azure Machine Learning (AML). The undeniable advantage of AML is that it exists in an Azure environment, so is as close to the data as possible within Veracity. It provides an easy to use API for managing this data. In this solution, we provide code samples on how to automate parts of the Machine Learning workflow. In particular, we focus on consuming and retraining the AML Web Service with usage of Azure Functions. The following code description applies to the .NET implementation, as it is the base platform used for the tool.

### Implementation and usage
The solution contains several projects, covering functionalities like consuming AML Web Service and retraining the AML Web Service. There is sample Azure Function code showing how to use retraining code in a specific scenario. The tutorial assumes that AML Web Service with a retraining experiment is already setup and deployed to Azure. For information on how to deploy the AML, visit the [Analytics](https://developer.veracity.com/doc/analytics) documentation. For additional information about how to create a retraining experiment and publish in Azure you can also look [here](https://docs.microsoft.com/en-us/azure/machine-learning/machine-learning-retrain-models-programmatically).

Source code described in detail below is available on [GitHub](https://github.com/veracity/veracity-machinelearning-automation).

#### Consuming AML Web Service
One of the standard operations executed whilst working with Machine Learning is asking the Web Service via the REST API for predictions given some input data. At this stage, the model is already trained and will expect only a particular set of input data.
Here, we will focus on how to send data and receive predictions in real-time. 

There is also the possibility to consume Web Service in batch mode, this will be covered when describing the retraining algorithm, as it uses this approach.

The WebServiceConsumer class is the one responsible for sending the scoring request and receiving predictions from the AML Web Service. To setup it correctly we need to set two properties via the constructor:

```cs
public WebServiceConsumer(string webServiceUrl, string apiKey)
{
  ServiceUrl = webServiceUrl;
  ApiKey = apiKey;
}
```

All this data is available from AML Studio. The API Key is available directly after choosing the correct Web Service. ServiceUrl is available after choosing what kind of request we want to make.

As mentioned in the introduction, there are two possibilities: single request-response action and batch mode. 
In the following example, we use the url for single request-response action.

The main method for communication with the Web Service is shown below:

```cs
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

We then use the Http Client from System.Net.Http to send the request and retrieve response. Note that the original service url should be extended with

```cs
"/execute?api-version=2.0&details=true"
```
The API key is used for authorization and set as the default request header:

```cs
client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", ApiKey);
```
Our input data is represented here as a Request class.

```cs
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
  GlobalParameters = new Dictionary<string, string>();
};
```
The structure of the request can also be found in AML Studio, after choosing the proper Web Service and proper action. In this case, single request-response action. As we can see, we can have several inputs as it is represented as a dictionary. The single input needs to provide a name and a structure called StringTable.

```cs
public class StringTable
{
  public string[] ColumnNames { get; set; }
  public string[,] Values { get; set; }
}
```

This structure contains a one-dimensional array of type string, for column names, and a two-dimensional array of type string for values. Each dimension needs to have the same number of values as the number of columns.

As output, we receive JSON string formatted like the input structure, but with the difference that there are two additional values containing the predictions.

#### Retraining AML Azure Function
When working with Azure Machine Learning, you will find the need to update the AML model from time to time. This operation is called retraining, and can be executed via the Web Service REST API.

Code for how to do the retraining is available [here](https://github.com/veracity/veracity-machinelearning-automation/tree/master/MachineLearningRetrain). The code includes all the steps needed to retrain the Model.

There are two main classes to be concerned about.
- [WebServiceRetrainer](#Web-Service-Retrainer-class)
- [WebServiceUpdater](#Web-Service-Updater-class)

##### Web Service Retrainer class
Just like in WebServiceConsumer we need to provide two properties via the constructor when initializing the class.
```cs
public WebServiceRetrainer(string serviceUrl, string apiKey)
{
  ServiceJobsUrl = serviceUrl;
  ApiKey = apiKey;
}
```
Both parameters are available from AML Studio. The API Key is available directly after choosing the correct Web Service, and the ServiceUrl is available after choosing batch mode.

As we are using batch mode, we need to create a special kind of request message that we will send to Web Service later.

The message we need is created in the method PrepareRequest.
```cs
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

As an output from retraining, we get an .ilearner file - our new retrained model. We need to store it somewhere and later update our predictive model using WebServiceUpdater class. We can use the same Azure Storage Account but it’s not required, so we need to specify it. We need to provide the container and blob name information to the storage.

With request data prepared like this we can use HttpClient from System.Net.Http and send it via the REST API.

```cs
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

```cs
client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", ApiKey);
```

Once the request is sent correctly, we receive a Job ID created for our request. The next step is to execute that job.
We do that by sending:

```cs
response = await client.PostAsync(ServiceJobsUrl + "/" + jobId + "/start?api-version=2.0", null);
```

Now we have started the training process. As this is not a simple request-response action, we will not get the result immediately. 
The last line of the Retrain method is about monitoring how this job evaluates and what is its progress. 

In the MonitorProgress method we have a loop which asks WebService for the status of our job.

After the job is completed, we receive the location of our .ilearner file. The file will be used by WebServiceUpdater to update the predictive model.

```cs
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

##### Web Service Updater class
When initializing the updater class, we need to provide the WebService URL and API key

```cs
public WebServiceUpdater(string serviceEndPointUrl, string endpointApiKey)
{
  ServiceEndpointUrl = serviceEndPointUrl;
  EndpointApiKey = endpointApiKey;
}
```

The Web Service URL needs to point to the Web Service with the predictive model. Note that the API key is not taken from the default Web Service endpoint. We need to create a special endpoint used only for the updates. You can find out more about adding new endpoints and updating the trainer model [here](https://docs.microsoft.com/en-us/azure/machine-learning/machine-learning-retrain-a-classic-web-service).

The UpdateModel method is the method that takes the .ilearner file we created while retraining, and is used to update the predictive model. As input to the method we pass a collection of AzureBlobDataReference objects.

```cs
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

Now, using the HttpClient from System.Net.Http we send a PATCH request.

```cs
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

We need to remember to provide a proper authentication header value just like for WebServiceConsumer and WebServiceRetrainer classes.

After a successful response, we have new retrained and updated the predictive model.

### GitHub  
Follow our open projects related to open source on https://github.com/veracity

### Stack Overflow
Stack Overflow is the largest, most trusted online community for developers to learn and share their programming knowledge. The Veracity developer team monitor Stack Overflow forum posts that include the tag Veracity Platform.

[Visit Stack Overflow](https://stackoverflow.com/questions/tagged/veracity+platform?mode=all)
