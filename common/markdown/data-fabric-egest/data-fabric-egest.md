---
Title : "Data Fabric Egest"
Author: "Brede Børhaug"
Contributor: "Rachel Hassall"
---

## Overview
Data egest is the action of extracting data from a data storage container. There are various ways to egest data from Veracity. The method best suited to you will depend on your technical ability as well as your intended use.

This guide will show you how into egest data to the Veracity data fabric. To proceed with your data egest, you will need to be set up with a Veracity account. If you are not already set up with an account, please click [here](https://my.dnvgl.com/Register)

Link to Quick-Start:

- [Egest using Azure Storage Explorer](#egest-using-azure-storage-explorer)
- [Egest data programmatically](#egest-data-programmatically)
	- [.NET implementation](#net-implementation)
	- [Java Implementation](#java-implementation) 
	- [NodeJs Implementation](#nodejs-implementation)
	- [Python Implementation](#python-implementation)
	- [C++ Implementation](#c-implementation)
- [Use AzCopy to egest data](#egest-data-using-azcopy)
- [Use AzCopy to synchronize data](#Synchronize-data-using-AzCopy)

## Quick start

### Egest using Azure Storage Explorer
When doing a manual egest of data from Veracity, we recommend using Azure Storage Explorer. This independent application from Microsoft allows you to manually retrieve, view and interact with the data. This tool allows you to access any Veracity storage container you have been granted access to. Azure Storage Explorer is available through Windows, macOS and Linux.

#### Download and install Azure Storage Explorer 
Download Azure Storage Explorer from [www.storageexplorer.com](http://storageexplorer.com/). Select what type of operative system you are using (Windows, Mac or Linux) and the client download will start automatically.

#### Connect to a Veracity container using your key
The first time you open Azure Storage Explorer, you will see a window as shown below. If you do not already have a key from Veracity, go to [My Data](https://data.veracity.com) to open your data access page and retrieve a key. The keys provided by Veracity are known as Shared Access Signature Tokens, or SAS. The token is generated uniquely for you, and is used to monitor the access to each container respectively. Go to [data fabric keys](https://developer.veracity.com/doc/data-fabric-keys) to read more about keys.

In Azure Storage Explorer click “connect to a new storage account”, and then the radio button labeled "Use a shared access signature (SAS) URI or connection string" as shown below. Then click next.

![](https://veracityprod.blob.core.windows.net/static-documentation/ingest-ase-step-1.png "Connect to Azure Storage Explorer")

![](https://veracityprod.blob.core.windows.net/static-documentation/ingest-ase-step-2.png "Connect to Azure Storage Explorer")

The key you have received from Veracity is in the form of a SAS URI. Select the radio button labeled "Use a SAS URI" and paste the key into the field that is now available, you may now click next, and the Azure Storage Explorer will attempt to connect to the container.

If you have previously opened Azure Storage Explorer on your machine, you can connect to a new storage container by clicking the connection icon in the black menu on the left. It has been marked with a blue square in the picture below. Once you have clicked this button, you can connect to your data container in Veracity using your SAS token by following the steps listed above.

![](https://veracityprod.blob.core.windows.net/static-documentation/ingest-ase-step-3.png "Azure Storage Explorer")

You should now have access to the container that your key unlocks. You can find your container in the hierarchy by using the search feature, in the upper left corner of the application, as shown in the picture below.

![](https://veracityprod.blob.core.windows.net/static-documentation/ingest-ase-step-4.png "Azure Storage Explorer")

Depending on the type of key you have been provided, you may now browse, read,
create and/or delete data from the container.


#### Working with Azure Storage Explorer
When working with files in Azure Storage Explorer, you are working directly with the data stored within the container. This means that once you have modified the file, it is modified for everyone using the data. We recommend using a read-only key for any work that does not require you to make other changes to the data.

In some cases, you may find it useful to do curation on the data from a user interface. If you are doing manual data work, such as cleaning or transformation, you may want to lock the data set to prevent others from accessing it whilst you are uploading a new version. This can be accomplished by acquiring a lease on the given file, as shown below.

![](https://veracityprod.blob.core.windows.net/static-documentation/ingest-ase-work-1.png "Working with Azure Storage Explorer")

A lease will prevent anyone from modifying the file until you release it. The lease acquired through Azure Storage Explorer is permanent, which means it is critical that you break the lease as soon as possible. A lease is bound to your current key, so you must break the lease before the key expires to ensure that the file is not locked permanently. This is shown in the picture below.

![](https://veracityprod.blob.core.windows.net/static-documentation/ingest-ase-work-2.png "Working with Azure Storage Explorer")

#### Common pitfalls

##### Authentication Error
When looking for your container in the hierarchy, you might see an item ending with (SAS), if you try to expand this node, you may get an error stating: "Authentication Error. The specified signed resource is not allowed for this resource level." In this case, you are attempting to expand a sub-node that is not supported by the SAS URI's for containers. Instead, look for your container in the node labeled (SAS-Attached-Services).

##### Proxy Configuration
Working with the Azure Storage Explorer requires direct access to the Internet on Port 443. If your Internet Access is going via a Proxy, you need to click on the menu "Edit->Configure Proxy" to set up the proxy according to your proxy.

### Egest data programmatically
This quick start guide will show you how to view and interact with your data using some common programming languages. For details on how the code works consult the readme file in the HelloWorld applications or the tutorials on each language in the next sections.

Implementations:
- [.NET implementation](#net-implementation)
- [Java Implementation](#java-implementation) 
- [NodeJs Implementation](#nodejs-implementation)
- [Python Implementation](#python-implementation)
- [Cpp Implementation](#cpp-implementation)

#### .NET implementation
We will look at how to programmatically read data from Veracity using a .NET Framework application. On GitHub you will find the  [sample code](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-egest-data) for this application. If you do not have access to a Veracity data container, you can grab the [Veracity-Storage-Manager](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-developer-storage-manager/developer_storage) sample from our GitHub repository and create local emulated storage.

In this sample, we use the following NuGet packages:


In this sample we use the following nuget packages:

- Microsoft.WindowsAzure.Storage (client library enables working with the Microsoft Azure storage services)

Firstly, we need to create a .Net Framework application and add the constant holding SAS key provided by Veracity to the Main method.

```cs
static void Main(string[] args)
{
  // Create the constant holding the key provided by Veracity. Add your key.
  const string veracityContainerSAS = "< your SAS key go here >";

  // Add some methods under this line  

  // Hold the console
  Console.ReadLine();
}
```

Add the following packages to the program:

```charp
using System;
using System.IO;
using System.Text;
using Microsoft.WindowsAzure.Storage;
using Microsoft.WindowsAzure.Storage.Blob;
using System.Collections.Generic;
```

Now 3 main tasks remain, we need to get a reference to the container using a SAS key,
```cs
//Return a reference to the container using the SAS URI.
CloudBlobContainer container = new CloudBlobContainer(new Uri(sas));
```

get the blob URIs using the SAS URI for the container,

```cs
//Create a list to store blob URIs returned by a listing operation on the container.
List<ICloudBlob> blobList = new List<ICloudBlob>();

foreach (ICloudBlob blob in container.ListBlobs())
{
  blobList.Add(blob);
}

```
and finally read the content of the blob.

```cs
CloudBlockBlob blob = container.GetBlockBlobReference(blobList[0].Name);
MemoryStream msRead = new MemoryStream();
msRead.Position = 0;
blob.DownloadToStream(msRead);
```
 
Using these three steps, we can create a method that can interact with the container. We also add functionality to verify what access the provided Veracity SAS key gives.

```cs
// We create a method that interact with the container
static void UseContainerSAS(string sas)
{
  // We try to performe operations with the SAS provided.

  //Return a reference to the container using the SAS URI.
  CloudBlobContainer container = new CloudBlobContainer(new Uri(sas));

  //Create a list to store blob URIs returned by a listing operation on the container.
  List<ICloudBlob> blobList = new List<ICloudBlob>();

  //Write operation: write a new blob to the container.
  try
  {
    CloudBlockBlob blob = container.GetBlockBlobReference("blobCreatedViaSAS.txt");
    string blobContent = "This Veracity blob was created with a shared access signature granting write permissions to the container.";
    blob.UploadText(blobContent);

    Console.WriteLine("We were able to write to a blob using this SAS key");
    Console.WriteLine();
  }
  catch (StorageException e)
  {
    Console.WriteLine("Write operation failed using this SAS key");
    Console.WriteLine("Additional error information: " + e.Message);
    Console.WriteLine();
  }

  //List operation: List the blobs in the container.
  try
  {
    foreach (ICloudBlob blob in container.ListBlobs())
    {
      blobList.Add(blob);
    }
    Console.WriteLine("List operation succeeded for SAS key");
    Console.WriteLine();
  }
  catch (StorageException e)
  {
    Console.WriteLine("List operation failed for this SAS key");
    Console.WriteLine("Additional error information: " + e.Message);
    Console.WriteLine();
  }

  //Read operation: Get a reference to one of the blobs in the container and read it.
  try
  {
    CloudBlockBlob blob = container.GetBlockBlobReference(blobList[0].Name);
    MemoryStream msRead = new MemoryStream();
    msRead.Position = 0;
    using (msRead)
    {
      blob.DownloadToStream(msRead);
      msRead.Position = 0;
      // Just checking that we can read the buffer we retrieved
      Console.WriteLine(System.Text.Encoding.UTF8.GetString(msRead.GetBuffer()));
    }
    Console.WriteLine("Read operation succeeded for SAS ");
    Console.WriteLine();
  }
  catch (StorageException e)
  {
    Console.WriteLine("Read operation failed for SAS ");
    Console.WriteLine("Additional error information: " + e.Message);
    Console.WriteLine();
  }
  Console.WriteLine();

  //Delete operation: Delete a blob in the container.
  try
  {
    CloudBlockBlob blob = container.GetBlockBlobReference(blobList[0].Name);
    blob.Delete();
    Console.WriteLine("Delete operation succeeded for SAS ");
    Console.WriteLine();
  }
  catch (StorageException e)
  {
    Console.WriteLine("Delete operation failed for SAS ");
    Console.WriteLine("Additional error information: " + e.Message);
    Console.WriteLine();
  }
}
```

Finally we then need to call the method from the main method in the program. Your main method should then look like this.

```cs
static void Main(string[] args)
{
  // Create the constant holding the key provided by Veracity. Add your key.
  const string veracityContainerSAS = " < your SAS key go here >";

  // Add some methods under this line
  UseContainerSAS(veracityContainerSAS);
  // Hold the console
  Console.ReadLine();
}
```

#### Java implementation
We will in this quick start look at how to programmatically read data from Veracity using a Java. On GitHub you will find the [sample code](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-egest-data) for this application. If you do not have access to a Veracity data container, you can grab the [Veracity-Storage-Manager](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-developer-storage-manager/developer_storage) sample from our GitHub repository and create local emulated storage.

The samples are written in Java and use the [Azure Storage SDK for Java](https://github.com/azure/azure-storage-java). 

##### Minimum Requirements

* Java 1.6+
* Jackson-Core is used for JSON parsing.
* (Optional) SLF4J a logging facade.
* (Optional) SLF4J binding used to associate a specific logging framework with SLF4J.
* (Optional) Maven

The two dependencies, Jackson-Core and SLF4J, will be added automatically if Maven is used. Otherwise, please download the jar files and add them to your build path.

SLF4J is only needed if you enable logging through the OperationContext class. If you plan to use logging, please also download the SLF4J binding which will link the SLF4J API with the logging implementation of your choice. Simple is a good default, see the SLF4J user manual for more information.

In this sample we are using Maven project and reference the following dependencies:

- Microsoft Azure Storage Client SDK

You can download the dependencies from Maven repositories or add a dependency directly in pom.xml file:

```xml
<dependencies>
  <dependency>
    <groupId>com.microsoft.azure</groupId>
    <artifactId>azure-storage</artifactId>
    <version>5.5.0</version>
  </dependency>
</dependencies>
```

Next step is to add imports to the project:

```java
import java.net.URI;
import java.util.ArrayList;

import com.microsoft.azure.storage.*;
import com.microsoft.azure.storage.blob.*;
```

Three main steps now remain: we first need to get a reference to the container using a SAS key,

```java
CloudBlobContainer container = new CloudBlobContainer(new StorageUri(new URI(veracityContainerSAS)));
```

get the blob URIs using the SAS URI for the container,

```java
CloudBlockBlob blob = container.getBlockBlobReference("blobCreatedViaSAS.txt");
```
and finally read the content of the blob

```java
CloudBlockBlob blockBlob = container.getBlockBlobReference(blobList.get(0).getName());
String content = blockBlob.downloadText("UTF-8", null, null, null);
System.out.println("Read operation succeeded for SAS ");
System.out.println("Content: " + content);
```

We can also write content to the blob

```java
CloudBlockBlob blob = container.getBlockBlobReference("blobCreatedViaSAS.txt");
String blobContent = "This Veracity blob was created with a shared access signature granting write permissions to the container.";
blob.uploadText(blobContent);
```

or delete the blob if it's not needed anymore

```java
CloudBlockBlob blockBlobToDelete = container.getBlockBlobReference(blobList.get(0).getName());
blockBlobToDelete.delete();
```

Finally, it is good practice to wrap it in try..catch block to handle exceptions. The complete code is below.

```java
try {
  final String veracityContainerSAS = "< your SAS key go here >";

  // Container name must be lower case.
  CloudBlobContainer container = new CloudBlobContainer(new StorageUri(new URI(veracityContainerSAS)));

  //Write operation: write a new blob to the container.
  CloudBlockBlob blob = container.getBlockBlobReference("blobCreatedViaSAS.txt");
  String blobContent = "This Veracity blob was created with a shared access signature granting write permissions to the container.";
  blob.uploadText(blobContent);

  System.out.println("We were able to write to a blob using this SAS key");
  System.out.println();

  //Create a list to store blob URIs returned by a listing operation on the container.
  ArrayList<CloudBlob> blobList = new ArrayList<CloudBlob>();
  for (ListBlobItem blobItem : container.listBlobs()) {
    if (blobItem instanceof CloudBlob) {
      blobList.add((CloudBlob)blobItem);
    }
  }
  System.out.println("List operation succeeded for SAS key");
  System.out.println();

  //Read operation: Get a reference to one of the blobs in the container and read it.
  CloudBlockBlob blockBlob = container.getBlockBlobReference(blobList.get(0).getName());
  String content = blockBlob.downloadText("UTF-8", null, null, null);
  System.out.println("Read operation succeeded for SAS ");
  System.out.println("Content: " + content);
  System.out.println();
      
  //Delete operation: Delete a blob in the container.
  CloudBlockBlob blockBlobToDelete = container.getBlockBlobReference(blobList.get(0).getName());
  blockBlobToDelete.delete();
  System.out.println("Delete operation succeeded for SAS ");
}
catch (StorageException storageException) {
  System.out.print("StorageException encountered: ");
  System.out.println(storageException.getMessage());
  System.exit(-1);
}
catch (Exception e) {
  System.out.print("Exception encountered: ");
  System.out.println(e.getMessage());
  System.exit(-1);
}
```

#### NodeJs implementation
In this quick start guide we will describe how to programmatically read data from Veracity using a Node.js. On GitHub you will find the [sample code](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-egest-data) for this application. If you do not have access to a Veracity data container, you can grab the [Veracity-Storage-Manager](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-developer-storage-manager/developer_storage) sample from our GitHub repository and create a local emulated storage.

The samples are written in Node.js and use the [Azure Storage SDK for Node.js](https://github.com/Azure/azure-storage-node).

To obtain the package use Node Package Manager (NPM) from the command line or from wizard via Visual Studio.  When using command line, enter the following:

```ps
npm install azure-storage
```

Edit the js file to include the below entry: 
```js
var azure = require('azure-storage');
```
We now must get a reference to the container using a SAS key.
```js
var sharedBlobSvc = azure.createBlobServiceWithSas(hostUri, blobSas);
```

We are now ready to perform the write operation.
```js
sharedBlobSvc.createAppendBlobFromText(
  containerName,
  blobName,
  text,
  function(error, result, response) {
    if (error) {
      console.log("There was an error while doing blob upload.");
      console.error(error);
    } else {
      console.log("We were able to write to a blob using this SAS key");
    }
  }
);
```

We can also list existing blobs
```js
sharedBlobSvc.listBlobsSegmented(
  containerName,
  null,
  function(error, result, response) {
    if (error) {
      console.log("There was an error during listing blobs in container %s", containerName);
      console.error(error);
    } else {
      console.log('%s blobs: ', containerName);
      var index;
      for (index = 0; index < result.entries.length; index++) {
        console.log(result.entries[index].name);
      }
    }
  }
);
```

and read blob content. 
```js
sharedBlobSvc.getBlobToText(
  containerName,
  blobName,
  function(error, blobContent, blob) {
    if (error) {
      console.error("Couldn't download blob %s", blobName);
      console.error(error);
    } else {
      console.log("Sucessfully downloaded blob %s", blobName);
      console.log(blobContent);
    }
  }
);
```
Finally, we can delete blob if its not needed anymore.
 ```js
sharedBlobSvc.deleteBlob(containerName, blobName, function (error, response) {
  if (error) {
    console.log("There was an error during deletion of blob  %s", blobName);
    console.error(error);
  } else
    console.log("%s blob deleted sucessfully", blobName);
});
```

Complete sample is like below:
 ```js
function performAzureOperations() {

  // writing test to blob
  sharedBlobSvc.createAppendBlobFromText(
    containerName,
    blobName,
    text,
    function(error, result, response) {
      if (error) {
        console.log("There was an error while doing blob upload.");
        console.error(error);
      } else {
        console.log("We were able to write to a blob using this SAS key");

        // listing blobs in container
        sharedBlobSvc.listBlobsSegmented(
          containerName,
          null,
          function(error, result, response) {
            if (error) {
              console.log("There was an error during listing blobs in container %s", containerName);
              console.error(error);
            } else {
              console.log('%s blobs: ', containerName);
              var index;
              for (index = 0; index < result.entries.length; index++) {
                console.log(result.entries[index].name);
              }
              console.log("We were able to write list blobs using SAS key");

              // downloading blob to text
              sharedBlobSvc.getBlobToText(
                containerName,
                blobName,
                function(error, blobContent, blob) {
                  if (error) {
                    console.error("Couldn't download blob %s", blobName);
                    console.error(error);
                  } else {
                    console.log("Sucessfully downloaded blob %s", blobName);
                    console.log(blobContent);

                    // deleting a blob
                    sharedBlobSvc.deleteBlob(containerName, blobName, function (error, response) {
                      if (error) {
                        console.log("There was an error during deletion of blob  %s", blobName);
                        console.error(error);
                      } else
                        console.log("%s blob deleted sucessfully", blobName);
                      });
                  }
                });
            }
          });
      }
    });
}
```

#### Python implementation
In this quick start guide we will look at how to programmatically read data from Veracity using Python. On GitHub you will find the [sample code](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-egest-data) for this application. If you do not have access to a Veracity data container, you can grab the [Veracity-Storage-Manager](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-developer-storage-manager/developer_storage) sample from our GitHub repository and create local emulated storage.

The samples are written in Python and use the [Azure Storage SDK for Python](https://github.com/Azure/azure-sdk-for-python). 

In your python environment you will need to add the “azure-storage” package

 ```ps
azure-storage
 ```

and import BlockBlobService

```python
from azure.storage.blob import BlockBlobService
 ```
We create some variables that will come in handy.

```python
accountName = "<storage account name>"
veracityContainerSAS = "< your sas key without question mark'?' >"
```

If you are using the Veracity portal to get hold of the SAS key, and not the Veracity API, you will need to pick different parts from the SAS URI for each of the variables above. If we use the following SAS token as an example:

```url
https://ns4dnvglfstspus00001.blob.core.windows.net/devcontainer9ae56656-bd3a-4d6e-b257-cfbb6241b1ea?sv=2017-04-17&sr=c&sig=BPRAohaQyrwW4%2FCQt22BdJW%2FtVpv3qEH0LvQBbcZFJI%3D&st=2017-10-12T18%3A06%3A28Z&se=2017-10-12T20%3A06%3A01Z&sp=rwl
```

We have the SAS key as the parameter, and we have the account name as the subdomain. We then get the following:

```python
accountName = "ns4dnvglfstspus00001"
veracityContainerSAS = "sv=2017-04-17&sr=c&sig=BPRAohaQyrwW4%2FCQt22BdJW%2FtVpv3qEH0LvQBbcZFJI%3D&st=2017-10-12T18%3A06%3A28Z&se=2017-10-12T20%3A06%3A01Z&sp=rwl"
```

We must now get a reference to the container using a SAS key.

```python
try:
    sas_service = BlockBlobService(account_name=accountName, sas_token=veracityContainerSAS)
except Exception as e:
    print("There was an error during SAS service creation. Details: {0}".format(e))
```

We can now perform the read operation. At this point you should consult the documentation for the azure.storage.blob library. You can use the get_blob_to_path, get_blob_to_stream, get_blob_to_bytes, or get_blob_to_text methods. These are high-level methods that perform the necessary chunking when the size of the data exceeds 64 MB.

We first use the get_blob_to_path method within a try…catch block, 

```python
try:
    sas_service.get_blob_to_path(containerName, blobName, 'downloadedName.csv')
except Exception as e:
    print("There was an error during blob download. Details: {0}".format(e))
```

We can also use the get_blob_to_text method to read the content directly from a text blob.

```python
try:
    blob_text = sas_service.get_blob_to_text(containerName, blobName)
    print(blob_text.content)
except Exception as e:
    print("There was an error during blob reading. Details: {0}".format(e))
```

The complete code sample is below:

```python
from azure.storage.blob import BlockBlobService

accountName = "<storage account name>"
veracityContainerSAS = "< your sas key without question mark'?' >"
containerName = "< container name >"

## create service and keep reference to SAS container
print("Creating SAS service with {0} account".format(accountName))
try:
    sas_service = BlockBlobService(account_name=accountName, sas_token=veracityContainerSAS)
except Exception as e:
    print("There was an error during SAS service creation. Details: {0}".format(e))

## list blobs in container
print("Blobs in container: ")
try:
    generator = sas_service.list_blobs(containerName)
    for blob in generator:
        print(blob.name)
except Exception as e:
    print("There was an error during blobs listing. Details: {0}".format(e))

## download blob to path
blobName = "downloadedLocalFileName.csv"

try:
    sas_service.get_blob_to_path(containerName, blobName, 'downloadedName.csv')
except Exception as e:
    print("There was an error during blob download. Details: {0}".format(e))

## read blob from container
print("")
print("{0} blob content: ".format(blobName))
try:
    blob_text = sas_service.get_blob_to_text(containerName, blobName)
    print(blob_text.content)
except Exception as e:
    print("There was an error during blob reading. Details: {0}".format(e))

```
#### C++ implementation
We will now describe how to programmatically read data from Veracity using C++. On GitHub you will find the [sample code](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-egest-data) for this application. If you do not have access to a Veracity data container, you can grab the [Veracity-Storage-Manager](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-developer-storage-manager/developer_storage) sample from our GitHub repository and create local emulated storage.

The samples are written in C++ and use the [Azure Storage SDK for Cpp](https://github.com/Azure/azure-storage-cpp). 

With NuGet Package Manager install Azure Storage Client Library. Use the Package Manager Console and type:
```ps
Install-Package wastorage
```

At the top of Cpp file add following include statements:
```cpp
##include <was/storage_account.h>
##include <was/blob.h>
```
We must now get a reference to the container using a SAS key:
```cpp
azure::storage::cloud_blob_container container = azure::storage::cloud_blob_container::cloud_blob_container(azure::storage::storage_uri(veracity_container_sas));
azure::storage::cloud_block_blob blockBlob = container.get_block_blob_reference(U("blobCreatedViaSAS.txt"));
```
We are ready to perform write operation.
```cpp
try
{
  blockBlob.upload_text(U("This Veracity blob was created with a shared access signature granting write permissions to the container."));
  std::wcout << U("We were able to write to a blob using this SAS key") << std::endl;
}
catch (const std::exception e)
{
  std::wcout << U("There was an error during blob writing: ") << e.what() << std::endl;
}
```

We can also list existing blobs,

```cpp
try
{
  azure::storage::list_blob_item_iterator end_of_results;
  for (auto i = container.list_blobs(); i != end_of_results; ++i)
  {
    if (i->is_blob())
    {
      std::wcout << U("Blob: ") << i->as_blob().uri().primary_uri().to_string() << std::endl;
    }
    else
    {
      // just a check if we have a directory in container
      std::wcout << U("Directory: ") << i->as_directory().uri().primary_uri().to_string() << std::endl;
    }
  }
  std::wcout << U("List operation succeeded for SAS key") << std::endl;
}
catch (const std::exception e)
{
  std::wcout << U("There was an error during blob listing: ") << e.what() << std::endl;
}
```

and read blob content 

```cpp
try
{
  azure::storage::cloud_block_blob text_blob = container.get_block_blob_reference(U("blobCreatedViaSAS.txt"));
  utility::string_t text = text_blob.download_text();
  std::wcout << U("Read operation succeeded for SAS , content: ") << std::endl;
  std::wcout << text << std::endl;
}
catch (const std::exception e)
{
    std::wcout << U("There was an error during blob downloading: ") << e.what() << std::endl;
}
```
Finally, we can delete blob if it’s not needed anymore.

 ```cpp
try
{
  azure::storage::cloud_block_blob blockBlob = container.get_block_blob_reference(U("blobCreatedViaSAS.txt"));
  blockBlob.delete_blob();
  std::wcout << U("Delete blob operation succeeded for SAS");
}
catch (const std::exception e)
{
  std::wcout << U("There was an error during blob deletion: ") << e.what() << std::endl;
}
```

Complete sample is as below:

```cpp
##include "stdafx.h"
##include <was/storage_account.h>
##include <was/blob.h>

int main()
{
  //Return a reference to the container using the SAS URI.
  const utility::string_t veracity_container_sas(U("..."));
  azure::storage::cloud_blob_container container;
  azure::storage::cloud_block_blob blockBlob;
  try
  {
    container = azure::storage::cloud_blob_container::cloud_blob_container(azure::storage::storage_uri(veracity_container_sas));
    blockBlob = container.get_block_blob_reference(U("blobCreatedViaSAS.txt"));
  }
  catch (const std::exception e)
  {
    std::wcout << U("There was an error during blob referencing vis SAS: ") << e.what() << std::endl;
  }
  //Write operation: write a new blob to the container.
  try
  {
    blockBlob.upload_text(U("This Veracity blob was created with a shared access signature granting write permissions to the container."));
    std::wcout << U("We were able to write to a blob using this SAS key") << std::endl;
  }
  catch (const std::exception e)
  {
    std::wcout << U("There was an error during blob writing: ") << e.what() << std::endl;
  }

  //List operation: List the blobs in the container.
  try
  {
    azure::storage::list_blob_item_iterator end_of_results;
    for (auto i = container.list_blobs(); i != end_of_results; ++i)
    {
      if (i->is_blob())
      {
        std::wcout << U("Blob: ") << i->as_blob().uri().primary_uri().to_string() << std::endl;
      }
      else
      {
        // just a check if we have a directory in container
        std::wcout << U("Directory: ") << i->as_directory().uri().primary_uri().to_string() << std::endl;
      }
    }
    std::wcout << U("List operation succeeded for SAS key") << std::endl;
  }
  catch (const std::exception e)
  {
    std::wcout << U("There was an error during blob listing: ") << e.what() << std::endl;
  }

  //Read operation: Get a reference to one of the blobs in the container and read it.
  try
  {
    azure::storage::cloud_block_blob text_blob = container.get_block_blob_reference(U("blobCreatedViaSAS.txt"));
    utility::string_t text = text_blob.download_text();
    std::wcout << U("Read operation succeeded for SAS , content: ") << std::endl;
    std::wcout << text << std::endl;
  }
  catch (const std::exception e)
  {
    std::wcout << U("There was an error during blob downloading: ") << e.what() << std::endl;
  }

  //Delete operation: Delete a blob in the container.
  try
  {
    azure::storage::cloud_block_blob blockBlob = container.get_block_blob_reference(U("blobCreatedViaSAS.txt"));
    blockBlob.delete_blob();
    std::wcout << U("Delete blob operation succeeded for SAS");
  }
  catch (const std::exception e)
  {
    std::wcout << U("There was an error during blob deletion: ") << e.what() << std::endl;
  }

  std::string str;
  std::getline(std::cin, str);
  return 0;
}
```

### Egest data using AzCopy
AzCopy is a command line tool used to upload and download data to or from  BLOB containers and to transfer data between BLOB containers. It is designed to give high performance and works particularly well when copying data between containers in the same locations.
However, it can also be used to download data from a local computer or between any BLOBs in any subscriptions and locations.
AzCopy can be downloaded and installed for both Windows and Linux. After installation on Windows it is important to add the AZCopy.exe path to your system path. AZCopy can then be run either from the command prompt or from for example Windows Powershell.

The basic AzCopy command looks like this:

```batch
AzCopy /Source:\<source\> /Dest:\<Destination\> \[Options\]
```

The below examples illustrates three common scenarios, copying one file, copying several files using a mask and copying entire folders.
We assume you have obtained the appropriate access keys as described in a previous section.

(1) Copying one BLOB file in specific container to local file:

```batch
AzCopy /Source:https ://myblob.blob.core.windows.net/MyContainer /SourceKey:key /Dest:C:\MyLocalFolder /Pattern:myfile.csv 
```

When copying file from BLOB container to a local computer, the option /SourceKey has to be used.

(2) Copying multiple files from BLOB container:

```batch
AzCopy /Source:https ://myblob.blob.core.windows.net/MyContainer /SourceKey:key /Dest:C:\MyLocalFolder /Pattern:my  /S
```

This will copy all files starting with "my". Use option /S to copy more than one file.

(3) Copying a folder from a BLOB container:

```batch
AzCopy /Source:https ://myblob.blob.core.windows.net/MyContainer /SourceKey:key /Dest:C:\MyLocalFolder /S
```

Additionally insteady of using access keys you are able to use SAS tokens for specific container. 

Below examples similar to above but with SAS token usage.

(1) Copying one BLOB file in specific container to local file:

```batch
AzCopy /Source:https ://myblob.blob.core.windows.net/MyContainer /SourceSAS:sasToken /Dest:C:\MyLocalFolder /Pattern:myfile.csv 
```

When copying file from BLOB container to a local computer, the option /SourceKey has to be used.

(2) Copying multiple files from BLOB container:

```batch
AzCopy /Source:https ://myblob.blob.core.windows.net/MyContainer /SourceSAS:sasToken /Dest:C:\MyLocalFolder /Pattern:my  /S
```

This will copy all files starting with "my". Use option /S to copy more than one file.

(3) Copying a folder from a BLOB container:

```batch
AzCopy /Source:https ://myblob.blob.core.windows.net/MyContainer /SourceSAS:sasToken /Dest:C:\MyLocalFolder /S
```
### Synchronize data using AzCopy
Starting with AzCopy v10, the tool can also be used to synchronize data between a source and a destination, which means you can use it to keep files in your local machine (destination) up-to-date with files on your container (source) or vice-versa.
In the example below we use the `access key` for our container obtained from the `Access` page of containers at [data.veracity.com](https://data.veracity.com/containers). This will synchronize `mylocalfolder` so that it has every file from our container.

```ps
.\azcopy.exe sync "<access key>" "C:\mylocalfolder" --recursive=true
```

For full documentation on this functionality, refer to [docs.microsoft.com](https://docs.microsoft.com/nb-no/azure/storage/common/storage-use-azcopy-v10?toc=%2fazure%2fstorage%2fblobs%2ftoc.json#sync-incremental-copy-and-delete-blob-storage-only)


## GitHub  
Follow our open projects related to Veracity data fabric egest on https://github.com/veracity

## Stack Overflow
Stack Overflow is the largest, most trusted online community for developers to learn, share their programming knowledge. The Veracity developer team monitor Stack Overflow forum posts that include the tag Veracity Platform.

[Visit Stack Overflow](https://stackoverflow.com/questions/tagged/veracity+platform?mode=all)
 
## FAQ 

Q: I am using Ubuntu Linux and I have issues running storage explorer 

A: Some users have reported issues with running storage explorer. We tested it successfully with the Windows desktop operating systems: Windows 7, Windows 8, Windows 10 and with the server operating systems Windows Server 2008 and Windows Server 2012. The test failed with Ubuntu Linux 17.04.


Q: I attempt to use the SAS key in Azure Storage Explorer a second time and get the Authentication Error: The specific signed resource is not allowed for this resource level

A: This is a known bug in Azure Storage Explorer. This will occur if you did not detach the storage before you tried to reconnect using the same key. You will need to access the storage under the "(SAS-Attached Services)" storage account in Azure Storage Explorer. The storage should still be mapped there. The Microsoft Azure team will need to resolve this bug, and Veracity is not able to contribute to that. Please continue to update your Azure Storage Explorer when new releases are available.
