---
author: Veracity
description: Gives an overview of the Veracity Data Platform services and related components.
---

# Service bus consumer app using Docker
This tutorial will walk you through the steps to create an Azure ServiceBus consumer which receives messages from a queue. We'll create a C# console application which can optionally be run in a Docker container. 

## 1. Create a new C# console application
To create a new C# console application, you can use Visual Studio (or another IDE of choice) or the .NET Core CLI. We'll use the [.NET Core CLI](https://learn.microsoft.com/en-us/dotnet/core/tools/) in this tutorial.
Create a new directory for your project and navigate to it:
```cs
mkdir ServiceBusConsumer
cd ServiceBusConsumer
```
Create a new C# console application:
```cs
dotnet new console
```
### 1.1. Add the Azure ServiceBus NuGet package
To add the Azure ServiceBus NuGet package, run the following command:
```cs
dotnet add package Azure.Messaging.ServiceBus
```
Also add the following NuGet packages:

```cs
dotnet add package Microsoft.Extensions.Configuration
dotnet add package Microsoft.Extensions.Configuration.Json
dotnet add package Microsoft.Extensions.Configuration.EnvironmentVariables
dotnet add package Newtonsoft.Json
dotnet add package CommandLineParser
```
### 1.2. Create the configuration file
Create a new file called `appsettings.Localhost.json` in the root of your project and add the following content:
```json
{
  "ServiceBusConnectionString": "<your connection string>",
  "QueueName": "<your-queue-name>"
}
```
The connection string and queue name have been issued to you when you have been on-boarded to the Veracity DataFabric.

> **Important:**  
> Make sure to add the `appsettings.Localhost.json` file to your `.gitignore` file.

### 1.3. Create the Configuration builder
The configuration will be defined per environment. For `Localhost` it's fine to save the `ConnectionString` inside the file itself since the file it is not added to git. 
However for other environments, such as `Development` and `Production`, we need to use environment variables or read the configuration from an Azure KeyVault.
Add the following content inside `Program.cs` to implement the configuration builder:
```cs
using System;
using System.Threading.Tasks;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Configuration.Json;
using Microsoft.Extensions.Configuration.EnvironmentVariables;

namespace ServiceBusConsumer;
class Program
{
    static async Task Main(string[] args)
    {
        var env = Environment.GetEnvironmentVariable("ASPNETCORE_ENVIRONMENT");
        if (string.IsNullOrEmpty(env))
        {
            env = "Localhost";
        }
        
        var configuration = Configure(env).Build();
        
        var serviceBusConnectionString = configuration["ServiceBusConnectionString"];
        var serviceBusQueueName = configuration["QueueName"];

        Console.WriteLine($"ServiceBus connection string: {serviceBusConnectionString}");
        Console.WriteLine($"ServiceBus queue name: {serviceBusQueueName}");
    }
    
    private static IConfigurationBuilder Configure(string env)
    {
        return env switch
        {
            "Localhost" => ConfigureLocalhost(),
            "Development" => ConfigureDev(),
            _ => throw new InvalidOperationException($"Unknown environment: {env}")
        };
    }

    private static IConfigurationBuilder ConfigureLocalhost()
    {
        var configuration = new ConfigurationBuilder()
            .SetBasePath(AppContext.BaseDirectory)
            .AddJsonFile("appsettings.json", optional:true, reloadOnChange:true)
            .AddJsonFile("appsettings.Localhost.json", optional:false, reloadOnChange:true)
            .AddEnvironmentVariables();

        return configuration;
    }
    
    private static IConfigurationBuilder ConfigureDev()
    {
        var configuration = new ConfigurationBuilder()
            .SetBasePath(AppContext.BaseDirectory)
            .AddJsonFile("appsettings.json", optional:false, reloadOnChange:true)
            .AddEnvironmentVariables();

        return configuration;    
    }
}

```
Now edit your `.csproj` file and add the following content to make sure that the config files are copied to the output directory:

```json
<ItemGroup>
    <None Update="appsettings.json">
        <CopyToOutputDirectory>Always</CopyToOutputDirectory>
    </None>
    <None Update="appsettings.Localhost.json">
        <CopyToOutputDirectory>Always</CopyToOutputDirectory>
    </None>
</ItemGroup>
```

### 1.4. Create the Parameters class

We'll use an internal class to hold the parameters from the command line, such as `Environment` which is the environment name.

Create a new folder named `Lib` and inside it add a new class `Parameters.cs` with the following content:

