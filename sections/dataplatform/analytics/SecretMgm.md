---
author: Veracity
description: This page explains how to utilize the analytics capabilities
---

# Secure Management of Secrets in Databricks

To avoid injecting sensitive information directly into notebooks, we use a dedicated secret scope named "secrets". This approach keeps secrets secure and separate from your code. In our setup, administrators are granted write access (to add or update secrets), while users can only read (retrieve) these secrets.

-Secret Scope: The "secrets" scope is used to manage and store sensitive information securely.
-Role-Based Access: Administrators can add/update secrets, while users are limited to reading them.
-Security Benefits: By avoiding hardcoded secrets in notebooks, you reduce the risk of accidental exposure and adhere to security best practices.
-Easy Management: The Databricks SDK and dbutils commands provide simple methods to manage and retrieve secrets efficiently.

## Listing Available Secret Scopes
You can list all the available secret scopes to verify that the "secrets" scope exists:

```
# List all secret scopes
scopes = dbutils.secrets.listScopes()
print("Available secret scopes:", scopes)
``` 
If the "secrets" scope is set up correctly, it will appear in the list.


## Adding a Secret
Administrators can add secrets using the Databricks SDK. The following refactored code snippet demonstrates how to add a secret to the "secrets" scope:

``` 
from databricks.sdk import WorkspaceClient

# Create an instance of the WorkspaceClient
workspace_client = WorkspaceClient()

# Define the secret details
scope_name = "secrets"
secret_key = "secret-name"
secret_value = "secret-value"

# Add the secret to the specified scope
workspace_client.secrets.put_secret(scope=scope_name, key=secret_key, string_value=secret_value)
```

**Explanation:**
WorkspaceClient Initialization: We start by importing and initializing the WorkspaceClient from the Databricks SDK.
Defining Secret Details: We specify the scope ("secrets"), the key ("secret-name"), and the actual secret value ("secret-value").
Storing the Secret: The put_secret method securely stores the secret in the specified scope.


## Retrieving a Secret
Users retrieve the stored secret using the dbutils.secrets.get command. This method ensures that sensitive data is accessed securely:

```
# Retrieve the secret from the "secrets" scope
retrieved_secret = dbutils.secrets.get(scope="secrets", key="secret-name")
print("Retrieved secret:", retrieved_secret)
```

**Explanation:**
Secure Retrieval: The dbutils.secrets.get function fetches the secret from the "secrets" scope using the key "secret-name".
No Hardcoding: This method keeps the secret out of the notebook's source code, reducing the risk of accidental exposure.


