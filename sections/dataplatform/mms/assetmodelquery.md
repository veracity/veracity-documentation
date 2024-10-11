---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# How to query the asset model

Veracity Asset model allows consumers to query data using REST api or grapghQL. 

## Query Rest api
Explore the api [Asset Model Query](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/DataFabric-MMS-Query-API-swagger.json). 

Each query is within a tenant and tenant is hence part of query path. 
The tenant-alias to be used in query is given for the environment setup for you.

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)

**Example for Query**
In this example "dnves" is used as example tenant alias
https://api.veracity.com/veracity/mms/query/dnves/api/v1


### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).

## Access rights
Only users or service principles with access to an site can access the site; [for more details how to manage users](accesscontrol.md)


## Search for sites

### By id
Will search for sites using exact match on id (in this case Test123)
`{baseUrl}/{tenantAlias}/api/v1/sites/Test123`

This endpoint allows for using an assessment (optional), [see details](#query-site-using-assessment)

### Search by any metadata
You can search for sites using any metadata as criteria. You can combine serach criteria and decide which metadata to return in order to reduce the repsonse.

Example:

This eample returns all sites (user has access to) with Capacity AC greater than 70 and where City contains 'EL'. In addition the metadata in the response is reduced to only list SiteName, SiteId, City, Latitude and CapacityAC
```
https://api.veracity.com/veracity/mms/query/dnves/api/v1/odata/sites?$filter=CapacityAC gt 70 and contains(City, 'El')&$select=SiteName, SiteId, City, Latitude, CapacityAC
```

If $select is not specified, alle metadata fields defined are returned

In this example - dnves is used as tenant.

NOTE: No space between ?$filter=   and &$select=

#### Standard Filter Operators

|Operator | Description | Example|
|--|--|--|
|eq|Equal |  $filter=Altitude eq 385|
|ne| Not Equal| $filter=CapacityAC ne 900 |
|gt| Greater than|$filter=CapacityAC gt 900 |
|ge| Greater than or equal|$filter=CapacityAC ge 900 |
|lt| Less than | $filter=CapacityAC lt 900 |
|le| Less than or equal|$filter=CapacityAC le 900 |
|and | Logical and |$filter=Altitude gt 700 and contains(City, 'El')&$select=Altitude, City, Latitude, CapacityAC |
|or | Logical or |$filter=Altitude gt 700 or contains(City, 'El')&$select=Altitude, City, Latitude, CapacityAC |
|not| Logical not  | $filter=not contains(City, 'El')|
|contains | string contains | $filter=contains(City, 'El')|
|endswith|  string ends with | $filter=startswith(City, 'El')|
|startswith|  string starts with | $filter=endsswith(City, 'KO')|


### By name
Search for all sites that contains "ter" in its name (using naming filter).
- Pagesize: Indicate max no of sites in return.
- SortD


`{baseUrl}/{tenantAlias}/api/v1/sites?start=0&pageSize=10&sortColumn=SiteName&sortDirection=0&nameFilter=ter`
## Query for Devices
### Within one site and using product type filer
Search for all devices of type Inverter  return max 1000 (defined by pagesize)
`{baseurl}/{tenantAlias}/api/v1/sites/{siteId}/devices?start=0&pageSize=1000&sortColumn=Description&sortDirection=0&productTypeFilter=Inverter`

### Across sites 
Will search for all Meters accross sites you have access to and return max 1000 (defined by pageSize)
`{baseUrl}/{tenantAlias}/api/v1/devices?start=0&pageSize=100&sortColumn=Description&sortDirection=0&productTypeFilter=Meter`

## View a standard

To view the standard as a list of all defined asset models (sites and all device types):
`{baseUrl}/{tenantAlias}/api/v1/standard/standards/3.1.1`

Use 'latest' if you do not know current version
`{baseUrl}/{tenantAlias}/api/v1/standard/standards/3.1.1`


## Query data using a specific version of standard
To return the response of your query according to a specific version of the standard, specify version in standardVersion query parameter

`{baseUrl}/{tenantAlias}/api/v1/devices?start=0&pageSize=100&sortColumn=Description&sortDirection=0&productTypeFilter=Meter&standardVersion=3.1.1`


## Query site using assessment

Assessments allows user to create a version of the metadata defined in the assessment type. 
You can query a site by id, and specify to use a spesific assessment. The response wll be site metadata where the values defined in the assessment will be returned instead of the values defined on site.

`{baseUrl}/{tenantId}/api/v1/sites/{siteId}?assessmentName={assessmentName}`



## GrapghQL
GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more.

GrapghQL in Veracity Asset Model is based on "Hot Chocolate" - an open-source GraphQL server for the Microsoft .NET platform that is compliant with the newest GraphQL October 2021 spec + Drafts. Hot Chocolate is compatible to all GraphQL compliant clients like Strawberry Shake, Relay, Apollo Client, and various other GraphQL clients and tools.

The grapghql endpoint uses same authentication as REST-ai.

Veracity Asset Model only supports queries in grapghQl (not mutations).

For more information, [Fetching data with grapghQL](https://chillicream.com/docs/hotchocolate/v13/fetching-data)
