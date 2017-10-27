---
Title : "Introduction"
Author: "Brede Børhaug"
Contributors: "Rachel Hassall"
---

## Welcome to Veracity for Developers


Veracity is designed to help companies unlock, qualify, combine and prepare data for analytics and benchmarking. We want to help our customers leverage the ever-increasing amount of data they own. 
On the platform’s marketplace, asset owners will get access to industrial applications and data analytics services that can help them make better use of their data to optimize their performance. These apps will be provided not only by DNV GL, but by many other qualified providers of data, data analytics and digital solutions as well. Veracity for Developers is designed to support both the IT pros and developers at the data provider side, and the developer, data analysts and IT Ppros at the data consumer side.

### Where do I start?
With all the new opportunities Veracity enables for both asset owners and service providers, it can be a daunting task to figure out which services you need to support in your solution architecture. This section highlights the Veracity services that developers commonly use, and where to start.

#### Veracity high-level architecture
The Veracity infrastructure is based on Microsoft Azure, and supplemented by key partners in the industry, enabling Big Data capability on a global scale. Veracity consists of some key components. 

##### Marketplace
The Marketplace within Veracity is an Oracle based E-Commerce solution which allows external customers to browse, enquire and purchase digital services that are offered by both DNV GL and external providers. Veracity is an open neutral platform, and for that reason we will allow services to be offered by both internal and external providers. There is no need for a direct affiliation with DNV GL , however there is an integration process which has mandatory requirements to ensure the quality of product and service provided. To get going with this process, please reach out to Veracity team and we will help you get started. Also check out the [Onboarding a Service](https://developer.veracity.com/doc/onboarding-a-service) documentation for more technical detail.

##### My services
My services 



##### Service API's
[TO BE UPDATED]


##### Data fabric - private preview
The data sharing and data analytics part of Veracity lets you analyze, share and combine data in a trusted eco-system. The data fabric is in private preview, and will be in public preview in the near future. 


###### Data fabric security

The Veracity System Key is never shared with the Veracity storage owner or other customers. Vercity does not store your Veracity storage system key or SAS Token hash-code in any database or storage – it's all in a Azure Key Vault. Azure Key Vault traffic is encrypted, the secrets and keys are encrypted in Azure Key Vault at rest. For additional details on keys, you may consult the [data fabric keys](https://developer.veracity.com/doc/data-fabric-keys) documentation.

Our ledger keeps a history of all operations done on a storage container by all users with access to the container. It also keeps track of sharing and claiming keys in the system. 

The shared access signature (SAS) URI that is shared with you is your private key – users should treat it as a key to their home. All usage of SAS URIs is the user's responsibility. Veracity will never email the SAS URI to any user. Veracity will only email notification that a key is available to you, and a link to where you can retrieve the key.
