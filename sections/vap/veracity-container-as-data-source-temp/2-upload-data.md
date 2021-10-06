---
author: Veracity adapter for Power BI
description: Veracity container as data source - step 2
---

# 2. WHAT DO YOU NEED TO DO IN THE CONTAINER?  
When you develop your Power BI report to use data from a Veracity container there are some steps to be aware of. When this description is written there are limitations in functionality both from Microsoft Power BI REST API used by VAP and from Veracity. This document describes how you currently can set it up both from a Veracity Container, from Power BI and from VAP.

When you build a Power BI report on top of data from a container, the data source, access key and file name are stored as settings in your Power BI report. The Veracity container access key used when building the report has a maximum validity of 6 months. Once the key in your report expires, it will not be possible to refresh the report. Here you will learn the steps you have to take to make sure VAP can always refresh your report.

## 2.1	Upload data source file to your container
We assume you have Data Steward access to a container on Veracity (if not, please contact Veracity). 

Make sure you have uploaded at least one file to your Container. We will use myContainerData.csv as an example. If data changes make sure you upload a new file to the container and overwrite the file you used when building your report. The file name is case sensitive, so you must replace the old file. In VAP you can set up scheduled refresh. If you know when the data has changed you could also refresh OnDemand in VAP. 

<figure>
	<img src="assets/1.jpg"/>
</figure>

## 2.2 Share access to VAP service account

A Veracity container access key has a maximum validity of 6 months.

When you develop a Power BI report and use data from a Veracity container you use your own access key. When you upload the file int Veracity Adapter for Power BI, VAP needs to have access to your container in order to refresh the report.

To allow VAP to get a new access token/key to the container automatically you have to share a key from your container to the VAP Service account [VAP@veracity.com](mailto:VAP@veracity.com). Please click Access as shown in the image below.

<figure>
	<img src="assets/2.jpg"/>
</figure>

When sharing the key, please select ' **Set key as recurring'** , set access level to ' **Read, write and list** ' and set **duration to the longest period** . Then click Share.

<figure>
	<img src="assets/3.png"/>
</figure>

[Next](3-get-file-url.md)