---
author: Veracity
description: Description of Operational Vessel Data Standards in Veracity
---

# Operational Vessel Data (OVD)

  <a href="https://veracitycdnprod.blob.core.windows.net/digisales/myservices/cdn/content/marketplace/docs/OVD%203.2%20interface%20description.xlsx" target="_blank">
    <img src="assets/Btn-InterfaceDescription.png" alt="Interface Description" height="40">
  </a>

  <br>

  <a href="https://ovdguide.veracityapp.com" target="_blank">
    <img src="assets/Btn-OVDGuide.png" alt="OVD Guide" height="30">
  </a>

  <a href="https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2Fveracity%2Fveracity-documentation%2Fmaster%2Fsections%2Fdatastandards%2Fassets%2FCSVfileconverterv1.83.xlsm&wdOrigin=BROWSELINK" target="_blank">
    <img src="assets/Btn-CSVfileConverter.png" alt="CSV File Converter" height="30">
  </a>

  <a href="https://veracitycdnprod.blob.core.windows.net/digisales/myservices/cdn/content/marketplace/docs/OVD%20sample%20files.zip" target="_blank">
    <img src="assets/Btn-Samples.png" alt="Samples" height="30">
  </a>

  <a href="https://www.veracity.com/ovd-whitepaper" target="_blank">
    <img src="assets/Btn-OVDWhitepaper.png" alt="OVD Whitepaper" height="30">
  </a>

<br>

Operational Vessel Data (OVD) is a standard for log abstracts and other operational data from vessels, and a data service on DNV’s Veracity Data Platform. To learn more about the purpose, history and background of OVD, have a look at the <a href="https://www.veracity.com/ovd-whitepaper" target="_blank">OVD Whitepaper</a>.

The OVD data service on Veracity is continuously assuring data from thousands of vessels. By submitting data to Veracity OVD, your data is structured, analyzed, enriched and quality assured before you have the option to use it in one of the many services running on Veracity, like MRV and DCS/CII verification, Emissions Connect, or to share quality assured data via the Veracity Data Workbench with stakeholders or other parties or solutions that will utilize your data, like Poseidon Principles or Sea Cargo Charter. 

A full and comprehensive description of the OVD standard can be found in the [OVD Interface Description](https://veracitycdnprod.blob.core.windows.net/digisales/myservices/cdn/content/marketplace/docs/OVD%203.2%20interface%20description.xlsx). To further learn, play with and test your OVD data, the [OVD Guide](https://ovdguide.veracityapp.com) has interactive guidance to the most important elements of OVD and allow you to test upload files. 

OVD consists of several schemas. A schema is a definition of how to fill in the operational vessel data, with defined columns and clear rules for what to put into each of the columns/rows. The two most used schemas in OVD are Log Abstract (LA), listing all key events from the vessels’ operations, and the Bunker Reports (BR), listing all bunkers in the relevant period. Both the Log Abstract and the Bunker Reports are required for DNV’s verification services, like MRV and DCS/CII verification. 

Below is an example of how the OVD Log Abstract would look for a vessel sailing from Hamburg to Rotterdam: 

<figure>
    <img src="assets/data-table.png"/>
</figure>

Have a look at the [Sample Files](https://veracitycdnprod.blob.core.windows.net/digisales/myservices/cdn/content/marketplace/docs/OVD%20sample%20files.zip) to find more examples. 

Data can be submitted to DNV’s Veracity OVD via continuous and automated transfer using modern REST API interfaces, or via manual upload of CSV files. Please contact [Veracity Support](mailto:support@veracity.com) if you want to know more about how to establish automated transfer of OVD data. 

The [CSV File Converter](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2Fveracity%2Fveracity-documentation%2Fmaster%2Fsections%2Fdatastandards%2Fassets%2FCSVfileconverterv1.83.xlsm&wdOrigin=BROWSELINK) can be used to enter OVD data via Excel for selected, basic use cases.
