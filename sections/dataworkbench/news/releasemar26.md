---
author: Veracity
description: This is the changelog for the February 2026 third release of Data Workbench.
---

# February 2026 third release: Egest API
To improve system performance and reduce unnecessary data processing, access to historical data within the Egest API has been restricted. 
Data before the defined cutoff years is no longer returned.

## Cutoff Rules Applied
* Compliance Data Quality MRV EU (OVDQ MEU): Year ≥ 2025
* Compliance Data Quality MRV UK (OVDQ MUK): Year ≥ 2025
* Compliance Data Quality DCS (OVDQ DCS): Year ≥ 2025
* Compliance Data Quality FuelEU (OVDQ FEUM): Year ≥ 2025
* Emissions Connect Data Quality (OVDQ VLV): Year ≥ 2023

* Data before these cutoff years will be returned as empty periods.
* **If you want to keep those data, please download it before 11 March 2026.**

## Expected Impact
* Reduced volume of unnecessary historic data.
* Improved system response times and performance.
* More focused views for end users.
