---
author: Veracity
description: Create a report using Data Workbench Uploaded data sets and upload it in VAP
---

# Create a report using Data Workbench Uploaded data sets and upload it in VAP

You can use an Uploaded data set from Data Workbench in a Power BI report and then upload the report in VAP. Start by generating a SAS token for the data set.

> For data set concepts, types, and the definition of "Uploaded" data sets, [go here](../../dataworkbench/datacatalogue.md).

## To generate an access token for an Uploaded data set

You can generate access keys from the Data Workbench UI or with an API call. Access keys must have an expiry date. You can optionally enable auto renew in VAP.

> The "Key" generated in Data Workbench is the same as the SAS Token used in VAP. You will paste it in the **Credential** field when editing the resource.

### Using the Data Workbench UI
1. Open your Data Workbench workspace.
2. Go to **Data Catalogue > Created data sets**.
3. Choose a data set whose **Type** is **Uploaded**.
4. Open the data set and in the top right corner select **Generate access keys**.
5. Under **Set access level**, select **Read**.
6. Under **Set access end**, select the expiry date and time.
7. Select **Generate key**, then **Copy key**.

<figure>
  <img src="assets/generateaccesskey.png"/>
</figure>

### With an API call
Call the endpoint `/workspaces/{workspaceId}/data sets/{data setId}/sas`, authenticate, and provide:
* `{workspaceId}` as UUID
* `{data setId}` as UUID
* `durationInMinutes` as int32
* `type` set to `dfs`

> For details, [check the Data Workbench API specification](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json).

In Data Workbench, when you open a data set, you can read the following from its URL path:
- `workspaceId` (comes after `ws/`)
- `data setId` (comes after `datasets/`)

<figure>
  <img src="assets/wsdatasetinfo.png"/>
</figure>

## Connect the Uploaded data set in Power BI Desktop

> Do not use the "Web" data connector for Uploaded data sets, as this results in an empty data set.

1. Open Power BI Desktop.
2. Select **Get Data** > **Azure** > **Azure Data Lake Storage Gen2**.
3. In the connection window:
   - **URL**: paste the part of the SAS URL that is **before** the `?`.
   - **Authentication method**: select **Shared access signature (SAS)**.
   - **Token**: paste the part of the SAS URL that starts **with** `?`, including `?`.

## Load and transform data
1. After the connection succeeds, Power BI shows the data set contents.
2. Select **Transform Data** to open Power Query.
3. Make any adjustments, then select **Close & Apply**.

## Save and upload the Power BI file in VAP
1. Build visuals and save the file as `.pbix`.
2. In VAP, upload the Power BI file as a **Resource File**.
3. If the data source shows a connection error, select **Edit** on the resource file and set:
   - **Data Source Sub Type** to `DWB Structured Data Set`.
   - Paste the SAS token into **Credential**.
   - Select **Update** to apply the token.
   - Select the **refresh** icon to validate the connection.
   - Wait for "Connect to data source successfully."
   - Select **Save**.

**Remember**: The SAS Token you paste in **Credential** is the same as the Key generated in Data Workbench.

## Optional: Enable auto renew of SAS token in VAP
1. In the Edit Resource File screen, toggle **Auto Renew SAS Token** to ON.
2. Ensure both **Data Workbench Workspace ID** and **Data Set ID** are filled in.
3. Select **Save**.

> If either ID is missing, auto renew will not work.

## Optional: Use a parameter to store the token in Power BI Desktop
VAP currently has no UI to set parameters, but you can still organize your `.pbix` using a parameter.

1. In **Home**, select **Transform data** > **Transform data**.
2. In **Manage Parameters**, select **New Parameter**.
3. Name the parameter and set **Current Value**. Ensure **Required** is checked, then select **Ok**.
4. When entering connection details, use the parameter instead of pasting the token directly.

<figure>
  <img src="assets/8.png"/>
</figure>

<figure>
  <img src="assets/9.png"/>
</figure>

<figure>
  <img src="assets/10.png"/>
</figure>

<figure>
  <img src="assets/11.png"/>
</figure>

## Enable scheduled refresh in VAP
See the refresh plan details [here](../admin-tab/resource.md).

A scheduled or on-demand refresh will fail if:
* The data set schema or structure changed.
* The SAS token expired.
* The data set was deleted.

## Update data in Data Workbench and refresh in VAP
To update the data used in the report, upload a new version of the data set in Data Workbench without changing its name or structure. 
After that, refresh the resource in VAP (scheduled or manual) to load the updated data.