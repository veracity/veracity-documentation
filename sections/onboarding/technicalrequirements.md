# Onboarding your service to Veracity - technical requirements
## Here you will find a summary of the technical requirements for onboarding your service to Veracity. You will find links below to further documentation which will help you to implement the changes required.
*Changelog:*
*2021-09-12: Changed in requirement 8. Policy API section to point to more detailed online documentation. Changed wording in requirement 3. Database Sync session to better explain why it is a requirement.*
*2021-05-25: Changed wording in intro to be more precise about use of OAuth 2.0. Changed wording in section 6 to reflect name change from DTC Analytics Solution to Veracity Assurance Applications. Changed link in section 1 to point to updated documentation. Changed some references from DNV GL to DNV.*
*2021-03-18: Fixed broken link under section 8 "Policy API".*
*2020-01-31: Changed "client credentials" to "application credentials" for accuracy.*
*2020-01-09: Added a section in the beginning to explain the expected process during technical onboarding. Changed the link to the API portal in section 3 so it does not point to an unavailable API endpoint.*
*2019-10-08: Changed the wording about testing on external computers to include non-DNV GL services. Changed wording in section 6 to include non-DNV GL services.*
*2019-10-02: Amended point 4 to better explain what we mean by "authorization". Added reference to the Developer website above point 1.*
*2019-09-30: Added section about browser support in point 10. Edited point 3 to make it clearer what we mean and removed one of the unnecessary links.*
**The following technical points only apply if you intend to integrate your application to Veracity. It does not apply if you only want a lead-generating site on Veracity.**
**<u>Always test your application on both internal company computers (VERIT for DNV) and non-company computers on both internal company networks and external networks.</u>**
The Veracity platform runs on Microsoft Azure and uses Azure AD B2C for identity (OpenID Connect OAuth 2.0). Technical integration is easier if your application is a web app written in a common language and is hosted on Azure, AWS or another large cloud platform. However if your application is written in an unusual language or is a desktop application, it will make the technical integration more difﬁcult and consequently more time consuming.
### The general process of technical onboarding:
Here is what you can expect to happen during the technical onboarding phase.
It will be normal to have a few meetings with the onboarding manager and technical personnell during the technical onboarding.
1. You set up a non-production Veracity service yourself and start working on it to comply with the technical requirements stated on this page. You will receive a set of application credentials for a "test" or "staging" Veracity application (depending on what you choose).
2. If you encounter challenges or have questions about the requirements you may contact the Veracity onboarding manager (onboarding@veracity.com). Please note that it might take a few days before you receive a reply if we have our hands full.
3. Reach out to the onboarding manager once you are confident your application complies with the technical requirements.
4. The onboarding manager will review your application to ensure that it is compliant.
5. A new set of client credentials will be issued for a production-version of your application.
6. You configure your own production-application with the new set of application credentials.
7. A second review is done to ensure nothing broke when the application credentials were changed.
Once all these steps are successful the technical onboarding is considered complete.
Please note that technical part and commercial part of onboarding usually happens at the same time.
If you would like a Veracity Marketplace presence, please look at the information available at https://developer.veracity.com/services/marketplace
**Setting up a Veracity service happens at https://developer.veracity.com/**
After you have created an application here you will be provided with a set of client credentials which you may use to call the Veracity service API's described below.
### The requirements
#### 1. Log in
There is mandatory integration with our identity provider, enabling the Single Sign On (SSO) experience. If the user has already logged into his/her Veracity account it should not be necessary to login a second time when opening your application from Veracity. For more information see documentation.
#### 2. Logout button
A log out button is required to be implemented and be clearly visible inside the app. This should clear relevant cookies and return the user to the Veracity logout endpoint. A logout option shall be available in all Digital Services on Veracity. The logout shall ensure the logout from the Digital Service, and then send the user to the identity provider logout process. If applicable, delete all local session info - including session cookies. Redirect to the following endpoint that will ensure logout both from ADFS and Azure AD B2C: https://www.veracity.com/auth/logout
#### 3. Database synchronization & subscription management by calling API's
We cannot have a situation where a service is storing information about a Veracity user, but Veracity does not know about it. A user can request to have their user permanently deleted by Veracity - in those cases we must delete all data about the user, including the data stored in your app database. If a user has a subscription to your service, then Veracity knows that we should reach out to your app owner and request deletion of the user's data.
If you add a Veracity user in your own database then the user should also have a subscription created for them on the Veracity side. Subscriber synchronization of users through the service API is mandatory. When a service has their own database of users we need to sync this with Veracity's own database of users. If you delete a user in your own database or deactivate a user in your own database, something similar should happen on the Veracity side.
As a service owner you cannot delete a user on the Veracity side, but you can delete a user's subscription to your service. Ideally you create an administrator control panel inside your application so that non-technical admins can add and remove subscribers by clicking buttons, which in turns makes API calls to Veracity.
In the link below you will find the list of available API's. Please note that only the "My" and "This" viewpoints are available to you. The viewpoints "Directory" and "Options" are not available. Only API calls in the "My" viewpoint can be called directly in the browser. All other calls should be performed with Postman or similar when your are testing.
https://api-portal.veracity.com/docs/services/veracity-myservices%20V3/operations/My_Info?&groupBy=tag
#### 4. Authentication & authorization
Veracity can perform authentication, but not authorization. In other words: Veracity can tell you who a user is and other information about the user (authentication), but Veracity does not directly control which users gain access to your application (authorization).
As a service owner we wish you to have full control over authorization for a paid application - Veracity should not be able to grant users access to your application without the service owner's permission. You should therefore not rely on a Veracity subscription as the only authorization method for paid applications. Veracity will alert the service owner of new purchases made, but Veracity will not take steps to authorize the user so they gain access to the application - this should be done by the service owner.
For free applications the situation is different because you might not want any authorization method at all. We discuss the authorization method for free applications on a case-by-case basis during the onboarding process.
Veracity provides the following information by claim: unique identiﬁer (Veracity ID), email, ﬁrst name, last name, displayName. Other information must be handled through Veracity API.
#### 5. User ID
Do not use email addresses as unique identiﬁers for users inside your application, please instead use the unique Veracity ID which is associated with Veracity user accounts. The reason is that Veracity users can change their email addresses on their accounts. Please refrain from storing the other information from the claim whenever possible, we recommend not storing it and instead reading this information from the bearer token issued after login. This way you always have the up to date proﬁle information and avoid user info sync issues.
#### 6. Hosting
Veracity generally does not offer hosting of solutions. E.g Virtual Machines, webservers etc.
Veracity recommends hosting the application at a reputable hosting provider (Azure, AWS etc) or using your own infrastructure to host the application.
For DNV services: If you have hosting needs, please contact GSS IT or Veracity Assurance Applications.
#### 7. User groups
The service provider must control user groups inside the application. I.e. if there are several subscription options you must have the option to assign users to different groups with different access layers. Veracity can assign a subscription to each user which the application can detect through the service API, but the administration of user access must happen inside the application itself.
#### 8. Policy API
Implementation of the policy API is mandatory. The policy API checks if a given user has accepted the newest terms & conditions and it also checks if a user has a subscription for the given service on Veracity.
Read more about how the Policy API functions here:
https://developer.veracity.com/docs/section/identity/policy-service
#### 9. GDPR
We must know where we keep customer data. You might be asked to terminate users stored on your side of the application if they send a GDPR termination request to Veracity, however this is still a manual process and relies on the subscriber databases being synced and correct. Please be vigilant and keep the subscriber databases synced so that we are GDPR compliant. This is a re-iteration of point 3, but with a focus on GDPR.
#### 10. HTTPS & browser support
Lastly, HTTPS is required.
Your app should support the following browsers:
1. Chrome
2. Firefox
3. Edge
4. IE11 (please pay extra attention to caching in IE11)^.
We fully understand that IE11 is not fun to work with. If you do not wish to support a browser you can instead opt to display a warning message to the user informing them that you do not support a browser.
**See also our Veracity GitHub: https://github.com/veracity**
