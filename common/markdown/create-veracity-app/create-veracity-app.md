---
Title : "Create Veracity App"
Author: "Brede Børhaug"
Contributors: 
---



## Overview 
To make life easy for you, Veracity have created a Yeoman generator to get you started with your applications. The generator require Node to be installed in order to run. You may pick your language of choise for the Veracity application in the generator.


Create your application:
- [Set up your dev environment](#set-up-your-dev-environment)
- [Install and update the Veracity application generator](#install-the-veracity-application-generator)
- [NodeJS application](#nodejs-application)
- .NET application


## Quick start 


### Set up your dev environment
To set up your dev environment to run the Veracity application generator, you first need to install Node on your computer. If NodeJs is not installed, go to [Nodejs.org](https://nodejs.org/en/download/) and get the latest stable version. When you are all done, you may go ahead and install the Veracity application generator. 

### Install the Veracity application generator
The Veracity application generator is based on Yeoman, and design to get you started developing on Veracity. The source code for the generator is located at [GitHub](https://www.github.com/veracity) and published as a package on [npm](https://www.npmjs.com/package/@veracity/generator-veracity). The first thing you need to do to install the generator is to install Yeoman on your system. You do that in the following way:

```ps
npm install -g yo
```

You should now have Yeoman installen on your systemm. To install the Veracity application, put the following into your terminal/powershell:
```ps
yo install -g @veracity/generator-veracity
```

Now Veracity application generator is installed on your system. You may procede to create your application. 

We encurrage you to periodically check for updates to the generator, to make sure you get the latest and greatest. In order to update the generator, you do the following:

```ps
yo
```
Then select update generator, and then the @veracity/generator-veracity. You should then be updated to the latest.

### NodeJs application
The usage of the Veracity generator is given in the following way:
```ps
yo @veracity/veracity:app [options]
```

To list the latest apps available in the generator, write the following:

```ps
yo --help
```

#### NodeJs webapp demo
To install and run the NodeJs webapp demo, you do the following steps.

Open your terminal or powershell and navigate to an empty folder where you want to store your project. To create an empty folder, do the following:

```ps
mkdir MyNewFolderName
```
Then go ahead and create the demo application by typing in:

```ps
yo @veracity/veracity:node-webapp-demo
```

As stated by the generator, you will need to get your clientID and clientSecret, and put them into the config.js in the root directory of your new app.

When the clientID and clientSecret are correctly added, go to the terminal and write:

```ps
npm start
```


Now, go to your browser of choice, and visit [https://localhost:3000](https://localhost:3000), and check out your app.



## GitHub  
Follow our open projects related to ingest on https://github.com/veracity

## Stack Overflow
Stack Overflow is the largest, most trusted online community for developers to learn, share their programming knowledge. The Veracity developer team monitor Stack Overflow forumposts that include the tag Veracity Platform.

[Visit Stack Overflow](https://stackoverflow.com/questions/tagged/veracity+platform?mode=all)

 
 
## Price model 
Creating an application in Veracity for development, test and staging is of course free. When you are ready to go production, get in touch with our onboarding team, and we will get you set up. Happy coding!
 
 
