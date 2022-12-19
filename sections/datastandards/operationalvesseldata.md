---
author: Veracity
description: Description of Operational Vessel Data Standards in Veracity
---

# Operational Vessel Data (OVD)

[<img src="assets/OVD-interface-description-button.png" align="left" alt="assets/OVD-interface-description-button" height="50">](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2Fveracity%2Fveracity-documentation%2Ff1d378a3791f32f1bcfb9ae7816967e6f8cdcb81%2Fsections%2Fdatastandards%2Fassets%2FOVD31interfacedescription.xlsx&wdOrigin=BROWSELINK)

[<img src="assets/OVD-Guide-button.png" align="left" alt="assets/OVD-Guide-button" height="50">](https://ovdguide.veracityapp.com)

[<img src="assets/CSV-File-Converter-button.png" align="left" alt="assets/CSV-File-Converter-button" height="50">](https://veracitycdnprod.blob.core.windows.net/digisales/myservices/cdn/content/marketplace/docs/OVD%20CSV%20file%20converter%20v1.81.xlsm)

[<img src="assets/Sample-Files-button.png" alt="assets/Sample-Files-button" height="50">](https://veracitycdnprod.blob.core.windows.net/digisales/myservices/cdn/content/marketplace/docs/OVD%20sample%20files.zip)


Operational Vessel Data (OVD) is a standard for log abstracts and other operational data from vessels, and a data service on DNV’s Veracity Data Platform. 

The OVD data service on Veracity is continuously assuring data from thousands of vessels. By submitting data to Veracity OVD, your data is structured, analyzed, enriched and quality assured before you have the option to use it in one of the many services running on Veracity, like MRV and DCS/CII verification, Emissions Connect, or to share quality assured data via the Veracity Data Workbench with stakeholders or other parties or solutions that will utilize your data, like Poseidon Principles or Sea Cargo Charter. 

A full and comprehensive description of the OVD standard can be found in the [OVD Interface Description](https://veracitycdnprod.blob.core.windows.net/digisales/myservices/cdn/content/marketplace/docs/OVD%203.1%20interface%20description.xlsx). To further learn, play with and test your OVD data, the [OVD Guide](https://ovdguide.veracityapp.com) has interactive guidance to the most important elements of OVD and allow you to test upload files. 

OVD consists of several schemas. A schema is a definition of how to fill in the operational vessel data, with defined columns and clear rules for what to put into each of the columns/rows. The two most used schemas in OVD are Log Abstract (LA), listing all key events from the vessels’ operations, and the Bunker Reports (BR), listing all bunkers in the relevant period. Both the Log Abstract and the Bunker Reports are required for DNV’s verification services, like MRV and DCS/CII verification. 

Below is an example of how the OVD Log Abstract would look for a vessel sailing from Hamburg to Rotterdam: 

<figure>
    <img src="assets/data-table.png"/>
</figure>

Have a look at the [Sample Files](https://veracitycdnprod.blob.core.windows.net/digisales/myservices/cdn/content/marketplace/docs/OVD%20sample%20files.zip) to find more examples. 

Data can be submitted to DNV’s Veracity OVD via continuous and automated transfer using modern REST API interfaces, or via manual upload of CSV files. Please contact [Veracity Support](mailto:support@veracity.com) if you want to know more about how to establish automated transfer of OVD data. 

The [CSV File Converter](https://veracitycdnprod.blob.core.windows.net/digisales/myservices/cdn/content/marketplace/docs/OVD%20CSV%20file%20converter%20v1.81.xlsm) is an easy-to-use tool to get your data into OVD format. This is intended only for smaller cases where IT capabilities are not available to automate the output of data in OVD format. 
