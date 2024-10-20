--- 
author: Veracity 
description: Veracity Services API
---

# Veracity Services API version 4

We have released the fourth version of Veracity Services API.

## Essential changes
Veracity Services API version 4 is the API used in [Veracity Tenant Management (VTM)](https://developer.veracity.com/services/tenantmanagement). Because of that, it is meant for tenant-aware applications and the endpoints are organized in the following groups.

**Endpoint groups**
* Applications: Provides methods to interact with applications within a tenant. Supports retrieving applications, verifying user licenses, and managing user and group licenses.
* Groups: Provides methods to manage groups and their members within a tenant. Supports retrieving groups, group members, and updating group properties.
* Me: Provides methods to retrieve information about the signed-in user, including their applications, groups, and tenants.
* Tenants: Provides methods to interact with tenants, including retrieving tenant details, and managing tenant administrators.
* Users:  Provides methods to manage users within a tenant, including retrieving user details, groups, and applications.

## Support for version 3
We maintain support for Veracity Services API version 3. However, if you're building a new application, we recommend that it uses version 4.

## API specification
See [the API specification for Veracity Services API version 4](https://developer.veracity.com/docs/section/api-explorer/api-explorer).

## Usage examples
See examples of how to use this API in [Veracity Tenant Management for Developers](https://developer.veracity.com/docs/section/tenantmanagement/tenantmanagement).

## Veracity Access Hub
You can use [Veracity Access Hub Guide](https://developer.veracity.com/docs/section/customerservices/accesshub) to do most of the actions that are possible through the Veracity Services API version 4.
