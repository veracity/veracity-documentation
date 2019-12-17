---
author: Veracity
description: Instructions on how to create the Node SPA app
---

# NodeJs application

The usage of the Veracity generator is given in the following way:
```ps
yo @veracity/veracity:app [options]
```

To list the latest apps available in the generator, write the following:

```ps
yo --help
```

## NodeJs SPA demo
To install and run the NodeJs SPA demo, you do the following steps.

Open your terminal or powershell and navigate to an empty folder where you want to store your project. To create an empty folder, do the following:

```ps
mkdir MyNewFolderName
```
Then go ahead and create the demo application by typing in:

```ps
yo @veracity/veracity:node-spa
```

As stated by the generator, you will need to get your clientID and clientSecret, and put them into the config.js in the root directory of your new app.

When the clientID and clientSecret are correctly added, go to the terminal and write:

```ps
npm start
```


Now, go to your browser of choice, visit [https://localhost:3000](https://localhost:3000), and check out your app.


