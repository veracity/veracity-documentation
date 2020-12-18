---
author: Veracity
description: Description of quick start section
---

# Veracity IoT Power BI Connector
The Veracity IoT Power BI Connector is a custom data connector for Power BI that enables fetching data on behalf of the user from the Veracity IoT APIs.

## On the IoT API
The Veracity IoT API is a core platform offering on Veracity that services requests for timeseries data on assets and responds

The API is ip-firewalled in higher environments to only service requests inbound from API Management. The API also requires a valid bearer token issued for the user, which it validates and authenticates before serving the user data. The user request for data is scoped down only to the assets / channels the user has access to.

In addition the API can also service requests from applications. Applications get a bearer token from the IDP (B2C) using client credentials grant. The API does the same validation and authentication checks on these calls as well and will only service data which the application has access to (assets and channels).

## IoT API Authentication
In order to fetch data from the IoT API incoming requests must contain a bearer token. This token is issed by the identity provider (Azure B2C) using one of the supported oauth2 flows on Veracity, either implicit flow, authorization code flow or client credentials.

