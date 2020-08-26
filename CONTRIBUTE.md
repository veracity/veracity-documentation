# Contribute to Veracity developer documentation
In this article, you will find a step-by-step guide on how to add documentation to the Veracity for Developers GitHub repository.

[*Step 1:* Cloning the documentation repository in GitHub](#user-content-step-1-cloning-the-documentation-repository-in-github)<br />
[*Step 2:* Creating and editing pages](#user-content-step-2-creating-and-editing-pages)

1. Creating a new section
2. Setting up a folder for images, downloads, and other assets
3. Create and edit a documentation page wih:
  a. Markdown
  b. Linking images
  c. From markdown to Veracity for Developers
4. Set up a table of contents

[*Step 3:* Publishing pages by creating a pull request](#user-content-step-3-publishing-pages-with-pull-requests)

## Step 1: Cloning the documentation repository in GitHub
All documentation happens trough the GitHub pages repository. You have to do some simple steps to actually be able to edit this repository. You will need a GitHub user and a code editor.

1.	Create a GitHub user at Github.com
2.	Download [GitHub Desktop](https://desktop.github.com/) and a code editor like [Atom](https://atom.io/) or [Visual Studio Code](https://code.visualstudio.com/)

GitHub Desktop allows you to clone a version of the documentation pages to your computer, to then later merge it with the original repository. You can use any code editor to write the documentation.

3.	Create a forked copy of the documentation folders to edit on your computer.

To edit the documentation you need to first create a forked copy of the project that you can work with locally on your computer.

- Visit https://github.com/veracity/veracity-documentation
- Click the green clone button and select "Open in desktop"

![Open in Desktop](/assets/openindesktop.png)

- GitHub desktop will open up and ask you where you would like to clone the project locally. When you have selected the wanted path, click on "Clone"

![Clone](/assets/clone.png)
![Cloning](/assets/cloning.png)

This repository, all the documentation folders and will then be copied to your selected path on your computer and will be represented as a repository on your GitHub user account.

- You are now ready to create new documentation pages. If you have installed Atom or another code editor, GitHub Desktop should show you an option to directly open the document there.

![Open project](/assets/openproject.png)


## Step 2: Creating and editing pages

Now that you have the document available on your computer locally you can start to add or edit the existing documentation.

### 1)	Creating a new section

To create a new section, you simply have to create a new folder inside the "sections" folder of the local clone of the repository. Locate the project on your computer. Name it with the topic that you want to publish on. The name of the folder has to be all lowercase letters. *Be aware that the name of the folder will be the name of the URL path in Veracity for Developers.*

![New section folder](/assets/newsectionfolder.png)

Each section folder will contain other folders and page-files, that will be parsed into the final documentation page. In the next step you will be guided on how to fill up your section with content by adding an asset folder and assets that you can use to link to your page documents.

### 2)	Setting up a folder for images, downloads, and other assets

In the section folder you have created, simply create a new folder called "assets".  We recommend you to upload images in png format, PDFs, and excel files into this folder.  Make sure that all files are named in lowercase letters.

Here is an example of an asset folder with images and other files:

![Example section](/assets/examplesection.png)

### 3)	Create and edit documentation pages with markdown

The easiest way to create pages is through using a code editor.

We recommend [Atom](https://atom.io/) and will show how you can use it through this editor.

Once you have Atom, or another code editor downloaded – open it to access the file structure of the forked project.

![Open project](/assets/openproject1.png)

In the folder sidebar in Atom, Locate the project and the section folder where you want to create your documentation page. In Atom you can right-click and select "New document" to add it to this folder.

![Open selection](/assets/rightclick.png)

![Name file](/assets/namefile.png)

When you do this be sure to name the folder with all lower case letters and with the extension .md making it a Markdown file.

Now you can start to edit your document that will become the new page you are setting up.

#### Markdown

The easiest way to start writing a document is to look at previously created documents to see the format that they are written in.

Here is an example of a very simple Markdown - .md document in Veracity for Developers:

![Markdown example](/assets/markdownexample.png)

Each of the Markdown documents starts with the author and a short description of the document. This part of the document will not be visible for readers of the document.

Each markdown document must have at least a Header 1 element starting with #.

Basic copy text is writing without any syntax, as shown in the example above.

Here are some other markdown elements you can use in the document.


*Headers*

`# This is an H1
## This is an H2
###### This is an H6`


*Bullet Points*

`* Red
* Green
* Blue`


*Numbered Lists*

`1. Bird
2. McHale
3. Parish`


*Emphasis*

`*bold*
_italics_`

*Links*

`[Visble copy](https://link.io/)`

*Images and downloadable files*

After having added your .png image files with the correct naming in the "Assets" folder of the project, you can now add it to the different sections in the document.

This can be done with the following syntax:

`![Image name](/assets/imagename.png)`

The same goes for downloadable files.

`<a href="assets/examplefile.xlsx" download>Name of file in Copy</a>`

If you want to learn more about how to add other elements to your document visit [Basic Syntax in Markdown](https://www.markdownguide.org/basic-syntax/).


Learn more about what format writing documents with this [Markdown Guide](https://www.markdownguide.org/).


#### Markdown to Veracity for Developers

After successfully merging your changes for the forked project, in Veracity for Developers, the markdown document will look like this:

![Markdown in Veracity for Developers](/assets/markdowninvd.png)

The right-hand table of contents will be created from subtitles (with the ## syntax) so that the use easily can navigate to these parts of the page without too much scrolling.

![Right table of contents](/assets/righttoc.png)

The left-hand table of contents will contain the table of contents for the entire section, and we will guide you through how to make this now.

### Setting up a table of contents

To make a table of contents, create a separate toc file in the section folder where you are working. You can do this the same way you created a file in your code editor. The file must be placed in the section where it belongs and have the name *toc.json*.

The easiest way to create a table of contents is just to copy it from another section, and then replace all the "text" and "href" elements with their respective page names and links.  You can add elements to the toc with the following code:
`{
    "text": "Name of link to be shown in TOC",
    "href": "markdowndocument.md"
  }`

You can see an example of a full table of contents here:

![Right table of contents](/assets/toc.png)

## Step 3: Publishing pages with pull requests

After you have added all documents and assets, and after linking them correctly, you are now ready to push the changes to GitHub.

Before you start a pull request, we would like you to contact us at <developer@veracity.com> so that we are aware of the changes you want to make.

*Please make sure to delete all .ds-store files that come with the cloning of the project before you start doing this process.*

Open GitHub desktop. Now you will be able to see the changes you have made to the entire clone of the repository, and how this matches with what you have on GitHub.

Review your changes, write a short description of the additions or changes you have done in the title field and select "Commit to master" on the bottom-left.

![Changes in GitHub Desktop](/assets/changesgithub.png)


You will now see a "Push to origin" button on the right. Click on this.

![Push to origin](/assets/pushtoorigin.png)

After doing this you can visit your repository page in GitHub and try to find the "Pull requests" tab at the top. After going to the pull-request page, click on the "New Pull Request button" on the right side.

![Pull Requests](/assets/pullrequests.png)

After clicking this button you will get another page where you can compare your changes. Make sure, before you click on "Create pull request", that you are merging your changes to the original "master" branch of the Veracity documentation. Here is an example

![Create Pull Requests](/assets/createpr.png)

After clicking "Create pull request" we will be automatically notified to approve it. Now there are just a couple of simple steps that need to be done on our end, and your new files and section should be visible on Veracity for Developers. We will contact you in case we need any changes in the repository.
