---
author: Veracity
description: Overview of the Manage Users tab in the admin tab.
---

# Users

The 'Users' page shows all users in your VAP service.

## To sort and filter
You can sort the **User Name** and **Email** columns alphabetically. To sort a column, select the column header.

To filter users:
1. In the right corner, select the search icon. The following filter options will show below the search icon: **Name**, **Email**, **Entity**, **Roles**, and **Clear all filters**.
2. To apply a filter, select its name.
3. Enter or select a value by which you want to filter, and select the **Apply** button. You can apply multiple filters.
<figure>
	<img src="assets/users_filter.png"/>
</figure>

To remove a filter:
1. Select the name of the filter.
2. Select the garbage can icon labeled **Remove filter**.
<figure>
	<img src="assets/users_remove_filter.png"/>
</figure>

To remove all filters, select **Clear all filters**.
<figure>
	<img src="assets/users_clear_all_filters.png"/>
</figure>

To hide the filters, select the search icon.

## To add a user

To add a user to an entity:
1. In the top right corner, select the plus icon. Alternatively, from the left sidebar, select the plus icon and **Add User**.
2. Enter the user's email address or their unique Veracity ID, and select the **Check** button. If the email address is not associated with a Veracity account, you must invite the user to create one. Once they have created an account, you can add them to your VAP..
3. Under **Entity List**, select the entity (entities) to which you want to add the user and confirm with the **Add to Entity List** button.
4. Under **Roles**, select one or more [roles](../user-roles.md) for the user. Each role gives different kinds of permissions in your VAP.
5. Optionally, select **Send notification to this user** if you want to notify the user that they have been added to an entity in VAP.
6. To confirm adding the user, select the **Add** button.

<figure>
	<img src="assets/add_user.png"/>
</figure>

## To batch add users
In one batch add, you can import up to 200 users.

To batch-add users to an entity:
1. From the left sidebar, select the plus icon and **Batch Add User**. Alternatively, on the **Users** page, select the plus icon in the top right corner and then **Batch Add User**.
2. Under **User Excel File for Batch Add**, drag and drop the CSV file from your local machine onto **Drop file here, or click to upload** or select **Drop file here or click to upload** to add a CSV file from your local machine. In this section, you can also find a template for the file (see the text 'Click here to download the template file').
3. Under **Entity List**, select the entity (entities) to which you want to add the users and confirm with **Add to Entity List**.
4. Under **Roles**, select one or more [roles](../user-roles.md) for the users. Each role gives different kinds of permissions in your VAP.
5. Optionally, select **Send notification to this user** if you want to notify the users that they have been added to an entity in VAP.
6. To confirm adding the users, select the **Add** button.

Note that if you try to add an already existing user, their data (role, entity) will get updated instead.

Note that you can check the status of batch-adding users in the [Background Jobs](background-jobs.md).

<figure>
	<img src="assets/batch_add_user.png"/>
</figure>

## To edit user
To edit a user:
1. In the row with the user's name, in the **Actions** column, select the edit (pencil) icon.
2. Edit the user. You can change the entities they have access to and their roles and notify them about the changes. You cannot change the user email or ID because they come from the user's Veracity account.
3. To confirm the changes, select the **Save** button.

<figure>
	<img src="assets/edit_user.png"/>
</figure>

## To delete a user
1. In the row with the user's name, in the **Actions** column, select the garbage can icon.
2. To confirm, select the **Delete** button.

<figure>
	<img src="assets/delete_user.png"/>
</figure>

## To see statistics for a user

The **Interactions (1Y)** column displays the number of interactions each user has had with the VAP instance in the past year. Note that this column is not sortable.
To view details, select **View History** from the "Actions" column for the desired user.

<figure>
	<img src="assets/see_user.png"/>
</figure>

The View History window is divided into two tabs: Admin Operate History and User Visit History.

The **Admin Operate History** tab shows information about user role upgrades and downgrades:
* Under **Operate user**, see who upgraded or downgraded a user role.
* Under **Description**, see the names of new and old user roles.
* Under **Date time**, see when the user role was changed.

The **User Visit History** tab shows what entities the user has interacted with and when.
