# Node.JS Authentication library
**[@veracity/node-auth](https://github.com/veracity/node-auth)**

Authentication is a core feature of the Veracity Data Platform. In order to aid developers in building secure applications that utilize authentication we have published an open-source library called [@veracity/node-auth](https://github.com/veracity/node-auth). This library handles all the complexity around authenticating with Veracity and aquiring access tokens for you so that you can focus on building your application.

## Example
This is a quick example of getting up and running with the Node.JS authentication library for Veracity. For additional documentation and more examples see the [projects GitHub page](https://github.com/veracity/node-auth).

You need to register your application with Veracity before you can authenticate. You can do this by visiting the [Veracity for Developers Project portal](https://developer.veracity.com/projects) and creating an Application Credential resource.

Install the library
```
npm i @veracity/node-auth
```

Install the necessary dependencies
```
npm i express express-session passport
```

Your application needs to be built on these for this example. See the readme on GitHub for advanced scenarios.

Configure authentication using the built-in helper function `setupAuthFlowStrategy`
```javascript
setupAuthFlowStrategy({
	appOrRouter: app, // app is your express application instance
	apiScopes: [], // Provide any API scopes you wish to fetch access tokens for. Remove this to use the default.
	strategySettings: {
		clientId: "", // From the Developer Portal
		clientSecret: "", // From the Developer Portal
		replyUrl: "", // From the Developer Portal
	},
	sessionSettings: {
		secret: "ce4dd9d9-cac3-4728-a7d7-d3e6157a06d9", // Replace this with your own secret
		store: new MemoryStore() // Use memory store for local development only
	}
})
```

Users should now be able to authenticate with Veracity through your application by visiting `https://[your-application]/login`