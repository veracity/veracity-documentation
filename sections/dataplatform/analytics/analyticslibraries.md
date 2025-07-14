---
author: Veracity
description: This page explains how to utilize the analytics capabilities
---

# Library management
You can install Python libraries using a **requirements.txt** file in the Veracity-managed Azure Databricks environment.

## List already supported libraries

Run following command to see which libraries already installed in your cluster

```
!pip list
```

## Import new libraries
You can define required packages in the **requirements.txt** file and libraries will be installed on cluster level. The requirement.txt file is available in the /Workspace/Shared" folder.  You can add any libraries you wish to be automatically installed when a cluster starts. 

Define packages in the requirements.txt file, one library per line:

**Example**
```json
python-dateutil==2.9.1
pandas==2.3.1
```

Installed packages are immediately available for use in your notebook session. **Note:** You are responsible for ensuring that only secure and trusted packages are included.

### Install libraries on notebook level
You can install libraries that only applies to your notebook.

This example will downgrade your Pandas library from 2.3.1 running on cluster (because of your requirements.txt file) to 2.2.0
**Example**
```python
pip install pandas==2.2.0
%restart_python

#check version
import pandas as pd
print(pd.__version__)
```


## Git integration
Git integration is supported, allowing the requirements.txt file to be synced along with your notebooks.

If you’re already managing a requirements.txt file via Git integration, you can submit a support ticket to update the path to point to your Git-managed file instead.

