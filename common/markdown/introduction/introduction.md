---
Title : "Introduction"
Author: "Brede Børhaug"
---

## Welcome to Veracity for Developers


Veracity is designed to help companies unlock, qualify, combine and prepare data for analytics and benchmarking. We are not looking to own data, but to help our customers leverage the ever-increasing amount of data they own. 
On the platform’s marketplace, asset owners will get access to industrial applications and data analytics services that can help them make better use of their data to optimize performance. These apps will be provided not only be DNV GL, but by a host of other qualified providers of data, data analytics and digital solutions. Veracity for Developers is design to support both the IT Pro’s and developers at the data provider side, and the developer, data analysts and IT Pro’s at the data consumer side.

### Where do I start?
With all the new opportunities Veracity enables for both the asset owners and the service providers, it can be a daunting task to figure out which services you need to support in your solution architecture. This section highlights the Veracity services that developers commonly use, and where to start.

#### Veracity high-level architecture
The Veracity infrastructure is based on Microsoft Azure, and supplemented by key partners in the industry, enabling Big Data capability on a global scale. Veracity consist of some key components. 

##### Marketplace
The Marketplace within Veracity is an Oracle based E-Commerce solution which allows external customers to browse, enquire and purchase digital services that are offered by both DNVGL and external providers. Veracity is an open neutral platform, and for that reason we will allow services to be offered by both internal and external providers. There is no need for a direct affiliation with DNVGL , however there is an integration process which will have mandatory requirements to ensure quality of product and service provided. To get going with this process reach out to Veracity team, and we will help you get started. Also check out the [Onboarding a Service](https://developer.veracity.com/doc/onboarding-a-service) documentation for more technical details.

##### My services
My services 



##### Veracity service API's
[TO BE UPDATED]


##### Veracity Data Fabric - private preview
The data sharing and data analytics part of Veracity lets you analyze, share and combine data in a trusted eco-system. The data fabric is in private preview, and will be in public preview in the near future. 


###### Veracity data fabric security

The Veracity System Key is never shared with ether the Veracity storage owner or other customers. Vercity do not store your Veracity storage system key or SAS Token hash-code in any database or storage – its all in Azure Key Vault. Azure Key Vault traffic is encrypted and the secrets and keys are encrypted in Azure Key Vault at rest. For additional details on keys, you may consult the [data fabric keys](https://developer.veracity.com/doc/data-fabric-keys) documentation.

Our ledger keeps the history of all operations done on a storage container by all users with access to the container. It also keeps track of sharing and claiming keys in the system. 

The shared access signature (SAS) URI that is shared with you is your private key – users should treat it as a key to their home. All usage of SAS URIs is on the users responsibility. Veracity will never email the SAS URI to any user. Veracity will only email notification that a key is awailble to you, and a link to where you can retrieve the key.




