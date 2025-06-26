---
author: Veracity
description: This page explains how to utilize the analytics capabilities
---

# Library management
You can install Python libraries using a requirements.txt file in the Veracity-managed Azure Databricks environment.

## List already supported libraries

Run following command to see which libraries already installed in your cluster

```
!pip list
```

## Import new libraries
You can define required packages in a requirements.txt file and libraries will be installed on cluster level. 

The requirement.txt file is available in the /Workspace/Shared" folder.

You can add any libraries you wish to be automatically installed when a cluster starts.
Define packages in a requirements.txt file (for example, pandas==2.2.1).

Installed packages are immediately available for use in your notebook session.

Note: You are responsible for ensuring that only secure and trusted packages are included.


### Git integration
Git integration is supported, allowing the requirements.txt file to be synced along with your notebooks.

If you’re already managing a requirements.txt file via Git integration, you can submit a support ticket to update the path to point to your Git-managed file instead.


### Install libraries on workspace level
You can load libraries to workspace files the same way you load other files.
[For more details](https://docs.databricks.com/aws/en/libraries/workspace-files-libraries)

