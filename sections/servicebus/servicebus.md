---
author: Veracity
description: Veracity Domain Events documentation
---

# Veracity Domain Events Documentation 

Domain Events are useful for service providers and Veracity developers because they bind a service bus connection to the service and send notifications about what happens to your service. Thus, Domain Events lets the applications react to changes rather than periodically pull data and check for changes. 

Before using Domain Events, you must configure it in the Developer portal and specify what kind of notifications you want to receive. 

## Setup 

To use Domain Events: 

1. On developer.veracity.com, go to **My projects**, and [create a Veracity service](../developerexperience/introduction.md). Alternatively, use an existing service.  For this service, create a Resource of the **Domain Event Management** type.
2. When setting up a Domain Event Management resource, on the **Configure** step, under **Service**, select the service for which you want to get notifications about events. Then, under **Subscriptions**, select the event types for which you want to be notified.
3. In the **Advanced** step, set **Max delivery count**. For example, if the 'Max delivery count' is set to 3, if you are notified about an event but your code fails to pick up the message, it will retry retrieving it 3 times. If those attempts fail, the message returns to the queue.
4. In the **Advanced** step, set **Default message time to live (days)**. This setting determines how long an event message will wait in the queue before your code picks it up. The message will be deleted if it isn't picked up within this time. Note that this time is defined in days, and the default value is 1.00:00:00, which means 'one day'.
5. Optionally, on the **Advanced** step, toggle on **Require session**. When this toggle is on, you get notifications and messages in the chronological order in which the events happened.  **Note that** you cannot change this setting later; you can only delete the resource and create a new one which means losing any messages that were in the queue.
6. In the **Summary** step, ensure that everything is set up correctly, and when it is, select **Submit** to publish your resource.


After the setup, Domain Events notifies you about changes in
the information you listen to. 

Note that you can enable and disable Domain Events notifications for your
applications. 

## To get connection strings
In the Developer portal, you can check connection strings for Domain Events and then save them to your key vault for later use. 

To do so:
1. On developer.veracity.com, go to **My projects**, and open the Domain Event Management resource you created during setup.
1. Select the Settings tab.
1. Now, you can copy or regenerate your connection strings.


## Confidentiality 

Domain Events send notifications only to relevant services and does not
share information with parties that are not supposed to get it.  

In detail: 

-   Changes specific to your service are shared only with you and the
    service.  

-   Changes to user subscriptions are notified to all tenants and
    services that the user has a relationship with. However,
    notifications are sent through separate channels to ensure
    confidentiality. 
Note that [tenants](../tenantmanagement/tenantmanagement.md) can get all information relating to tenant users (profiles) and user groups. So, every application installed on a tenant has access to it.  

## Messages from Domain Events 

