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

