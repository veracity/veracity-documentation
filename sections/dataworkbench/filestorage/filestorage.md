---
author: Veracity
description: This page explains how to use File storage in Data Workbench and how to migrate to it from Data Fabric.
---

# File storage

In your [Data Catalogue](../datacatalogue.md), you can find a tab called **File storage** and use it for uploading, sharing, and accessing files.

> **Note**  
> File storage is an optional module for Data Workbench. You need to have an active File storage subscription to use this feature. After you purchase it, Veracity sets up your account and notifies you via email when it’s ready. You may already have access to it as part of another Veracity service.

**If you want to access it via API**, see [File storage API endpoints in API docs](../apiendpoints.md).

You can also [connect File storage with Azure Storage Explorer](ase.md).

---

## To go to File storage

1. In your workspace, go to the **Data catalogue** page.
2. Select the **File storage** tab.

<figure>
	<img src="../assets/access.png"/>
	<figcaption>Location of File Storage.</figcaption>
</figure>

---

## Folders

In File storage, you can use folders to organize files. If you are a workspace admin, you can create folders.

> **Note**  
> You cannot rename or move folders. However, you can delete them if you are a workspace admin.

To create a folder:
1. In the top right corner, select **Create folder**.
2. Name the folder.
3. Select **Save**.

---

## To upload files

1. In the top right corner, select **Upload files**. You can upload multiple files at once.
2. Select the coloured circle with the file icon and select the files from your computer. Alternatively, drag and drop files.
3. Select **Upload**.

---

## Access levels

When sharing files or folders, you must set an access level:
- **Read**: Recipients can view and download the content. They **cannot** create SAS keys or reshare.
- **Read and write**: Recipients can upload, delete, or modify files. They **cannot** reshare with another workspace, but **can** generate SAS keys. These actions are logged in the original owner's workspace under Activity log.

This distinction is important, especially for users coming from Data Fabric where the term "container" was used—here we use **workspace** and **folder** instead.

---

## To share files and folders

1. In a row with a file or folder, select the three dots and then **Share**.
2. In the window that opens, under **Share access with**, add the email address of the person you want to share the file or folder with.
   1. Optionally, to allow further sharing, tick **Allow recipients to share**.
   2. Optionally, add a **Note to recipient**.
3. Select the **Share** button.

> **Note**  
> Shared files and folders show in the **Shared with me** tab in the Data catalogue.  
> If the recipient deletes the shared folder, it only disappears from their workspace; the original folder in your workspace remains unchanged.

---

## To revoke access to shared files or folders

You can revoke access at any time.

1. In the row with the shared file or folder, select the three dots and then **Revoke sharing**.
2. Next to the person whose access you're revoking, select the X icon.
3. Select **Save and Close** to confirm.

---

## Action menu in File storage

For each file or folder, you can open the action menu (three dots) to do the following:

- **Download** the file or folder.
- **Share** it with others.
- **Revoke access** to shared items.
- **Generate SAS keys** for external system access.
- **Delete** (only available for items you own and if you are a workspace admin).

<figure>
	<img src="../assets/filestorage.png"/>
</figure>

---

## To download files and folders

If you are a workspace reader or admin, you can download files and folders. To do so:

1. In the row with the file or folder, select the three dots on the right.
2. Select **Download**.

---

## To generate a SAS token

If you are a workspace admin and have **Read and write** access to the file or folder, you can generate SAS (Shared Access Signature) tokens to enable external system access.

1. In the row with a file or folder, select the three dots.
2. Select **Generate key**.
3. Under **Set access level**, choose:
   - **Read**
   - **Read and write**
4. Under **Set access end**, choose the expiration date after which the SAS key becomes invalid.
5. Select **Generate key**. A new field called **Access key** appears.
6. Select **Copy key**.

> **Note**  
> SAS keys can only be generated for files and folders shared with **Read and write** access.  
> SAS key creation and usage is logged in the Activity log of the original owner’s workspace.  
> You can revoke all SAS keys at any time.

---

## Need Support?

1. Visit the [Help Center](https://help-center.veracity.com/en/collections/3824716-data-workbench) for articles and video tutorials on Data Workbench.
2. Contact the [support team](mailto:support@veracity.com) if you need assistance.
