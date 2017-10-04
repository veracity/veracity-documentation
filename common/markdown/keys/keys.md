# Overview 
The data protection and keys assosiated with access to storage in Veracity are built around shared access signature (SAS). This enable sharing of data, where access is granted based on policies, and where the granted access can be revoked at any time. The activity related to the data can in this way be tracked by the container owner, and reviewed in the container owner.


Short links:
- [Security](#security)
- [Write key](#write-key)
- [Read and list](#read-and-list)
- [Read, write and list](#read-write-and-list)
- [Read, write, list and delete](#read-write-list-and-delete)


# Security
All the different keys available in Veracity are of the type "shared access signature" (SAS) keys. The SAS key provides a way to grant limited access to objects in your storage to others, without exposing your account key. The account key is stored with Veracity data fabric, and is not able to be retrieved by any users. 

## What is shared access signature
In Veracity the SAS gives you granular control over the type of access you grant to clients who have the SAS, including:

- The time which the SAS is valid.
- The permissions granted by the SAS. In Veracity these levels are: 
    1. Write
    2. Read and list
    3. Read, write and list
    4. Read, write, list and delete
- You may revoke the key you have shared at any time
- You can enable the client to renew the key, while it is only valid for a limited time when key is claimed.

[](https://veracitydevtest.blob.core.windows.net/static-documentation/keys-share.PNG)


## Key duration
A SAS key may be granted for a limited time, where the options in Veracity are:
    - 1 hours
    - 8 hours
    - 1, 2, 3, 4, 5 and 6 months
Note that when a key is shared one share the right to claim a key. The person who have recieved the key may claim that key at any time, and from that point on the timer will start. It is strongly recomended that one limit the duration on the key, and rather add the repeat/recuring option, enabling the client to reclaim the key.

## Recuring keys
All keys can be given a repeating property, which means it is automatically renewed until the owner of the container revokes it. Enabling this option allow for much lower duration on keys, which increase the security. The client who have been granted a SAS key, would need to reclaim the key after the duration expire. This can either be done through the Veracity MyData, or through the Veracity API.



# Type of keys 
Veracity support 4 different keys, where one can define the duration of the key, and the if the key will be recuring.

## Write key
Write key gives the user rights to write to a container for the given amount of time, but not list the content. Typically used for applications or developers that should only write to a data container.

## Read and list
Read and list key gives the user rights to read a container and browse the content of the container for the given amount of time. Typically used for projects, sharing data for single operations or sharing read access to Analytics Providers.

## Read, write and list
Read, write and list key gives the user rights to read, write and browse the content of a data container for the given amount of time. Typically used for Provider Services or single operations for an analyst.

## Read, write, list and delete
Read, write, list and delete key gives the user full access to the content of your data container for the given amount of time. Typically used for data managers/providers. 


# Pattern & Practices 
How to securely use keys
 
# References 

# GitHub  
Follow our open projects related to keys on https://github.com/veracity

# Stack Overflow
Stack Overflow is the largest, most trusted online community for developers to learn, share​ ​their programming ​knowledge. The Veracity developer team monitor Stack Overflow forumposts that include the tag Veracity
 
[Visit Stack Oerflow](https://stackoverflow.com/questions/tagged/veracity?mode=all)
 
# Resources  

 
# FAQ 

 