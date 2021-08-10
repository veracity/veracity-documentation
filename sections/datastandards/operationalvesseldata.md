---
author: Veracity
description: Description of Operational Vessel Data Standards in Veracity
---

# Operational Vessel Data (OVD)

The Operational Vessel Data (OVD) interface standard for exchanging data between software solutions is a comprehensive and easy to adapt format for operational vessel data, like Noon and Arrival reports.

The standard supports data sharing in the Fleet Performance Management context but is also applicable for MRV/DCS data provision to the Verifier and other services.

Event reports like Noon, BOSP, Departure are catered by the standard as well as instantaneous information like engine performance reports. The most commonly used data fields reported in typical event reports are covered. For instance, consumptions and distances, weather, propulsion and auxiliary work, ETA, Ordered Speed, bunker intake, etc., to name a few.

The OVD interface file is a CSV file and its simple structure makes it easy to process the data on both, the import and export side of the data flow. Furthermore, being based on a CSV file the OVD standard is bridging automated and manual input in a nice way.

On Veractiy APIs exist for import and export of OVD files. The import API can validate the data on record level and supports logging and archiving. Updating and deletion of records are supported by the Veracity API too. The OVD standard is actively developed by DNV and StormGeo and has a history since 2014. You can download the latest OVD interface description here.

<a href="assets/odv-flatfile-interface-description.xlsx" download>Download Operational Vessel Data - Flatfile Interface Description</a>
