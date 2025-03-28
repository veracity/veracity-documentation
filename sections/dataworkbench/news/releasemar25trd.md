---
author: Veracity
description: Changelog for the March 2025 third release of Data Workbench.
---

# March 2025 third release
Read this page to learn what has changed in Veracity Data Workbench with the March 2025 third release.

## New features

### Revoke all SAS keys  
Workspace admins can now revoke SAS keys in **File storage** using the new **Revoke all keys** button.  

- The button is located in **Data catalogue > File storage** under the action menu (three dots in the top-right corner).  
- Clicking the button opens the **Revoke all keys** dialog, where admins can select:  
  - **Revoke all read access keys**  
  - **Revoke all read and write access keys**  
- The list is a multiple selection list, allowing admins to revoke keys based on workspace policies.  

### Activity log for revoked SAS keys  
Admins and users can now track revoked SAS keys in the **Activity log**. After a key is revoked, an **Access key revoked** event appears in the log.  

### Activity log for read-only SAS key generation  
Workspace users can now see an event in the **Activity log** when a read-only SAS key is generated for an uploaded dataset.  

## Bug fixes  

### Improved activity log entries  
Activity log messages have been updated to provide clearer and more informative details.  