# Overview 
Data quality is a prerequisite for ensuring trust in the data stored in. Data quality can be measured for a number of metrics usually grouped in categories (dimensions). Veracity supports some generic metrics for time-series data such as completeness (missing records), uniqueness (duplicate records), below min and above max. The level of data quality for any metric is expressed as a Data Quality Index (DQI). The DQI is defined as 1 - RB/RT, where RB is the number of records that failed to meet the data quality requirement whereas RT is the number of total records assessed. The DQI will yield a number between 0 and 1 where a score of 0 will mean all records failed (low quality) and 1 will mean all records passed (high quality). Other metrics will need to be custom-made based on data quality requirements for any particular data source. The data quality metrics defined in Veracity are displayed in a data quality dashboard that can be accessed in the Veracity portal (https://dataservices.dnvgl.com). The user can select any metric and drill down to any level to investigate when the error occurred and for which sensor.


# Quick start
The data quality dashboards are available for all MyDNVGL users with the appropriate access rights to projects that contain data with applied data quality metrics. The below screenshot shows some sample projects where one (MDC-NYK Venus) has a data quality dashboard. The data management services can be accesses from https://dataservices.dnvgl.com . Select Data quality (in red box) to proceed to the data quality dashboard. The next section, Tutorial, provides a more detailed explanation for how to use the data quality dashboard. 

![](https://veracitydevtest.blob.core.windows.net/static-documentation/dataquality1.png "Data Management Services")

Figure – The Veracity landing page for data services and data quality (https://dataservices.dnvgl.com)

# Tutorial
The data quality functionality in data management services is divided in three layers; Data quality dashboard, data quality gauge and data quality drilldown. The dashboard contains a gauge for each metric and each gauge provides drilldown to specific data points.

## Data quality dashboard
When selecting the Data quality (INSERT PIC OF ICON) icon for a project, the user will be presented with the data quality dashboard displaying all defined data quality metrics for the data management services project. The screenshot below shows a data quality dashboard with six defined metrics. The first four (uniqueness, above min, above max and completeness) are generic metrics for time-series data, whereas Goodness is a custom metric based on a data quality flag present in this data stream. The metric labelled Usable measures the ratio of records without any data quality issues, ie any record which satisfies all data quality requirements.

![](https://veracitydevtest.blob.core.windows.net/static-documentation/dataquality2.png "Data Quality dashboard") 

Figure - Data quality dashboard
## Data quality gauge
Each data quality gauge has an information icon in the top right corner. If the user hovers over this icon a detailed description of the data quality metric is displayed. The below figure show the information box for the metric labelled Usable. Table 1 also shows the information text for the generic time-series data quality metrics. 

![](https://veracitydevtest.blob.core.windows.net/static-documentation/dataquality3.png "Usable data quality metric") 
Figure – Information for the Usable data quality metric

| Metric | Information|
| ------------- |:-------------:| 
| Uniqueness   | Measures the proportion of data points registered as a single value, ie no timestamp collision |
| Above min     | Measures the proportion of data points above the minimum value set in the metadata      |  
| Below max     | Measures the proportion of data points below the maximum value set in the metadata      |  
| Completeness  | Measures how many data points are present in the data set according to a given samplling rate      |  


Table - Generic metrics and information texts

Each data quality metric is represented on the dashboard as a data quality gauge. The below figure shows the gauge for the generic metric labeled Completeness with a description of the main gauge properties. The gauge properties are also described in more detail in the below table.

| Gauge property  | Description |   
| ------------- |:-------------:| 
|  Metric name   | A short descriptive name of generic or custom data quality rule |
| Ratio meeting requirements | Ratio (0 to 1) of data points meeting the requirement       |  
| Ratio not meeting requirements | Ratio (0 to 1) of data points not meeting the requirement      |  
| Data quality requirement  | A user specified requirement to the data quality index for the metric      |  
| Data quality index  | The data quality index as defined previously      |  
| Metric description  | Metric description from above table      |  
| Deviation from requirement  | The difference between the required and the measured DQI. If the measured DQI falls short of the requirement a red dot is displayed      |  

Table – Gauge properties

![](https://veracitydevtest.blob.core.windows.net/static-documentation/dataquality4.png "Dashboard gauge characteristics") 

Figure – Overview of dashboard gauge characteristics
## Data quality drilldown
Clicking on any data quality gauge provides a drilldown to identify the offending data points. The drilldown displays both a historical representation as well as a hierarchical representation.  The historical representation currently has a fixed resolution of one week. The below figure shows a sample historical drilldown for the Completeness metric. The horizontal red line represents the Data quality requirement whereas the blue line represent the measured data quality. For the shown case, the data quality falls short of the requirements except for in the start and end of the period. 

![](https://veracitydevtest.blob.core.windows.net/static-documentation/dataquality5.png "Drilldown for historical data") 

Figure – Drilldown for historical data

The hierarchical drilldown provides both a list- and tree- view representation of sensors in a functional breakdown structure. The sensors must have been mapped to the breakdown structure in a previous process, please refer to (REF). The below figure shows an example for a hierarchical drilldown for a compressor sensor. The measured data quality index is shown for each sensor and the sensors that doesn’t satisfy the requirements are labelled with a red circle, like the labelling on the data quality gauge.

![](https://veracitydevtest.blob.core.windows.net/static-documentation/dataquality6.png "Drilldown for hierarchical data") 

Figure – Drilldown for hierarchical data

The combination of both historical and hierarchical drilldowns provides a powerful means of determining the specific sensors not meeting the data quality requirements as well as in what time interval the problem occurred. 

# Pattern & Practices
The data quality metrics used in the Data Quality dashboard are based on measurement principles as outlined in ISO8000/8. Further, we recommend to follow the guidelines described in the recommended practice titled Data Quality Assessment Framework (DNVGL-RP-0497). The recommended practice suggests to use ISO 8000/8 for data quality measurements, data management maturity model to assess the organizational capabilities to respond to data quality issues, risk assessment to determine business impact and prioritize tasks and plan-do-check-act cycles to ensure continuous improvement.  
The below sections provide short descriptions of the main activities that should be performed as a part of the data quality process, please refer to DNVGL-RP-0497 for further details.

## Scope and requirements
The first step of the data quality process should involve a detailed description of the scope and context of the assessment, such as which systems, data sources and areas of usage should be included. All measurements should be documented by the relevant requirements.

## Data Profiling and exploration
In the initial phase of a data quality assessment, data profiling and data exploration can be used to both validate existing business rules and requirements as well as to establish new rules and requirements.

## Data Quality measurement 
ISO 8000/8 divides data quality issues into three main categories: Syntactic, Semantic and Pragmatic. Syntactic data quality measures conformance to schema and business and domain rules, semantic data quality measures conformance to the real world or reference data and pragmatic data quality is a measure of the user’s perception of the fitness for use. The data quality metrics on the data quality dashboard falls into the syntactic category. The semantic category commonly relies on sampling techniques or reference to trusted data such as provided by registers or digital twins. The pragmatic data quality is commonly measured by interviews and questionnaires.

## Data Management Maturity (DMM)
The DMM model divides the organizational capabilities to handle data quality issues in eight categories and five levels. The categories include people and processes, technology and standards as well as data quality metrics and dimensions. The levels include initial, repeatable, defined, managed and optimized. It is important to establish both the current maturity level as well as the desired level to define any deviations and activities required to close the gap. 

## Risk Assessment
Well known and established techniques for risk assessment can readily be used to determine the criticality of data quality issues. This will provide both an analysis of business impacts of data quality as well as help to prioritize activities based on cost and criticality. 

## Continuous improvement
The effect of the implemented data quality activities should be monitored carefully to determine the effect of the activity and as such establish the return on investment. Any inefficient activities should be redesigned or terminated.

The below figure shows the overall process for the activities described above.

![](https://veracitydevtest.blob.core.windows.net/static-documentation/dataquality7.png "Overall process for data quality assessment") 


Figure – The overall process for data quality assessment

# References
DNVGL-RP-0497 Data quality assessment framework
ISO 8000/8 Information and data quality – concepts and measuring
Data Management Maturity (DMM) Model – CMMI Institute

# Resources 
In this section we have added resources that may provide you with additional learning. 
(E.g: FAQ, GitHub, Wiki, Stack overflow, videos)

# Price Model
In this section, you will find an overview of the price model and if it is applicable to you


