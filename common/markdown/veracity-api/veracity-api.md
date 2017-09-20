# Overview
This Veracity API's enable data providers and consumers to interact with veracity programatically.  

# API Reference
- Some reference....


# Tutorial
Veracity uses API Management. In order to get access, you will need to do the following two steps:
- You need to register at [https://api-portal.dnvgl.com/](https://api-portal.dnvgl.com/)
- Subscribe to the Veracity Platform API – Product, this will give you access to our DataAPI and ProvisionAPI with a subscription ID

NB! The endpoint URLs might be changed/refactored during private preview period to further enhance the developer experience. We will try to inform users of the API before such changes take place.


### Standard structure of API Call

#### Call header:
- **Ocp-Apim-Subscription-Key** - this header attribute is for authentication to API Management
- **Authorization** this header attribute needs to contain the Bearer Token gotten through atuhorization on Veracity

#### Query parameters:
Depeding on end-point

#### Authorization snippet (for developer)
You need to authorize to Veracity with code and copy the Bearer Token to your requests (we will provide later). Swagger UI can be used for now. Bearer token is usually valid for one hour, after that you need to request a new.

Best practice to always get a new token before a request. 

'''curl
curl -v -X GET "https://api.dnvgl.com/platform/Mydata/api/resources?shared={boolean}&owned={boolean}"
-H "Ocp-Apim-Subscription-Key: {subscription key}"
-H "Authorization: Bearer {token}"
'''

## Data API
The Veracity Data Platform DataAPI is an API where developers and applications can get information on data containers, get their key to a data container or share a key with another Veracity Data Platform user.



## Provision API

## Meta Data API


# Pattern & Practices 
In this section we will give theoretical and practical recommendations on how to best develop, design and implement your service 
 
# References 

## GitHub  
Follow our open projects related to veracity API on https://github.com/veracity

## Stack Overflow
Stack Overflow is the largest, most trusted online community for developers to learn, share​ ​their programming ​knowledge. The Veracity developer team monitor Stack Overflow forumposts that include the tag Veracity
 
[Visit Stack Oerflow](https://stackoverflow.com/questions/tagged/veracity?mode=all)


 
### Video 
Some text

 
# Resources  
In this section we have added resources that may provide you with additional learning.  


 
# FAQ 
Some text 
 
# Price model 
Some text
 
