---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Standard or taxonomy definition
A standards defines the asset models within your tenants. The standard defines different asset models where "Site" is a root model. All components are defined as "Devices" of different types. The metadata and timeseries names defines on "Site" and "Device" are inherited to all sub types of these models.

The standard supports several technologies. I.e. The technology Solar can have its own asset models defined and the technology Wind can have its own asset models.

The names of the metadata fields, their default values (if any), available values and units (if defined) and timeseries-names are defined in the standard used. 


All instances of your assets will be based on the selected technology within the standard.

Managing the standard and publishing new versions can be done using api or from the web portal (https://assetmodel.veracity.com)

## API
Explore the api [Asset Model Standard](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/DataFabric-MMS-Schema-API-swagger.json). 

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).


## DNV ES Standard
Energy System is defined a standard for Solar, Wind, Storage. The taxonomy defined, is defined by ES and is classified using existing standards:

Orange Button taxonomy for asset metadata
- Sunspec Modbus for solar operational data
- IEC 61400-25 for wind operation data
- IEC 81346 for asset classification

## Add new Asset Model
When creating new asset models from api - use 

See api explorer fo body content.
Basetype is  "Device" when a device type/component is created
Basetype is  "Site" wehna  subtype of site is created

```
POST base url/{tenant}/api/v1/{technology}/metamodels

{
  {
  "type": "string",
  "baseType": "string",
  "metadata": [
  ],
  "timeseries": [   
  ]
}
}
```

## Itemtypes
Item types are used to define "data type" and they are common for all technologies.

## Versioning
Multiple versions of the same schema is supported and enables renaming and adding of parameters and metadata as well as adding new asset models (device types).

Remove timeseries and metadata should be avoided because of back-compatibility.

### Publish version
To publish a new verson, select Publish from Draft model (action column). From api use endpoint: (and provide version and list of technologies in body)

```
POST base url/{tenant}/api/v1/standards

{
  "version": "string",
  "technologies": ["string"]
}
```

A single technology can be published and does not affect proposed work for other technologies in same standard.