---
author: Benedikte Kallåk
description: Description of quick start section
---

# Health Message
A health message is related to an equipment. Health status is provided as: 
- ok: All healthy
- notok: Need attention


```json
{
  {
    
    "timeStampUTC": "2021-09-29T10:15:00.269Z",
    "healthStatus": "string",
    "expiryDate": "2021-09-29T10:15:00.269Z",
    "equipmentId": [
      {
        "dataChannelId": "string",
        "namingRule": "string"       
      }
    ]
  }
}

```
* healtStatus: ok, notok
* expiryDate: Optional, equipment such as charts have expiry date
* equipmentId:
	* dataChannelId: The identifier /code used by the codebook used for asset categorization ( Vis code, mc key, JSME id etc.)
	* namingRule: name of codebook: Vis, JSME
* timeStampUtc: timestamp for event, UTC: format: "2021-04-06T14:22:48.950716+02:00"


