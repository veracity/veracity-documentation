---
author: Veracity
description: This is the changelog for the March 2026 second release of Data Workbench.
---

# March 2026 release: Egest DB
To improve stability and performance, OVD is reducing the amount of data quality results synchronized to the Egest DB via Data Workbench.

This change will be included in Data Warehouse release 3.38, scheduled for 11 March 2026.

## Cutoff Rules Applied
| Data Schema | Schema Code | Cutoff Date |
|-------------|-------------|-------------|
| Compliance Data Quality MRV-EU | OVDQ-MEU | Year ≥ 2025 |
| Compliance Data Quality MRV-UK | OVDQ-MUK | Year ≥ 2025 |
| Compliance Data Quality DCS | OVDQ-DCS | Year ≥ 2025 |
| Compliance Data Quality FuelEU | OVDQ-FEUM | Year ≥ 2025 |
| Emissions Connect Data Quality | OVDQ-VLV | Year ≥ 2023 |

* Data before these cutoff dates will not be available via DWB.
* VEC does not calculate historic data quality for the year 2024 and earlier.
* **If you want to keep those data, please download it before 11 March 2026.**

## Expected Impact
* Reduced volume of unnecessary historic data synchronized to Egest DB.
* Improved system stability and performance.
* More focused data views for end users.
