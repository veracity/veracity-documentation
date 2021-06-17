---
author: Benedikte Kallåk
description: This section describes the different endpoints of the IoT Api
---

# Use api from applications

Only users that has access to an asset as well as given permission to datachannel-datasets can access iot data from this asset.

The api is accessible from [api-portal](https://api-portal.veracity.com/)

## Access token
There are two ways of making requests to the Veracity Iot & Events API endpoints. You can request the API 
either as a user through API Portal/Postman or as application through Postman/Code. 
- When you request the endpoints as user, then your personal token and API Key are being used. 
- On the other hand, when you make requests as application then application token and API key are being used.

[See details about authentication and how to test the api](authenticate-api.md)


## C# SDK
Veracity IOT SDK can be used to connect to API from .NET application. Veracity IOT SDK is based on .Net Standard and availabale as Nuget packages.

- [model](https://www.nuget.org/packages/Veracity.IoT.SDK.Models/): Veracity.IOT.SDK.Models: models used for data ingest and output of data queries
- [client](https://www.nuget.org/packages/Veracity.IoT.SDK.Client/): Veracity.IOT.SDK.Client: To create HTTTP client to access API. Includes Veracity.IOT.SDK.Models
- [extentions](https://www.nuget.org/packages/Veracity.IoT.SDK.Client.Extensions/): Veracity.IOT.SDK.Client.Extensions: For dependency injections. Includes Veracity.IOT.SDK.Models and Veracity.IOT.SDK.Client

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