You can see the messaging pack containing message schemas on
[Veracity NuGet](https://www.nuget.org/profiles/Veracity)
Domain Events messages have an envelope and a payload with data. Note that
Domain Events do not send error messages. 

All messages have the following fields: 

-   Primary ID – Contains user ID or service ID. 

-   Secondary ID – Expresses the relationship between two identities.
    For example, it shows to which service a user is subscribed to. 

-   Entity type – Represents the topics you can listen to. For example,
    user, subscription, topic. 

-   Event type – Shows the type of the event. For example, created,
    updated, deleted. 

-   TS (Timestamp) – Shows when the change has happened. 

-   Subsystem – Shows in which subsystem the change has happened. 

-   Source – An optional field containing which Veracity system sent the
    message. For example, Veracity Identity. 

-   Actor– Shows the ID of the principal (user or system) who initiated
    the event. 

-   Support code (correlation ID) - You can use it to correlate the
    message to the state of what happened.  

-   Payload – See the JSON sample below. 

Below is the base class of the data sent over the bus. The payload
contains a JSON string (like below) and the actual data. 

```json
public abstract class EventPayload: IEventPayload
{
    public string PrimaryId { get; set; }

    [Obsolete("Typo, will be removed in the future", false)]
    public string SecoundaryId { get; set; }
    public string SecondaryId { get; set; }

    public EntityTypes EntityType { get; set; }
    public string Actor { get; set; }
} 
```
 

## Common messages 

This section shows the most common messages in the flow with their
schemas and the event types mapping to them. Note that a single topic
can have multiple schemas mapping to it. 

*User update JSON*

```json
 {   
   "Route": " SCIM ",   
   "primaryEntityId": "3dc22382-3fec-42de-a828-9d1d3ebedd6e",   
   "secoundaryEntityId": "3dc22382-3fec-42de-a828-9d1d3ebedd6e",   
   "secondaryEntityId": "3dc22382-3fec-42de-a828-9d1d3ebedd6e",   
   "eventType": "update",   
   "entityType": "User",   
   "source": "profileCore",   
   "subSystem": null,   
   "ts": "2023-10-25T11:53:49.8235161Z",   
   "actor": "3dc22382-3fec-42de-a828-9d1d3ebedd6e",   
   "supportCode": "87812d1a-9186-4dd5-bd14-7419bc31949b",   
   "payload": "{\r\n  \\action\\: \\update\\,\r\n  \\email\\:
 \\email@dnv.com\\,\r\n  \\firstName\\: \\Bob\\,\r\n  \\lastName\\:
 \\Bobson\\,\r\n  \\displayName\\: \\Bobson, Bob\\,\r\n  \\country\\:
 \\NO\\,\r\n  \\language\\: \\en\\,\r\n  \\mobile\\:
 \\+4799999999\\,\r\n  \\verifiedPhone\\: true,\r\n  \\verifiedEmail\\:
 true,\r\n  \\isActive\\: true,\r\n  \\disabledUserFlag\\:
 \\false\\,\r\n  \\isFederated\\: true,\r\n  \\primaryId\\:
 \\3dc22382-3fec-42de-a828-9d1d3ebedd6e\\,\r\n  \\secoundaryId\\:
 \\3dc22382-3fec-42de-a828-9d1d3ebedd6e\\,\r\n  \\secondaryId\\:
 \\3dc22382-3fec-42de-a828-9d1d3ebedd6e\\,\r\n  \\supportCode\\:
 \\87812d1a-9186-4dd5-bd14-7419bc31949b\\,\r\n  \\entityType\\:
 \\User\\,\r\n  \\actor\\:
 \\3dc22382-3fec-42de-a828-9d1d3ebedd6e\\\r\n}",   
   "targets": \[   
     "SCIM"   
   \],   
   "messageId": null   
 } 
 ```
  
*Delete user JSON*

```json
 {   
   "Route": "all",   
   "primaryEntityId": "5d25f847-e8ec-43fd-8cee-2ca239dab410",   
   "secoundaryEntityId": null,   
   "secondaryEntityId": null,   
   "eventType": "delete",   
   "entityType": "User",   
   "source": "profileCore",   
   "subSystem": null,   
   "ts": "2023-08-02T13:18:08.3475685Z",   
   "actor": "veracitySystem",   
   "supportCode": "cleaup",   
   "payload": "{\r\n  \\primaryId\\:
 \\5d25f847-e8ec-43fd-8cee-2ca239dab410\\,\r\n  \\supportCode\\:
 \\cleaup\\,\r\n  \\entityType\\: \\User\\,\r\n  \\actor\\:
 \\veracitySystem\\\r\n}",   
   "targets": \[\],   
   "messageId": null   
 } 
```
  
*Create user JSON*

```json
 {   
   "Route": " veracity ",   
   "primaryEntityId": "3dc22382-3fec-42de-a828-9d1d3ebedd6e",   
   "secoundaryEntityId": "3dc22382-3fec-42de-a828-9d1d3ebedd6e",   
   "secondaryEntityId": "3dc22382-3fec-42de-a828-9d1d3ebedd6e",   
   "eventType": "create",   
   "entityType": "User",   
   "source": "profileCore",   
   "subSystem": null,   
   "ts": "2023-11-02T15:11:42.6963003Z",   
   "actor": "3dc22382-3fec-42de-a828-9d1d3ebedd6e",   
   "supportCode": "|ee996fc3-4ec27260aac2acc4.ee996fc4\_",   
   "payload": "{\r\n  \\action\\: \\create\\,\r\n  \\email\\:
 \\email@dnv.com\\,\r\n  \\firstName\\: \\Bob\\,\r\n  \\lastName\\:
 \\Bobson\\,\r\n  \\displayName\\: \\Bobson, Bob\\,\r\n  \\country\\:
 \\DK\\,\r\n  \\language\\: \\en\\,\r\n \\isActive\\: false,\r\n 
 \\disabledUserFlag\\: \\false\\,\r\n  \\isFederated\\: true,\r\n 
 \\primaryId\\: \\3dc22382-3fec-42de-a828-9d1d3ebedd6e\\,\r\n 
 \\secoundaryId\\: \\3dc22382-3fec-42de-a828-9d1d3ebedd6e\\,\r\n 
 \\secondaryId\\: \\3dc22382-3fec-42de-a828-9d1d3ebedd6e\\,\r\n 
 \\supportCode\\: \\|ee996fc3-4ec27260aac2acc4.ee996fc4\_\\,\r\n 
 \\entityType\\: \\User\\,\r\n  \\actor\\:
 \\3dc22382-3fec-42de-a828-9d1d3ebedd6e\\\r\n}",   
   "targets": \[   
     "veracity"   
   \],   
   "messageId": null   
 } 
 ```

*Service administrator update JSON*

```json
 {   
   "Route": " 7c80ce2a71764e22b3ee25bf29f9947d veracity ",   
   "primaryEntityId": "7c80ce2a-7176-4e22-b3ee-25bf29f9947d",   
   "secoundaryEntityId": "d08fcbff-5114-46d4-92a6-a807a8ae8555",   
   "secondaryEntityId": "d08fcbff-5114-46d4-92a6-a807a8ae8555",   
   "eventType": "serviceAdministratorUpdate",   
   "entityType": "Service",   
   "source": "serviceMgt",   
   "subSystem": "api",   
   "ts": "2023-10-26T05:33:39.456865Z",   
   "actor": "5a6f95ed-ccd6-45cf-be34-d62da3f220f9",   
   "supportCode":
 "|4874f4df7d1eccf0a3fcf33184354900.0be7e5f5f2cf8fa2.",   
   "payload": "{\r\n  \\roles\\: \[\r\n   
 \\MYDNV\_ADM\_SERVICE\\,\r\n    \\MYDNV\_ADM\_SUBS\\,\r\n   
 \\MYDNV\_ADM\_NOTIF\\,\r\n    \\MYDNV\_ADM\_CHNL\\,\r\n   
 \\MYDNV\_ADM\_WIDG\\\r\n  \],\r\n  \\primaryId\\:
 \\7c80ce2a-7176-4e22-b3ee-25bf29f9947d\\,\r\n  \\secoundaryId\\:
 \\d08fcbff-5114-46d4-92a6-a807a8ae8555\\,\r\n  \\secondaryId\\:
 \\d08fcbff-5114-46d4-92a6-a807a8ae8555\\,\r\n  \\supportCode\\:
 \\|4874f4df7d1eccf0a3fcf33184354900.0be7e5f5f2cf8fa2.\\,\r\n 
 \\entityType\\: \\Service\\,\r\n  \\actor\\:
 \\5a6f95ed-ccd6-45cf-be34-d62da3f220f9\\\r\n}",   
   "targets": \[   
     "7c80ce2a-7176-4e22-b3ee-25bf29f9947d",   
     "veracity"   
   \],   
   "messageId": null   
 } 
 ```

*CreateServiceDefinition JSON*

```json
 {   
   "Route": " 56babbb61371406b8de91f750954603f ",   
   "primaryEntityId": "56babbb6-1371-406b-8de9-1f750954603f",   
   "secoundaryEntityId": null,   
   "secondaryEntityId": null,   
   "eventType": "createServiceDefinition",   
   "entityType": "Service",   
   "source": null,   
   "subSystem": null,   
   "ts": "2023-09-21T10:04:42.2847613Z",   
   "actor": null,   
   "supportCode": null,   
   "payload": "{\r\n  \\name\\: \\TeStIntegration\\,\r\n 
 \\businessOwner\\: \\\\,\r\n  \\description\\: \\This is for
 integration test\\,\r\n  \\shortName\\: \\test123\\,\r\n  \\tags\\:
 {},\r\n  \\primaryId\\: \\56babbb6-1371-406b-8de9-1f750954603f\\,\r\n 
 \\isPrivate\\: true,\r\n  \\entityType\\: \\Service\\\r\n}",   
   "targets": \[   
     "56babbb6-1371-406b-8de9-1f750954603f"   
   \],   
   "messageId": null   
 } 
 ```

*UpdateServiceDefinition JSON*

```json
 {   
   "Route": " 56babbb61371406b8de91f750954603f ",   
   "primaryEntityId": "56babbb6-1371-406b-8de9-1f750954603f",   
   "secoundaryEntityId": null,   
   "secondaryEntityId": null,   
   "eventType": "updateServiceDefinition",   
   "entityType": "Service",   
   "source": null,   
   "subSystem": null,   
   "ts": "2023-09-21T10:04:45.8318472Z",   
   "actor": null,   
   "supportCode": null,   
   "payload": "{\r\n  \\name\\: \\TeStIntegration\\,\r\n 
 \\businessOwner\\: \\\\,\r\n  \\description\\: \\test update
 service\\,\r\n  \\shortName\\: \\test123\\,\r\n  \\tags\\: {},\r\n 
 \\primaryId\\: \\56babbb6-1371-406b-8de9-1f750954603f\\,\r\n 
 \\isPrivate\\: true,\r\n  \\entityType\\: \\Service\\\r\n}",   
   "targets": \[   
     "56babbb6-1371-406b-8de9-1f750954603f"   
   \],   
   "messageId": null   
 } 
 ```

*DeleteServiceDefinition JSON*

```json
 {   
   "Route": " 56babbb61371406b8de91f750954603f ",   
   "primaryEntityId": "56babbb6-1371-406b-8de9-1f750954603f",   
   "secoundaryEntityId": null,   
   "secondaryEntityId": null,   
   "eventType": "deleteServiceDefinition",   
   "entityType": "Service",   
   "source": null,   
   "subSystem": null,   
   "ts": "2023-09-21T10:04:48.6445178Z",   
   "actor": null,   
   "supportCode": null,   
   "payload": "{\r\n  \\name\\: \\TeStIntegration\\,\r\n 
 \\businessOwner\\: \\\\,\r\n  \\description\\: \\test update
 service\\,\r\n  \\shortName\\: \\test123\\,\r\n  \\tags\\: {},\r\n 
 \\primaryId\\: \\56babbb6-1371-406b-8de9-1f750954603f\\,\r\n 
 \\isPrivate\\: true,\r\n  \\entityType\\: \\Service\\\r\n}",   
   "targets": \[   
     "56babbb6-1371-406b-8de9-1f750954603f"   
   \],   
   "messageId": null   
 } 
 ```

*UserSubscriptionRequestEvent JSON*

```json
 {   
   "Route": " ab0408cab27f4224ac1bc82683a492a6 ",   
   "primaryEntityId": "ab0408ca-b27f-4224-ac1b-c82683a492a6",   
   "secoundaryEntityId": "dd7084f7-911e-4b7b-b42c-d528d3503bbb",   
   "eventType": "UserSubscriptionRequestEvent",   
   "entityType": "Subscription",   
   "source": null,   
   "subSystem": null,   
   "ts": "2019-06-24T08:59:55.372394Z",   
   "actor": "A5CA71B3-EF03-4D8F-BF5B-DDBEBAC0052C",   
   "supportCode": null,   
   "payload": "{\r\n  \\accessLevel\\: \\Data consumer\\,\r\n 
 \\serviceType\\: 2,\r\n  \\serviceTitle\\: \\Veracity Data
 Fabric\\,\r\n  \\serviceInternalName\\: \\VeracityDataFabric\\,\r\n 
 \\user\\: {\r\n    \\firstName\\: \\Test2\\,\r\n    \\lastName\\:
 \\Veracity\\,\r\n    \\displayName\\: \\Veracity, Test2\\,\r\n   
 \\email\\: \\emailaddretwo@gmail.com\\,\r\n    \\id\\:
 \\dd7084f7-911e-4b7b-b42c-d528d3503bbb\\\r\n  },\r\n  \\primaryId\\:
 \\ab0408ca-b27f-4224-ac1b-c82683a492a6\\,\r\n  \\secoundaryId\\:
 \\dd7084f7-911e-4b7b-b42c-d528d3503bbb\\,\r\n  \\entityType\\:
 \\Subscription\\,\r\n  \\actor\\:
 \\A5CA71B3-EF03-4D8F-BF5B-DDBEBAC0052C\\\r\n}",   
   "targets": \[   
     "ab0408ca-b27f-4224-ac1b-c82683a492a6"   
   \]   
 } 
 ```

*UserSubscriptionRevokeEvent*

```json
 {   
   "Route": " ab0408cab27f4224ac1bc82683a492a6 ",   
   "primaryEntityId": "ab0408ca-b27f-4224-ac1b-c82683a492a6",   
   "secoundaryEntityId": "56d5f4cd-5521-4db9-959d-045c30523266",   
   "eventType": "UserSubscriptionRevokeEvent",   
   "entityType": "Subscription",   
   "source": null,   
   "subSystem": null,   
   "ts": "2019-06-25T06:00:08.5519815Z",   
   "actor": "A5CA71B3-EF03-4D8F-BF5B-DDBEBAC0052C",   
   "supportCode": null,   
   "payload": "{\r\n  \\serviceType\\: 2,\r\n  \\serviceTitle\\:
 \\Veracity Data Fabric\\,\r\n  \\serviceInternalName\\:
 \\VeracityDataFabric\\,\r\n  \\primaryId\\:
 \\ab0408ca-b27f-4224-ac1b-c82683a492a6\\,\r\n  \\secoundaryId\\:
 \\56d5f4cd-5521-4db9-959d-045c30523266\\,\r\n  \\entityType\\:
 \\Subscription\\,\r\n  \\actor\\:
 \\A5CA71B3-EF03-4D8F-BF5B-DDBEBAC0052C\\\r\n}",   
   "targets": \[   
     "ab0408ca-b27f-4224-ac1b-c82683a492a6"   
   \]   
 } 
 ```
  
## Events you can listen to

When you create a Domain Event Management resource, you choose the service about which you want to get notifications, and you choose the type of notifications you want to subscribe to.

An `entityType` is the thing about which you want to get information, and in the event messages you get, you can see different types of entities such as `Subscription`, `Service`, `User`, `Tenant`, and so on.

Below is a description of the main entity types:

-   User – Information tied primarily to the user. For example, email
    address change. It also has information on the opt-in states
    (approved terms of use or service-specific terms of use). Also,
    custom opt-ins like developer preview in the Developer. 

-   Service – Changes done in Developer towards the service definition.
    For example, you have an app, and you want images and logos to be
    consistent. So, upload a picture in the widget in Developer and get
    this message flowing through Domain Events.  

-   Subscription – User's relationship to a service. For example, adding
    a new user to the service. This legacy entity type doesn’t consider
    VTM service, hierarchical relations, and so on. 

-   Tenant – Every change in the tenant. Info about user groups, your
    direct subscriptions, and so on. It’s done to make a replica of the
    VTM data structure in your own database so you’re not dependent on
    VTM APIs. The first event tells you’ve been installed in a tenant,
    and you can use it in an automation.  

Note that: 

-   In each topic, there are multiple data schemas and event types. For
    example, you can distinguish if you want information on deleted
    users only. 

-    The topic list is dynamic.  

Always use a unique schema reference. The schema reference is a
combination of the entity type and event type. 

## Error handling and logging 

When using Domain Events, your application should have the
following: 

-   Error handling – There should be a retry mechanism if an operation
    fails. It may be already covered by your framework, but check it. 
-   Logging – You need logs to tell when an event or consumer is having
    a problem and to know what may have caused it. 