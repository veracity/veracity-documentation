---
author: Veracity
description: Instructions on how to set up the .NET application
---

# .NET core application

The usage of the Veracity generator is given in the following way:
```ps
yo @veracity/veracity:app [options]
```

To list the latest apps available in the generator, write the following:

```ps
yo --help
```

## .NET core demo

To install and run the .NET core application, you do the following steps.

Open your terminal or powershell and navigate to an empty folder where you want to store your project. To create an empty folder, do the following:

```ps
mkdir MyNewFolderName
```
Then go ahead and create the demo application by typing in:

```ps
yo @veracity/veracity:netcore-webapp
```

When the application is installed, go to the terminal and write:

```ps
dotnet run
```

Now, go to your browser of choice, and visit [https://localhost:3000](https://localhost:3000), and check out your app.

Check out the readme.md in the root folder for additional details.


## .NET application resources
Please refer [https://github.com/veracity/Veracity.Authentication.OpenIDConnect.AspNet](https://github.com/veracity/Veracity.Authentication.OpenIDConnect.AspNet) for recommendation and usage guideline. 

