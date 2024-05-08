---
author: Veracity
description: Overview of the Configure tab in the admin tab.
---

# Configure

## Statistics Report
Under "Statistics Report", you see statistics for your tenant (VAP service) and other statistical information divided into subtabs for easier navigation.

## Tenant Properties

Under "Tenant Properties", you can see tenant properties and edit them.

To edit tenant properties, select the **Edit** button and edit the fields you need to change. You can edit the following fields:
* Invoice Detail - Add information for invoicing, such as cost center, your project and task number, and so on.
* Invoice Contact Email - Provide an email address for sending invoices.
* Business Owner - Provide the name of the service owner.
* Contact Email - Provide an email address to contact you regarding your VAP service.
* Service Description - Describe your VAP service.
* Send notification to all users - Enable this to send notifications to users when their accounts are modified. This is the default setting, but you can override it for each user account.
* Notified Group - Select to notify users with a specific role (for example, UserAdmin) when a new user has successfully self-subscribed to the tenant or an entity in your tenant has turned on public view (access).
	
	Allow Self Subscribe - Enable to allow users to self-register and access your web service. 
	
	Enable manage filters - If you enable this default setting, a "Manage Filters" button will appear under "Manage Reports", and you wil be able to configure reusable report filters for your users.
	
	Show dataset and report id - Enable to show the ID of data sets and reports on Power BI reports in "Resources."
	
	Enable Power BI - Enable Power BI in your VAP service.
	
	Enable Web Apps - Enable connecting web applications to your VAP service.

## Tenant Documents

Under "Tenant Documents", you can define what documents should be available for all users from the "Home" menu. To sort them by column, select the column's name.

To add a document:
1. Select the **Add** button.
2. In the **Report title** dropdown, select the name of the document (PDF, image). You can only use the files already uploaded to your tenant (VAP service).
3. In the **Display name**, add the name for the document that should be shown to users.
4. Select the **Save** button.

In the right corner of each row, you can:
* Edit the document.
* Delete the document.

Note that you need to refresh the page first to to see the changes in footer, entity types or tenant properties.

## Header & Footer

Under "Header & Footer", you can:
* Under **Additional Icon**, change the icon (favicon) of your VAP service (select **Change**) or **Reset** it to the default icon. If this a DNV or Veracity-owned service, leave the default logo.
* Under **Footer**, you can see the following information for your VAP service:
	* Support contact email
	* Tenant information
	* Tenant information URL
* Under **Tutorial Template**, you can download a JSON template file for a tutorial. You can use it to walk your users through new reports and the latest changes. After modifying the template, upload it in [the "Resourcess" tab](resource.md) and connect it to the report in [the "Manage Reports" tab](reports.md).
