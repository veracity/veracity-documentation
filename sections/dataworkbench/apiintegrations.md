---
author: Veracity
description: This page explains using the API integrations tab in Data Workbench.

# API integrations

You can integrate APIs with Data Workbench. To do so, you need a service account.


## Add a new service account
To add a new account:
1. In your workspace, select the **API Integrations** tab. 
2. In the left sidebar, select **Add account**. 
3. Enter the name for the account.
4. Select **Add**. 

After that, your account will be created, and you will get the values for the service account secret, ID, and API key. You will need them to [authenticate API calls](authentication.md).

**Note that** you will see the service account secret only once. Copy it and store it securely. 

## Decide on access to data sets
By default, a service account has access to all data sets in a workspace. However, you can limit its access to specified data sets.

To limit access to specified data sets:
1. In your workspace, select the **API Integrations** tab. 
2. In the left sidebar, select a service account. 
3. Under **Access to data sets**, select **Select data sets manually**.
4. Choose data sets that should be available to this account. 

The datasets you have selected will be listed in the service account. To see details of a dataset, hover over it. 

To revoke access to a dataset, find it in the list, and select the **X** symbol next to its name.

## Regenerate service account secret
To regenerate a service account secret:
1. In your workspace, select the **API Integrations** tab. 
2. In the left sidebar, select a service account.
3. Next to the **Service account secret**, select **Regenerate**.