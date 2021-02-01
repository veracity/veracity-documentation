---
author: Veracity
description: Description of security section
---

# Security
Various keys are available in Veracity and all are of the type "Shared Access Signature" (SAS). The SAS key provides a way to grant platform users limited access to objects within your storage, without exposing your account key. The account key is stored within Veracity data fabric, and cannot be retrieved by any users.

## What is a Shared Access Signature (SAS)?
In Veracity, SAS tokens give you granular control over the type of access you grant to clients, including:

- The time for which the SAS is valid.
- The permissions granted by the SAS. In Veracity, these levels are: 
    1. Write
    1. List
    1. Read and list
    1. Read, write and list
    1. Read, write, list and delete
- The ability to revoke the key you have shared
- The ability to enable the client to renew the key, while it is only valid for a limited time when key is claimed.

### What does a key look like?
A SAS key is a string of characters, and a SAS URI also contain a protocol. An example of a SAS URI:
```
https://ne1gnvdltasfsus00001.blob.core.windows.net/devcontainer9ae56656-bd3a-4d6e-b257-cfbb6241b1ea?sv=2017-04-17&sr=c&sig=HkIguyFkms26jwP420X8Rfu3q%2B9fuwO8Ob5Aeth7UfM%3D&st=2017-10-27T20%3A29%3A55Z&se=2017-10-27T22%3A30%3A02Z&sp=rwdl
```
You should treat this information as you would treat a key to your home. It is personal, and do not share the key. A unique key will be generated for each individual user you choose to share with.

## Key duration
A SAS key can be granted for a limited time, the options are:

    - 1 hour
    - 8 hours
    - 1, 2, 3, 4, 5 and 6 months
    
Note that you share the right to claim a key. The person the key is shared with, may claim the key at any time after the key is shared. The timer will start only once the key has been claimed though the portal or through the data API. It is strongly recommended that the duration of the key is limited. There is an auto refresh option, enabling the client to reclaim the key if necessary.

## Recurring keys
All keys can be given an `autoRefreshed` property, which means the key can be renewed automatically, until the owner of the container revokes it. Enabling this option allows for a much lower duration on keys, which increases the security. The client who has been granted a SAS key would need to reclaim the key after the duration expire. This can either be done through Veracity MyData, or through the Veracity Data API.

## Revoking access
All keys are granted for a limited time (see [Key Duration](#key-duration)). Once the key is created, it will be active until the time expires. If the `autoRefreshed` property is set on the access share, a new key can be retrieved via the Data API or the MyData UI. 
When access is revoked, the auto refresh possibility will be disabled, and no new keys can be retrieved. 
> **!** Existing keys will remain to be active for the remainder of the time window.

In case a key has not been generated yet, then the access is revoked immediately upon revoke.

Best pratice is to grant a key with a short time window. For example 1 hour, set the possibilty for auto refresh and renew the key automatically via the API. A user will then have maximum 1 hour of access remaining after it has been revoked. 

