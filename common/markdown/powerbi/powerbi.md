# Overview

This tool is in Privat Preview. Contact Veracity Developers Toolbox team if you want details


Power BI is a self-service Business Intelligence tool which helps you to visualize and organize your data. Veracity has developed an integrated framework for Power BI, named Insight, which can be used to share the Power Bi reports and dashboards in a secure way to your customers. The tool also enable you to brand the application so that it follows with your own brand profile.

Power BI can be used to connect to a wide range of data sources, including but not limited to databases (SQL, Oracle, IBM, etc.), Azure and Files (Excel, CSV, XML, etc).



# Quick start
The quick start consists of three parts that will guide you through the necessary steps for you to complete before being able to have your nice reports available to your customers.  

### Part 1: Getting started with the Power BI desktop tool
1. Download the desktop tool by visiting the Power BI desktop site at Microsoft Power BI [here](http:\\www.powerbi.com). Microsoft releases a new version of Power BI Desktop every month. We encourage you to always have the latest version installed.  If you already have downloaded the power BI desktop, you can go irectly to section 2 [here](#Part-2:-How-to-request-the-Power-BI-insight-tool).

INSERT SCREENSHOT HERE

2. Click on 'Advanced download options'.

INSERT SCREENSHOT

3. Select language and click on 'Download'. To increase supportability, we recommend you to select English as a language.

INSERT SCREENSHOT

4. Check with your IT department to see if you have a 32 bit or 64 bit operating system. If you have the possibility to install Power BI in 64 bit, we strongly recommend this. Your download will start automatically when you have selected the file you wish to download.

INSERT SCREENSHOT

5. Follow the steps in the installation wizard: default settings should be sufficient. Click 'yes' when asked if the application can make changes on your hard drive. 
6. When the installation is completed, click 'finish' and if you keep the checkbox 'Launch Microsoft Power BI Desktop' checked, then Power BI desktop should start. You should now also have a desktop icon, a start menu item (Microsoft Power BI) and a taskbar icon.
7. Register a free account to start using Power BI. If your company has a Microsoft account, you may be able to use this as well.
8. On the first login, you may be asked to sign in and agree to the terms of use. Otherwise, the desktop tool should be ready at your disposal.
9. Please have a look at Microsoft Power BI guided learning to get started with how to use the tool.

You should now be able to start making reports and analysis your data with Power BI Desktop. Remember it's your responsibility to keep the Power BI Desktop up to date (Power BI releases a new version monthly). 

### Part 2: How to request the Power BI insight tool

The Power BI tool Insght is in Private Preview, but we are onboarding mature services at the moment. If you think you would fit into this category, contact the Veracity Developer Toolbox team for details.


### Part 3: How to use the Power BI publishing tool towards customers
You are now the owner and admin of your service in Veracity and will see your service as a tile under My Services. Now that you have created your first report you are ready to share it with your customer. Your customer(s) obtain access to your reports through your Power BI application page. When clicking on the tile you will land on the home page of your site:

INSERT SCREENSHOT

Navigate to the admin page where you will see four tiles: 

INSERT SCREENSHOT

To learn more about each item on this page, hover your mouse cursor over the ? icon and a tool tip will be displayed with more contextual information. The application is meant to give an intuitive user experience with several tool tips throughout. However, we recommend you read through the tutorial for the application the first time.


# Tutorial

## Architecture and principals 
The Insight application consist of both physical and logical level for the report files you upload. The application structure is described in the picture below.

INSERT ARCH PICTURE

Since the application differentiate between physical and logical report files, you can attach one logical report file to multiple projects and deliveries, and at one place replace the connection between the logical and physical report file at a later stage without the need to reconfigure any application. Another scenario is that you have one physical file connected to multiple logical files. At any time, you will then be able to reconfigure one of the logical files to point to a new physical file without affecting the other configured files. This is particularly beneficial when your product scale, and you want to create many tailor-made projects based on scalable reports. 


## Upload, configure and publish Power BI reports

**1. Manage Files**
a. Click on the first box named 'Manage Files'
b. Click 'upload file'.
c. Click 'browse' and select the power BI file you wish to upload.
d. Write in a name under 'Report name'.
e. If you do not use direct query, skip this step. If you use a database in your report you need to inform what the connection string is by checking the Connection string box and informing what the connection string is. This string is not stored in veracity but passed on to Power BI services to render the report. 
f. Click 'Save changes'.

INSERT PICTURE

e. You will now see your uploaded report file on the page.

*Return to the main page by clicking Admin in the upper left corner to go back to the main page.* 

**2. Manage Reports**
a. Click on the second box named 'Manage Reports'.
b. Click 'Create new report'.
c. Fill out title, menu name, description, PBI Filter Name, Filter Value and which Power BI file you wish to upload from the library.
d. Click 'add'.

INSERT SCREENSHOT

*Return to the main page by clicking Admin in the upper left corner to go back to the main page.*

**3. Manage Entities**
a. Click on the third box named 'Manage Entities'.
b. Click 'Add'.
c. Fill in Name , Type , 'Reports', Type Property Value Setting'. 
d. Click 'Add'. 

INSERT SCREENSHOT

*Return to the main page by clicking Admin in the upper left corner to go back to the main page.*

**4. Manage Users**
a. Click on the fourth box named 'Manage Users'. 
b. Click 'Add User' and a search box will appear.
c. Type in the name you wish to give access to and click 'Check Name'.
d. Now you have the option to choose which file you wish to grant access to and what type of roles they should have.
e. Click 'add'.

INSERT SCREENSHOT

### Training
Power BI has a lot to offer when it comes to analytics, and the best way to get started is with proper Power BI training. We recommend you to have a look at the tutorials Microsoft has created. It takes about 90 minutes to go through all of them and they can be found [here](https://powerbi.microsoft.com/en-us/guided-learning/).

### Data sources you can connect to
The Power BI embedded version in Azure only support refresh on Azure SQL database and Azure SQL Datawarehouse (directQuery). You can still connect to other data sources (those supported in Power BI) in Power BI Desktop, but be aware that you have to re-upload the file every time you want to refresh the data.


### Row level security
For Row Level Security to work you need to create a security role called "MyDNVGLUser" in Power BI Desktop. You also need the MYDNVGL ID which is a GUID to be able to use USERNAME()-It looks like this: 57a61395-4dc1-4ff1-ad04-2f14a1b9e6c5|16. 
GUID is a unique identifier in DNVGL and Veracity on an individual basis. If the person change company or email, he or she will still be able to use the same account. 
Contact Mona Olander for giving you access to the tool where you can get the MyDNVGL GUID's.
You can look up the GUID in the My DNV GL Admin tool: https://myadmin.dnvgl.com go to Users and look up the email address of the user. Click on the user. The GUID is the value in the Id field:

INSERT SCREENSHOTS

### Row limit 
Power BI uses a data limit rather than a row limit. Currently, the data limit is 1 GB for free users and 10 GB for users with a pro license. More information on how this works can be found at Microsoft.

### Where shall I store my report master files
Microsoft Power BI stores all reporting master files by default on your desktop computer. This is a vulnerable place to store these files, as your hard drive may crash or your file may get damaged, and then you don't have a backup. We therefore recommend to store your file on the file area (it's basically OneDrive for business) that comes with a Power BI app workspace. You can use 'check in/check out' to collaborate and have versioning on your PBIX files. If you get data from excel files, the file area will also update that once an hour automatically if you store it there instead of on your local machine.
Please be aware of security concerns! We recommend to use a place which has access restrictions to prevent people from getting unauthorized access to your reports. Power BI nowadays offers the possibility for report authors to download report files from published reports. Please be aware that this only applies to the published version, so if you were working on a newer version and it got lost, then you can still only get the last published version back.


# Legal
We recommend to check with your own legal department that you are operating within a legal framework before using Power BI with your customer s data.

# Terms
Before you start using this application you should consider two things

1. Understand and accept the Veracity Service Level Agreement. Make sure that our SLA does not make it difficult to meet the uptime you may be contractually bound to when you sell your service. 
2. Allocate a dedicated support person. Veracity service desk will need to have a contact point to assist in supporting the service.

# Pattern and practices
We have a set of best practices for report development. These consist of both development guidelines and visual guidelines

### Development guidelines
Insert text
### Visual guidelines/Design

#### Cart choice
Below you will find an overview of which charts are available and in which way they can best be used

INSERT SCREENSHOT

#### Report themes
With Report Themes, you can apply a color theme to your entire report, such as your companies corporate colors. Read the full guide on how to use report themes [here](https://powerbi.microsoft.com/en-us/documentation/powerbi-desktop-report-themes/).

#### Custom visuals
Microsoft offers a custom visual gallery in the Office Store. The user can easily download and use them in a report. There are some considerations a report developer should investigate before using or developing a custom visual as these are developed by third parties. Check-list and guidelines for using custom visuals from the Office Store.

*Using custom visuals from the Office Store:*

1. Is the data to be published in the visual sensitive in any way? If yes, custom visuals should be avoided as a rule since unless it is clarified with the Global Data Protection Officer and thorough code review should be performed before using the custom visual.
2. Is the publisher a trusted party? Check the publisher of the custom visual. We can assume that Microsoft published custom visuals are generally safe. Certified custom visuals are also considered safe. Which Custom visuals that are certified can be found here. For other publishers please review their privacy statement and webpage for validation.
3. Are you able to maintain and support the visual throughout the report lifetime? The custom visuals can update or stop working and the developer / report owner are responsible for updating and making the changes needed if a custom visual stop working.
4. Microsoft does not offer support or change handling to custom visuals as stated [here](https://powerbi.microsoft.com/en-us/visuals-gallery-terms/).
5. If the custom visual updates the report developer must update all your reports that uses this custom visual.
6. The report developer will be held responsible for any data protection issues when using custom visuals. The report developer is also responsible for licensing and correct use of the associated license with the custom visuals. Custom Visuals are third party software compared to Power BI.

*Using custom visuals published outside of the Office Store:*

1. Custom visuals available outside MS Visuals Gallery are potentially unsafe and should not be used.
2. If you want to investigate usage of a custom visuals make sure you do all necessary steps to evaluate that the publisher will not steal any of your data as stated [here](https://powerbi.microsoft.com/en-us/documentation/powerbi-custom-visuals-review-for-security-and-privacy/).
3. The report developer will be held responsible for any data protection issues when using custom visuals.
