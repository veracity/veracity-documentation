---
author: Veracity
description: Description of Operational Vessel Data Standards in Veracity
---

# Operational Vessel Data (OVD)

Operational Vessel Data (OVD) is a standard for log abstracts and other operational data from vessels, and a data service on DNV’s Veracity Data platform.

The OVD data service on Veracity is continuously assuring data from thousands of vessels. By submitting data to Veracity OVD, your data is structured, analyzed, enriched and quality assured before you have the option to use it in one of the many services running on Veracity, like MRV and DCS verification, Emissions Connect, or to share quality assured data via the Veracity Data Workbench with stakeholders or other parties or solutions that will utilize your data, like Poseidon Principles or Sea Cargo Charter.

A full and comprehensive description of the OVD standard can be found in [this Excel document](https://veracitycdnprod.blob.core.windows.net/digisales/myservices/cdn/content/marketplace/docs/OVD%203.0%20interface%20description%20-%20STAG.xlsx). To further learn, play with and test your OVD data, the [OVD Guide](https://ovdguide.veracityapp.com/) has interactive guidance to the most important elements of OVD and allow you to test upload of files.

OVD consists of several schemas. A schema is a definition of how to fill in a sheet in Excel, with defined columns and clear rules for what to put into each of the columns/rows. The two most used schemas in OVD are Log Abstract (LA), listing all key events from the vessels’ operations, and the Bunkers file (BR), listing all bunkers in the relevant period. Both the Log Abstract and the Bunkers file are required for MRV and DCS verification.
Below is an example of how the OVD Log Abstract would look for a vessel sailing from Hamburg to Rotterdam:

<figure>
    <img src="assets/data-table.png"/>
</figure>

Data can be submitted to DNV’s Veracity OVD via continuous and automated transfer using modern REST API interfaces, or via manual upload of CSV files. Please contact [Veracity support](mailto:support@veracity.com) if you want to know more about how to establish automated transfer of OVD data.
