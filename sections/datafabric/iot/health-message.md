---
author: Benedikte Kallåk
description: Description of quick start section
---

# Health Message
A health message is related to an equipment. Health status is provided as: 
- Green: All healthy
- Yellow: Need attention
- Red: Not healthy

The topology of the equipment is described as SystemData. ISO 19848 standard is used to identify the equipment. In this example DNV-Vis structure is used to name the equipment with VIS code.
A custom classification can be provided in addition.



```json
{
  "Topic": {
    "Name": "HealthReport",
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
        "NumberOfBodyElements": "2",
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
          "HealthData": {
            "Analyst": "analyst1",
            "HealthState": "Green",
            "RemainingUsefulLife": "2 hours",
            "Remarks": "remarks1"
          }
        },       
      
	  {
        "Equipment": {
          "Id": [
            {
              "Schema": "DNV-Vis",
              "Version": "3.3",
              "Code": "443.2-1F/C323",
              "Name": "Bow Thruster",
              "Custom": {
                "Class": "Machinery",
                "Type": "Thruster/BowThruster"
              }
            }            
          ],          
          "HealthData": {
            "Analyst": "analyst1",
            "HealthState": "Red",
            "RemainingUsefulLife": "2 hours",
            "Remarks": "remarks1"
          }
        }        
      }
    ]
  }
}

    ]
  }
}

```

Event id is OEMs unique identifier for events
Id of equipment should be using the VIS naming schema.