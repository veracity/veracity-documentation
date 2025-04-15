---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Access control for assets
Users and service principles can only access assets they have access to. User and service principles are handled in Data Workbench.

## Workspace 
Each instance of a site needs to be linked to a workspace in Veracity Dataworkbench. Only members of that workspace can sites (assets) associated with that workspace.  

## Portfolio
A portfolio is a group of sites. A site can be part on several portfolios.

## Roles
Currently on Admin and Reader is available as roles. New roles will be added shortly.

**Admin**
- Can create site
- Can add sites in a portfolio.
- Can update site (metadata, devices, hierarchies and parameters).
- Can delete site, devices.
- Can evaluate ruleset.
- Can create assessments.

**Reader**
- Can view site information.
- Can export devices.
- Can evaluate ruleset.
- Can view standard.

**Edit standard**
- Veracity needs to onboard the users that have access to edit and publish the standard. 
- Different users can have access to edit and publish different part of the standard, based on selected technology.

## Tenant manager
Tenant managers must be added by Onboarding team, contact (mail: support@veracity.com)
- Can access all assets with admin rights.


## Query for permissions
The query api has an endpoint for returning the permissions for the user

`{baseurl}/{tenantAlias}/api/v1/permissions`

**Response**
This user has view access to all sites in one portfilio and  admin (full access) to all sites in the first portfolio
```json
[  
  {
    "resourceType": "Portfolios",
    "resourceId": "08da6777-073a-45bb-802b-c1c563b0daba",
    "accessTypes": [
      "View",
      "Update",
      "Delete"
    ]
  },
  {
    "resourceType": "Portfolios",
    "resourceId": "0cb4fa51-f645-408f-a6a5-0923d507e577",
    "accessTypes": [
      "View"     
    ]
  },
````
