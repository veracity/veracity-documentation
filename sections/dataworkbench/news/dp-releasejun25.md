---
author: Veracity
description: This is the changelog for the June 2025 release of Data Platform.
---

# June 2025 release
Read this page to learn what has changed in Veracity Data Platform with the June 2025 release.

## New features

### Veracity Analytics Environment: support for requirements.txt

**What's new:**  
You can now install Python libraries using a `requirements.txt` file in the Veracity-managed Azure Databricks environment.

**What it means for you:**  
You no longer need to contact support to install custom Python packages. You can define required packages in a `requirements.txt` file and install them yourself, either at the cluster level or for individual notebooks. Git integration is supported, allowing the `requirements.txt` file to be synced along with your notebooks.

**How it works:**
- Define packages in a `requirements.txt` file (for example, `pandas==2.2.1`).
- Sync it with your notebook via Git.
- Install on a Databricks cluster or notebook directly from the UI.
- Installed packages are immediately available for use in your notebook session.

**Need help?**  
For assistance or to enable the Analytics Environment for your workspace, contact [support@veracity.com](mailto:support@veracity.com)
