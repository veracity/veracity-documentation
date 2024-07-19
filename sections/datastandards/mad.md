---
author: Veracity
description: Description of Maintenance Activity Data (MAD) Data Standard in Veracity.
---

# Maintenance Activity Data (MAD)

Maintenance Activity Data (MAD) is the DNV standard for maintenance activity data from vessels, and a data service on DNV’s Veracity Data Platform supporting digital class surveys.

The MAD data service on Veracity is continuously assuring data from vessels independent of class society. By submitting data to Veracity MAD, your data is structured, analyzed, enriched and quality assured before you can use it for digital class surveys or in services running on Veracity, like Machinery Maintenance Connect and Safety Connect.

A full and comprehensive description of the MAD standard can be found in the MAD User Guide (work in progress, we will link to it once it is ready).

## Transfer data to MAD through API
Data can be submitted to DNV’s Veracity MAD via continuous and automated transfer using modern REST API interfaces. Please contact Veracity Support if you want to know more about how to establish automated transfer of MAD data.

## MAD API specification
* [API specification in yaml format](https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/mad/mad.yaml)

Later, you will also be able to [see and download the specification in API Explorer](https://developer.veracity.com/docs/section/api-explorer/ppazc03b2c1f-c27a-4748-a03e-9065d5504fda/apis/provider/8f41f575445d4491920432654c671360).

## Data template
* [Data Template - MAD v 1.0 in PDF](https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/mad/Data%20Template%20-%20MAD%20v1.0.pdf)
* [Data Template - MAD v 1.0. in Power Point](https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/mad/Data%20Template%20-%20MAD.pptx)

## MAD data fields
* [MAD data fields](https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/mad/MAD%20datafields.xlsx)

## MAD schema
MAD consists of one schema. A schema is a definition of how to fill in the maintenance activity data, with defined columns and clear rules for what to put into each of the columns/rows.

Below is the MAD schema.
```json
{
  "required": [
    "company",
    "source",
    "created",
    "tasks"
  ],
  "properties": {
    "company": {
      "type": "string"
    },
    "source": {
      "type": "string"
    },
    "created": {
      "type": "string",
      "format": "date"
    },
    "tasks": {
      "items": {
        "type": "object",
        "required": [
          "imonumber",
          "vesselname",
          "classcomponent",
          "componentcode",
          "componentname",
          "jobtype",
          "jobname",
          "jobno",
          "jobdescription",
          "localjobdescription",
          "criticality",
          "workhours",
          "duehours",
          "donehours",
          "duedate",
          "donedate",
          "interval",
          "intervaltype",
          "postponed",
          "postponedhours",
          "postponeddate",
          "department",
          "reporting",
          "remarks",
          "reason",
          "symptom",
          "conditionbefore",
          "conditionafter"
        ],
        "properties": {
          "imonumber": {
            "type": "integer",
            "minimum": 0,
            "maximum": 9999999,
            "required": true
          },
          "vesselname": {
            "type": "string",
            "maxLength": 64,
            "required": true
          },
          "classcomponent": {
            "type": "string",
            "maxLength": 64
          },
          "componentcode": {
            "type": "string",
            "maxLength": 64,
            "required": true
          },
          "componentname": {
            "type": "string",
            "maxLength": 256,
            "required": true
          },
          "componenttype": {
            "type": "string",
            "maxLength": 64,
            "enum": [ "MACH", "DRILL", "PROD" ]
          },
          "componentcategory": {
            "type": "string",
            "maxLength": 64,
            "enum": [ "STAT", "N-STAT" ]
          },
          "jobtype": {
            "type": "string",
            "maxLength": 64
          },
          "jobname": {
            "type": "string",
            "maxLength": 64,
            "required": true
          },
          "jobno": {
            "type": "string",
            "maxLength": 64,
            "required": true
          },
          "jobrevno": {
            "type": "string",
            "maxLength": 64
          },
          "jobdescription": {
            "type": "string",
            "maxLength": 1024
          },
          "localjobdescription": {
            "type": "string",
            "maxLength": 1024
          },
          "criticality": {
            "type": "string",
            "maxLength": 64
          },
          "workhours": {
            "type": "integer",
            "minimum": 0
          },
          "duehours": {
            "type": "integer",
            "minimum": 0
          },
          "donehours": {
            "type": "integer",
            "minimum": 0
          },
          "duedate": {
            "type": "string",
            "format": "date"
          },
          "donedate": {
            "type": "string",
            "format": "date",
            "required": true
          },
          "interval": {
            "type": "string",
            "maxLength": 64
          },
          "intervaltype": {
            "type": "string",
            "maxLength": 64
          },
          "postponed": {
            "type": "string",
            "maxLength": 64
          },
          "postponedhours": {
            "type": "integer",
            "minimum": 0
          },
          "postponeddate": {
            "type": "string",
            "format": "date"
          },
          "deferred": {
            "type": "string",
            "maxLength": 64,
            "enum": [ "YES", "NO" ]
          },
          "measurement": {
            "type": "string",
            "maxLength": 256
          },
          "barrier": {
            "type": "string",
            "maxLength": 64
          },
          "department": {
            "type": "string",
            "maxLength": 64
          },
          "reporting": {
            "type": "string",
            "maxLength": 1024
          },
          "remarks": {
            "type": "string",
            "maxLength": 1024
          },
          "reason": {
            "type": "string",
            "maxLength": 1024
          },
          "symptom": {
            "type": "string",
            "maxLength": 1024
          },
          "conditionbefore": {
            "type": "string",
            "maxLength": 64
          },
          "conditionafter": {
            "type": "string",
            "maxLength": 64
          },
          "solas": {
            "type": "string",
            "maxLength": 64
          },
          "pmod": {
            "type": "string",
            "maxLength": 128
          }
        }
      }
    }
  }
}
```

## Data sample for MAD
```json
{
  "company":"Test company",
  "source":"From system",
  "created":"2021-06-09",
  "tasks": [
    {
      "imonumber": 1234567,
      "vesselname": "Test vessel",
      "classcomponent": "ABC",
      "componentcode": "123.123.123",
      "componentname": "Test comp",
      "jobtype": "CHK",
      "jobname": "Check comp",
      "jobno": "1",
      "jobdescription": "Check all components",
      "localjobdescription": "descriptive",
      "criticality": "Low",
      "duehours": 0,
      "donehours": 0,
      "workhours": 1,
      "duedate": "2020-02-04",
      "donedate": "2020-04-11",
      "department": "ENG",
      "interval": "1 mnth",
      "intervaltype": "CAL",
      "postponed": "No",
      "postponeddate": "2020-04-11",
      "postponedhours": 0,
      "reporting": "descriptive",
      "remarks": "descriptive",
      "reason": "descriptive",
      "symptom": "descriptive",
      "conditionbefore": "Good",
      "conditionafter": "Good",
      "solas": ""
    },
    {
      "imonumber": 1234567,
      "vesselname": "Test vessel",
      "classcomponent": "ABC",
      "componentcode": "123.123.123",
      "componentname": "Test comp",
      "jobtype": "CHK",
      "jobname": "Check comp",
      "jobno": "2",
      "jobdescription": "Check all components",
      "localjobdescription": "descriptive",
      "criticality": "Low",
      "duehours": 0,
      "donehours": 0,
      "workhours": 1,
      "duedate": "2020-02-04",
      "donedate": "2020-04-11",
      "department": "ENG",
      "interval": "1 mnth",
      "intervaltype": "CAL",
      "postponed": "No",
      "postponeddate": "2020-04-11",
      "postponedhours": 0,
      "reporting": "descriptive",
      "remarks": "descriptive",
      "reason": "descriptive",
      "symptom": "descriptive",
      "conditionbefore": "Good",
      "conditionafter": "Good",
      "solas": ""
    }

  ]}

```