---
author: Veracity
description: This is the changelog for the third September 2023 release of Data Workbench.
---

# September 2023 release

Release date: 28 September 2023

Read this page to learn what has changed in Veracity Data Workbench with the third September 2023 release.

## New features

### Share data set with a business partner
Now, you can share your data sets with your business partners. To do so:
1. In **Data catalogue**, open the data set you want to share.
2. Select the share icon.
3. Enter the email address of the person or workspace you want to share the data set with. Alternatively, select the contact list icon to choose the recipient from the list of previously used contacts. Note that sharing with workspace is possible only when some conditions are met. For details, see  "Shara data set with workspace" below.
4. Optionally, to allow the recipient to share the data set with other people, tick the box next to **Allow recipients to share this data set with others**. You can revoke the sharing permission later.
5. Optionally, under **Add note to recipient**, add a message to the person with whom you are sharing the data set.
6. To share the data set, select the **Share** button. The recipient will receive an email notification with a link to the data set.

### Add a shared data set to your workspace
Now, you can add data sets that were shared with you to a workspace in which you are an admin. 

To do so:
1. Open the data set that was shared with you. You can follow the link from the email notification you received or find it in the "Shared with me" tab.
2. Select the **Add to your workspace** button and then select a workspace.
3. Select the button to go forward. This will add the data set to your workspace.

Technically, the data set will be a copy of the original data set. The data set name will be the original name of the data set with a suffix. Now, all workspace members can view the data set in the "Shared with me" tab and reshare it if the person who shared the original data set has allowed that.

### Share data set with a workspace
Now, you can share a data set directly with a workspace on the condition that:

* From this workspace, someone has already shared a data set with the target workspace.
* The data set has been added to the target workspace.

### Revoke share
Now, you can stop sharing a data set if you are the person who started sharing it or the workspace admin. If you do so, everyone with whom it was shared will lose access. For example, if you shared it with Person A and then they reshared it with Person B, both Person A and B will lose access.

To revoke sharing a data set:
1. In **Data catalogue**, open the data set.
2. Select the **Details** tab.
3. In the line with the **Shared with**, select the editing icon.
4. Next to the person or workspace for which you want to revoke access, select the X icon.
5. Select the **Save and Close** button.

### Save filter settings for a shared data set
Now, you can apply filters for a data set that was shared with you and save this view. For details, go [here](https://developer.veracity.com/docs/section/dataworkbench/dataworkbench#data-sets).

Note that if you share a data set with certain filters applied, the recipient cannot see more than those filters allow. Using this, you can share only some information from a data set.  

For example, you can have a data set with information on your ten vessels but apply filters that show only two relevant ships and then share it with your business partner.
