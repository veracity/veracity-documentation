---
author: Veracity
description: Description of access to API
---

# Accessing APIs

For all request you need to provide **authorization** header with OAuth2 bearer token and **Ocp-Apim-Subscription-Key**  header with your subscription key  
  

More info about getting bearer token can be found [here](https://developer.veracity.com/doc/identity).  
Subscription key can be found from your [profile](https://api-portal.veracity.com/developer).  

Example request:
```
GET https://api.veracity.com/veracity/datafabric/data/api/1/users/me HTTP/1.1
Host: api.veracity.com
Content-Type: application/json
Ocp-Apim-Subscription-Key: {subscription-Key}
Authorization: Bearer {token} 
```