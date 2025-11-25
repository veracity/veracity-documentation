---
author: Veracity
description: Veracity Marketplace order event messages
---

# Veracity Marketplace order event messages

> When a customer purchases your service on Veracity Marketplace, the platform generates order messages that you can use to automate access provisioning.

This page covers the **order message** integration path, **one of several delivery patterns** described in the _Overview_ page.

Order messages are published to the **Veracity Message Bus (Azure Service Bus)**. Your application subscribes to receive them.

<br/>

## Order message payload

Below is a **shortened** order message payload highlighting selected key attributes:

```javascript
{
  // ...
  "eventType": "com.veracity.tenantservice.mp-order-created", // [1]
  "payload": {
    "properties": [
      {
        "name": "mp-order-created",
        "value": {
          "Contact": {
            "VeracityUserId": "a4d2d892-2ca5-455b-9854-5b993d50a837",
            "Email": "john.doe@example.com"
          },
          "MetaData": {
            "<key>": "<value>"  // [2]
          },
          "LineItems": [
            {
              "Sku": "ACME-PRODUCT", // [3]
              "Quantity": 1
            }
          ]
        }
      }
    ],
  },
}
```

Key attributes in the payload:

- **[1] Event type**: Your application must **filter messages** based on this to avoid reacting to other messages.

- **[2] Metadata**: Applications can pass URL parameters to the Marketplace checkout page to give context to orders. These are included in the order message `MetaData` object.

- **[3] SKU (Stock Keeping Unit)**: Unique identifier for the specific product that was purchased.

<br/>

## Supporting in-app purchases

If you want to start a purchase from within your application, you can pass URL parameters to the checkout page to **retain context**. These parameters are sent back in the order message’s `MetaData`. For example, if you pass `projectId=12345` in the checkout URL, the event payload will contain:

```javascript
"MetaData": {
  "projectId": "12345"
},
```

Use this mechanism to tie purchases to application-internal concepts like a "project", some specific data or a physical object that the purchase references.

<br/>

## Consuming the order messages

1. The order event is sent on the `tenant` topic of the `veracitydomainevents` message bus.

2. You must filter messages for `eventType` = `com.veracity.tenantservice.mp-order-created`.

3. Each message includes a `payload` attribute which will hold one record in the `properties` array.\
   _(Multiple records are supported for other message types, but order messages will only have one.)_

4. Parse twice: The order object is double-escaped in the message:
   - Parse the outer `payload` string to a JSON object.
   - Then parse the `payload.properties[0].value` to get the real order object.

<br/>

## Appendix - optional reading

### Full order message payload example

> ⚠️**NOTE**: You do **not** need to understand the full payload for basic integration, and many of the detailed attributes expose concerns best handled by the Veracity Marketplace, not your application. **Use with caution**.

Below is an example of a full order message payload. It contains a lot of system fields concerned with the routing of messages etc. which most applications can ignore.

```javascript
{
  "Route": " e26d9341494f46849a71f34cbf20a7c2 ",
  "primaryEntityId": "00000000-0000-0000-0000-000000000000",
  "secondaryEntityId": "e26d9341-494f-4684-9a71-f34cbf20a7c2",
  "eventType": "com.veracity.tenantservice.mp-order-created",
  "entityType": "Tenant",
  "source": "veracity-marketplace",
  "subSystem": null,
  "ts": "2025-10-01T07:13:28.1443436Z",
  "actor": "a4d2d892-2ca5-455b-9854-5b993d50a837",
  "supportCode": "fda0d1d170a645efa84891a1b35c062f",
  "payload": {
    "orderNumber": "1001012628",
    "AutoAssignSubscription": false,
    "properties": [
      {
        "name": "mp-order-created",
        "value": {
          "VeracityOrderNumber": "1001012628",
          "OrderDate": "2025-10-01T07:13:28Z",
          "RenewalTerm": 12,
          "Contact": {
            "VeracityUserId": "a4d2d892-2ca5-455b-9854-5b993d50a837",
            "FirstName": "John",
            "LastName": "Doe",
            "Email": "john.doe@example.com"
          },
          "MetaData": {
            "<key>": "<value>"
          },
          "LineItems": [
            {
              "Sku": "ACME-PRODUCT",
              "Quantity": 1,
              "PurchasedTerm": "Evergreen"
            }
          ]
        }
      }
    ],
    "RequestId": "fda0d1d170a645efa84891a1b35c062f",
    "PrimaryId": "00000000-0000-0000-0000-000000000000",
    "SecoundaryId": "e26d9341-494f-4684-9a71-f34cbf20a7c2",
    "SecondaryId": "e26d9341-494f-4684-9a71-f34cbf20a7c2",
    "SupportCode": "fda0d1d170a645efa84891a1b35c062f",
    "EntityType": "Tenant",
    "Actor": "a4d2d892-2ca5-455b-9854-5b993d50a837"
  },
  "targets": [
    "e26d9341-494f-4684-9a71-f34cbf20a7c2"
  ],
  "messageId": null
}
```

<br/>

### Order line variations in the payload

`LineItems` in order messages come in three variations based on the type of purchase.

> ⚠️**NOTE**: We recommend that applications **do not** try to track, update or terminate subscription lifecycles themselves, but leave this to the Veracity Marketplace. **Evergreen subscriptions** in particular will continue to renew and be charged for until the contract is terminated.

#### 1. Evergreen subscription purchases

Evergreen subscriptions are recurring plans that automatically renew until the customer cancels. In the order payload, `PurchasedTerm` will be set to "Evergreen". The `RenewalTerm` field defines the length of each renewal period in months.

```javascript
"RenewalTerm": 12, // Yearly renewal
"LineItems": [
  {
    "Sku": "ACME-PRODUCT",
    "Quantity": 1,
    "PurchasedTerm": "Evergreen" // Recurring until terminated
  }
]
```

#### 2. Fixed-term purchases

Fixed-term purchases will have the duration specified in the `PurchasedTerm` attribute, such as "`6 Month`" or "`1 Year`". The possible values are dictated by the product configuration in the Veracity Marketplace.

```javascript
"LineItems": [
  {
    "Sku": "ACME-PRODUCT",
    "Quantity": 1,
    "PurchasedTerm": "1 Year" // Fixed term
  }
]
```

#### 3. Perpetual or consumable purchases

Perpetual or consumable purchases do not expire. For these, `PurchasedTerm` is either omitted or set to null. This applies to products like perpetual software licenses or consumable items like "Compute credits".

```javascript
"LineItems": [
  {
    "Sku": "ACME-PRODUCT",
    "Quantity": 1,
    "PurchasedTerm": null // Time-independent
  }
]
```
