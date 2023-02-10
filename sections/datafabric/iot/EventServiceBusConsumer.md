# Subscribe to events 
Using the Veracity Event broker as infrastructure, applications (services) can be built that have real time access to data and events are received to private queues for that application.

Veracity Event Broker is built on Azure Service Bus, a fully managed enterprise message broker which is used to build applications and services that use an event-driven architecture. It provides message queues and publish-subscribe topics with at-least-once delivery guarantees. It also supports sessions, transactions, and dead-letter queues. 

## How to consume events from the queue
There are several options for how to consume the events. The following patterns are explained and code examples exist on github

- [Service Bus consumer using Azure Functions](ServiceBusConsumerAzureFunction.md). This guide will walk you through the process of creating a new Azure Function that uses a Service Bus trigger to consume messages in real-time. Code example written in C#.
- [Service Bus consumer using WebPubSub](ServiceBusConsumerWebPubSub.md). This tutorial will guide you through the process of creating a single page application (SPA) that connects to an Azure ServiceBus queue and consumes messages in real-time via a WebSocket connection.
- [Service Bus consumer using Docker](ServiceBusConsumerDocker.md). This tutorial will walk you through the steps to create an Azure ServiceBus consumer which receives messages from a queue. We'll create a C# console application which can optionally be run in a Docker container. 

## Security model
Each application receives a connection string to its private queue where only events application is subscribing to are being published. If an application is multi-tenant, there will be one queue per tenant.  
Each queue can receive events from multiple "data providers" and assets.

### How to subscribe to events
