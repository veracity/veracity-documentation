---
author: Veracity
description: Overview of the Manage Webs tab in the admin tab.
---

# Manage Webs

The "Manage Webs" page shows all connections created in your VAP service. To sort them by a specific column, select the column. 

In the right corner of each row, you can:
* See history.
* Edit and check the connection.
* Delete the connection.

The actions above are listed from the first to the last icon from the left.

## To create a new web connection

To create a new web connection:
1. Select the **Create new web app connection** button.
2. In the **Root URL**, provide the full root URL to your web application.
3. To accept the legal terms of using the service, below the ***Root URL***, enable the toggle **I accept and understand...**
4. In the **Display name**, provide the name that the end users should see when they change between different reports or applications.
5. Optionally, in the **Description** field, describe your web application for the end users. Note that currently the description is not shown to the users.
6. Below **Description**, you can enable the following toggles:

	Enable Dedicated Domain Name - if your web app requires a dedicated domain name, enable this to provide the domain name.
	
	Enable Service Worker - if your web app uses service workers, enable this and provide the full URL of the JS file where you register the service workers for your web app.
	
	Single page application (SPA) - if your web app is a single page application, enable this, and select your app's framework, and the full URL of the "App.js" file containing routing configuration for your SPA framework.
	
	Host In One Gateway - if your web app is hosted in One Gateway, enable this, and provide your app's Client ID for One Gateway. Then, go to your One Gateway, and allow access for the VAP Web App. Also, allow for VAP to control the authentication. After that, the configuration for your web app will disable URL direct access, making it only valid when interacting from VAP.
	
	Attach User Token - if you want to attach user token in the request header, enable this.

7. Select the **Check connection** button to verify if your web application can connect to your VAP service.
8. After establishing a connection, select the **Add** button to add the connection.
9. After you have added a new web connection, go to [Manage Reports](manage-reports.md) and add your web application to a new or existing report object.
10. After that, go to [Manage Entities](manage-entities.md) and add your web application to a new or existing entity.

For help with connecting your web app to VAP, go to [Veracity Community](https://community.veracity.com/t/how-to-plug-the-web-apps-into-vap/145/3).
