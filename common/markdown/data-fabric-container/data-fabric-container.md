---
Title : "Data Fabric Container"
Author: "Brede Børhaug"
Contributors: "Rachel Hassall"
---

## Overview 
Veracity Storage Containers allow you to store unstructured data at a massive scale in block blobs. There are no limitations to the type of unstructured data you may store, and you can dump database files into the storage for sharing. You may store images, video, audio or time series. Your stored data can then easily be shared with others for data analysis, either in the cloud or on-premises at the service provider.


Quick links:

- [Specifications](#specifications)
- [Regions for storage](#regions-for-storage)
- [Availability, backup and disaster recovery](#availability-backup-and-disaster-recovery)


## Specifications
Veracity supports files of any type and size. In this section, we will provide details on the storage specifications in Veracity.
Ingress refers to all data (requests) being sent to a storage account. Egress refers to all data (responses) being received from a storage account.

All data in Veracity are stored in hot storage.

|Resource | Limitations |
| ------------- |:-------------:|
| TB per storage account | 500 TB|
| Max ingress per storage account (US Region) |	20 Gbps |
| Max egress per storage account (US Regions) |	30 Gbps |
| Max ingress per storage account (EU Regions) | 10 Gbps |
| Max egress per storage account (EU Regions) |	15 Gbps |
| Total Request Rate (assuming 1 KB object size) per storage account | Up to 20,000 IOPS, entities per second, or messages per second |



## Regions for storage 
Veracity is designed for global scalability, and will support storage all over the world. At the moment, the following regions are supported:
- East US (Virginia)
- North Europe (Ireland)
- West Europe (Netherlands)
- Norway East (Oslo)

You can select either option during the creation of the storage container in My Data or by setting the the storageLocation parameter using the provisioning API. The provisioning API contains an endpoint to retrieve the latest supported regions. 
All regions generally available will have full feature support in Veracity.


## Availability, backup and disaster recovery
The storage accounts in Veracity are deployed to the region in which the storage account owner has configured. In that region Veracity ensures Locally Redundant Storage (LRS). Veracity will replicate your data three times within the data centre, in the region in which you created your storage account. Each of the three replicas reside in separate fault domains and upgrade domains within one storage scale unit. A storage scale unit is a collection of racks of storage nodes. A fault domain (FD) is a group of nodes that represent a physical unit of failure and can be considered as nodes belonging to the same physical rack. An upgrade domain (UD) is a group of nodes that are upgraded together during the process of a service upgrade (rollout). The three replicas are spread across UDs and FDs within one storage scale unit to ensure that data is always available, even if hardware failure impacts a single rack or when nodes are upgraded during a rollout.


Veracity will not geo-replicate the data, this ensures that data governance restrictions related to replicating data within a country are met. 

### What region to choose
Veracity will create your storage in the EU by default. Upon creation you can choose one of the other supported regions, like US. If there are no regulatory reasons for choosing one region over the other, we recommend that you choose the region closest to yourself and your business partners. There are benefits from a cost perspective when data and analytics are conducted in the same region, as this reduces the costs related to transferring data. This is particularly important when there are large amounts of data involved. If you are uncertain on where to place your data, you may contact the Veracity support team to get additional guidance.

### Storage availability
There are multiple components of Veracity in play when interacting with your data. While the overall Veracity service does not explicitly state an Service Level Agreement (SLA), you will have an SLA of 99.9% with respect to your storage account. This does not include the claim of a SAS or the renewal of the SAS. Please contact the Veracity team if you would like details on the SLA for your individual case.


- We guarantee that at least 99.9%  of the time, we will successfully process requests to read data 
- We guarantee that at least 99.9%  of the time, we will successfully process requests to write data



## GitHub
Follow our open projects related to containers on https://github.com/veracity

## Stack Overflow
Stack Overflow is the largest, most trusted online community for developers to learn and share their programming knowledge. The Veracity developer team monitor Stack Overflow forum posts that include the tag Veracity Platform.

[Visit Stack Overflow](https://stackoverflow.com/questions/tagged/veracity+platform?mode=all)
 

 
