---
Title : "Data Fabric Keys"
Author: "Brede Børhaug"
Contributors: "Rachel Hassall"
---

## Overview 
The data protection and keys associated with access to storage in Veracity are built around shared access signature (SAS) tokens. This enables the sharing of data, the granting of policy based access, and the revoking of granted access at any time. Activity related to data within Veracity can, in this way, be tracked and reviewed by the container owner.

Keys are only possible to share with other platform users, and the SAS key may only be obtained by authenticated users.


Short links:
- [Security](#security)
- [Write key](#write-key)
- [Read and list](#read-and-list-key)
- [Read, write and list](#read-write-and-list-key)
- [Read, write, list and delete](#read-write-list-and-delete-key)


## Security
Different keys are available in Veracity but all are of the type "shared access signature" (SAS). The SAS key provides a way to grant others limited access to objects within your storage, without exposing your account key. The account key is stored within the Veracity data fabric, and is not able to be retrieved by any users.

### What is shared access signature
In Veracity, SAS tokens give you granular control over the type of access you grant to clients, including:

- The time for which the SAS is valid.
- The permissions granted by the SAS. In Veracity, these levels are: 
    1. Write
    2. Read and list
    3. Read, write and list
    4. Read, write, list and delete
- The ability to revoke the key you have shared at any time
- The ability to enable the client to renew the key, while it is only valid for a limited time when key is claimed.

[](https://veracitydevtest.blob.core.windows.net/static-documentation/keys-share.PNG)

#### What does a key look like?
A SAS key is a string of characters, and a SAS URI also contain a protocol. An example of a SAS URI would be like this:
```ps
https://ne1gnvdltasfsus00001.blob.core.windows.net/devcontainer9ae56656-bd3a-4d6e-b257-cfbb6241b1ea?sv=2017-04-17&sr=c&sig=HkIguyFkms26jwP420X8Rfu3q%2B9fuwO8Ob5Aeth7UfM%3D&st=2017-10-27T20%3A29%3A55Z&se=2017-10-27T22%3A30%3A02Z&sp=rwdl
```
You should treat this information as you would treat a key to your home. It is personal, and do not share the key. A unique key will be generated for each individual user you choose to share with.

### Key duration
A SAS key may be granted for a limited time, options for Veracity are:

    - 1 hours
    - 8 hours
    - 1, 2, 3, 4, 5 and 6 months
    
Note that one share the right to claim a key. The person the key is shared with, may claim the key at any time after the key is shared. The timer will start only once the key has been claimed though the portal or though the provisioning API. It is strongly recommended that the duration of the key is limited. There is a repeat/recurring option, enabling the client to reclaim the key if necessary.

### Recurring keys
All keys can be given a repeating property, which means the key is automatically renewed until the owner of the container revokes it. Enabling this option allows for a much lower duration on keys, which increases the security. The client who has been granted a SAS key would need to reclaim the key after the duration expire. This can either be done through the Veracity MyData, or through the Veracity API.



## Types of keys 
Veracity supports 4 different keys. For each key, the duration of the key and whether the key will be recurring can be defined.

### Write key
A write key gives the user rights to write to a container for a given amount of time, but not list the content. Typically this key is used for applications or for developers that should only write to a data container.

### Read and list key
Read and list keys give the user rights to read a container and browse the content of the container for a given amount of time. Typically used this key is used for projects, sharing data for single operations or sharing read access to analytics providers.

### Read, write and list key
A read, write and list key gives the user rights to read, write and browse the content of a data container for a given amount of time. Typically this key is used for provider services or single operations for an analyst.

### Read, write, list and delete key
Read, write, list and delete keys give the user full access to the content of your data container for a given amount of time. Typically used for data managers/providers. 


## Pattern & Practices 

### Best practices when sharing keys
A data storage owner or a data steward may share the data in their containers with other users. When they share a key, it is best practice to choose as short a duration as possible for the key. 

In general the following should be taken into consideration when sharing keys:

- Give only the access the user requires to your data, if they just need to read your data, don't give the user write/delete permissions as well.
- If access to storage is going to be used over a prolonged period it is recommended that you choose the recurring key option
- The recurring key option forces the user to renew the key when it expires, which is more secure than long duration keys
- The renewal of the key can be done either through the Veracity MyData Page (under access settings on container) or programmatically using the Veracity Data API.


### Best practices when using keys
- When your application uses a SAS key from Veracity it is recommended that you build a call to the Veracity API for renewal of the key, prior to the accessing of the data, into your application. In this way you will always have the latest valid key. 
- When retrieving a key, treat it like any other secret and store it securely.



## GitHub  
Follow our open projects related to Veracity data fabric keys on https://github.com/veracity

## Stack Overflow
Stack Overflow is the largest, most trusted online community for developers to learn and share their programming knowledge. The Veracity developer team monitor Stack Overflow forum posts that include the tag Veracity Platform.

[Visit Stack Overflow](https://stackoverflow.com/questions/tagged/veracity+platform?mode=all)

 
