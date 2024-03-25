---
author: Veracity
description: This is the changelog for the March 2024 release of Data Workbench.
---

# March 2024 release

Release date: March 2024

Read this page to learn what has changed in Veracity Data Workbench with the March 2024 release.

## New features
This section covers new features.

### Request data from UI
Now, as a workspace admin, you can ask a data provider to share a data set with your workspace. A data provider has stored large amounts of data, such as time series data (IoT) for solar plants, and they can share a subset of this data with you.

<figure>
	<img src="assets/requestdata.png"/>
</figure>

To request that a data provider shares a data set with you:
1. In Data Workbench UI, go to **Data catalogue**.
2. In the upper right corner, select **Request data**. 
3. In the window that shows, under **Data set name**, enter a name for the data set you want to create. 
4. Under **Data provider**, select a data provider. 
5. Fill in other fields in the form.
6. To send your data request, select **Request** 

Your data request will be processed, and when it's complete, you will see your new data set with the requested data in your workspace's **Data Catalogue** in the **Created data sets** subtab.

Below are detailed information on the fields in a data request:
* For **Data provider**, you can select only one data provider from the providers subscribed to your Data Workbench.
* For **Portfolio**, a portfolio is a grouping of sites (assets), and you can select only one portfolio.
* A **Site** is an asset (for example, a solar plant or a windmill), and you can select only one.
* For **Device type**, you can add one or multiple devices based on site (for example, a transformer or inverter). A device is a different component of the site that can provide data (usually, it is time series data).
* For **Add parameters**, each device type has different parameters that can be configured for the request, and a parameter can only be selected once for a device type. A parameter is one data channel where time series data are logged. There can be many parameters per device. A parameter can only have one value at any given time, for example, for a car's speedometer a parameter can be the current speed of the car in kilometers per hour. 
* For **Aggregation**, each parameter has an aggregation setting (for example, default, min, max). A parameter can only have one aggregation for a device type. This is how data is aggregated given the granularity time period; for example, "min" would aggregate with the lowest value recorded in the time period (for example, within 5 minutes if that was the granularity)
* For **Granularity**, this is the time unit for the granularity. For example, it can be in minutes.
* For **Interval**, select the start and end date for the data you are requesting. For example, you can request data from 20 January 2024 to 10 March 2024. 
* You can tick the tickbox **Run Python execution analytics** and select an available Python script. This script will transform the data you are getting from your request, which can give you additional contextualization or transformation of the data and thus increase its quality and relevance.