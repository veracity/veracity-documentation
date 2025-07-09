---
author: Veracity
description: This is the changelog for the July 2025 release of Data Platform.
---

# July 2025 release
Read this page to learn what has changed in Veracity Data Platform with the July 2025 release.

## New features

### New Dataworkbench V2 endpoints for dataset ingest

You can now use the Dataworkbench V2 API to manage dataset ingest operations more flexibly and securely. Workspace admins can:

- **Create** a new ingest dataset.
- **Update** an existing ingest dataset (for example, using Upsert, Delete, Overwrite, or Append).
- **Validate** the file before triggering ingest.
- **Start** the ingest job manually (if not using auto-start).
- **Check status** of the ingest job via a dedicated endpoint.

In addition, you can now query:
- **Job history**
- **Workspace history**

These features are available to workspace administrators through the `gateway/v2` endpoints.

> Refer to the [API documentation](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json) for payload examples and full endpoint structure.
