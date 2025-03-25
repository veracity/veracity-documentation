---
author: Veracity
description: Changelog for the March 2025 second release of Data Workbench.
---

# March 2025 Second release

Here's what's new and improved in the March 2025 second release of Veracity Data Workbench.

## Changes in existing features

### Granular access control for shared items
You can now set specific access levels ('Read' or 'Read and write') when sharing files, datasets, and folders in File Storage. Previously, sharing defaulted to 'Read' only.

- **'Read and write' access:** Allows recipients to upload files, create folders, and delete files (within the shared folder's children).
- **'Read' access:** Recipients can only view content and won't see upload or folder creation options.

You can view and manage access levels in the dataset's Details tab. When reshareing, you can't grant higher access than you currently have.

### Generate SAS tokens for write-accessible shares
Users with 'Read and write' access to shared files or folders can now generate SAS tokens directly from the 'Shared with me' tab or guest view.

### Removed Python Execution from Data Requests
The option to run Python execution analytics during data requests has been removed. This feature is replaced by our enhanced analytics capabilities; see [documentation](../analytics.md) for details.

## Bug fixes

### Consistent calendar validation errors
Calendar validation errors now consistently appear when filtering data for time periods outside the original share's range.

### Fixed calendar error in Data Requests
The calendar no longer re-opens after you select a date in the data request dialog.

### Correct error message for revoked file shares
Users now see the correct "File/folder no longer available" message when accessing a revoked shared file via a link, instead of a generic "Something went wrong" page.

### Navigation fix in 'Shared with me'
Navigation in Data Catalogue > 'Shared with me' now works correctly on the first page load. You no longer need to click page numbers twice.