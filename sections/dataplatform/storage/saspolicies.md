---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Sas policies

## List SAS policies for internal storage
To list all SAS policies for internal storage, call the `https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId:guid}/storages/policies` endpoint with the GET method.


Note that:
* `containerName` is the name of the container for which the SAS policy needs to be granted.
* `connectionString` is the connection string of the external storage account.

## Revoke a SAS policy

### Revoke a SAS policy for internal storage
To revoke a SAS token for internal storage, you don't revoke the token directly. Instead, you revoke the policy that the token is attached to.  Revoking the policy revokes all SAS tokens associated with that policy.

To revoke a SAS policy, call the following endpoint with the DELETE method:
`https://api.veracity.com/veracity/dw/gateway/api/v1/workspaces/{workspaceId:guid}/storages/sas/revoke`

Note that:
* You must be a workspace admin to revoke SAS policies.
* This endpoint accepts an optional query parameter called `policyToRevoke`.

Regarding `policyToRevoke` parameter, here are some important considerations:
* **If you don't provide the** `policyToRevoke` **parameter**: You'll revoke all SAS policies for the entire storage container (workspace). This means all active SAS tokens for that container will be revoked, regardless of which policy they were associated with.
* **If you do provide the** `policyToRevoke` **parameter**: You'll revoke only the specified policy. This means only the active SAS tokens associated with that specific policy will be revoked. Other tokens tied to different policies will remain active.


Regarding the payload fields, here are some important considerations:
* `containerName`: This is the name of the container where the SAS policy you want to revoke is applied. It is required.
* `connectionString`: This is the connection string for the external storage account. It is required.
* `policyName`: This is the name of the specific policy you want to revoke. It is required. Unlike revoking internal storage policies, you must specify the `policyName` for external storage. There's no option to revoke all policies for a container in a single call.