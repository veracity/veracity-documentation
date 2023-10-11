---
author: Mariusz Klimek (DNV)
description: Introduction to the Client Credentials flow
---

Client credentials refer to a set of credentials that a client (usually a software application or service) uses to authenticate itself to a server or an identity provider in a networked system.

## How Client Credentials Flow usually works:

1. **Client Application**: The client can be a web application, mobile app, or any software component that needs to access resources or perform actions on a remote server or service.

2. **Server or Identity Provider**: The server can be a web server, API server, or identity provider like OAuth 2.0 Authorization Server. This server hosts the resources or services the client wants to access.

3. **Client Credentials**: These are typically a pair of secrets:

4. **Client ID**: A public identifier for the client application. This is often included in requests to the server.

5. **Client Secret**: A confidential, secret key known only to the client application and the authorization server or identity provider. It is used to authenticate the client and establish trust.

6. **Authentication**: The client sends a request to the server along with its client credentials (ID and secret). The server validates these credentials.

7. **Authorization**: If the credentials are valid, the server grants the client access to the requested resources or services. The server may issue access tokens or other credentials that the client can use to make authorized requests to protected resources.

## Common uses of Client Credentials Flows

Client credentials are commonly used in scenarios like:

- **API Authentication**: Client applications use client credentials to access APIs securely. OAuth 2.0 provides a framework for such authentication.

- **Service-to-Service Communication**: In microservices architectures, one service may need to authenticate itself to another service.

- **Machine-to-Machine (M2M) Communication**: Devices or software components may use client credentials to securely communicate with servers.

### Remember!
Protect your client credentials. They act as the keys to access resources or perform actions on the server. 

Leakage or misuse of these credentials can compromise the security of the system. 

Therefore, they should be stored securely, and best practices like using OAuth 2.0 or other secure authentication protocols should be followed when implementing client credential-based authentication.

## Content

1. What is Client Credentials and when should you use it **<- You are here**
2. [Creating an API in Veracity](2-api-creation-in-veracity.md)
3. [Creating a client application in Veracity](3-client-creation-in-veracity.md)
4. [Acquiring an Access Token using MSAL](4-msal-access-token.md)
5. [Validating a Client Credentials token](5-validating-cc-token.md)

Now, lets start building with configuring your API in Veracity.

---

[Next - 2. Creating an API in Veracity](2-api-creation-in-veracity.md)