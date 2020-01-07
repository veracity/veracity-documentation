---
author: Veracity
description: Describes how to set up a basic ExpressJS web server in the NodeJS Webapp tutorial.
---

# 3. Express webserver
[Previous - 2. Development environment](2-development-environment.md)

Previously we set up our development environment and installed all the necessary dependencies needed to build our application. Now we can start writing the actual code :)

To separate our source from other scripts that we may need to add (such as build scripts) we'll create a new folder called `src`. Here is where all our application code will be placed.

We'll start with the setup of our core server. In order to be able to authenticate with Veracity our server has to serve our site over HTTPS. This is a requirement of the platform as it is transferring secure information to the users browser and this should always be done over a secure connection.

Create a file in the `src` folder called `server.ts`. This file will be responsible for configuring your https server. Add the following:
```typescript
import https from "https";

export const createServer = () => {

};

export default createServer;
```

Notice that VSCode will complain about a few things before you save the file:

<figure>
	<img src="assets/server-initial-file.png"/>
	<figcaption>VSCode will yell at us for several things in this file.</figcaption>
</figure>

Let's have a closer look at these errors:

- **Line 1** - This is a TypeScript issue. Although the `https` module is a core part of node and can be imported, TypeScript does not know of the typing information for this module and therefore complains that it cannot find it. To fix this we must install the types for node. In the terminal run `npm i -D @types/node` Once installed you should see this error disappear. We'll need to install types for multiple other libraries later.
- **Line 3-5** - This is the linter notifying us that we have an empty block of code. For us this is not a problem since we will be implementing it momentarily, but it's useful to highlight these in general as it prevents us from saving and committing useless code.
- **Line 7** - This is also the linter complaining that our file does not end with a newline. Read more about the rule here: [https://eslint.org/docs/rules/eol-last](https://eslint.org/docs/rules/eol-last)

The only issue that actually blocks us from writing our code is the one on line 1. Apply the fix described and the error will go away. Let's now implement the createServer function:
```typescript
import { generateCertificate } from "@veracity/node-auth/helpers"
import { RequestListener } from "http"
import https from "https"

export const createServer = (
	requestListener: RequestListener,
	portOrPipe: number | string) => {
	const server = https.createServer({
		...generateCertificate()
	}, requestListener)
	server.on("error", (error) => {
		console.error(error)
		process.exit(1)
	})
	server.listen(portOrPipe, () => {
		console.log("Server listening for connections")
	})
	return server
}

export default createServer

```
This function is responsible for setting up our https server. Let's go through it line by line.

```typescript
import { generateCertificate } from "@veracity/node-auth/helpers"
import { RequestListener } from "http"
import https from "https"
```
Here we import the necessary dependencies. We'll use `generateCertificate` to create a self-signed certificate for our development server. This is obviously not suitable for production, but suits us nicely for development purposes.

```typescript
export const createServer = (
	requestListener: RequestListener,
	portOrPipe: number | string) => {

	// ...
}
```
Now we define our function. It should be exported as we intend it to be used from code outside of this file. The function takes two arguments:
- `requestListener` - The request listener is a function that will be called upon every incoming server request. Our code will simply pass the express application instance as this argument as it is a valid `RequestListener` function.
- `portOrSocket` - Defines the port or socket our server will open and listen on.

```typescript
	const server = https.createServer({
		...generateCertificate()
	}, requestListener)
```
Here is where we create our server instance and set up its basic configuration. It requires an `options` object that must contain the properties `key` and `cert`. Fortunately this is exactly what `generateCertificate` creates so we will just spread that result over a new configuration object. Te second argument is the handler function that we pass in.

```typescript
	server.on("error", (error) => {
		console.error(error)
		process.exit(1)
	})
	server.listen(portOrPipe, () => {
		console.log("Server listening for connections")
	})
```
Server objects in node implement what is called event emitters. Event emitters are a generalized data structures that allow registering functions to react on named events. Here we register a handler that will fire if an `error` event occurs. It will simply log the error and kill our process. The number simply indicates what exit code the OS will see. By convention anything other than 0 indicates an error.

The last three lines tell our server to start listening for connections on the port or pipe specified and then tell us when it is ready.

Now that we have a function that helps us configure our server we can begin setting up Express. ExpressJS is a (Connect-compatible) web application framework that has wide community support and extensive plugins available. To set it up let's create another file called `start.ts`. This will be the main file for our app. Here we'll instantiate our express server and create our endpoints. Add this to the file:
```typescript
import express from "express"
import { createServer } from "./server"

const app = express()

app.get("/", (req, res) => {
	res.send("OK")
})

createServer(app, 3000)
```

First off we import the dependencies we need. You'll probably notice that express will be marked as not found. Again that is because we have no type definitions for it. Install express types by running `npm i -D @types/express`

```typescript
const app = express()
```
Then we create our application instance. The application instance is essentially just a really fancy request listener and we can therefore pass it directly to the raw server instance via `createServer`.

```typescript
app.get("/", (req, res) => {
	res.send("OK")
})
```
This is how we register a handler for a specific endpoint in Express. This code creates a handler for all `GET` requests to the root of our application. Once such a request is received it will simply return the text "OK" back to the client.

```typescript
createServer(app, 3000)
```
Finally we create our server and give it our app and a port to listen on, in this case 3000.

With all this in place you should now be able to start your application and see it running. Make sure the `start.ts` file has focus and hit the F5 key. This will start the debugger for this file. Now open your browser, visit [https://localhost:3000](https://localhost:3000) and you should see "OK". Congratulations! You have a working web application in Node!

Next up we'll set up authentication using the `@veracity/node-auth` library to help us.

[Previous - 2. Development environment](2-development-environment.md) --- [Next - 4. Authentication](4-authentication.md)
