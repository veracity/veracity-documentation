---
Title : "Data Fabric Container"
Author: "Brede Børhaug"
---

# Overview 
Veracity Storage Containers are allowing you to store unstructured data at a massive scale in block blobs. There are no limitations to what type of unstructured data you may store, and you may also dump database files into the storage for sharing. You may store images, video, audio or time series. Your stored data can then easily be shared with others for data analysis either in the cloud or on-premises at the service provider.


Quick links:

- [Specifications](#spesifications)
- [Regions for storage](#regions-for-storage)
- [Availability, backup and disaster recovery](#availability-backup-and-disaster-recovery)


# Specifications
Veracity support file of any type and size. In this section, we will provide details on the storage Specifications in Veracity.

|Resource | Limitations |
| ------------- |:-------------:|
| TB per storage account | 500 TB|
| Max ingress per storage account (US Region) |	20 Gbps |
| Max egress per storage account (US Regions) |	30 Gbps |
| Max ingress per storage account (EU Regions) | 10 Gbps |
| Max egress per storage account (EU) |	15 Gbps |
| Total Request Rate (assuming 1 KB object size) per storage account | Up to 20,000 IOPS, entities per second, or messages per second |

Ingress refers to all data (requests) being sent to a storage account. Egress refers to all data (responses) being received from a storage account.

All data in the Veracity are stored in hot storage.

# Regions for storage 
Veracity is designed for global scale, and will support storage all over the world. At the moment, there are two regions in general availability in Veracity, one in EU (Northe Europe) and one in USA (East US). You are able to select this during the creation of the storage container in My Data or by setting the the storageLocation parameter using the provisioning API. All regions in general availability will have full feature support in Veracity.


# Availability, backup and disaster recovery
The storage accounts in Veracity are deployed to the region the storage account owner configures. In that region Veracity ensure Locally redundant storage (LRS). Veracity will replicate your data three times within the datacenter in the region in which you created your storage account. Each of the three replicas each reside in separate fault domains and upgrade domains within one storage scale unit. A storage scale unit is a collection of racks of storage nodes. A fault domain (FD) is a group of nodes that represent a physical unit of failure and can be considered as nodes belonging to the same physical rack. An upgrade domain (UD) is a group of nodes that are upgraded together during the process of a service upgrade (rollout). The three replicas are spread across UDs and FDs within one storage scale unit to ensure that data is available even if hardware failure impacts a single rack or when nodes are upgraded during a rollout.

Veracity will not geo-replicate the data to ensuring that restrictions related to replicating data only within a country due to data governance requirements are met. 

## What region to choose
Veracity will create your storage in EU as default. You may choose to switch that to US when you create the storage. If there are no regulatory reasons for choosing one region over the other, we recommend that you choose the region closest to yourself and your business partners. There are benefits from a cost perspective that data and analytics are conducted in the same region. This reduce the costs related to transferring data. This is in particular important when there are large amounts of data involved. If you are uncertain of where to place your data, you may contact the Veracity support to get additional guidance.

## Storage availability
There are multiple components of Veracity in play when interacting with your data. While the overall Veracity service does not explicitly state an SLA, you will have an SLA of 99.9% with respect to your storage account. This does not include the claim of a SAS or renewal of the SAS. Please contact the Veracity team for details on the SLA in the individual case.

- We guarantee that at least 99.9%  of the time, we will successfully process requests to read data 
- We guarantee that at least 99.9%  of the time, we will successfully process requests to write data



# GitHub
Follow our open projects related to containers on https://github.com/veracity

# Stack Overflow
Stack Overflow is the largest, most trusted online community for developers to learn, share their programming knowledge. The Veracity developer team monitor Stack Overflow forumposts that include the tag Veracity Platform.

[Visit Stack Overflow](https://stackoverflow.com/questions/tagged/veracity+platform?mode=all)
 

 
