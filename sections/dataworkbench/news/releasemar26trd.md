# Share Request Updates
This release enhances the Share Request functionality in the Data Platform API, enabling you to use new sharing capabilities. The changes affect how you create, manage, and query share requests.

We have updated [Dataworkbench API specifications](https://docs.veracity.com/apis/platform/dataworkbenchv2) to reflect these changes.
## New share request statuses
Two new statuses have been added to support improved workflows:

### Proposed
A share request created in a draft-like state.
Use this when the requestor wants to create a request that should not be immediately actionable by the receiver. 

Also, you can create this request without specifying who should receive it and keep it as a draft for future requests to data owners.

Example of creating a Proposed request:
```JSON
{
  "schemaVersionId": "75ef9474-089f-4f77-9bcf-63cf9658387e",
  "columns": ["IMO", "Vessel_Name"],
  "requestorNotes": "Test notes",
  "initialStatus": "Proposed"
}
```

### Abandoned
Indicates that a request is no longer valid or was never finalized.
A request may become Abandoned when the sender cancels it or when system-defined conditions expire it.

These statuses are returned by the Get/Query Share Requests endpoint.

## Receiver identification rules
A share request may identify its receiver in one of three ways:
- By ReceiverWorkspaceId 
- by ReceiverWorkspaceId + groupId
- by ReceiverEmail only

Note that `ReceiverWorkspaceId` and `ReceiverEmail` are **mutually exclusive** – you can provide one or the other, but not both.

It is possible for a request not to identify a share request receiver but only if the share is in "Proposed" status. See example below:
```JSON
{
    "receiverEmail": "test@dnv.com",
    "schemaVersionId": "75ef9474-089f-4f77-9bcf-63cf9658387e",
    "columns": [
        "IMO",
        "Vessel_Name"
    ],
    "queryFilters": [
        {
            "column": "IMO",
            "filterType": "List",
            "filterValues": [
                "9226425",
                "9626053"
            ]
        }
    ],
    "requestorNotes": "Test notes",
    "initialStatus": "Proposed"
}
```

### Why groupId requires ReceiverWorkspaceId
A group refers to a permission group inside the receiving workspace.
Because groups belong to a workspace, a receiver workspace must be provided when supplying groupId.

## New and updated properties
The following properties are now available on share requests:

| Property           | Description                                                         |
|-------------------|---------------------------------------------------------------------|
| groupId           | Optional group identifier within the receiver’s workspace. Only returned when supplied during share creation.         |
| ReceiverEmail     | Email address of the intended receiver. Returned only when the request was created with receiverEmail. |
| ReceiverNote      | Optional note added by the receiver when accepting or declining a request.             |
| RequestNote       | Previously named Notes – this field has been renamed.                |
 
 `ReceiverWorkspaceId` and `ReceiverEmail` are **mutually exclusive** – you can provide one or the other, but not both.

## New bulk resolve endpoint
Now, you can call a new endpoint to accept or decline share requests in bulk. You can also do it from the UI in Data Workbench, [see details here](https://docs.veracity.com/releases/march-2026-second-release).

This aligns with Data Workbench UI: Data Catalogue > Requests now supports bulk approve/decline and receiver notes.”


| Method | Endpoint                                                     | Description                                      |
|--------|---------------------------------------------------------------|--------------------------------------------------|
| POST   | workspaces/{workspaceId}/sharerequests/resolve | Bulk accept or decline multiple share requests   |


When calling this endpoint, provide IDs of share requests and, optionally, use ``receiverNote`` to add information to explain why you are accepting or declining share requests.

Request Body to accept multiple data sharing requests:

```JSON
{
    "action": "Accept",
    "shareRequestIds": [
        "9024dbf1-e50d-4146-b884-8362ffa27544",
        "1a8672cb-60ec-444e-92b3-7741e4a37194"
    ],
    "receiverNote": "receiver note content"
}
```

Request Body to decline multiple data sharing requests:
```JSON
{
    "action": "Decline",
    "shareRequestIds": [
        "9024dbf1-e50d-4146-b884-8362ffa27544",
        "1a8672cb-60ec-444e-92b3-7741e4a37194"
    ],
    "receiverNote": "receiver note content"
}
```

**Notes:**
- The API may return partial successes if some items fail.
- Requests already resolved (accepted/declined) will return detailed errors per ID.

## Updated endpoints
| Endpoint               | Changes                                                                                                                         |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Create Share Request   | Now supports ``Proposed`` status, ``ReceiverEmail``, ``groupId``, and ``ReceiverNote``                                                          |
| Accept Share Request   | Now supports adding ``ReceiverNote``                                                                                                |
| Decline Share Request  | Now supports adding ``ReceiverNote ``                                                                                               |
| Get/Query Share Requests | Returns new statuses (``Proposed``, ``Abandoned``) and new properties (``groupId``, ``ReceiverEmail``, ``ReceiverNote``, ``RequestNote``)               |