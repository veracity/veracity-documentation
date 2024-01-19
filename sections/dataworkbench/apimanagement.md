---
author: Veracity
description: This page explains using the API management tab in Data Workbench.
---
# API management

You can integrate APIs with Data Workbench. To do so, you need a service account.

## To add a new service account
To add a new account:
1. In your workspace, select the **API management** tab. 
2. In the left sidebar, select **Add account**. 
3. Under **Account name**, enter the name for the account.
4. Under **Contact email**, enter the contact email to the owner of this service account.
5. Under **Access to data sets**, decide whether the account should have access to all data sets in the workspace ("Grant all workspace data") or just to selected data sets ("Select data sets manually").
6. Select the **Create service account** button. 

After that, your account will be created, and you will get the values for the service account secret, ID, and API key. You will need them to [authenticate API calls](authentication.md).

**Note that** you will see the service account secret only once. Copy it and store securely. 

## To copy the base URL endpoint
To copy the base URL endpoint of a service account:
1. In your workspace, select the **API management** tab. 
2. In the left sidebar, under **Service accounts**, select an account.
3. In the row under **Endpoints base URL**, select **Copy**.

## To update a service account's name
To update the name of a service account:
1. In your workspace, select the **API management** tab. 
2. In the left sidebar, under **Service accounts**, select an account.
3. Under **Account name**, update the name.
4. Select the **Save** button.

## To update a service account's contact email
To update the name of a service account:
1. In your workspace, select the **API management** tab. 
2. In the left sidebar, under **Service accounts**, select an account.
3. Under **Contact email**, update the email.
4. Select the **Save** button.

## To update shared data sets

For a service account with "Select data sets manually" enabled, do the following to update the data sets shared with this account.
1. In your workspace, select the **API management** tab. 
2. In the left sidebar, under **Service accounts**, select an account.
3. Under **Access to data sets**: 

   To share new data sets with the account, select **Select data sets**.

   To see the details of a data set, select its name. This will open a new tab in your browser.
   
   To stop sharing the data set with the service account, select the **X** icon in the row with the data set's name.
4. To save changes, select the **Save** button.

## To regenerate a service account secret
To regenerate a service account secret:
1. In your workspace, select the **API management** tab. 
2. In the left sidebar, select a service account.
3. Next to the **Service account secret**, select **Regenerate**.

## To delete a service account
To delete a service account:
1. In your workspace, select the **API management** tab. 
2. In the left sidebar, select a service account.
3. In the bottom right corner, select the **Remove service account** button. A pop-up window will appear.
4. In the pop-up window, select the **Delete** button.

## Ready for use Python script for API management
Now, in API management, you can generate a sample Python code that will include your credentials. Then, you can download it and immediately start making API calls with it.

To generate the code:
1. Go to API management > Service accounts.
2. Select a service account.
3. Under **Generate sample Python code**, select the **Generate** button.

