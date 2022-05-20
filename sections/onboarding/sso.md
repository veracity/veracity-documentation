# Setting up Single Sign-On with Veracity

## General information
Veracity offers a Single Sign-On (SSO) solution where customers can log in to Veracity with their company accounts making the logon process very smooth.


The setup applies to all users with email address matching the email domain that has been configured for SSO.

The SSO setup is between the Veracity platform and the customer company, thus applies to all Veracity-integrated services.

The following protocols are supported:
- Open ID Connect 1.0
- SAML 2.0

Setup of SSO is free of charge. It will give access to log in with the customer's company accounts to the Veracity platform and  users will have access to the free services on the Veracity platform. If users want to use some of the paid services, they can buy a license for those in the [Veracity Marketplace](https://store.veracity.com).


## SSO user experience
The below figure shows the login flow for a user where SSO is set up:
![](./SSOUserExperience.png)



## Provisioning of users
When users enabled for SSO log in, they will automatically get a profile in Veracity, there is no need to provision users in advance. We plan to support user provisioning later so that customers will be able to upload users in advance and manage their permissions. This will be implemented through an API endpoint that will support the SCIM protocol.

## How to information
**../customerservices/sso.md**
