---
author: Benedikte Kallåk
description: Description of quick start section
---

# Topology Message
An topology describes the equipment with its systemdata.

ISO 19848 standard is used to identify the equipment. In this example DNV-Vis structure is used to name the equiment with VIS code.
Optianlly, a custom classification can be provided.

```json
{
  "Topic": {
    "Name": "Equipment/TopologyReport",
    "Version": "1.0"
  },
  "Asset": {
    "Name": "ASSETNAME",
    "Id": [
      {
        "Schema": "IMO",
        "Id": "123"
      }      
    ]
  },
  "TimeStampUtc": "2021-04-06T12:22:48.9502389Z",
  "Payload": {
    "Header": {
      "Event": {
        "EventId": "0cad04ab-93c1-4051-92fe-f1ffea67b05b",
        "TimeStampUtc": "2021-04-06T12:22:48.9506662Z",
        "TimeStampLocal": "2021-04-06T14:22:48.950716+02:00",
        "EventSource": "eventsource",
        "NumberOfBodyElements": "1",
        "ReportMethod": "automatic",
        "TriggerType": "regular_daily"
      },
      "Operation": {
        "OperatingMode": "Sailing",
        "VoyageId": "543",
        "GeoPosition": {
          "GeoLocation": {
            "SourceId": "APS-A",
            "Latitude": -19.142333333333333,
            "Longitude": 118.13816666666666
          },
          "Location": {
            "Name": "Bergen",
            "Type": "unlocode",
            "Code": "ABCDEF12"
          }
        }
      },
      "ReportedBy": {
        "Position": "Chief Engineer",
        "UserId": "Ola N"
      }
    },
    "Body": [
      {
        "Equipment": {
          "Id": [
            {
              "Schema": "DNV-Vis",
              "Version": "3.3",
              "Code": "443.1-1F/C323",
              "Name": "Bow Thruster",
              "Custom": {
                "Class": "Machinery",
                "Type": "Thruster/BowThruster"
              }
            }            
          ],
          "SystemData": {
            "Manufacturer": "Manufacturer123",
            "ModelName": "modelname",
            "ModelNo": "modelnumber",
            "HardwareType": "HardwareType123",
            "HardwareValue": "HardwareValue123",
            "SoftwareVersion": "swversion",
            "CertificateReference": "cert12"
          }          
        }
        
      }

    ]
  }
}

```

If your solution cannot use the device libraries, devices can use the MQTT v3.1.1, HTTPS 1.1, or AMQP 1.0 protocols to connect natively to your hub.
- SDK: https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-sdks
- Communicate with your IoT hub using the MQTT protocol: https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-mqtt-support
