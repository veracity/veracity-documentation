---
author: Veracity
description: Overview of the Resource tab in the admin tab.
---

# Resources

The 'Resources' tab consists of the **File** subtab (that opens by default) and the <a href="#webapp">**Web App** subtab</a>.

Resources are shown in a table and each resource is presented in one row. Some columns are sortable which is inidcated by arrow symbols next to the column name. To sort the column, select its name.

In the **Actions** column, you can:
* See the history of the changes done to the resource (1).
* Edit the resource (2).
* Delete the resource (3).
* Download the resource which file type is .PBIX (4). 

Note that:
* Due to limitations set by Microsoft, you cannot download a large .pbix. It may time out after 4 minues. If it happens, send a support ticket to get help to download the report. For more information, go [here](https://learn.microsoft.com/en-us/power-bi/create-reports/service-export-to-pbix#limitations-when-downloading-a-report-pbix-file).
* Downloading .PBIX file types is only possible if a System Admin enabled it. To enable the download of Power BI files, on the **Config** page, in the **Tenant Properties**, select **Edit** and toggle on **Allow download Pbix**.


<figure>
	<img src="assets/resource_actions.png"/>
</figure>

## To find a SAS token
Your report can use Data Workbench data sets as data source. If it does, you will be prompted to provide a SAS token for this data set. 

To generate a SAS token in Data Workbench UI, follow [the instructions](https://developer.veracity.com/docs/section/dataworkbench/filestorage/filestorage#to-generate-a-sas-token).
To generate a SAS token with Data Workbench API, refer to the API specification:
1. Under Data sets, call the `workspaces/{workspaceId}/datasets/{datasetId}/sas` endpoint to get a readonly SAS token for a workspace data set, including an uploaded data set. [See the detailed instructions here](../file-storage-as-data-source/create-report.md).
1. Under Storages, call the `/workspaces/{workspaceId}/shares/{shareId}/storage/sas` to get a SAS token for a data set in File Storage that was shared with you. [See the Data Workbench API specification for the details on this endpoint](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json).


## File

Once you have built your report in Power BI, you can upload it into VAP and share access to it with your clients. By default, VAP will use the data sources from the report, but you can override and update them when uploading a file. For details on data sources and security, go [here](../data.md).

### Refresh Schedule Plan

Data Admins, Report Admins, and System Admins can access Refresh Schedule Plans on the Resources page and plan when the reports should be refreshed.

To schedule refresh plans for reports:
1. In the top right corner of Resources > File, select the schedule icon.
2. In the panel that shows, **Add** a new plan, **Edit** an existing plan, or **Delete** a plan.

When you have scheduled a refresh plan, you can apply it to reports.

<figure>
	<img src="assets/schedule.png"/>
</figure>

### To apply a refresh plan
To apply a refresh plan to a file:
1. In the row with a Power BI report (File Type must be .PBIX), in the **Refresh** column, select the schedule icon.
2. Under **Select a Schedule Plan**, select a Refresh Schedule Plan.
3. In the bottom right corner of the panel, select **Save**.

Note that the scheduled refresh of paginated reports in .RDL format is not supported.

<figure>
	<img src="assets/scheduleicon2.png"/>
</figure>

### To refresh a file on demand
You can apply an on-demand refresh on Power BI reports (File Type must be .PBIX ord .RDL) which datasource is a semantic model. This functions allows you to refresh the data in your reports whenever you need the most current information. We recommend you use this feature for the reports relying on real-time data or requiring frequent updates.

To refresh a file on demand, in the row with a Power BI report, under **Refresh**, select the **Refresh Report** icon.

<figure>
	<img src="assets/refreshreport.png"/>
</figure>

**Note that** most Power BI semantic models using dynamic data sources cannot be refreshed in a paginated report. To check if your dynamic data source can be refreshed, follow [this instruction](https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-data#refresh-and-dynamic-data-sources).

### To upload a file

To upload a file:
1. In the top right corner, select the plus icon. Alternatively, from the left sidebar, select the plus icon and the **Add Resource File** button.
2. Under **File Name**, enter the name for the file. Veracity recommends including in the file name information that would help recognize the latest version of the file, such as, for example, the client's name, the report's date, and the upload date.
3. Drag and drop the file from your local machine onto **Drop file here or click to upload**. You can also select **Drop file here or click to upload** to select a file from your local machine. Supported file formats are PBIX, PDF, PNG, JPEG, GIF, RDL.
4. Under **Personal data policy**, confirm if the file contains no personal data or it contains personal data and you agree to process it according to Veracity DPA.
5. Select the **Upload** button.


If you upload a Power BI report:
* Under **Privacy Level**, select a privacy level for the report. For details, see the 'Privacy Level' subsection below.
* Toggle "I accept and understand that I'm responsible for the content I share in my report".
* Optionally, toggle **I am using Azure Analysis Service** if you are using this service. Using this as a data source will load your data significantly faster than from Azure SQL DB. **Before enabling this toggle**, check the prerequisites under <a href="#AAS">'To use Azure Analysis Service as a data source'</a>.

Note that:
* If you are using a database for the first time in VAP, use the icons from the warning message to set the credentials for the database.
* If your data source cannot be automatically refreshed, you can either check whether your data is stored in a [location supporting refreshable data sources](../data.md) or accept the default fix (no automatic data refresh) and do manual data updates by replacing the file with your report.

#### Paginated report

You can upload a paginated report in .rdl format. Paginated reports are ideal for presenting content with tightly controlled rendering requirements, such as certificates, audit findings, test results, purchase orders, and long tabular data that must be printed on multiple pages. These reports ensure that your data is presented in a precise and organized manner, meeting the high standards of professional documentation.

##### Service Principal required

To upload a paginated report, your VAP service must use a Service Principal account. If your service is a new setup using Service Principal, then the **Paginated Report** toggle button can be turned on in Admin. You cannot upload the paginated report file for the legacy Power BI Service Principal. If you try to do so, you will get the error message 'Paginated report is not enabled to upload'. 

##### Supported data sources

We support the following methods to add a data source to a paginated report.
* You can connect a database as a data source directly. We support Azure SQL database.
* You can connect a semantic model as a data source. We support Azure SQL database, on-premises SQL database, Web (API call), files (.csv, .xlsx, and more) and Azure Blob.

##### Report reloading

The report reloads after an hour of interacting with it. When it happens, you will see a reload icon. To continue reading the report, wait for the report to finish reloading.

##### Session expiry

If you do not interact with a paginated report for ten minutes, your session expires. You can close the session expiry dialog with the 'X' icon or select **Refresh**. It will extend the report session time and allow you to continue interacting with your report.

### To use Azure Analysis Service as a data source
<a id="AAS"></a>
To be able to load data, add a Veracity VAP service account to your Azure Analysis Services Cube for PowerBI:
* If your VAP service URL starts with insight.**dnv**.com, add 'srvPBIAppPBIEProd@dnv.onmicrosoft.com' to your Azure Analysis Services Cube for PowerBI.
* If your VAP service URL starts with insight.**veracity**.com, add 'srvPBIAppPBIEProdVAP@dnv.onmicrosoft.com' to your Azure Analysis Services Cube for PowerBI.

When uploading your report file, enable 'I am using Azure Analysis Service'.

After this, VAP will pass the Veracity user 'GUID' (the unique Veracity user ID) to the 'CustomData' field in your report. The CustomData feature lets you add a Row filter in your Power BI report. Then, your report can control what Power BI data the user can view.

For more information, refer to [Power BI documentation](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fpower-bi%2Fdeveloper%2Fembedded%2Fembedded-row-level-security&data=05%7C02%7CMichal.Zieba%40dnv.com%7Cf56e31065363481d6fdc08dbfc95dc7e%7Cadf10e2bb6e941d6be2fc12bb566019c%7C0%7C0%7C638381492816141580%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=l%2FsdbYT6obGcAl6T8ijvWheeWEariONKXRPzvPFYKOE%3D&reserved=0).

### Privacy Level

There are the following privacy levels:
* None - Before this release, it was the default setting.
* Organizational
* Private
* Public

For details on privacy levels, go [here](https://learn.microsoft.com/en-us/power-bi/guidance/powerbi-implementation-planning-security-content-creator-planning#privacy-levels).

Note that privacy levels set in Power BI Desktop are **not transferred** during the upload. However, after uploading the report, you can set data privacy for each data source separately.

#### For organizational privacy level
Suppose the privacy level in Power BI Desktop data source is organizational. In that case, you must also set it on the data source in your service to avoid issues with refreshing the data source. For details, go [here](https://learn.microsoft.com/en-us/power-bi/guidance/powerbi-implementation-planning-security-content-creator-planning#privacy-levels).

### To set a privacy level for a data source

To set a privacy level for a data source, in the Admin Panel > Manage Files, in the row with the name of the report:
1. Select the editing icon.
2. Select the **Load datasource status** button.
3. Select the icon shown below.
4. For each data source, under **Privacy Level**, select a privacy level.

<figure>
	<img src="assets/privacylevel.png"/>
</figure>

<p id="webapp"></p>

## Web App 

The "Web app" subtab shows all connections created in your VAP service. This tab is available on request, so if you don't have it, you can contact [VAP support](mailto:mailto:VAP@dnv.com) to request it.

## To create a new web connection

To create a new web connection:
1. From the left sidebar, select the plus icon and the **Add Web App** button.
2. In the **Root URL**, enter the full root URL to your web application.
3. To accept the legal terms of using the service, below the **Root URL**, enable the toggle **I accept and understand...**
4. In the **Display name**, enter the name that the end users should see when they change between different reports or applications.
5. Optionally, in the **Description** field, describe your web application for the end users. Note that currently the description is not shown to the users.
6. Under **Personal data policy**, confirm if the web app contains no personal data or it contains personal data and you agree to process it according to Veracity DPA.
7. Below **Personal data policy**, you can enable the following toggles:

	Enable Dedicated Domain Name - if your web app requires a dedicated domain name, enable this to enter the domain name.
	
	Enable Service Worker - if your web app uses service workers, enable this and enter the full URL of the JS file where you register the service workers for your web app.
	
	Single page application (SPA) - if your web app is a single page application, enable this, and select your app's framework, and the full URL of the "App.js" file containing routing configuration for your SPA framework.
	
	Host In One Gateway - if your web app is hosted in One Gateway, enable this, and enter your app's Client ID for One Gateway. Then, go to your One Gateway, and allow access for the VAP Web App. Also, allow for VAP to control the authentication. After that, the configuration for your web app will disable URL direct access, making it only valid when interacting from VAP.
	
	Attach User Token - if you want to attach user token in the request header, enable this.

7. Select the **Check connection** button to verify if your web application can connect to your VAP service.
8. After establishing a connection, select the **Add** button to add the connection.
9. After you have added a new web connection, go to [Reports](reports.md) and add your web application to a new or existing report object.
10. After that, go to [Entities](entities.md) and add your web application to a new or existing entity.

For help with connecting your web app to VAP, go to [Veracity Community](https://community.veracity.com/t/how-to-plug-the-web-apps-into-vap/145/3).

