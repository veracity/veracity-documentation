---
author: Veracity
description: This is the changelog for the June 2025 B2B file sharing release in Data Workbench.
---

# June 2025 third release

Read this page to learn what changed in Veracity Data Workbench with the June 2025 release focused on workspace-to-workspace sharing of files and folders.

These changes allow users to directly share file storage resources between workspaces within the same tenant, simplifying collaboration and removing the need for manual file exchanges.

## New features

### Share files and folders with other workspaces

You can now share files and folders from **File storage** with another workspace under the same tenant.

To do this:

1. In the **Data catalogue**, open the **File storage** tab.
2. Next to a file or folder, select the three-dot icon and choose **Share**.
3. In the **Share access with** field, select a workspace from the list. You can either type to search or click the contacts icon to browse recently used contacts and available workspaces.
4. Choose access level (**Read** or **Read and write**) and optionally add a note.
5. Select **Share** to complete the action.

You can see and manage what you shared in the **Shared with** dialog. The recipient workspace will see the file or folder in the **Shared by other workspaces** subtab of **File storage**.

**Note that** reshare is only available when originally allowed, access level is restricted by the user’s role in the receiving workspace, and recipients cannot reshare from the detail page view.

### See shared files from other workspaces

A new subtab, **Shared by other workspaces**, is now available under **File storage**.

It shows the files and folders your workspace received from other workspaces in the same tenant. The page lists shared items, who shared them, who they were shared with, and when. If no files have been shared, an empty state is shown.

You can take the following actions, based on your workspace role and access level:

| Actions           | Admin with ReadWrite access | Admin with Read access | Reader with Read access | Reader with ReadWrite access |
|------------------|-----------------------------|-------------------------|--------------------------|------------------------------|
| Download         | ✓                           | ✓                       | ✓                        | ✓                            |
| Share            | ✓*                          | ✓*                      | ✓*                       | ✓*                           |
| Revoke sharing   | ✓*                          | ✓*                      | ✓*                       | ✓*                           |
| Generate keys    | ✓                           | ✗                       | ✗                        | ✗                            |
| Delete access    | ✓                           | ✓                       | ✗                        | ✗                            |
| Create Folder    | ✓                           | ✗                       | ✗                        | ✗                            |
| Upload Files     | ✓                           | ✗                       | ✗                        | ✗                            |
| Delete Folder/File | ✓                         | ✗                       | ✗                        | ✗                            |

✓* Actions marked with an asterisk are only available if the original sharer enabled reshare permissions, or if the user previously reshared the item.

### To revoke access from your workspace
To revoke access from your workspace, select the three-dot icon next to the item and choose **Delete access**.

### Add shared files to your workspace (admin only)

If you are an admin of one or more workspaces, you can now **add shared files or folders to your own workspace** for easier navigation and access management.

To do this:

1. Go to **File storage > Shared by other workspaces**.
2. Find the shared file or folder and select **Add to my workspace**.
3. In the popup, choose your workspace from the list.

The file or folder will appear in your main **File storage** tab, under **Workspace file storage**.

**Note that** if the folder is already added or you do not have any workspaces where you are an admin, the option will be disabled.
