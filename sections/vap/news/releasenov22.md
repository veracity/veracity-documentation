---
author: Veracity
description: This is the changelog for the release 4.4 of Veracity Adapter for Power BI (VAP).
---
# VAP 4.4 release with an in-app tutorial
Release date: 9 November 2022

Read this page to learn what has changed in Veracity Adapter for Power BI.

## New features
This section covers new features:
* [PDF viewer with clickable links and searching](#pdf-viewer-with-clickable-links-and-searching)
* [Viewer for sharing public reports](#viewer-for-sharing-public-reports)
* [New endpoint Get entities in service](#new-endpoint-get-entities-in-service)

### PDF viewer with clickable links and searching
Now, a PDF document with links is clickable.You can also search inside the PDF. To use the search funcitonality, click F5 in the browser.

### Viewer for sharing public reports
In June 2022 in [release 4.2](https://community.veracity.com/t/vap-veracity-adapter-4-2-release-with-the-new-vap-product-viewer-available-16-june-22/168), Veracity has introduced a new VAP product called the Viewer. It offloads your user doing Veracity sign ups and signs in to interact with publicly available analytics.
Also, it allows creating a freemium business model.

Now, the Viewer is now available for both Veracity and DNV domains.

Web apps are currently not supported. When a publicly enabled entity has a web app included, it will not be available through the Viewer. Logging into Veracity and using the standard VAP service will show the web app in the entity.

### New endpoint Get entities in service
Veracity has exposed a new endpoint in Admin API: Get entities in service.

## Changes in existing features
This section covers changes in existing features:
* [Web app supports user tokens](#web-app-supports-user-tokens)

### Web app supports user tokens
Now, the web app supports passing Veracity user tokens to web applications.