---
author: Veracity
description: Description of Maintenance Activity Data (MAD) Data Standard in Veracity.
---

# Maintenance Activity Data (MAD)

<a href="https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/mad/MAD%20datafields.xlsx" download>
    <img src="assets/mad-interface.png" alt="Interface Description" height="40">
  </a>

<br>

<a href="https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/mad/mmc_schema.json" download>
    <img src="assets/mad-schema.png" alt="MAD schema" height="30">
 </a>

<a href="https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/mad/test_json_body.json" download>
    <img src="assets/mad-data-sample.png" alt="MAD data sample" height="30">
 </a>

Maintenance Activity Data (MAD) is the DNV standard for maintenance activity data from vessels, and a data service on DNV’s Veracity Data Platform supporting digital class surveys.

The MAD data service on Veracity is continuously assuring data from vessels independent of class society. By submitting data to Veracity MAD, your data is structured, analyzed, enriched and quality assured before you can use it for digital class surveys or in services running on Veracity, like [Machinery Maintenance Connect](https://www.dnv.com/services/machinery-maintenance-connect-mmc--168870/) and Safety Connect.

## Transfer data to MAD through API
Data can be submitted to DNV’s Veracity MAD via continuous and automated transfer using modern REST API interfaces. Please contact Veracity Support if you want to know more about how to establish automated transfer of MAD data.

## MAD API specification
* [API specification in yaml format](https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/mad/mad.yaml)

Later, you will also be able to [see and download the specification in API Explorer](https://developer.veracity.com/docs/section/api-explorer/ppazc03b2c1f-c27a-4748-a03e-9065d5504fda/apis/provider/8f41f575445d4491920432654c671360).

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