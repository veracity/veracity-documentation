--- 
author: Veracity 
description: Veracity Access Hub Guide with user groups
---

# Veracity Access Hub Guide with user groups

## Overview

Veracity Access Hub (VAH) lets you manage access to your applications and the apps you are addedibing to in the Veracity ecosystem.

For developer documentation, go [here](../tenantmanagement/tenantmanagement.md).

It is up to you how much access control you delegate to VAH. Veracity Access Hub offers three types of access control:

* Fully managed by Veracity - You configure access rights only in Veracity.
* Hybrid access control – You configure basic access rights in Veracity and the details in an application.
* Complex access models – The application handles access rights, and Veracity shows you the applications, the users who have access to them, and some other general information.

For hybrid and complex access, note that some applications do not support user groups, so you cannot grant bulk access with groups. However, you can still grant access to individual users.

## With or without user groups?
User groups can be beneficial when you have a large user count in your company account. It is a good way to group and administrate application access based on different roles and functions for users.

By default, user groups are disabled in your VAH. However, you can enable them in Settings > User groups > Current settings.

**This version of the guide includes information on user groups**.  If you choose not to enable user groups, you may want to navigate to [the user guide that omits sections on user groups](accesshub.md).

## Sample use case

Suppose you are a ship owner with five ships, and you bought an application called Emission Connect to account for your emissions according to the European Emissions Trading System (EU ETS).

Then, to give your users access to Emissions Connect:

1. In Veracity Access Hub, go to your company account.
2. On the **Users** page, select the **Add users** button, and add relevant people to your company account.
3. On the **Application** page, select an application (in this case, Emissions Connect).
4. Select the **Add user** button.
5. Select the user that should get access to the application.
 
Note that for applications that are fully managed by Veracity and use access levels, you set access levels for users when you give them access to the application. Access level defines what the user can do in the application, and each application may have different access levels. 

## Choosing company account


