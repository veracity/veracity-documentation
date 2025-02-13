---
author: Veracity
description: These are release notes for the first release of Domain Events in February 2025.
---
We are releasing Domain Events, a service bus that lets your application listen to events happening in the Veracity ecosystem and react to them in real-time. This simplifies integration with Veracity, enabling you to build more responsive and efficient applications by eliminating the need for constant polling and improving data synchronization.

# Events you can listen to
The service bus supports a wide range of events related to:

* User management: Track user account creation, updates, and deletions.
* Service configuration: Receive notifications about changes to service definitions and administrators.
* Tenant administration: Stay informed about updates to tenant information and user groups.
* Subscription management: Handle user subscription requests and revocations dynamically.

## Message format
Service bus messages are delivered in a structured JSON format, containing both an envelope and a payload of data. Key fields include identifiers, event types, timestamps, and details about the changes.

## Error handling and logging
Robust error handling and logging are essential for ensuring reliable integration with the Domain Events. Your application should implement appropriate mechanisms for retrying failed operations and maintaining a comprehensive log of events.

## Documentation
See [Domain Events documentation](servicebus.md).