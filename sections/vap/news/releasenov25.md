---
author: Veracity
description: This is the changelog for the release 4.26 of Veracity Adapter for Power BI (VAP).
---
# VAP 4.26 release

Read this page to learn what has changed in the Veracity Adapter for Power BI with the 4.26 release.

This release focuses on platform security, stability, and maintainability. There are no visible changes to the user interface or workflows, but several important improvements have been made behind the scenes to ensure long-term reliability.

## New features
There are no new user-facing features in this release.

## Changes in existing features

### Improved quality assurance and reliability
We expanded our automated test coverage to exceed 80 percent. This helps ensure smoother performance across the platform and reduces the likelihood of regressions in future releases.

### Enhanced security compliance
Infrastructure-as-Code templates were updated to address and resolve Azure Defender alerts. These changes strengthen the overall security posture of the platform without affecting user workflows.

### Updated internal components and libraries
Several NuGet packages were upgraded to remove medium-level security findings identified in Veracode. This improves maintainability and reduces potential security risks within the code base.