Note that only admins can create, edit, and delete user groups. When creating user groups, be consistent in their naming. You can see a
[sample naming](#_Naming_user_groups ) convention here.

<figure>
	<img src="assets/image4.png"/>
</figure>

## To manage applications available for user groups

If you are an admin, select a user group. This will open its details in the Applications page where you can:

-   Delete the group (1).

-   Give the group access to an application (2).

-   See all the applications the group has access to (3). If you select an application, you navigate to its details. For details, see
    [Applications.](#_Applications )

-   Revoke access to an application from the group (4).

Note that you can add the group only to the applications your company account has access to. If you need to add a new application addediption to your account, [go to Marketplace](https://store.veracity.com/).

<figure>
	<img src="assets/image5.png"/>
</figure>

## To manage group's membership

If you are an admin, after opening a group in Members page, you can:

-   Delete the group (1).

-   Change the members view to Direct users and groups or Expanded users. For details, [see the section below.](#direct-users-and-groups-vs-expanded-users) (2)

-   See all the groups and members that belong to the group (3).

-   Add a user or user group to the group (4).

-   Remove a member (user group or user) from the group (5).

<figure>
	<img src="assets/image6.png"/>
</figure>

## Direct users and groups vs expanded users

Groups can be added to other groups, and we call it nesting. To each group, you can add up to five groups. All nested groups get access to the applications the top group is added to.

‘Direct users and groups’ were added directly to the group you are viewing, and they get their application access from this group.

‘Extended users’ means both ‘direct user and groups’ and the users and groups that have access from the group you are viewing because the group they belong to was nested in this group.

To illustrate who are expanded users, see the screenshot above where we have a group called Oslo\_Office and we have added to it the following three other groups (they are members of the Oslo\_Office).

The groups are:

-   Engineering\_Team

-   Finance\_Team

-   Legal\_Team

Now, imagine that:

-   Not everyone in those groups works from the Oslo office, but everyone visits it regularly.

-   The office uses an application for booking meeting rooms and desks and we give access to this application to everyone who belongs to the Oslo\_Office group.

So, people from the groups above and anyone who happens to be added directly to the Oslo\_Office group will have access to this app and we will see all of them under Expanded users.

So, as you see, people in those three groups get access to this application because their groups were added (as members) to the Oslo\_Office. Also, anyone who was added directly to the Oslo\_Office group would have access to the booking app.

## Naming user groups 

When naming user groups, inform who should belong to them (either by role or by addediptions they give) and avoid ambiguous names. To reach these goals, be consistent in naming groups and consider adding explanatory descriptions for each group.

Veracity suggests following your own naming convention. However, you might base it on the following suggestions:

-   The name should describe for whom the group is meant and what they can do. For example, 'Finance\_Department', 'Auditors', or
    'MPP\_Admins'. 

-   Avoid using spaces, special characters, and reserved words\* in User Group names. Spaces and special characters can cause problems with some applications and scripts that interact with Veracity Access Hub.  

-   Establish a naming convention across your company account, document it, and follow it to ensure consistency and avoid conflicts and errors. For example, you can use a format like
    '\[Prefix\]\_\[Name\]\_\[Suffix\]' for all User Groups and define what each element means and how to use it. 

\* Reserved words are words that have a specific meaning or function in Veracity Access Hub or Windows, such as 'Administrator', 'Domain', or
'Everyone'. Using these words in User Group names can cause confusion. Instead, use underscores (\_) or hyphens (-) to separate words in User Group names, and avoid using reserved words or abbreviate them. 

## Applications 

This page shows the applications available to the company account. Here, you can:

-   Search for available applications (1).

-   See available applications (2).

-   Browse Marketplace to find and buy subscriptions to new applications
    (3).

<figure>
	<img src="assets/image7.png"/>
</figure>

When you select an application, you can:

-   Add users and user groups to this application so that they can use it (1).

-   Change the subscriptions' view (2). Direct users or groups have been given access to this app directly while Expanded users lists all the users with access to the application including those that got it from being members of a [nested group](#direct-users-and-groups-vs-expanded-users).

-   See the groups and users with access to this application (3).

-   Control Access level that users and groups have in the application
    (4). This is possible only for apps that are fully managed by Veracity and have application levels built in.

-   Revoke the users' and user groups' access from this application (5).

Note that some users are service principals meaning they are machines performing necessary background tasks. You cannot you cannot revoke their access from the application which is indicated by the padlock symbol (6).

<figure>
	<img src="assets/image8.png"/>
</figure>

## Pending requests

This page shows user requests to join the company account. If you are an admin, you can **Approve** or **Reject** them.

Note that you will see this page only if joining your account is set to require admin approval (Settings > Discoverability > Apply for).

## Settings 

### Name
Under Name, you can change the name of your company account.

### Icon
Under Icon, you can change the logo of your company account. The logo appears together with the company name in applications that support company accounts.

### Discoverability
Under Discoverability, you can choose how users can join your company account:

-   Restricted – Users cannot find your company account, but you can invite them to join.  

-   Apply for – Users can see that your company account exists and request to join it.

-   Automatic – Everyone registered with your email domain is automatically added to the company account. For example, for DNV, everyone with a Veracity account registered for an email in @dnv.com domain would be added to the company account.  

Note that your default discoverability is set to Restricted. If you want to change it, [contact Veracity support](https://support.veracity.com/?loggedin=1) so we can confirm that you own the email domain you wish to use. After confirming your domain ownership, you can change your account's discoverability settings.

If you want to switch to Automatic discoverability:

-   Consider doing it outside regular working hours, for example, at the weekend or night. The reason is that this job may take a long time to complete, and your company account might not work properly until the job is finished.

-   If the change affects a significant number of users (currently,
    500), you will not be able to do this change on your own. Instead, you can apply for help from Veracity. 

### User groups
User groups can be beneficial when you have a large user count in your company account. It is a good way to group and administrate application access based on different roles and functions for users.

If you want to use them, under **Current setting**, select the toggle so that it becomes blue and says 'On'. Now, you are reading the version of the guide that includes user groups. However, if you disable them, you may want to navigate to [the user guide that omits sections on user groups](accesshub.md).

### Administrators

This section shows the administrators of the company account. Here, you can:

* Add administrator (1).
* Revoke the administrator’s access from a user (2).

<figure>
	<img src="assets/image10.png"/>
</figure>