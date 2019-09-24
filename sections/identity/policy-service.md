# Veracity Policy Service
The Policy Service is a small API that allows third-party applications to verify that the user has approved both the generic Veracity Terms of Service as well as any other such policies specific to your service. It is not directly associated with the Veracity Identity Provider (IDP), but they are usually used together during the authentication process.

The Policy Service consists of two API endpoints in the Services API that check whether the current user has approved the latest version of any Policy. If any are outstanding it will return a URL the user must be redirected to in order to approve the policy. Once the user approves they will be returned back to your application. Because of this required user interaction only web and native applications should use the policy API.

To call the Policy API you will need an access token for the Services API as well as a reply url that users can be redirected back to once they approve the policy. This means that the user must be authenticated first, then your application should check the policy endpoint for any outstanding policies. If the user returns without approving an outstanding policy they should not be allowed to authenticate.

## Requests

To validate general Veracity policies call this URL:
```url
https://api.veracity.com/veracity/services/v3/my/policies/validate()
```
This should be called by all services built on Veracity to validate that the user has approved the relevant terms of service. These terms may be updated which will invalidate the users previous approval and the API must therefore be consulted on every login.

To validate policies specific to a service call this URL:
```url
https://api.veracity.com/veracity/services/v3/my/policies/{serviceId}/validate()
```
The service ID is the id you have been provided for your service. If you do not use custom policies for your service you do not need to call this endpoint.

## Responses
The Policy Service has two normal responses in addition to generic errors. If the response status code is `204` (no content) that means the user has no outstanding policies that require approval. If the response code is `406` (not acceptible) that means the user **has** some outstanding policies that require approval. Inspect the body of the response for details.