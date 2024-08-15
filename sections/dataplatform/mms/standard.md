---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Standard or taxonomy definition
A standards defines the asset models within your tenants. All instances of your assets will be based on the standard.


## DNV ES Standard
Energy System has defined a standard for Solar & Wind. The taxonomy defined, is defined by ES and is classified using existing standards:

Orange Button taxonomy for asset metadata
- Sunspec Modbus for solar operational data
- IEC 61400-25 for wind operation data
- IEC 81346 for asset classification



## Managing standards
Managing the standard and publishing new versions can be done using api or from the web portal (https://assetmodel.veracity.com)

Base url: https://api.veracity.com/veracity/dw/gateway/api/v2/

Explore the api [Asset Model Standard](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/DataFabric-MMS-Schema-API-swagger.json). 



## Versioning
Multiple versions of the same schema is supported and enables renaming and adding of parameters and metadata as well as adding new models (device types).

Remove parameters and metadata should be avoided because of back-compatibility.

### Publish version