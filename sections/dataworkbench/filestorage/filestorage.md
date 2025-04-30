---
author: Veracity  
description: This page explains how to use File storage in Data Workbench, and how to share files and folders using access levels and SAS keys.
---

# File storage

In your [Data Catalogue](../datacatalogue.md), you can find a tab called **File storage** for uploading, organizing, sharing, and accessing files.

**If you want to access it via API**, see [File storage API endpoints in API docs](../apiendpoints.md).

You can [connect File storage with Azure Storage Explorer](ase.md).

---

## Folders

In File storage, you can use folders to organize files.

**You can:**
- Create folders (admin only).
- Delete folders (admin only).
- Nest files inside folders.

**You cannot:**
- Rename folders.
- Move folders.

To create a folder:
1. In the top right corner, select **Create folder**.
2. Name the folder.
3. Select **Save**.

---

## To upload files

1. In the top right corner, select **Upload files**. You can upload multiple files at once.
2. Select the coloured circle with the file icon and choose files from your computer. Alternatively, drag and drop files.
3. Select **Upload**.

---

## Access levels

When sharing files or folders, you can choose between two access levels:

- **Read only**: Recipients can view or download the item but **cannot create SAS keys** or re-share it.
- **Read and write**: Recipients can edit, upload new files, and **create SAS keys**. However, they **cannot share the folder with another workspace** directly.

> ℹ️ If the recipient uses a SAS key with read and write access, the activity is logged in the **original sharer’s** workspace Activity Log.

---

## Action menu in File storage

For each file or folder, select the three dots in the row to open the action menu. You can:
- **Download** the item.
- **Share** the item.
- **Revoke access** to shared items.
- **Generate SAS key** (admin only, and only for items shared with *read and write* access).
- **Delete** files or folders (admin only, permanent).
  
<figure>
	<img src="../assets/filestorage.png"/>
</figure>

---

## To share files and folders

1. In the row with the file or folder to share, select three dots and then **Share**.
2. In the popup:
   - Under **Share access with**, enter the recipient’s email.
   - Choose **Access level**: Read or Read and write.
   - (Optional) Enable "Allow recipients to share..." to let the recipient re-share the file/folder with others (read-only).
   - (Optional) Add a **Note to recipient**.
3. Select **Share**.

> Shared files and folders appear in the **Shared with me** tab in the Data Catalogue.

> 🔁 If the recipient deletes a shared folder, it is removed only from their workspace—not the original owner's.

---

## To generate a SAS token

> ⚠️ Only workspace **admins** can generate SAS keys, and only for items shared with **Read and write** access.

1. In the row with a file or folder, select three dots > **Generate SAS key**.
2. Under **Set access level**, choose:
   - **Read**: For view/download only.
   - **Read and write**: For uploading/modifying files.
3. Under **Set access end**, choose the expiration date for the key.
4. Select **Generate key**.
5. A new field called **Access key** appears.
6. Select **Copy key**.

> 💡 **Best practices**: Use the minimum required access level and set an appropriate expiration date.

You can also:
- **Generate workspace-level keys**.
- **Revoke all SAS keys** if needed.

---

## To revoke access to shared files or folders

You can revoke access at any time.

1. In the row with the shared item, select three dots > **Revoke sharing**.
2. Find the person whose access you want to revoke and select the **X** icon next to their name.
3. Select **Save and Close**.

---

## To delete files and folders

If you are a workspace admin:
1. In the row with the file or folder, select three dots > **Delete**.
2. Confirm by selecting **Delete** in the popup.

> ⚠️ Deletion is **permanent** and cannot be undone.

---

## To download files and folders

If you are a workspace **reader** or **admin**:
1. In the row with the file or folder, select three dots > **Download**.

---

## Need Support?

1. Visit the [Help Center](https://help-center.veracity.com/en/collections/3824716-data-workbench) for articles and video tutorials.
2. Contact [support@veracity.com](mailto:support@veracity.com) for assistance.
