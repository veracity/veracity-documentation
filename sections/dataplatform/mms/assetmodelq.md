---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# How to query the asset model

Veracity Asset model allows consumers to query data using REST api or grapghQL. 

## Query Rest api
Explore the api [Asset Model Query](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/DataFabric-MMS-Query-API-swagger.json). 

Base url: https://api.veracity.com/veracity/mms/query/

Each query is within a tenant and tenant is hence part of query path. 
The tenant-alias to be used in query is given for the environment setup for you.

## Authentication
Use bearer token and subscription key [for more details how to acquire a token](..authentication.md)

## Access rights
Only users or service principles with access to an site can access the site; [for more details how to manage users](accesscontrol.md)


## Search for sites
### By name
Search for all sites that contains "ter" in its name (using naming filter).
- Pagesize: Indicate max no of sites in return.
- SortD

In this example "dnves" is used as example tenant name
```cs
https://api.veracity.com/veracity/mms/query/dnves/api/v1/sites?start=0&pageSize=10&sortColumn=SiteName&sortDirection=0&nameFilter=ter

```
### By id
Will search for sites using exact match on id (in this case Test123)
```
https://api.veracity.com/veracity/mms/query/dnves/api/v1/sites/Test123
```

## Query for Devices
### Within one site and using product type filer
Search for all devices of type Inverter  return max 1000 (defined by pagesize)
```
https://baseurl/tenant/api/v1/sites/fb8d57eb-be14-433b-b3b9-b4df64374163/devices?start=0&pageSize=1000&sortColumn=Description&sortDirection=0&productTypeFilter=Inverter
```

### Across sites 
Will search for all Meters accross sites you have access to and return max 1000 (defined by pageSize)
```
https://api.veracity.com/veracity/mms/query/dnves/api/v1/devices?start=0&pageSize=100&sortColumn=Description&sortDirection=0&productTypeFilter=Meter
```

## View a standard

To view the standard as a list of all defined asset models (sites and all device types):
```
https://we1dnvtwappvcvquery.azurewebsites.net/dnves/api/v1/standard/standards/3.1.1
```
Use 'latest' if you do not know the latest 
```
https://we1dnvtwappvcvquery.azurewebsites.net/dnves/api/v1/standard/standards/latest
```

## Search using a specific version of standard
To return the response of your query according to a specific version of the standard, specify version in standardVersion query parameter
```
https://baseUrl/dnves/api/v1/devices?start=0&pageSize=100&sortColumn=Description&sortDirection=0&productTypeFilter=Meter&standardVersion=3.1.1

```


## GrapghQL
GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more.

GrapghQL in Veracity Asset Model is based on "Hot Chocolate" - an open-source GraphQL server for the Microsoft .NET platform that is compliant with the newest GraphQL October 2021 spec + Drafts. Hot Chocolate is compatible to all GraphQL compliant clients like Strawberry Shake, Relay, Apollo Client, and various other GraphQL clients and tools.

The grapghql endpoint uses same authentication as REST-ai.

Veracity Asset Model only supports queries in grapghQl (not mutations).

For more information, [Fetching data with grapghQL](https://chillicream.com/docs/hotchocolate/v13/fetching-data)