---
author: Veracity
description: This page explains how to connect File storage with Azure Storage Explorer.
---
# Connect File storage with Azure Storage Explorer
This page explains how to connect File storage with Azure Storage Explorer.

## To generate a SAS token
You will need a File storage SAS token to connect File storage with Azure Storage Explorer. You can generate it if you are a workspace admin in Data Workbench.
1. In the row with a file or folder you want to generate a SAS token for, on the right, select three dots.
2. Under **Set access level**, choose access level (read or read and write).
3. Optionally, under **Set access start**, choose a date from which this file or folder should be accessible.
4. Under **Set access end**, choose a date from which this file or folder will no longer be accessible.
5. Select **Generate key** and a new field called **Access key** will show.
6. Select **Copy key**. 

## To connect DWB File storage with Azure Storage Explorer
1. Launch Azure Storage Explorer on your computer.
2. Click on the **Open Connect Dialog** button.
3. In the dialog, select **ADLS Gen2 container or directory**.
4. Select **Shared access signature URL (SAS)** as the connection method and click **Next**.
5. Generate an Access Key in Veracity Data Workbench as described in the section **To generate a SAS token** above.
6. Review the connection summary and click **Connect**.
7. Once connected, the new container will appear in the explorer. You can view files and folders on the right side.


Note that:
* You can use the buttons on the top or right-click to perform actions like open, download, and preview.
* Connected containers will remain available in the explorer as long as they are not expired.