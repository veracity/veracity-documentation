---
author: Veracity
description: This page explains how to utilize the analytics capabilities
---

# Workflows
In Azure Databricks, a job is a way to automate and schedule tasks such as running notebooks, JARs, Python scripts, or workflows. A job can have multiple tasks, forming a workflow and can be executed on schedule or on-demand.

Azure Databricks does not use distinct terminology to separate the job definition (the configuration of tasks, clusters, and schedule) from the job run (the actual execution instance). Both are referred to under the umbrella of “jobs,” but conceptually:

* **Job (Definition):** The configured workflow, including tasks, dependencies, cluster settings, and schedule. Each job has its own job id.
* **Job Run (Execution):** An instantiation of that job definition when it is triggered (either manually or by schedule). Each run has its own **Run ID**, logs, and status.

## Use case
Develop a service that triggers and executes an analytics job either on specific events or through manual initiation. The service communicates with Dataworkbench and the analytics environment via APIs. The job performs operations such as reading datasets, aggregating data, and other analytical tasks.

## Create job definition
Jobs are defined within databricks. The job creator orchestrates tasks, dependecies, cluster settings.  Only Admin in workspace can create jobs.

Assign service principals as the “Run as” identity for the job. This ensures job execution does not depend on individual user accounts, preventing failures if a user leaves or loses permissions.  The run-as is by default set to job creator.

Create a service account in Data workbench (API management) and grant this account Admin access. When defining 'run-as' in databricks search for the account name.

[Configure and edit Lakeflow Jobs](https://docs.databricks.com/aws/en/jobs/configure-job)

## Job parameters
Job parameters allow you to make jobs more dynamic and reusable by passing values at runtime. Parameters are key-value pairs that you define in the job configuration.  The key is the name of the parameter defined during job-defintion and the value is defined when running a job.

The parameters can be referenced inside notebooks, scripts, or tasks to customize behavior without hardcoding values.


**Example**
Key: InputDataset  Value: (can have a default value)
Key: ResultDatasetName  Value:  (can have a default value)

Since the key/value pairs representing the job parameters does not contain a "description field", create a job tag with same key as the job parameter where value describes what this parameter is.

Key: InputDataset  Value: Name of operational dataset to be aggregated
Key: ResultDatasetName  Value:  Name of output dataset

**Best Practices**

* Use clear names and default values for parameters.
* Validate parameter values inside your code to avoid runtime errors.
* Combine with widgets in notebooks for interactive runs.
* Create a job tag, with same key as the job parameter where value describes what this parameter is.

For more documentation](https://docs.databricks.com/aws/en/jobs/parameters)

## List all jobs definitions 

From Databricks you can list all jobs available. When creating a job definition, the job is not autoamtically shared with all workspace users and others will not see it in the list of available jobs. However, the api-endpoint listing jobs will list all jobs (also the ones not shared).

To use the api, you need a token, see [Authentication](#authentication-and-authorization)


```
GET: https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceid}/jobs
```
Workspaceid is data workbench worksace id.

The response will be a list of all defined jobs in the databricks workspace related to the data workbench workspace.

```
[
{
        "jobId": 364946379282376,
        "jobName": "Assessment",
        "creatorUserName": "benedikte.harstad.kallak@dnv.com",
        "createdTime": "2025-12-15T08:35:52.282+00:00"
}
]
```

## Run a job

To run a job, the job can be started (invoked) from Databricks.

To run the job without entering Databricks, use the job id for the job defintion and use endpoint:

```
POST: https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/{workspaceid}/jobs/331283232308510/invoke
```

The body must containt the values for the defined job parameters. In the following example the job has defined two parameters: InputDataset and ResultDatasetName.
```
{
  "InputDataset": "turbinedata2023",
  "ResultDatasetName": "aggregateddata"
}
```
The notebook or script needs to know how to interpret the value.

The api will return run id

## Get status of a jon run
Use the run id and request status of the run

```
GET: https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/473ef07d-e914-4db4-959f-6eb737e391a6/runs/{runid}/status
```

## Cancel a run

```
GET: https://api.veracity.com/veracity/dw/gateway/api/v2/workspaces/473ef07d-e914-4db4-959f-6eb737e391a6/runs/{runid}/cancel
```

## Cluster
Jobs run on clusters, which can be:

* Job clusters: clusters created for the job and terminated after completion.
* All-purpose clusters: shared clusters used for interactive work and jobs.


## API endpoints
To browse the api, go [here](https://developer.veracity.com/docs/section/api-explorer/76904bcb-1aaf-4a2f-8512-3af36fdadb2f/developerportal/dataworkbenchv2-swagger.json).  **See section Analytics**

### Baseurl
See [overview of base urls](https://developer.veracity.com/docs/section/dataplatform/apiendpoints)

### Authentication and authorization
To authenticate and authorize your calls, get your API key and a bearer token [here](../auth.md).
