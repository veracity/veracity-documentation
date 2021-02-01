---
author: Veracity
description: Description of overview
---

# Overview

The data protection and keys associated with access to storage in Veracity are built around Shared Access Signature (SAS) tokens. This enables the sharing of data, the granting of policy based access, and the revoking of granted access. Activities related to data within Veracity can, in this way, be tracked and reviewed by the owner of the container.

Keys are only possible to share with other platform users, and the SAS key may only be obtained by authenticated users.

## Types of keys

Veracity supports five different keys. For each key, the duration of the key and whether the key will be recurring can be defined.

### Write key
A write key gives the user rights to write to a container for a given amount of time, but not list or read the files. Typically this key is used for applications or for developers that should only write to a data container.

### List key
A list key gives the user the rights to list the files in the container for a given amount of time. Typically this key is used for applications that only need to show the files in the container, but not require to read the content of the files.

### Read and list key
Read and list keys give the user rights to read and list the files in the container for a given amount of time. Typically this key is used for projects, sharing data for single operations or sharing read access to analytics providers.

### Read, write and list key
A read, write and list key gives the user rights to read, write and list access to the files in the container for a given amount of time. Typically this key is used for provider services or single operations for an analyst.

### Read, write, list and delete key
Read, write, list and delete keys give the user full access to the files in the container for a given amount of time. Typically used for data managers/providers. 


## Pattern & Practices

### Best practices when sharing keys

As a data storage owner or data steward, you may share the data with other Veracity users. When you share a key, it is best practice to choose a duration as short as possible. If access to storage is going to be used over a prolonged period it is recommended that you choose the recurring key option, this means the key will need to be renewed by the user after the duration expires. The renewal of the key can be done either through the Veracity MyData page, or programmatically using the Veracity Data API.

### Best practices when using keys

When your application uses a SAS key from Veracity it is recommended that you build a call to the Veracity API for renewal of the key, prior to the accessing of the data, into your application. In this way you will always have the latest valid key.