---
author: Veracity
description: Setting up Single Sign-On with Veracity.
---

# Single Sign-On with Veracity

You can sign in to Veracity with your company account using the Single Sign-On (SSO) solution. The benefits are:
* Convenient sign-in - use your company account credentials.
* Easy access management - if an employee leaves the company, terminate their company account to revoke their access to Veracity resources.

The SSO setup is free of charge and available for all resources integrated with Veracity. If you want to see the sign-in flow for the user once SSO is configured, go [here](#sso-user-experience).

## Provisioning users
You do not need to provision users. When a user enabled for SSO signs in to Veracity, they automatically get a Veracity account.
However, Veracity plans to enable provisioning users in advance so that customers can upload their users and manage their permissions. This would be implemented through an API endpoint supporting the SCIM protocol. For details, contact [support@veracity.com](mailto:support@veracity.com).

## How to set up SSO?
Veracity's SSO supports the following protocols:
* Open ID Connect 1.0
* SAML 2.0

The setup depends on who is your company's identity provider:
* If your company's identity provider is Azure Active Directory (Azure AD), go [here](#sso-with-azure-ad).
* If you have another identity provider, go [here](#identity-providers-other-than-azure-ad).

The setup applies to all users with email addresses matching the email domain that has been configured for SSO.
    
## SSO with Azure AD
Veracity implements SSO by using the Open ID Connect 1.0 protocol. Everything is pre-configured by installing the Veracity Single Sign-On app from Azure AD App Gallery. This application controls the trust relationship between Veracity and your Azure AD. 
Note that:
* To implement SSO, you need to be an Application administrator or Global administrator in your company's Azure AD.
* You will need to allow the app to sign in users and read the profile data for the signed-in users.
* User's profile data is handled according to the [Veracity Terms of use](https://id.veracity.com/terms-of-use) and [Privacy statement](https://services.veracity.com/PrivacyStatement).

If you want to stop using SSO for Veracity, delete the Veracity Single Sign-On app in your Azure AD.

### Implementation
To implement SSO with Azure AD, follow the steps below.
1. Sign in to the Azure Portal with an account that is an Application administrator or Global administrator in your company's Azure AD.
2. Go to **Azure Active Directory** > **Enterprise applications** and select **New application**.
3. Find the **Veracity Single Sign-On** app and select **Sign up for Veracity Single Sign-On**.
4. Ensure that the app requests permissions for **all users in your organization**, and select **Accept**. The app will be installed in your Azure AD in the **Enterprise applications** blade. The name of the app is **Veracity Single Sign-On**. 
5. You will be redirected to another page and asked to:
    - Provide the email domain(s) for which you want to set up SSO. Note that these domains must match the **mail** attribute of your users' accounts in Azure AD.
    - Prove that you own the domain by registering a TXT record in your DNS.
    - Enter your company name, technical contact and support contact email addresses.
    - Once the DNS records are verified, Veracity will analyze your existing user base in Veracity. If there are issues, the process will stop, and you will receive a request for manual cleanup.
    - If there are no issues, you will be able to proceed with the SSO setup.  After selecting the **Submit** button, the whole process usually takes five to ten minutes.


## Identity Providers other than Azure AD

If you use an identity provider other than Azure AD, send a request for implementing SSO to [support@veracity.com](mailto:support@veracity.com).  Provide the following information:

* The name of the email domain for which you need SSO. For example, @dnv.com.
* The name of your identity provider. For example, Ping Identity or ADFS.
* The protocol you want to use. Choose OpenID Connect 1.0 or SAML 2.0.
* The Metadata URL for your identity provider.
* The claims that will be sent to Veracity as tokens containing:
    - First name
    - Last name
    - Email
    - Unique identifier within the federated domain
* Optionally, a name of the claim indicating that the multi-factor authentication was done within the customer company.

## Verify the implementation
When you have implemented SSO, verify if it works properly by following the steps below. Avoid using the administrator account, and choose a regular user account instead.

1. Restart your browser.
2. Go to the [Veracity home page](https://www.veracity.com).
3. In the upper right corner, select the **Sign in** button.
4. Enter an email address for a regular user account and select **Continue**.
5. You should be redirected to your identity provider. Authenticate there.
6. If this is the first time you sign in to Veracity, you will be asked to specify your country and accept the terms of use.
7. You should be redirected to the [Veracity home page](https://www.veracity.com). 
8. To verify you are signed in, in the upper-right corner of the page, find your initials or profile picture.
<figure>
    <img src="assets/Enrollment1.png"/>
</figure>

## SSO user experience
To see the SSO sign-in flow for a user, consult the diagram below.
<figure>
	<img src="assets/SSOUserExperience.png"/>
</figure>

## Support
If you need support, contact [support@veracity.com](mailto:support@veracity.com).
