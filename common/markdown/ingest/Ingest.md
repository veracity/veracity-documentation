
# Overview 
Data ingestion is the action of importing data to a data storage, for either immediate use or for use later. There are various ways to ingest data to Veracity. The best direction for you will depend on your technical ability as well your intention for using Veracity.   


This guide will show you how into ingest your data into Azure cloud. To proceed with your data ingest, you will need to be set up with a Veracity account. If you are not already set up with an account, please click here. 



Quick-Start 

- [Ingest using Azure Storage Explorer (one time data load)](#Ingest-using-Azure-storage-explorer)
- [Ingest using Blob, REST API, AZCopy or Azure CLI (continuous data load)](#Ingest-using-Blob-REST-API-AZCopy-or-Azure-CLI)


Tutorial 

- How to work in Azure Storage Explorer 

- How to work in Blob, REST API, AZCopy or Azure CLI 

- Ingest using Mac 

- Inges using Linux 

- Other 





# Quick start 
## Ingest using Azure storage explorer
When doing a manual ingest to Veracity, we recommend using Azure Storage Explorer. This independent application from Microsoft allows you to manually upload, view and interact with your data. This tool allows you to access any Veracity storage container. Azure Storage Explorer is available through Windows, macOS and Linux. 

### Download and install Azure Storage Explorer 
Download Azure Storage Explorer from http://storageexplorer.com/. Select what type of operative system you are using (Windows, Mac or Linux) and the client download will start automatically. Do not use an outdated version from the Codeplex repository, as these are most likely the versions which are shown on the screen when you use BING to search for "Azure Storage Explorer". The correct download screen should look like this:  

![](https://raw.githubusercontent.com/veracity/Documentation/master/common/images/ingest-ase-download.png?token=ATKIGzfMe8EsHLvrUimjnExhsKcQk4Doks5ZiwhZwA%3D%3D "Download Azure Storage Explorer")

If you are having problems with the installation, please visit our FAQ section for Azure
Storage Explorer.

### Step by step installation

1.	Download the executable from http://storageexplorer.com/
2.	Run the executable, you should now see a window as seen below:

![](https://raw.githubusercontent.com/veracity/Documentation/master/common/images/ingest-ase-install.png?token=ATKIG4dnUE0UbtqAKfwg3QHysrtKNVPUks5ZiwgvwA%3D%3D "Install Azure Storage Explorer")



3.	Follow the instructions provided in the installation wizard. Note that you cannot complete the installation without accepting Microsoft's terms of use
4.	Azure storage explorer is now installed, and should open automatically
After the first installation, regularly check for updates and apply them. They are indicated when available


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


## Programmatically ingest data

These applications allow you to programmatically view/interact with your data. This quick guide will show you how to do this using some common languages. For details on how the code work consult the readme file in the HelloWorld applications or the tutorials on each language in the next sections. 

Implementations:
- .NET implementation
- Java Implementation 
- NodeJs Implementation
- Python Implementation



### .NET implementation
We will in this quick start look at how to programaticaly write data to Veracity using a .NET Framework application. On Github you will find the [sample code](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-ingest-data) for this application. If you do not have access to a Veracity data container, you may grab the [Veracity-Storage-Manager](https://github.com/veracity/veracity-quickstart-samples/tree/master/101-developer-storage-manager/developer_storage) sample from our github Repo and create a local emulated storage container. 

In this sample we use the following nuget packages:
- Microsoft.WindowsAzure.Storage (client library enables working with the Microsoft Azure storage services)


First we need to create a .Net Framework application. Then add the constant holding the SAS key provided by Veracity to the Main method.

```csharp
static void Main(string[] args)
    {
    // Create the constant holding the key provided by Veracity. Add your key.
    const string veracityContainerSAS = " < your SAS key go here >";

    // Add some methods under this line


    // Hold the consol
    Console.ReadLine();
    }
```

Add the following packages to the program:

```charp
using System;
using Microsoft.WindowsAzure.Storage;
using Microsoft.WindowsAzure.Storage.Blob;
```

Then we need to create a method that can interact with the container. We add functionality to both write, but also read so that we can verify that the write operation succeded.


```csharp
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

            // To verify that the content was written to the blob, we grab the blob, and try to readd the content

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


## Ingest data usinng AzCopy
AzCopy is a command line tool used to upload and download data to or from  BLOB containers and to transfer data between BLOB containers. It is designed to give high performance and works particularly well when copying data between containers in the same locations.
However, it can also be used to upload data from a local computer or between any BLOBs in any subscriptions and locations.
AzCopy can be downloaded and installed for both Windows and Linux. After installation on Windows it is important to add the AZCopy.exe path to your system path. AZCopy can then be run either from the command prompt or from for example Windows Powershell.

The basic AzCopy command looks like this:

```batch
AzCopy /Source:\<source\> /Dest:\<Destination\> \[Options\]
```

The below examples illustrates three common scenarios, copying one file, copying several files using a mask and copying entire folders.
We assume you have obtained the appropriate access keys as described in a previous section.

(1) Copying one local file to a BLOB container:
```batch
AzCopy /Source:C:\MyLocalFolder /Dest:https ://myblob.blob.core.windows.net/MyContainer /DestKey:key /Pattern:myfile.csv
```
When copying from a BLOB container to a local computer, the option /SourceKey has to be used.

(2) Copying multiple local files to a BLOB container using a file mask:
```batch
AzCopy /Source:C:\MyLocalFolder /Dest:https ://myblob.blob.core.windows.net/MyContainer /DestKey:key /Pattern:my /S
```
This will copy all files starting with "my". Use option /S to copy more than one file.

(3) Copying a local folder to a BLOB container:
```batch
AzCopy /Source:C:\MyLocalFolder /Dest:https ://myblob.blob.core.windows.net/MyContainer /DestKey:key /S
```

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
Link to videos related to Ingest

 
# Resources  
In this section we have added resources that may provide you with additional learning.  

Wiki 
Link 

 
# FAQ 
Q: I am using Ubuntu Linux and I have issues running storage explorer 
A: Some users have reported issues with running storage explorer. We tested it successfully with the Windows desktop operation systems: Windows 7, Windows 8, Windows 10 and with the server operations systems Windows server 2008 and windows server 2012. The test failed with Ubuntu Linux 17.04 
 
 
# Price model 
The prosess of ingesting data is at the moment not subject to cost. Storage does have cost related to it, and you may find additional information HERE  
 
 
 