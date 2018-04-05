---
Title : "Analytics"
Author: "Brede Børhaug"
Contributors: "Rachel Hassall"
---

## Overview

The Veracity Data Platform brings people with data closer to those who can help bring knowledge and value out of that data. In this section you can read about some of the tools that you can use to help you analyse data on Veracity. In the tutorial section you have access to comprehensive guides that describe how to do this.

In order to fully utilize what is described in this document you will need a Microsoft Azure subscription.

## Tutorial

### Data Science Virtual Machine 
To get quickly started with analytics, a good option can be to create a Virtual Machine (VM) in Azure. To simplify this, we have created two handy buttons for you. Pick your favourite:

|Ubuntu|Windows Server 2016|
|:-------------:|:-------------:|
[![Deploy to Azure](https://veracityprod.blob.core.windows.net/cdn/assets/deploybutton.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FVeracity%2Fveracity-quickstart-samples%2Fmaster%2F101-data-science-virtual-machine%2Fdata-science-virtual-machine-Linux%2Fdeployazure.json) |[![Deploy to Azure](https://veracityprod.blob.core.windows.net/cdn/assets/deploybutton.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FVeracity%2Fveracity-quickstart-samples%2Fmaster%2F101-data-science-virtual-machine%2Fdata-science-virtual-machine-Windows%2Fazuredeploy.json) 

#### Data Science Virtual Machine Linux (Ubuntu)
The Data Science VM's come bundled with lots of nice tools pre-installed for you. The highlights are:

- Microsoft R Server 9.1 with Microsoft R Open 3.3.3
- Anaconda Python 2.7 and 3.5
- JupyterHub with sample notebooks
- Apache Drill for querying non-relational data using SQL
- Spark local 2.1.1 with PySpark and SparkR Jupyter kernels
- Single node local Hadoop (HDFS, Yarn)
- Azure command-line interface
- Visual Studio Code, IntelliJ IDEA, PyCharm, and Atom
- JuliaPro, a curated distribution of Julia Language and tools
- Vowpal Wabbit for online learning
- xgboost for gradient boosting

For the complete list, check out this [link](https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/overview)

#### Data Science Virtual Machine Windows 2016
The Data Science VM's come bundled with lots of nice tools pre-installed for you. The highlights are:

- Microsoft R Server - Dev. Ed. (Scalable R)
- Anaconda Python
- SQL Server 2016 Dev. Ed. - With In-Database R analytics
- Microsoft Office 365 ProPlus BYOL - Shared Computer Activation
- Julia Pro + Juno Editor
- Jupyter notebooks
- Visual Studio Community Ed. + Python, R & node.js tools
- Power BI Desktop
- Deep learning tools e.g. Microsoft Cognitive Toolkit (CNTK 2.1), TensorFlow & mxnet
- ML algorithm libraries e.g. xgboost, Vowpal Wabbit
- Azure SDKs + libraries for various Azure Cloud offerings. Integration tools are included for: 
    1. Azure Machine Learning
    2. Azure Data Factory
    3. Stream Analytics
    4. SQL Data Warehouse
    5. Hadoop + Apache Spark (HDICluster)
    6. Data Lake
    7. Blob storage
    8. ML & Data Science tutorials as Jupyter notebooks

### Analytics using Azure Machine Learning Studio
This section is a basic tutorial on how to set up a Machine Learning experiment on Microsoft Machine Learning Studio and use data stored in your Veracity data container as input.

In particular, you will find some guidance on:
-	how to set up a Machine Learning Workspace on your Azure subscription
-	how to import data into your ML experiment in Microsoft Machine Learning Studio, either from your local drive or from a Veracity container that you own or that is shared with you
-	how to incorporate custom Python scripts into a ML experiment on Microsoft Machine Learning Studio
-	how to export data back into Veracity once you have performed your data analytics with Microsoft Machine Learning Studio

#### Create a machine learning workspace
In order to start using Microsoft Machine learning studio, you need to create a machine learning workspace. You do that in two ways. You could just press this button:

[![Deploy to Azure](https://veracityprod.blob.core.windows.net/cdn/assets/deploybutton.png)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FVeracity%2Fveracity-quickstart-samples%2Fmaster%2F101-azure-machine-learning-studio-workspace%2Fdeployazure.json) 

or you can do it in the following way:

1.	Log in into https://portal.azure.com/ with your Microsoft Azure credentials
2.	On the Azure Portal, select the “New” icon, then “Internet of Things” and then “Machine Learning Workspace”
3.	Insert the details required for creating your workspace (see the guide provided here: [https://docs.microsoft.com/en-gb/azure/machine-learning/machine-learning-create-workspace](https://docs.microsoft.com/en-gb/azure/machine-learning/machine-learning-create-workspace)
4.	Note that a Storage Account must be associated to your Machine Learning Workspace. You can either use an existing storage account or create a new one.

NOTE: It will reduce cost and latency if the machine learning workspace is created in the same region as where the data you will work with is located. You can check My Data to verify the location of your data.

####	Upload data into your storage account
If you have data that you want to upload to your storage account, you can proceed as follows using Azure storage explorer.

An easy way to upload and manage data on your storage is to use Microsoft Azure Storage Explorer application. Download and install the explorer from: https://azure.microsoft.com/en-us/features/storage-explorer/

1.	Launch the program and in the main window select “Add account” 
2.	In the pop-up window, select “Use a shared acces signature (SAS) URI or connection string” and then “next”
3. Click "Use a SAS URI" and paste in the SAS key you can obtain from [My Data](https://www.veracity.com/mydata), and click "next" and "connect".
4.	The Veracity container will now be available under "(SAS-Attached Services)"
5. You can now drag and drop files into Veracity

Additional details can be found under [here](https://developer.veracity.com/doc/ingest)

####	Open your machine learning workspace in Azure Machine Learning Studio
We now want to perform some machine learning and data analytics using our data. Having set up a Machine Learning Workspace, proceed as follows:
1.	Log in into [https://portal.azure.com/](https://portal.azure.com/)
2.	Under “All resources”, locate and select the Machine Learning Workspace that you previously created, then select “Overview”
3.	Click on “Launch Machine Learning Studio”
4.	On the new webpage, select “my experiments”, this will launch the Machine Learning Web Studio app

#### Create and access experiments in machine learning studio
In Machine Learning Studio, an experiment is the virtual space in which you can perform your data analytics. To perform any machine learning we first have to create an experiment.

1.	In the lower part of the Machine Learning Studio webpage, select “+NEW” and then “Experiment” and then “Blank Experiment”
2.	You are prompted to a new blank experiment. You can now drag and drop modules from the left panel into the experiment canvas to create your model. 
3.	Remember to save your experiment, this is done using the save option in the lower part of the screen
4.	Once created, you can access the experiment from the “Experiments” tab on the left part of the screen

#### Import data into your machine learning experiment
You normally want to import data in your experiment. At this point, it can get interesting depending on where in the world your target data is stored. It is worth bearing in mind that there is less cost related to moving data within a region, than transferring over large distances. This is particularly important when the data is of TB or PB size.

##### Import data from Veracity.

1.	Access your experiment in ML Studio
2.	Under “Data Input and Output”, locate the “Import Data” module and drag it into the experiment sheet. Select the block and then “Launch Import Data Wizard”  
3.	Select the “Web URL via HTTP” in the Launch Import Data Wizard, and then the “next” arrow 
4.	You now have to provide a data source URL, which is (almost) the SAS URL you received. Note that, for the Import Data module to work the SAS URL must refer to a specific file and not to a folder or to a container. If you received an SAS URL pointing directly to the dataset file you want to import (and not to its container), simply copy and paste that URL into the “Data source URL” field of the Data Import Wizard. If your URL points to the container, you first have to modify the SAS URL so that it refers directly to the file of interest. For example, you may receive an SAS URL of the following form:

```url
https://veracitydeveloper.blob.core.windows.net/container-developer-test?st=2017-08-08T13%3A42%3A00Z&se=2017-08-09T13%3A42%3A00Z&sp=rwdl&sv=2015-12-11&sr=c&sig=PlIPcYzFQHGPXJith1vIZ%2FMuLWDQAJSFUDsDbP4ItMw%3D

https://  <-- Protocol
  veracitydeveloper  <-- Storage name
  .blob.core.windows.net  <-- Blob host
  
  /container-developer-test  <-- Container
    ?st=2017-08-08T13...  <-- SAS token
```

From analyzing the above URL, we can understand that it refers to a container named “container-developer-test”, hosted in storage named “veracitydeveloper”. The last part of the URL (following the container name) is the SAS token that grants you access to the storage for a limited time frame. Let us now assume that the container hosts a folder named “folder_test” and a file named “file_test.csv” which you want to import in your machine learning experiment. You can then modify the URL as:

```url
https://veracitydeveloper.blob.core.windows.net/container-developer-test/folder_test/file_test.csv?st=2017-08-08T13%3A42%3A00Z&se=2017-08-09T13%3A42%3A00Z&sp=rwdl&sv=2015-12-11&sr=c&sig=PlIPcYzFQHGPXJith1vIZ%2FMuLWDQAJSFUDsDbP4ItMw%3D
```

By analysing the above URL, you can see that the SAS token has not been modified, while we have added the path to the desired csv file in between the container name and the SAS token portions of the URL.
You can now use the modified URL in the Import Data module.
 
5.	Select the “next” arrow to terminate the Import Data module setup. 
6.	To actually import the data contained in the specified file into your machine learning experiment, you have to run the experiment. You can also run the Import Data module only and not the entire experiment by right clicking on the module and select “Run Selected”.
7.	Once the file is imported, you can save the data by clicking on the output node of the Import Data block and selecting “Save as Dataset”, so that you can easily access the data it in the future:
 
It is advisable to save the dataset after having imported it, otherwise you will have to run the import data module every time you re-open the experiment. This can be very time (and resource) consuming, depending on the size of the dataset.
 
##### Import data into your experiment from a previously saved dataset
All your saved datasets will be available under the “Saved Datasets” tab. To use them in your project, simply drag and drop the dataset on the Experiment canvas:
1.	Access your experiment
2.	On the left side of the screen, select “Saved Dataset”
3.	Select the dataset you are interested into and drag and drop it on the Experiment canvas.

#### Perform data analytics
You can now use the imported data as input for your machine learning experiment.

Different options exist as to how to execute your analytics, it's possible to:
1.	Use the built-in modules to perform different kind of analytics (from basic statistical analysis, to data manipulation and on to machine learning). The advantage of using the built-in module is that there is no need to write code. The downside is that there is limited flexibility in the tuning of algorithms.
2.	Perform the data manipulation and analytics that you want by leveraging the “Execute Python Script” module, the “Execute R script” module and the “Create R model” module.

We are not going to describe how to use the built-in analytic tools of Machine Learning Studio.

For including a custom Python script into your experiment, follow these 5 steps:

1.	Access your Experiment
2.	From the left panel, select “Python Language Module” tab and then drag the “Execute Python Script” module into the experiment’s canvas:
3.	The module has 3 import ports and 2 output ports. Two of the input ports can be used as data input, while the third port can be used to import Python script bundles (in zip format). These optional zip bundles must first be uploaded as datasets (See Section 6.1) and then dragged into the experiment just like any other dataset. The first output port contains the output of the script, which must be in a Python Pandas library DataFrame format. The second output port is used to display both the Python console output and PNG graphics (possibly created by the Python script) using the Python interpreter.
4.	To enter your code, select the “Execute Python Script”. Then, on the right panel which appears, click on the “Pop-out the screen editor” icon.
5. You can now enter your code in the popped-out window.

#### Save the results as a dataset in Machine Larning Studio
The output of every module can be saved as a dataset and then re-used in an other experiment. To do so, simply right click on the output port and select “Save as Dataset”. This dataset can now be used in another experiment.

#### Upload a dataset from Machine Learning Studio to Veracity
You may want to upload your resultant dataset from your analysis back to the Veracity Storage Account associated with your machine learning Workspace.
To do so, you can use the “Export Data” module.

The key you already have for the Veracity container needs to be reused, make sure your key has write access to the storage. The SAS key will be in this form:
https://veracitydeveloper.blob.core.windows.net/container-developer-test?st=2017-08-28T16%3A03%3A00Z&se=2017-08-29T16%3A03%3A00Z&sp=rwdl&sv=2015-12-11&sr=c&sig=9ibuxt04shaWDxwZB2WmeL8wUkYpaswRKKe%2FUoP3qvQ%3D
From analyzing the above URL, we can understand that it refers to a container named container-developer-test on a storage named “veracitydeveloper”. The last part of the URL is the SAS token that grants you access to the storage for a limited time frame.
Now:
1.	Access your experiment in the Machine Learning Studio web page
2.	From the “My Datasets” tab on the left side of the screen, select the data you are interested in, (e.g. “file_test.csv”), and drag it into the experiment canvas 
3.	On the left side of the screen, select the “Data Input and Output” tab and drag the “Export Data” module into the experiment canvas
4.	Connect the output port of the dataset module to the input port of the “Export Data” module.
5.	Select the “Export Data” module, and fill in the information on the right panel:
    a.	Set Azure Blob Storage as your data destination
    b.	Set “SAS” as “Authentication type”
    c.	Under “SAS URL”, you must enter the path to the file you want to upload. This path is obtained by modifying the SAS URL you         received so that it points to the container and possible subfolder you are interested into.
    Let's now assume that we want to upload our dataset, naming it file_test_SAS.csv, into a folder named “output_test”, to be stored in    the container “container-test” which is hosted on the storage account.
    You can then write the URL as:
    https://veracitydeveloper.blob.core.windows.net/container-developer-test/output_test/file_test_SAS.csv?st=2017-08-28T16%3A03%3A00Z&se=2017-08-29T16%3A03%3A00Z&sp=rwdl&sv=2015-12-11&sr=c&sig=9ibuxt04shaWDxwZB2WmeL8wUkYpaswRKKe%2FUoP3qvQ%3D
    Note that if the subfolder “output_test” does not exist, it will be created in the process.
6.	Run the experiment:

### GitHub  
Follow our open projects related to ingest on https://github.com/veracity

### Stack Overflow
Stack Overflow is the largest, most trusted online community for developers to learn and share their programming knowledge. The Veracity developer team monitor Stack Overflow forum posts that include the tag Veracity Platform. 

[Visit Stack Overflow](https://stackoverflow.com/questions/tagged/veracity+platform?mode=all)
