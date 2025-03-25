---
author: Veracity
description: This is the changelog for the March 2025 second release of Data Workbench.
---

# March 2025 second release

Read this page to learn what has changed in Veracity Data Workbench with the March 2025 second release.

## Changes in existing features

### Set access level when sharing files, data sets, and folders
Previously, in File Storage, when you shared a file, data set, or folder, you were sharing it in read mode. Now, you must set access level to 'Read' or 'Read and write'. 

If you gave the share recipient the 'Read and write' access to a folder, they can:
* Upload files
* Create folders
* Delete files in the folders, but only in the children files/folders of the shared folder.
However, a person with 'Read' access won't see the buttons for uploading files or creating folders, and they won't be able to delete files.

Note that:
* When you open the Details tab for a data set, you can see with whom it was shared and what access level they have.
* When you reshare a data set, you cannot set the access level for the share recipient to a higher access level than you have. So, if you only have 'Read' access to a data set, you cannot reshare it with 'Read and write' acces.

## Generate SAS token with access level
As a workspace user, when I open 'shared with me' tab, and I am able to see listed shared file/folders. When I click on the actions dropdown of one file/folder that is write access, I am able to see generate sas token button. And I am able to click the generate sas token button to generate sas token.

As a guest view user, when I open the guest view,  I am able to see listed shared file/folders. When I click on the actions dropdown of one file/folder that is write access, I am able to see generate sas token button. And I am able to click the generate sas token button to generate sas token.

## Removed Run Python execution analytics from data request
When you requested a data provider to share a data set with your workspace, you could tick the box **Run Python execution analytics (optional)** and select an available Python script.
Then, the script would transform the data you were getting from your request, which could give you additional contextualization or transformation of the data and thus increase its quality and relevance. 

Now, you cannot do that since we removed the box. You no longer need it because we introduced superior analytics; for details, [see the documentation](../analytics.md).

## Bug fixes

### Calendar validation error not showing consistently
When someone shared with you a data set with data for a certain period, and you tried to filter the data for the time that wasn't available in the original share, you should always get a validation error from the Calendar, but sometimes the error wasn't showing. Now, this is fixed.

### Calendar error in requesting a data set
Bug description: 
In request data, calendar is popped again after picking 1 date in generate key dialog

To reproduce
Go to a workspace with Request data button available
Click Request data button, then data request dialog shows.
Click on the Interval start date.
Screenshots
       Image

Expeceted:
The selected date is applied and calendar dialog is closed.

Actual (what happens, this is a bug):
 Calendar is popped again after picking 1 date in generate key dialog

### File Share > Something went wrong page is displayed when user accessed to revoked shared file by link
To reproduce:
UserA shared a file to userB.
UserA revoked the share.
UserB opened the link in Shared notification.
Refresh the page

Expeceted:
      3. Page with "File/folder no longer available" is displayed
      4. Page with "File/folder no longer available" is displayed

Actual (what happens, this is a bug):
      3. Page with "File/folder no longer available" is displayed
      4. Something went wrong page is displayed.

### Navigation not working on the first load in Shared with me
In Data Catalogue > Shared with me, when you tried to go to the second page of the list, you had to click the page number twice to navigate there. Now, this is fixed.