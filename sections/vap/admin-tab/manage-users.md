---
author: Veracity
description: Overview of the Manage Users tab in the admin tab.
---

# Manage Users

The "Manage Users" page shows all users in your VAP service. You can:
* Filter each column providing the text to filter by or choosing an option from a dropdown. To clear all the filters, select the **Clear** button in the right corner of the row with the filters.
* Sort the "Name" and "Email" columns by selecting them.

You can only add Veracity users to a VAP entity. However, if you try to add a non-Veracity user, you will be offered an option to invite them to Veracity. To get access to the VAP entity, this person needs to accept the invitation and complete their Veracity account registration.

## To add a user

To add a user to an entity:
1. Select the **Add User** button.
2. Provide the user's email address or their unique Veracity ID, and select the **Check Email / User ID** button.
3. In the **Grant access to** dropdown, select the entity (entities) to which the user should be added.
4. In the **Roles** dropdown, assign a [role](../user-roles.md) to the user.
5. Optionally, deselect "Send notification to this user" if you do not want to notify the user that they have been added to an entity in VAP.

## To batch add users
In one batch add, you can import up to 200 users.

To batch add users to an entity:
1. Select the **Batch Add Users** button.
2. In the **Grant access to** dropdown, select the entity/enteties to which the users should be added.
3. In the **Roles** dropdown, assign a [role](userroles.md) to the users.
4. Select the **Choose File** button and choose a CSV file from your local machine to batch import users.

For a template for batch importing users, look below the **Choose File** button. If you try to add an already existing user, their data (role, entity) will get updated instead.

Note that you can check the status of batch adding users in the [Background Jobs](background-jobs.md).
