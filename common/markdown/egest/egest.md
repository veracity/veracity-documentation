
# Overview 
Data egest is the action of extracting data from a data storage. There are various ways to egest data from Veracity. The method best suited for you will depend on your technical ability as well as intended use.  

This guide will show you how into egest data to the Veracity cloud. To proceed with your data egest, you will need to be set up with a Veracity account. If you are not already set up with an account, please click here.

Link to Quick-Start

- [Egest using Azure Storage Explorer](#Egest-using-Azure-storage-explorer)
- [Egesting data using REST API](#Egesting-data-using-REST-API)

Link to tutorial:
-	How to work in Azure Storage Explorer
-	How to work in Blob, REST API, AZCopy or Azure CLI
-	Egest using Mac
-	Egest using Linux
-	Other




# Quick start 
## Egest using Azure storage explorer
When doing a manual egest of data from Veracity, we recommend using Azure Storage Explorer. This independent application from Microsoft allows you to manually retrieve, view and interact with the data. This tool allows you to access any Veracity storage container you have been granted access to. Azure Storage Explorer is available through Windows, macOS and Linux.

### Download and install Azure Storage Explorer.
Download Azure Storage Explorer from http://storageexplorer.com/. Select what type of operative system you are using (Windows, Mac or Linux) and the client download will start automatically. Do not use an outdated version from the Codeplex repository, as these are most likely the versions which are shown on the screen when you use BING to search for "Azure Storage Explorer". The correct download screen should look like this: 

 
![](https://raw.githubusercontent.com/veracity/Documentation/master/common/images/ingest-ase-download.png?token=ATKIGzfMe8EsHLvrUimjnExhsKcQk4Doks5ZiwhZwA%3D%3D "Download Azure Storage Explorer")


If you are having problems with the installation, please visit our FAQ section for Azure
Storage Explorer.

Step by step installation

1.	Download the executable from http://storageexplorer.com/
2.	Run the executable, you should now see a window as seen below:

 ![](https://raw.githubusercontent.com/veracity/Documentation/master/common/images/ingest-ase-install.png?token=ATKIG4dnUE0UbtqAKfwg3QHysrtKNVPUks5ZiwgvwA%3D%3D "Install Azure Storage Explorer")

3.	Follow the instructions provided in the installation wizard. Note that you cannot complete the installation without accepting Microsoft's terms of use
4.	Azure storage explorer is now installed, and should open automatically after the first installation, regularly check for updates and apply them. They are indicated when available

### Connect to a Veracity container using your key
The first time you open Azure Storage Explorer, you will see a window as shown below. If you do not already have a key from Veracity, click [HERE] to open your data access page and retrieve a key. The keys provided by Veracity are known as Shared Access Signature Tokens, or SAS. The token is generated uniquely for you, and is used to monitor the access to each container respectively. 

![](https://raw.githubusercontent.com/veracity/Documentation/master/common/images/ingest-ase-connect-01.png?token=ATKIG7Il5z2-kdlKl4v6Mi9qeDJyVtFAks5Ziwf4wA%3D%3D "Connect to Azure Storage Explorer")

In Azure Storage Explorer, click the radio button labeled "Use a shared access signature (SAS) URI or connection string" as shown below. Then click next.

![](https://raw.githubusercontent.com/veracity/Documentation/master/common/images/ingest-ase-connect-02.png?token=ATKIG1zlRlexQAfuOykdzcpjyyprS2Tdks5Ziwh0wA%3D%3D "Connect to Azure Storage Explorer")

The key you have received from Veracity is in the form of a SAS URI, select the radio
button labeled "Use a SAS URI" and paste the key into the field that is now available, you
may now click next, and the Azure Storage Explorer will attempt to connect to the
container.

If you have previously opened Azure Storage Explorer on your machine, you can connect
to a new storage container by clicking the connection icon in the black menu on the left.
It has been marked with a blue square in the picture below. Once you have clicked this
button, you may follow the steps listed above.

![](https://raw.githubusercontent.com/veracity/Documentation/master/common/images/ingest-ase-connect-03.png?token=ATKIG2XF9xlPjyyijY-bxADuqTWH6DqJks5ZiwikwA%3D%3D "Azure Storage Explorer")

You should now have access to the container that your key unlocks. You can find it in the
hierarchy by using the search feature, in the upper left corner of the application, as shown in the picture below.

![](https://raw.githubusercontent.com/veracity/Documentation/master/common/images/ingest-ase-connect-04.png?token=ATKIG0TH1o6Hda3_d5LYCIlDvzH-7Gx1ks5Ziwi7wA%3D%3D "Azure Storage Explorer")

Depending on the type of key you have been provided, you may now browse, read,
create and/or delete data-sets from the container.


### Working with Azure Storage Explorer
When working with files in Azure Storage Explorer, you are working directly with the
data stored within the container. This means that once you have modified the file, it is
modified for everyone using the data. Therefore, we recommend using a read-only key
for any work that does not require you to make other changes to the data.

In some cases, you may find it useful to do curation on the data from a user interface. If
you are doing manual work, such as cleaning or transformation of the data, you may
want to lock the data set to prevent others from accessing it while you are uploading a
new version. This can be accomplished by acquiring a lease on the given file, as shown
below.

![](https://raw.githubusercontent.com/veracity/Documentation/master/common/images/ingest-ase-working-01.png?token=ATKIG5yYwW1gNo5iFwLOYfZx3M3cwCx8ks5ZiwjYwA%3D%3D "Working with Azure Storage Explorer")

A lease will prevent anyone from modifying the file until you release the file. The lease acquired through Azure Storage Explorer is permanent, which means it is critical that you break the lease as soon as possible. As a lease is bound to your current key, you must break the lease before the key expires to ensure that the file is not locked permanently. This is shown in the picture below.

![](https://raw.githubusercontent.com/veracity/Documentation/master/common/images/ingest-ase-working-02.png?token=ATKIGwJjRoIYdt2ANxK9NgZPOWl28Natks5ZiwjtwA%3D%3D "Working with Azure Storage Explorer")

### Common pitfalls
Authentication Error. The specified signed resource is not allowed for this resource level.
When looking for your container in the hierarchy, you might see an item ending with (SAS), if you try to expand this node, you may get an error stating: "Authentication Error. The specified signed resource is not allowed for this resource level." In this case, you are attempting to expand a sub-node that is not supported by the SAS URI's for containers. Instead, look for your container in the node labeled (SAS-Attached-Services).

#### Proxy Configuration
Working with the Azure Storage Explorer requires direct access to the Internet on Port 443. If your Internet Access is going via a Proxy, you need to click on the menu "Edit->Configure Proxy" to set up the proxy:

![](https://raw.githubusercontent.com/veracity/Documentation/master/common/images/ingest-ase-pitfalls-proxy-01.png?token=ATKIG7vLmSmwfmMNmZz1NItrva4FqMk9ks5Ziwk-wA%3D%3D "Working with Azure Storage Explorer")


## Egesting data using REST API
These applications allow you to programmatically view/interact with your data. This quick guide will show you how to do this using some common languages. For details on how the code work consult the readme file in the HelloWorld applications or the tutorials on each language in the next sections. 

Implementations:
- [.NET implementation](#.NET-implementation)
- [Java Implementation](#Java-Implementation) 
- [NodeJs Implementation](#NodeJs-Implementation)
- [Python Implementation](#Python-Implementation)



### .NET implementation
We will in this quick start look at how to programaticaly read data from Veracity using a .NET Framework application. On Github you will find the [sample code](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-egest-data) for this application. If you do not have access to a Veracity data container, you may grab the [Veracity-Storage-Manager](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-developer-storage-manager/developer_storage) sample from our github Repo and create a local emulated storage. 

In this sample we use the following nuget packages:
- Microsoft.WindowsAzure.Storage (client library enables working with the Microsoft Azure storage services)


First we need to create a .Net Framework application. Then add the constant holding the SAS key provided by Veracity to the Main method.

```csharp
 static void Main(string[] args)
        {
            // Create the constant holding the key provided by Veracity. Add your key.
            const string veracityContainerSAS = "< your SAS key go here >";

            // Add some methods under this line            

            // Hold the consol
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

We now basically need to do three things. We first need to get a reference to the container using a SAS key
```csharp
//Return a reference to the container using the SAS URI.
CloudBlobContainer container = new CloudBlobContainer(new Uri(sas));
```

Get the blob URI's using the SAS URI for the container,

```csharp
//Create a list to store blob URIs returned by a listing operation on the container.
List<ICloudBlob> blobList = new List<ICloudBlob>();

foreach (ICloudBlob blob in container.ListBlobs())
{
    blobList.Add(blob);
}

```
And finaly read the content of the blob

```csharp
CloudBlockBlob blob = container.GetBlockBlobReference(blobList[0].Name);
MemoryStream msRead = new MemoryStream();
msRead.Position = 0;
blob.DownloadToStream(msRead);
```
 
Using these three steps, we can create a method that can interact with the container. We add functionality to also verify what access the provided Veracity SAS key provide.

```csharp
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

                Console.WriteLine("We where able to write to a blob using this SAS key");
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

Finaly we then need to call the method from the main method in the program. Your main method should then look like this.

```csharp
        static void Main(string[] args)
        {
            // Create the constant holding the key provided by Veracity. Add your key.
            const string veracityContainerSAS = " < your SAS key go here >";

            // Add some methods under this line
            UseContainerSAS(veracityContainerSAS);
            // Hold the consol
            Console.ReadLine();


        }
```



### Java implementation
We will in this quick start look at how to programaticaly read data from Veracity using a Java. On Github you will find the [sample code](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-egest-data) for this application. If you do not have access to a Veracity data container, you may grab the [Veracity-Storage-Manager](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-developer-storage-manager/developer_storage) sample from our github Repo and create a local emulated storage.

The samples are written in Java and use the [Azure Storage SDK for Java](https://github.com/azure/azure-storage-java). 

#### Minimum Requirements

* Java 1.6+
* Jackson-Core is used for JSON parsing.
* (Optional) SLF4J is a logging facade.
* (Optional) SLF4J binding is used to associate a specific logging framework with SLF4J.
* (Optional) Maven

The two dependencies, Jackson-Core and SLF4J, will be added automatically if Maven is used. Otherwise, please download the jars and add them to your build path.

SLF4J is only needed if you enable logging through the OperationContext class. If you plan to use logging, please also download an SLF4J binding which will link the SLF4J API with the logging implementation of your choice. Simple is a good default. See the SLF4J user manual for more information.




### NodeJs implementation
We will in this quick start look at how to programaticaly read data from Veracity using NodeJs. On Github you will find the [sample code](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-egest-data) for this application. If you do not have access to a Veracity data container, you may grab the [Veracity-Storage-Manager](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-developer-storage-manager/developer_storage) sample from our github Repo and create a local emulated storage.

The samples are written in NodeJs and use the [Azure Storage SDK for NodeJs](https://github.com/azure/azure-storage-java). 



### Python implementation

 
# Tutorial 
In this section you will find a collection of materials that will provide a deeper understanding and insight on how to ingest your data to a data storage.  
 
# Pattern & Practices 
In this section we will give theoretical and practical recommendations on how to best develop, design and implement your service 
 
# References 

## GitHub  
Follow our open projects related to ingest on https://github.com/veracity

## Stack Overflow
Stack Overflow is the largest, most trusted online community for developers to learn, share​ ​their programming ​knowledge. The Veracity developer team monitor Stack Overflow forumposts that include the tag Veracity
 
[Visit Stack Oerflow](https://stackoverflow.com/questions/tagged/veracity?mode=all)


 
### Video 
Link to videos related to Egest

 
# Resources  
In this section we have added resources that may provide you with additional learning.  

Wiki 
Link 

 
# FAQ 
Q: I am using Ubuntu Linux and I have issues running storage explorer 
A: Some users have reported issues with running storage explorer. We tested it successfully with the Windows desktop operation systems: Windows 7, Windows 8, Windows 10 and with the server operations systems Windows server 2008 and windows server 2012. The test failed with Ubuntu Linux 17.04 
 
 
# Price model 
The prosess of ingesting data is at the moment not subject to cost. Storage does have cost related to it, and you may find additional information HERE  
 
 
 
