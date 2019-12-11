# Security

Different keys are available in Veracity but all are of the type "shared access signature" (SAS). The SAS key provides a way to grant others limited access to objects within your storage, without exposing your account key. The account key is stored within the Veracity data fabric, and is not able to be retrieved by any users.

## What is shared access signature

In Veracity, SAS tokens give you granular control over the type of access you grant to clients, including:
* The time for which the SAS is valid.
* The permissions granted by the SAS. In Veracity, these levels are:  
    1. Write
    2. Read and list
    3. Read, write and list
    4. Read, write, list and delete

* The ability to revoke the key you have shared at any time
* The ability to enable the client to renew the key, while it is only valid for a limited time when key is claimed.

## What does a key look like?

A SAS key is a string of characters, and a SAS URI also contain a protocol. An example of a SAS URI would be like this:

    https://ne1gnvdltasfsus00001.blob.core.windows.net/devcontainer9ae56656-bd3a-4d6e-b257-cfbb6241b1ea?sv=2017-04-17&sr=c&sig=HkIguyFkms26jwP420X8Rfu3q%2B9fuwO8Ob5Aeth7UfM%3D&st=2017-10-27T20%3A29%3A55Z&se=2017-10-27T22%3A30%3A02Z&sp=rwdl

You should treat this information as you would treat a key to your home. It is personal, and do not share the key. A unique key will be generated for each individual user you choose to share with.

## Key duration

A SAS key may be granted for a limited time, options for Veracity are:
* 1 hours
* 8 hours
* 1-6 months

## Recurring keys

All keys can be given a repeating property, which means the key is automatically renewed until the owner of the container revokes it. Enabling this option allows for a much lower duration on keys, which increases the security. The client who has been granted a SAS key would need to reclaim the key after the duration expire. This can either be done through the Veracity MyData, or through the Veracity API.

