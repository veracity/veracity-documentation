# Veracity for Developers Documentation
Welcome to the open source documentation for [Veracity for Developers](https://developer.veracity.com/docs). Here you will find all the source files for the documentation on Veracity for Developers.

## Making changes to the documentation
Everyone can propose changes to the Veracity documentation. [Learn how to make changes to the documentation here](./CONTRIBUTE.md)

## File structure
The documentation is organized into sections where each section can define not only which document should be contained within it, but also where it can be found. The root of the repository defines a set of known folders in which documentation can be placed:

Folder|Description
-|-
`common`|A folder containing legacy documentation. Future documentation should be placed in the `sections` folder under a relevant section.
`schemas`|A folder containing JSON schemas defining known json object such as the table of contents (`toc`).
`sections`|The root folder for documentation sections. This is where you should place all documentation.

## Sections
All documentation is grouped into sections. A section is a distinct set of documentation resources describing a service, topic or other logically groupable entity within Veracity. Within a section you can write documentation as markdown files, place assets that are used by said files and define a table-of-contents to describe what can be found within the section. These are the rules for a root folder within the `sections` folder (such as `identity`):

1. Must contain a single toc.json file matching the schema `toc.json` from the `schemas` folder.
2. Must contain 1 or more markdown files.
3. Can contain an `assets` folder (name must match exactly).
4. `assets` folder can contain 0 or more assets (images, videos, PDFs ++) that can be linked to from the markdown files.
5. All `assets` links must be relative to the markdown file location.

For sub folders all rules apply except number 1. A table of contents is only supported in the root of a section folder.
