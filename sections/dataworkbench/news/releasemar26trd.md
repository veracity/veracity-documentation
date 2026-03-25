# Share Request Updates
This release enhances the Share Request functionality in the Data Platform API, enabling you to use new sharing capabilities. The changes affect how you create, manage, and query share requests.

We have updated [Dataworkbench API specifications](https://docs.veracity.com/apis/platform/dataworkbenchv2) to reflect these changes.

## New share request statuses
Two new statuses have been added to support improved workflows:

### Proposed
A `Proposed` share request is a draft share request.

Use this status when the requestor wants to prepare a share request that is not yet active for a receiver. A `Proposed` request can be created without specifying a receiver.

Example of creating a `Proposed` request:

```JSON
{
  "schemaVersionId": "75ef9474-089f-4f77-9bcf-63cf9658387e",
  "columns": ["IMO", "Vessel_Name"],
  "requestorNotes": "Test notes",
  "initialStatus": "Proposed"
}
```

### Abandoned
`Abandoned` indicates that a share request is no longer active because another share request in the same group has been submitted.

When multiple share requests have the same `groupId` and one of them is submitted, the other share requests in that group are automatically set to `Abandoned`.

These statuses are returned by the Get/Query Share Requests endpoint.

## Receiver identification rules
A share request may identify its receiver in one of three ways:
- By `receiverWorkspaceId` 
- by `receiverWorkspaceId` and `groupId`
- by `receiverEmail`
`receiverWorkspaceId` and `receiverEmail` are mutually exclusive. You can provide one or the other, but not both.

A share request can also be created without identifying a receiver, but only when its initial status is `Proposed`.

Example of a `Proposed` request without a receiver:

```JSON
{
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
Because groups belong to a workspace, `receiverWorkspaceId` must be provided when `groupId` is supplied.

## New and updated properties
The following properties are now available on share requests:

| Property           | Description                                                         |
|-------------------|---------------------------------------------------------------------|
| groupId           | Optional group identifier within the receiver’s workspace. Only returned when supplied during share creation.         |
| receiverEmail     | Email address of the intended receiver. Returned only when the request was created with receiverEmail. |
| receiverNote      | Optional note added by the receiver when accepting or declining a request.             |
| requestNote       | Previously named Notes – this field has been renamed.                |
 
 `receiverWorkspaceId` and `receiverEmail` are **mutually exclusive** – you can provide one or the other, but not both.

## New bulk resolve endpoint
Now, you can call a new endpoint to accept or decline share requests in bulk. You can also do it from the UI in Data Workbench, [see details here](https://docs.veracity.com/releases/march-2026-second-release).

This aligns with Data Workbench UI: Data Catalogue > Requests now supports bulk approve/decline and receiver notes.


| Method | Endpoint                                                     | Description                                      |
|--------|---------------------------------------------------------------|--------------------------------------------------|
| POST   | workspaces/{workspaceId}/sharerequests/resolve | Bulk accept or decline multiple share requests   |


When calling this endpoint, provide IDs of share requests and, optionally, use `receiverNote` to add information to explain why you are accepting or declining share requests.

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
| Create Share Request   | Now supports `Proposed` status, `receiverEmail`, and `groupId`                                                         |
| Accept Share Request   | Now supports adding `receiverNote`                                                                                                |
| Decline Share Request  | Now supports adding `receiverNote `                                                                                               |
| Get/Query Share Requests | Returns new statuses (`Proposed`, `Abandoned`) and new properties (`groupId`, `ReceiverEmail`, `ReceiverNote`, `RequestNote`)               |

## Sample create-request cases
The Create Share Request endpoint supports these request patterns:

**Case 1: Create a share request with receiver workspace ID**

```JSON
{
  "receiverWorkspaceId": "a33060fe-de8f-469c-8cb2-864753f46d64",
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
  "requestorNotes": "Test notes"
}
```

**Case 2: Create a share request with receiver workspace ID and group ID**
```JSON
{
  "receiverWorkspaceId": "a33060fe-de8f-469c-8cb2-864753f46d64",
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
  "initialStatus": "Proposed",
  "groupId": "4581e345-a89e-4974-ad05-7cbc58e312f4"
}
```

**Case 3: Create a share request with receiver email**
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
  "requestorNotes": "Test notes"
}
```
