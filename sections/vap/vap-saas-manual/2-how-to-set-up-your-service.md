---
author: Veracity adapter for Power BI
description: VAP introduction - how to set up your service
---

# How to set up your service

[Previous - Introduction](1-introduction.md)

Every new service starts with an empty environment, where you need to upload files, link files and projects and show this to the users. 

In this section, we will give a brief overview of which menus are available to you as a service owner and administrator, and what they do.

In the top menubar, we find two main sections: the reports, and the admin menu. The admin menu is only available and visible to those that have one of the elevated access rights assigned. 

<figure>
	<img src="assets/2-main-admin-view.png"/>
	<figcaption>VAP Admin main menu</figcaption>
</figure>
If you find yourself in this view, but don't see all the items above, it is most probably because you are not assigned a <i>System Admin</i> role. 

The first item, manage files, is the place where you upload files that are to be used in the service. It is also in almost all cases where you start since the next menus are mainly based on these files. The file types supported are Power BI files (.pbix), PDF's and some image files (.png .jpeg and .gif). For detail on how to upload files, see the [Upload your Power BI files](3-upload-your-power-bi-files.md) section of this tutorial.

The next menu item, <i>Manage Reports</i>, is where you describe your uploaded files, and define the names the end-user will see in their menu systems etc. It is very similar to the actual files but lets you at a later stage replace the source file, without needs to reconfigure your entire application. For detail on how to use the manage reports functionality, see the [Manage reports](4-manage-reports.md) section of this tutorial.

The third item, and slightly more abstract functionality, is the Manage Entities. In this menu, you will define the top-level structure. It can represent, e.g. a project, an asset, or a client etc. It is at this level you also will give your end-users access. E.g., if you are delivering the results of a project to your customer as a Power BI report, you could create an entity for the project number, and give the customer access to that project. For more details, examples and step-by-step guidance, see the [Understand and manage enttities](5-understand-and-manage-entities.md) section of this tutorial.

The fourth menu item is the user management section. This is pretty straight forward and is where you do all the user management of your service. You give clients access to the entities that contain one or many reports and manage the elevated access rights for the admins of your VAP service. For more details, see the [How to do users management](6-how-to-do-users-management.md) section of this tutorial.

The fifth and final menu item is the configure section. This section is where you do the advanced settings. To which extent you need to work with this section depends on your use-case and how you interact with your users. You can in this section, define and change everything from parts of look and feel, content in the footer, how notification service work, scheduling refresh of data, and settings for how users get access to the service. For more details, see the [Advanced settings](7-advanced-settings.md) section of this tutorial.


How, lets learn how to upload your Power BI files!

[Next](3-upload-your-power-bi-files.md)

