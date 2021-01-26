---
author: Benedikte Kallåk
description: This section describes the different endpoints of the IoT Api
---

# Veracity IoT Api

Only users that has access to an asset can access data from this asset.

The api is accessible from [api-portal](https://api-portal.veracity.com/)


# Subscribe to API

Data can be accessed using Veracity IoT api. The API is managed by Azure API management and hence you need a subscription. 
1.	Go to Veracity api portal:[api-portal](https://api-portal.veracity.com/)
2.	Sign in
3.	Select Product
4.	Select Veracity Platform API. This api contains all the Veracity platform APIs which allow you to integrate with platform and enjoy the platform features by calling related API, it contains all the legacy "My service API" and "Data fabric API".
5.	Select Subscribe
6.	After subscription, your access keys are available from Products
 
 
# Test api from portal.	

1.  Go to [api-portal](https://api-portal.veracity.com/)
2.	Sign in
3.	Select API
4.	Select Data Fabric Time Series API
5.	Select Group  by Tag
6.	Select an endpoint – i.e [api](https://api.veracity.com/veracity/timeseries/api/v1/Assets)
7.	Select Try It
8.	If you are  signed in Ocp-Apim keys are filled out.  This is the key you can get from subscription key described above
9.	Select Authorization code from Authorization 
10. Fill in required parameters in payload and select SEND

# Use api from application

You will receive credentials for your service app:
- Client Id
- Client secret
- APIM subscription key

The service app is granted access to the asset(s).



## C# SDK
Veracity IOT SDK can be used to connect to API from .NET application. Veracity IOT SDK is based on .Net Standard.

- [model](https://www.nuget.org/packages/Veracity.IoT.SDK.Models/)
- [client](https://www.nuget.org/packages/Veracity.IoT.SDK.Client/)
- [externtions](https://www.nuget.org/packages/Veracity.IoT.SDK.Client.Extensions/)


<ul>
<li>Veracity.IOT.SDK.Models: models used for ingest of data and output of data queries</li>
<li>Veracity.IOT.SDK.Client: To create HTTTP client to access API. Includes Veracity.IOT.SDK.Models</li>
<li>Veracity.IOT.SDK.Client.Extensions: For dependency injections. Includes Veracity.IOT.SDK.Models and Veracity.IOT.SDK.Client  </li>
</ul>


## Code example
This code snippet shows how to instantiate a VeracityHTMLClient, create pauyloads  and invoke api's for requesting timeseries data

   ```cs
         string baseUrl = "https://api.veracity.com/veracity/timeseries/api/v1/";
         var tokenProvider = new ClientCredentialsTokenProvider(ClientId, ClientSecret);
         IVeracityIoTTimeSeriesClient clientConfig = new VeracityIoTTimeSeriesClient(tokenProvider, baseUrl, ApiSubscriptionkey);
        
         DefaultQueryPayload payload = new DefaultQueryPayload()
         {
                AssetIds = new System.Collections.Generic.List<Guid>() { assetGuid }
         };

         DateTime start = new DateTime(2020, 09, 25);
         DateTime end = new DateTime(2020, 10, 05);
         payload.Start = new DateTimeOffset(start);
         payload.End = new DateTimeOffset(end);      //max date for Timestamp
         payload.Limit = 1000;  //i.e. max no of datapoints 
	     payload.DownScaleInt = "PT4H";  //i.e. downscale to 4 hours

         //request data on channels based on their shortid or channelUUID (guid)
         payload.DataChannelIdType = DataChannelIdTypeEnum.DataChannelUuid;
         payload.DataChannelIds = new System.Collections.Generic.List<string>();
         //datachannels was received from requesting datachanneøs for asset
         foreach (var ch in dataChannels)
         payload.DataChannelIds.Add(ch.DataChannelId.UUID.ToString());

        //Alternative use shortId - ie
        //payload.DataChannelIdType = DataChannelIdTypeEnum.ShortId;
        //payload.DataChannelIds = new System.Collections.Generic.List<string>() { "Voltage", "ActiveEnergy" };

        payload.TypeOption = TypeOption.SddData;  //both data and metadata			
			
       var result2 = await clientConfig.GetTimeSeriesData(payload);
       //datapoints are delivered as Tabular data  when downscaling is used, and values only in Average, max and min (value is null)
       
	  //request raw data - datapoints are delivered as Event data			
		 payload.DownScaleInt = null;  //get raw data
	     var result = await clientConfig.GetTimeSeriesData(payload);  						

```            
payload when requesting the n-latest values received (in this example 10)

  ```cs
            LatestQueryPayload payload = new LatestQueryPayload()
            {
                AssetIds = new System.Collections.Generic.List<Guid>() { assetGuid },
                LatestNValues = 10,
				TypeOption = TypeOption.Data,
				DataChannelIdType = DataChannelIdTypeEnum.DataChannelUuid, 
				DataChannelIds = <list of channels>
            };

 ```
			


## Python SDK
SDK for Python: [Python](https://github.com/veracity/Python-Sample-to-Connect-to-Veracity-Service)






