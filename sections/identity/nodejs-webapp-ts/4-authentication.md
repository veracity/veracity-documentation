---
author: Veracity
description: Describes how to perform authentication with the Veracity IDP.
---

# 4. Authentication
[Previous - 3. Express webserver](3-express-webserver.md)

In the previous section we set up our webserver to handle https requests and even managed to return some text from it. In this section we will expand it to allow users to log in via Veracity and return to our application when done. We will also set up our code to negotiate for access tokens so that we can call other APIs on behalf of the currently logged in user.

Veracity uses a process called **OpenID Connect** to authenticate users and **OAuth 2 Authorization code flow** to retrieve access tokens for resources. There is also a library provided for Node applications that handle all the details for us using a PassportJS strategy. We will use this library to avoid having to deal with the intricacies of these processes, but it is recommended that you at least have a basic understanding of the underlying details. With that said, let's take a peek at the library we'll be using. You can find up-to-date documentation on the library GitHub page at [https://github.com/veracity/node-auth](https://github.com/veracity/node-auth).

<figure>
	<img src="assets/veracity-node-auth-readme.png"/>
	<figcaption>The readme file for the Veracity Node Auth library provides all the details needed to use it.</figcaption>
</figure>

There are one primary way to use the library:

We can use a helper function called `setupWebAppAuth` that handles all the application configuration for us. This is the easiest way to get started, but it does take away some control from you regarding the actual setup process.

This approach only requires us the ensure we have the necessary configuration parameters ready to drop in. Looking at the example from the library GitHub page, we end up with a relatively simple code snippet for setting up authentication:

```typescript
setupWebAppAuth({
	app,
	strategy: { // Fill these in with values from your Application Credential
		clientId: "",
		clientSecret: "",
		replyUrl: "https://localhost:3000/user"
	},
	session: {
		secret: "12345678", // Replace this with your own secret
		store: new MemoryStore() // Use MemoryStore only for local development
	}
})
```

Provided we fill in our application details this is sufficient to get users authenticated and negotiating the access token needed to talk to the Services API on Veracity. Behind the scenes this helper function will set up passport, session and even register the necessary endpoints on our application.

We already have the necessary dependencies installed in our project and our `start.ts` file sets up the basic server nicely for us. Now we need to configure authentication. Let's create a file called `setupAuth.ts` where we can do all the necessary steps.

First we create the setup function that will take the necessary arguments and configure the rest. We also import the dependencies we will need here. Notice the errors on some of the types. We should also install type definitions for these. Like before run this in a terminal:

```
npm i -D @types/passport @types/express-session
```

```typescript
import {
	setupWebAppAuth
} from "@veracity/node-auth"
import { Router } from "express"
import { MemoryStore } from "express-session"


export const setupAuth = (app: Router) => {
	const { refreshTokenMiddleware } = setupWebAppAuth({
		app,
		strategy: { // Fill these in with values from your Application Credential
			clientId: "",
			clientSecret: "",
			replyUrl: "https://localhost:3000/user"
		},
		session: {
			secret: "1234567", // Replace this with your own secret
			store: new MemoryStore() // Use MemoryStore only for local development
		}
	})

	app.get("/refresh", refreshTokenMiddleware(), (req: any, res: any) => {
		console.log("Refreshed token")
		res.send({
			updated: Date.now(),
			user: req.user
		})
	})
	
}
```


With OpenID Connect you are required to specify certain identifying parameters for your application. For Veracity they are: `clientId`, `clientSecret` and `replyUrl` (sometimes called redirect url). If you haven't already done so now would be an excellent time to head over to [Veracity for Developers](https://developer.veracity.com) and register your application. You will need to create an **Application Credential** resource in the portal there and take note of the parameters it returns. Once done you should fill inn these parameters in the settings object passed to `setupWebAppAuth`.

```typescript
import express from "express"
import { createServer } from "./server"
import { setupAuth } from "./setupAuth"

const app = express()

setupAuth(app)

app.get("/", (req, res) => {
	res.send("OK")
})
app.get("/user", (req, res) => {
	if (!req.isAuthenticated()) {
		res.status(401).send("Unauthorized")
		return
	}
	res.send(req.user)
})

createServer(app, 3000)
```
Let's add an endpoint that will dump our user information if the user is authenticated so we can see what's been stored.

You should now be able to authenticate with Veracity using your application. Let's test it out by running our start file in debug mode. Open your browser to [https://localhost:3000/login?returnTo=/user](https://localhost:3000/login?returnTo=/user). You should be prompted for your credentials and then after some round trips returned back to `/user` in your application. Neat! If you are not redirected to `/user` then you can manually go there.

<video controls loop>
	<source src="assets/authentication-working.mp4">
</video>

That's it for authentication. Next up, calling apis in order to get additional user information.

[Previous - 3. Express webserver](3-express-webserver.md) --- [Next - 5. Calling APIs](5-calling-apis.md)
