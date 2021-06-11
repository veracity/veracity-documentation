---
author: Benedikte Kallåk
description: Description of quick start section
---

# Generic event

Using naming of topics, any events can be defined as a set of datapoints in a dataset.
The body is an array of elements in which each element consist of an equipment Id and a dataset.



```json
{
  "Topic": {
    "Name": "topictest",
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
        "NumberOfBodyElements": "3",
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
       },
        "DataSet": [
          {
            "Id": [
              {
                "Schema": "Maranics",
                "Key": "Thruster1-Status",
                "Name": "Bow Thruster 1"
              },
              {
                "Schema": "DNV-Vis",
                "Key": "443.1-1F/C323//status",
                "Name": "Bow Thruster 1"
              }
            ],
            "Value": "running",
            "Metadata": {
              "Detail": "1 / 2"
            }
          }
        ]
      }

    ]
  }
}

```
