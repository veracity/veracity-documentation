---
author: Veracity
description: These are release notes for the first release of Service Bus in February 2025.
---
We are releasing the Veracity service bus which lets your application listen to events happening in the Veracity ecosystem and react to them in real-time. This simplifies integration with Veracity, enabling you to build more responsive and efficient applications by eliminating the need for constant polling and improving data synchronization.

## Events you can listen to
The service bus supports a wide range of events related to:

* User management: Track user account creation, updates, and deletions.
* Service configuration: Receive notifications about changes to service definitions and administrators.
* Tenant administration: Stay informed about updates to tenant information and user groups.
* Company interactions: Monitor company creation, modifications, and affiliation requests.
* Subscription management: Handle user subscription requests and revocations dynamically.

## Message format
Service bus messages are delivered in a structured JSON format, containing both an envelope and a payload of data. Key fields include identifiers, event types, timestamps, and details about the changes.

## Error handling and logging
Robust error handling and logging are essential for ensuring reliable integration with the service bus. Your application should implement appropriate mechanisms for retrying failed operations and maintaining a comprehensive log of events.

## Documentation
See [Veracity service bus documentation](servicebus.md).