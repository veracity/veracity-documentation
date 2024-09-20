---
author: Veracity
description: This is the changelog for the initial release of Veracity Copilot Builder.
---

# Initial release of Veracity Copilot Builder

Release date: 16 September 2024

We are thrilled to announce the initial release of Veracity Copilot Builder (VCB), a specialized toolkit designed to simplify the integration of chatbots (copilot projects) into applications within the Veracity ecosystem. This tool focuses on a code-first approach, enabling the creation of more advanced solutions compared to low-code/no-code alternatives.

Note that you need to use .NET to write plugins and customize VCB. However, you can make chat bots that call applications made in other languages through API regardless of the language in which those apps were written.

## New features
This section covers new features.

### Easy Plugin Creation
Build plugins (functions/tools) in that seamlessly integrate with Veracity Identity. Retrieve information or perform actions in your application, such as calling your API to update information through these plugins.

### Knowledge Augmentation
Enhance your copilot’s knowledge by uploading relevant documents to a shared database. Control access to these documents, making them private to your copilot project or public for knowledge sharing across Veracity copilot projects.

### Code Interpreter
Allows the Large Language Model (LLM) to execute code when necessary, for example, to extract insights from data, visualize data and create graphs, or perform math operations.

### Usage Tracking
Monitor copilot usage to identify potential abuse and gain insights. Track usage and rate limit per user to prevent a single user from consuming excessive resources.

### Nested Agent Hierarchy
Organize your copilot’s functionalities using a hierarchical structure. Avoid context window limitations by grouping plugins by agent responsibility. Share your agent as a NuGet package for others to integrate into their applications.

## Benefits for users
This section covers benefits for users.

* **Reduced Complexity**: Simplifies the process of integrating chatbots into applications.
* **Advanced Solutions**: Create more powerful and versatile chatbots compared to low-code/no-code solutions.
* **Enhanced Functionality**: Allows code execution for complex tasks and creative text generation.
* **Better Resource Management**: Enables usage tracking to identify potential abuse and optimize resource allocation.
* **Modular Design**: Supports a hierarchical agent structure for better organization and reusability.