```cs
using CommandLine;

namespace ServiceBusConsumer.Lib;

internal class Parameters
{
    [Option(
        'e',
        "Environment",
        Required = false,  
        Default = "Localhost",
        HelpText = "The name of the desired environment.  If not specified, Localhost will be used.")]
    public string Environment { get; set; }
}
```
Update the `Program.cs` file to use the `Parameters` class. The `Main` method should now look like this (note that we're using the `Parameters` class to get the environment name and we're no longer using the `ASPNETCORE_ENVIRONMENT` environment variable):

```cs
static async Task Main(string[] args)
{
    Parameters parameters = null;
    Parser.Default.ParseArguments<Parameters>(args)
        .WithParsed(parsedParams =>
        {
            parameters = parsedParams;
        })
        .WithNotParsed(errors => Environment.Exit(0));

    var configuration = Configure(parameters.Environment).Build();
    var serviceBusConnectionString = configuration["ServiceBusConnectionString"];
    var serviceBusQueueName = configuration["QueueName"];

    Console.WriteLine($"ServiceBus connection string: {Regex.Replace(serviceBusConnectionString, @"\bSharedAccessKey=(.+);\b", "SharedAccessKey=**********;")}");
    Console.WriteLine($"ServiceBus queue name: {serviceBusQueueName}");
}
```
### 1.5. Receive messages from the queue
Now we're ready to receive messages from the ServiceBus queue. Messages are received via a task list, and the code uses batching.
We'll use the official `Azure.Messaging.ServiceBus` SDK and we'll use the code from official [Update inventory](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-tutorial-topics-subscriptions-portal#receive-messages) tutorial from the Azure docs as reference.
Create a new method `ReceiveMessages` in the `Program` class with the following content:
```cs
private static async Task ReceiveMessages(IConfigurationRoot configuration, CancellationToken ct)
{
    try
    {
        await using var client = new ServiceBusClient(configuration["ServiceBusConnectionString"]);
        var receiver = client.CreateReceiver(configuration["QueueName"]);
        
        while (!ct.IsCancellationRequested)
        {
            IReadOnlyList<ServiceBusReceivedMessage> messages = await receiver.ReceiveMessagesAsync(maxMessages: 100, cancellationToken: ct);
            if (messages.Any())
            {
                int i = 0;
                foreach (ServiceBusReceivedMessage message in messages)
                {
                    
                    Console.WriteLine($"Received message: {message.Body}");
                    IReadOnlyDictionary<string, object> applicationProperties = message.ApplicationProperties;
                    Console.WriteLine($"topic={applicationProperties["topic"]}; eventType={applicationProperties["eventType"]}; assetId={applicationProperties["assetId"]}");
                    
                    await receiver.CompleteMessageAsync(message, ct);
                    i++;
                }
            }
            else
            {
                Console.WriteLine("No messages received.");
            }
        }
    }
    catch (TaskCanceledException) { } // ct was signaled
    catch (Exception ex)
    {
        Console.WriteLine($"[ERROR] Unexpected Exception {ex.Message}");
        Console.WriteLine($"\t{ex.ToString()}");
    }
}
```
The `ReceiveMessages` method receives the `configuration` object as a parameter, so that it can access the configuration settings. It also receives a `CancellationToken` object, which is used to cancel the task when the user presses `Ctrl+C`.
The `ReceiveMessages` method creates a `ServiceBusClient` instance, which is used to receive messages from the queue. 
The receive call to the Service Bus is kept open for while the console app is running and if messages arrive, they're returned immediately and a new receive call is issued. This concept is called _long polling_. You can read more about how Service Bus queues work in the [Azure docs](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quickstart-portal).
Update the `Main` method to call the `ReceiveMessages` method:

```cs
static async Task Main(string[] args)
{
    // ...
    // previous content omitted for brevity
    // ...
        
    // Wait until the app unloads or is cancelled
    Console.WriteLine("Press control-C to exit.");
    var cts = new CancellationTokenSource();
    AssemblyLoadContext.Default.Unloading += (ctx) => cts.Cancel();
    Console.CancelKeyPress += (sender, eventArgs) =>
    {
        eventArgs.Cancel = true;
        cts.Cancel();
        Console.WriteLine("Exiting...");
    };

    ReceiveMessages(configuration, cts.Token).Wait();
    await WhenCancelled(cts.Token).WaitAsync(cts.Token);
}
```
Lastly, add the `WhenCancelled` method to the `Program` class:

```cs
private static Task WhenCancelled(CancellationToken cancellationToken)
{
    Console.WriteLine("WhenCancelled called.");
    var tcs = new TaskCompletionSource<bool>();
    cancellationToken.Register(s => ((TaskCompletionSource<bool>)s).SetResult(true), tcs);
    return tcs.Task;
}
```
## 2. Run the console app
Now, we're ready to run the console app. Refer to the Developer documentation for information on how to publish messages to the Veracity IoT Platform. 
When you publish one or more messages to the Veracity IoT Platform, the message will be routed to the Service Bus queue and the console app will receive the message.
To run the console app, open a command prompt and navigate to the `ServiceBusConsumer` folder. Run the following command:
```cs
dotnet run
```
The console app will start and you should see the following output:
```cs
ServiceBus connection string: <your connection string>
ServiceBus queue name: <your queue name>
Press control-C to exit.
```
## 3. Add Docker support
To run the console app in a Docker container, we need to add Docker support to the project. 

### 3.1. Create a Dockerfile
Create a new file named `Dockerfile` in the `ServiceBusConsumer` folder with the following content:

```cs
#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/runtime:6.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["ServiceBusConsumer.csproj", "."]
RUN dotnet restore "./ServiceBusConsumer.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "ServiceBusConsumer.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "ServiceBusConsumer.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "ServiceBusConsumer.dll"]
```
The `Dockerfile` is based on the default Dockerfile that is created when you add Docker support to a .NET Core console app.

### 3.2. Create a .dockerignore file
Since we're building the Docker image from the source code, we don't need to copy the `bin` and `obj` folders to the Docker image. 

> **Important:**  
> We also need to add the `appsettings.Localhost.json` file to .dockerignore, since it contains the connection string to the Service Bus queue.

Create a new file named `.dockerignore` in the `ServiceBusConsumer` folder with the following content:

```cs
**/.classpath
**/.dockerignore
**/.env
**/.git
**/.gitignore
**/.project
**/.settings
**/.toolstarget
**/.vs
**/.vscode
**/*.*proj.user
**/*.dbmdl
**/*.jfm
**/azds.yaml
**/bin
**/charts
**/docker-compose*
**/Dockerfile*
**/node_modules
**/npm-debug.log
**/obj
**/secrets.dev.yaml
**/values.dev.yaml
appsettings.Localhost.json
```
## 4. Build the Docker image
To build the Docker image, open a command prompt and navigate to the `ServiceBusConsumer` folder. Run the following command:
```cs
docker build -t servicebusconsumer .
```
The Docker image is now built and you can run it in a container.
## 5. Run the Docker container
### 5.1. Pass the connection string to the Docker container
Since we have excluded the `appsettings.Localhost.json` file, we need to pass the connection string as an environment variable to the Docker container.

To run the Docker container, open a command prompt and run the following command:
```cs
docker run -it -e ServiceBusConnectionString="<your connection string>" --rm servicebusconsumer
```
The console app will start and you should see the following output:

```cs
ServiceBus connection string: <your connection string>
ServiceBus queue name: <your queue name>
Press control-C to exit.
```
### 5.2. Pass the connection string to the Docker container using a secrets file
To avoid passing the connection string as an environment variable, we can use the `Secret Manager` tool which stores sensitive data during the development of an ASP.NET Core project. 
Refer to the [Secret Manager tool documentation](https://learn.microsoft.com/en-us/aspnet/core/security/app-secrets) for more information.

### 5.3 Use Azure managed identities to get the secret from an Azure Key Vault 
When deployed to Azure and running in production, a better approach is to use Azure managed identities to get the secret from an Azure Key Vault. This avoids having to set the connection string anywhere other than the Azure Key Vault. 
This scenario is detailed in the [Azure Container Instances](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-managed-identity) documentation.

### 5.4 Stop the Docker container
To stop the container, press `Ctrl+C`. Alternatively, you can run the following command:
```cs
docker kill <container id>
```
To get the container id, run the following command:
```cs
docker ps
```
## 6. Publish the Docker image to Azure Container Registry
To publish the Docker image to Azure Container Registry (ACR), you need to create a Container Registry instance. Refer to the [Azure docs](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal) for information on how to create an Azure Container Registry.

Once you've created an ACR, you can publish the Docker image to the registry. Open a command prompt and run the following command:
```cs
az acr login --name <your registry name>
```
The command will log you in to the Azure Container Registry.
Next, tag the Docker image with the name of the Azure Container Registry:
```cs
docker tag servicebusconsumer <your registry name>.azurecr.io/servicebusconsumer
```
Finally, push the Docker image to the Azure Container Registry:
```cs
docker push <your registry name>.azurecr.io/servicebusconsumer
```
The Docker image is now published to the Azure Container Registry and can be deployed as a container instance. Refer to the [Azure docs](https://docs.microsoft.com/en-us/azure/container-instances/container-instances-quickstart) for information on how to do that.

## References
* [Azure Service Bus](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview)
* [Azure Service Bus queues](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dotnet-get-started-with-queues)
* [Veracity Developer documentation](https://developer.veracity.com/)
