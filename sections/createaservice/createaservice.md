---
author: Veracity
description: Introduction to how to create a service in Veracity.
---

# Create a digital service in Veracity

Digital Services in Veracity come in many different flavors. You may choose to use a few or a wide range of platform capabilities in your service. Independently of what platform services you want to take advantage of, there are a few mandatory steps to create a service.


## What is a project

All services in Veracity needs to be part of a project in the Provider Hub. You can find your projects located on the menu bar in developer.veracity.com. Resources like application credentials used for Veracity Identity can be provisioned self-service from here.

A project in Veracity Provider Hub is what holds all resources related to your product. Resources are organized in resource groups. You can add collaborators into a project, and assign access rights to these collaborators. You would typically have one project for every product. E.g. the DNV product DNV Oil and Gas Standards and Recommended Practices, would usually have one project called DNV Oil and Gas Standards and Recommended Practices.

Inside a project, you can create a resource. A resource can be application credentials for using Veracity Identity in your service or any other platform capabilities. You can think of a project as a resource group, with some user management.


## What are resources and resource groups?

A resource is any platform capability that needs provisioning for your project to use it. An example of a resource is Application credentials, which is used to register your application toward the Veracity Identity Provider so that you can log in with Veracity.

Some of the resources you can provision self-service, as a part of a project by default, and some are configured by Veracity Onboarding before your product is released to production on Veracity. An example of this is Marketplace, which is provisioned by Veracity Onboarding and will be done in close collaboration with you.

A resource group is used to collect a set of resources. Currently the resource group will be labeled with environments, such as “devtest”, “test”, “staging or “production”.

<figure>
	<img src="step-by-step-guide/assets/ProjectStructure.png" alt="Example of a project structure"/>
	<figcaption>Example of a project structure</figcaption>
</figure>

## Next steps

[Sign up ](https://developer.veracity.com/)for a profile to create a Project, resource group and application credentials.

Check out our [documentation](https://developer.veracity.com/docs) to understand how to integrate use our platform services.
You can create your service from scratch using any language you want.
