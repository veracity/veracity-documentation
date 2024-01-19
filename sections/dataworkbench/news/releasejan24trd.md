---
author: Veracity
description: This is the changelog for the January 2024 third release of Data Workbench.
---

# January 2024 third release

Read this page to learn what has changed in Veracity Data Workbench with the January 2024 third release.

## Changes in existing features
This section covers changes in existing features.

### Connector and connections renamed to data integrations
We have renamed connectors and connections to 'Data integrations'. 

### Removed the word 'connector' from some names
We have renamed the following names:
* OVD Connector to Operational Vessel Data.
* DNV Maritime Production Platform Connector to DNV Maritime Production Platform.
* For ExternalConnectors.Ovd, renamed the Swagger title from 'Swagger OVD Connector {ENV}' to 'Swagger OVD {ENV}'.
* For TemplateConfig templates/templates.tsx connector,  renamed "OVD Connector" to "Operational Vessel Data".
* For templates/types.tsx, renamed TemplateConfig 'OVD Connector' to 'perational Vessel Data'.
* For ShareDatasetPage.tsx, renamed .includes('ovd') to .includes('operational vessel data').

### Renamed API integrations tab to API management
We have renamed the API integrations tab to API management.

### Some API endpoints accept empty body requests with POST
Now, the following endpoints accept empty body for POST requests and do not return an error:
* https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/datasets/query endpoint
* https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceId}/datasets/{datasetId}/query endpoint
* https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId}/datasets/{datasetId}/query endpoint