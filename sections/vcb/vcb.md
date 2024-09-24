---
author: Veracity
description: Overview of Veracity Copilot Builder
---

# Veracity Copilot Builder
<a href="https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/vcb/Veracity%20Copilot%20Builder%20documentation.pdf" download>
    <img src="assets/vcbbutton.png" alt="Veracity Copilot Builder documentation" height="40">
  </a>

  <br></br>

Veracity Copilot Builder (VCB) is a specialized toolkit that simplifies integrating chatbots (copilot projects) into applications within the Veracity ecosystem. It focuses on a code-first approach, enabling the creation of more advanced solutions compared to Microsoft Copilot Studio’s low-code/no-code solutions.

Note that you need to use .NET to write plugins and customize VCB. However, you can make chat bots that call applications made in other languages through API regardless of the language in which those apps were written.

Please note that VCB is restricted to use by internal projects and teams, and access is granted by contacting [support@veracity.com](mailto:support@veracity.com).

## Features
* **Easy Plugin Creation**: Build plugins (functions/tools) in .NET that seamlessly integrate with Veracity’s authorization system. These plugins can retrieve information or control functionalities within your application.
* **Knowledge Augmentation**: Enhance your copilot’s knowledge by uploading relevant documents to a shared database. You can control access to these documents, making them private to your copilot project or public for knowledge sharing across Veracity copilot projects.
* **Code Interpreter**: Lets the Large Language Model (LLM) execute code when necessary. This is particularly useful for requests involving math calculations or generating creative text formats based on data. 
* **Usage Tracking**: Monitor copilot usage to identify potential abuse and gain insights. Track usage and rate limit per user to prevent a single user from consuming excessive resources.
* **Nested Agent Hierarchy**: Organize your copilot’s functionalities using a hierarchical structure. This is helpful when your copilot has many plugins, as it avoids context window limitations. You can also share your agent as a NuGet package for others to integrate into their applications.

## Benefits for users
* **Reduced Complexity**: Simplifies the process of integrating chatbots into applications.
* **Advanced Solutions**: Enables the creation of more powerful and versatile chatbots compared to low-code/no-code solutions.
* **Enhanced Functionality**: Allows code execution for complex tasks and creative text generation.
* **Better Resource Management**: Enables usage tracking to identify potential abuse and optimize resource allocation.
* **Modular Design**: Supports a hierarchical agent structure for better organization and reusability.

## Documentation
<a href="https://veracitycdnprod.blob.core.windows.net/developer/veracitystatic/vcb/Veracity%20Copilot%20Builder%20documentation.pdf" download>
    <img src="assets/vcbbutton.png" alt="Veracity Copilot Builder documentation" height="40">
  </a>
