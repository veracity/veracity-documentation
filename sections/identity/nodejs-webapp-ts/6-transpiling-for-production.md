---
author: Veracity
description: How to transpile code for production in the NodeJS Webapp tutorial.
---

# 6. Transpiling for production
[Previous - 5. Calling APIs](5-calling-apis.md)

Now that we have a fully working application that is able to authenticate users and call APIs we only need to put it somewhere where users can access it. If we had written everything in plain JavaScript this would be a trivial task of copying our code over to the server where we want it to run and start it up. But since we are using TypeScript we need to do one additional thing first. This step is called transpiling.

Transpiling is a term often heard when talking about JavaScript. It essentially means to "convert code written in one language to another". For JavaScript this is quite a common scenario because the language is constantly evolving and changing and browsers do not always have the ability to keep up. 

There are also several concepts that may exist in a "trial-phase" (draft phase) before they are officially adopted into the language, yet one might still want to use them when writing code. Like using the async/await syntax before it is officially adopted by common browsers. There are several ways to perform transpilation on code and several tools available to do it. Since we are using TypeScript we will be using the TypeScript compiler for this, but another very common tool is [Babel](https://babeljs.io/).

Technically we could run our application on the server by simply installing `ts-node` and running `start.ts` through that instead of using plain node. However this would cause a performance hit because every file still needs to be transpiled for node to understand it, the process is just done on-the-fly. So we will be transpiling our code first and then we can run the final output on our servers as plain, old-fashioned, home-grown JavaScript.

We already have the TypeScript compiler installed, we just haven't used it directly before. You can test it out by running it in the root folder using `npx`:

```
npx tsc --build tsconfig.json
```

This should create a folder in your project called `dist` and output JavaScript files from the `src` folder. We now have a JavaScript-only version of our application. Unfortunately it does not include our production dependencies from `node_modules`. We need to ensure you have everything necessary to run the application.

Now we could just copy the entire `node_modules` folder over to dist, zip it up and push ut out, but that would include all of our dev dependencies as well. The better approach is to just copy the `package.json` and and `package-lock.json` files over and then run `npm i --production` in the dist folder. This will install only our production dependencies resulting in a much smaller package.

There are many different ways we could achieve this, but we'd like to keep control within our application so let's write a small helper script that will copy the remaining files over to `/dist` after we're done transpiling. Create a new folder `scripts` and a new file there called `copyFiles.ts`. Now let's write the code that will copy files:

```typescript
import fs from "fs"
import path from "path"
import { promisify } from "util"

const pCopyFile = promisify(fs.copyFile)
const root = path.resolve(__dirname, "../")
const dest = path.resolve(root, "dist")

const filesToCopy = [
	"package.json",
	"package-lock.json"
]

const start = async () => {
	for (const file of filesToCopy) {
		const fullSource = path.resolve(root, file)
		const fullDest = path.resolve(dest, file)
		console.log(`Copy ${fullSource} -> ${fullDest}`)
		await pCopyFile(fullSource, fullDest)
	}
}

start().catch((error) => {
	console.error(error)
	process.exit(1)
})
```

This is a standalone script that we will run from the command line. The last few lines of the file that call the `start` function allows it to work even if it's async and handles errors correctly. Running this file will result in all files in the `filesToCopy` array being copied from the root of the project to `dist`.

Now we have the pieces we need to "build" our code. We can run them from a terminal like this:
```
npx tsc --build tsconfig.json
npx ts-node -T scripts/copyFiles.ts
```

The first command runs the TypeScript compiler using our config file while the second runs our `copyFiles` script using `ts-node` which is equivalent to simply running node, but for TypeScript files.

One last thing the build does not do yet is clean up the `dist` folder before rebuilding. This may result in old files being kept in the output. To fix this we will install a small module called `rimraf` whose primary purpose is to clear folders and files. Run:
```
npm i -D rimraf
```

With this in place the steps needed to completely rebuild our application are:
```
npx rimraf dist
npx tsc --build tsconfig.json
npx ts-node -T scripts/copyFiles.ts
```

Running all of these is a bit cumbersome. We have to remember each step and make sure we do them in the correct order. Fortunately, the `package.json` file supports named `scripts` that we can call simply by running `npm run [name of script]`. Open the `package.json` file and in the `scripts` section add the following:
```json
  "scripts": {
    "build:copy": "ts-node -T scripts/copyFiles.ts",
    "build:tsc": "tsc --build tsconfig.json",
		"build": "rimraf dist && npm run build:tsc && npm run build:copy",
		"start": "node start.js"
  },
```

Now we can simply run `npm run build` from the terminal and it will execute all the steps in the proper order for us.

An that's it. We now have a built application ready for install in the `dist` folder. To run it on a server somewhere simply copy the files over, install dependencies using `npm i --production` and start it up with `npm start`.

[Previous - 5. Calling APIs](4-calling-apis.md) --- [Next - 7. Summary](7-summary.md)