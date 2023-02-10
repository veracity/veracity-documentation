# Data consumer

Veracity IoT ensures secure access to data. Only users granted access can read data.

A data consumer reads data from Veracity IoT using:
- Api : query for data using rest-api 
- Listen to subscription queue: Events you have subscribed to are published to your own service bus
- Event hub: Sensor-data can be written directly to an event-hub consuming application can access using connection string
 
[Sensor data query api](IotQueryApi.md)
[Event data query api](EventQueryApi.md)
[Consume events directly from service bus for real-time access](ServiceBusConsumerAzureFunction.md)