---
author: Veracity
description: Service bus documentation
---

# Service Bus Documentation 

### Overview 

The service bus is useful for service providers and Veracity developers because it binds a service bus connection to the service and sends notifications about what happens to your service. Thus, the service bus lets the applications react to changes rather than periodically pull data and check for changes. 

Before using the service bus, you must configure it in the Developer
portal and specify what kind of notifications you want to receive. 

### Setup 

To use the Veracity service bus: 

1.  Create Veracity service. Alternatively, use an existing service. 
2.  In the Developer portal, choose which type of information you want
    to listen to. For example, you can listen to changes regarding users
    (user subscriptions) or tenants.  
3.  In Developer, choose how long the messages from the bus will live.
    You can also check the connection string and put it in the key vault
    for later use. 

After the setup, the Veracity service bus notifies you about changes in
the information you listen to. 

Note that you can enable and disable service bus notifications for your
applications. 

### Confidentiality 

Service bus sends notifications only to relevant services and does not
share information with parties that are not supposed to get it.  

In detail: 

-   Changes specific to your service are shared only with you and the
    service.  

-   Changes to user subscriptions are notified to all tenants and
    services that the user has a relationship with. However,
    notifications are sent through separate channels to ensure
    confidentiality. 

Note that
[tenants](https://dnv.sharepoint.com/:w:/r/teams/VeracityIdentityTrustNetwork/_layouts/15/Doc.aspx?sourcedoc=%7BCA837B6C-5984-4FD5-9AE5-B187ED93CB3B%7D&file=Veracity%20Tenant%20Management%20for%20Developers.docx&action=default&mobileredirect=true%22%20%EF%B7%9FHYPERLINK%20%22https://dnv.sharepoint.com/:w:/r/teams/VeracityIdentityTrustNetwork/_layouts/15/Doc.aspx?sourcedoc=%7BCA837B6C-5984-4FD5-9AE5-B187ED93CB3B%7D&file=Veracity%20Tenant%20Management%20for%20Developers.docx&action=default&mobileredirect=true)
can get all information relating to tenant users (profiles) and user
groups. So, every application installed on a tenant has access to it.  

### Messages from the service bus 

You can see the messaging pack containing message schemas on
[Veracity NuGet](https://www.nuget.org/profiles/Veracity)
Service bus messages have an envelope and a payload with data. Note that
the service bus does not send error messages. 

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
 public abstract class EventPayload : IEventPayload   
 {   
   public string PrimaryId { get; set; }   
    \[Obsolete("Typo, will be removed in the future", false)\]   
    public string SecondaryId { get; set; }   
    public string SupportCode { get; set; }   
    public EntityTypes EntityType { get; set; }   
    public string Actor { get; set; }   
} 
```
 

### Common messages 

This section shows the most common messages in the flow with their
schemas and the event types mapping to them. Note that a single topic
can have multiple schemas mapping to it. 

*CompanyCreateEvent JSON*

```json
 {   
   "route": null,   
   "primaryEntityId": "d361cda3-2f5c-4b89-a9ea-67a24c7747ce",   
   "secoundaryEntityId": null,   
   "secondaryEntityId": null,   
   "eventType": "CompanyCreateEvent",   
   "entityType": "Company",   
   "source": "tenantManagement",   
   "subSystem": null,   
   "ts": "2023-09-25T11:06:09.7514515Z",   
   "actor": "3dc22382-3fec-42de-a828-9d1d3ebedd6e",   
   "supportCode": "824d9f09-adef-494e-ac20-a0afdd374089",   
   "payload": "{\r\n  \\company\\: {\r\n    \\name\\:
 \\string\\,\r\n    \\address\\: {},\r\n    \\domains\\:
 \\kk.no\\,\r\n    \\mdmName\\: \\string\\,\r\n    \\customerId\\:
 \\string\\\r\n  },\r\n  \\primaryId\\:
 \\d361cda3-2f5c-4b89-a9ea-67a24c7747ce\\,\r\n  \\supportCode\\:
 \\824d9f09-adef-494e-ac20-a0afdd374089\\,\r\n  \\entityType\\:
 \\Company\\,\r\n  \\actor\\:
 \\3dc22382-3fec-42de-a828-9d1d3ebedd6e\\\r\n}",   
   "targets": \[   
     "veracity"   
   \],   
   "messageId": null   
 } 
 ```
  

*CompanyModifiedEvent JSON*

```json
 {   
   "route": null,   
   "primaryEntityId": "c426bc01-1fe4-42f9-a312-d86eae7e9dc5",   
   "secoundaryEntityId": null,   
   "secondaryEntityId": null,   
   "eventType": "CompanyModifiedEvent",   
   "entityType": "Company",   
   "source": "tenantManagement",   
   "subSystem": null,   
   "ts": "2023-08-31T10:20:59.8840617Z",   
   "actor": "c681d6fb-fcac-4bd2-9168-312035262633",   
   "supportCode": "b8b61b0c-1656-4c37-9cdf-1e47b3046447",   
   "payload": "{\r\n  \\name\\: \\Heimdalr Guitars\\,\r\n  \\domains\\:
 \\gmail.com\\,\r\n  \\mdmName\\: \\Heimdalr Guitars\\,\r\n 
 \\customerId\\: \\123456789\\,\r\n  \\primaryId\\:
 \\c426bc01-1fe4-42f9-a312-d86eae7e9dc5\\,\r\n  \\supportCode\\:
 \\b8b61b0c-1656-4c37-9cdf-1e47b3046447\\,\r\n  \\entityType\\:
 \\Company\\,\r\n  \\actor\\:
 \\c681d6fb-fcac-4bd2-9168-312035262633\\\r\n}",   
   "targets": \[   
     "veracity"   
   \],   
   "messageId": null   
 } 
 ```

*CompanyAffiliationRequestEvent JSON*

```json
 {   
   "route": null,   
   "primaryEntityId": "c426bc01-1fe4-42f9-a312-d86eae7e9dc5",   
   "secoundaryEntityId": "b8da9d4d-dd5b-41af-a022-c0c52c2e13ce",   
   "secondaryEntityId": "b8da9d4d-dd5b-41af-a022-c0c52c2e13ce",   
   "eventType": "CompanyAffiliationRequestEvent",   
   "entityType": "Company",   
   "source": "tenantManagement",   
   "subSystem": null,   
   "ts": "2023-08-31T12:54:15.0757789Z",   
   "actor": "c681d6fb-fcac-4bd2-9168-312035262633",   
   "supportCode": "0f9cbee3-11ba-4a61-84bf-1d93b93aa144",   
   "payload": "{\r\n  \\primaryId\\:
 \\c426bc01-1fe4-42f9-a312-d86eae7e9dc5\\,\r\n  \\secoundaryId\\:
 \\b8da9d4d-dd5b-41af-a022-c0c52c2e13ce\\,\r\n  \\secondaryId\\:
 \\b8da9d4d-dd5b-41af-a022-c0c52c2e13ce\\,\r\n  \\supportCode\\:
 \\0f9cbee3-11ba-4a61-84bf-1d93b93aa144\\,\r\n  \\entityType\\:
 \\Company\\,\r\n  \\actor\\:
 \\c681d6fb-fcac-4bd2-9168-312035262633\\\r\n}",   
   "targets": \[   
     "veracity"   
   \],   
   "messageId": null   
 } 
```

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
  

### How to get connection strings 

In the Developer portal, you can check connection strings for the
service bus and then save them to your key vault for later use. Note
that, as of May 2024, this is not possible yet. 

### Entity types 

Entity types are things you want information about, mainly: 

-   User – Information tied primarily to the user. For example, email
    address change. It also has information on the opt-in states
    (approved terms of use or service-specific terms of use). Also,
    custom opt-ins like developer preview in the Developer. 

-   Service – Changes done in Developer towards the service definition.
    For example, you have an app, and you want images and logos to be
    consistent. So, upload a picture in the widget in Developer and get
    this message flowing through the service bus.  

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

### Error handling and logging 

When using the Veracity service bus, your application should have the
following: 

-   Error handling – There should be a retry mechanism if an operation
    fails. It may be already covered by your framework, but check it. 

-   Logging – You need logs to tell when an event or consumer is having
    a problem and to know what may have caused it. 
