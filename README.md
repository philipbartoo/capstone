# Project Overview

**Problem**: FEMA Mitigation personnel do not have a single knowledge management solution for managing $1.6 Billion in grants which is resulting in delays closing out projects.  Coordination is taking place via email and spreadsheets without a single source of truth. Managers cannot determine the exact status of a project without heavy email coordination.

**Proposal**: This app integrates data from FEMA grant application systems with locally collected information to easily track the workflow status of each grant funded project.

# Functionality

The user experience will begin with a login screen from which they access the application. Each user will require a username, password and email.  A registration page will be provided if they do not have credentials.  This information will update a user database.

Upon login, the user will be transported to the main page. The main page will provide the user with a 1/4 width side navigation bar that will include a cascading dropdown navigation filter on the left, and a 3/4 width detail section on the right which will display a list of Disasters.  Each disaster will be linked to a Disasters detail page.  The cascading dropdown will be linked to a Disaster database and a Project database. The information displayed on the right will come from the Disaster database.

When a user selects a disaster (linked), they will be taken to a Disaster Details page which displays disaster information on the left 2/3rds of the page and includes a list of associated Projects on the right 1/3rd of the page.  Each Project name will be linked to a Projects Detail page.

When a user selects a Project, they are taken to the Project Details page which will include static information on the project and enrichment data which tracks workflow progress.  Workflows are stages a Project must pass through prior to being closed out.  An indicator will be provided on the Project Details page which identifies which stage the project is at for quick reference. It is expected that this is where most users will spend their time, updating enrichment data on each project.

An administration page will also be included that will feature a button to import .csv file data into the Disaster and Project databases.  

The following constitutes the minimum viable product requirements:
* Four databases: User, Disaster, Project, and Enrichment created in Django
* Pages to search Disasters, drill down to Projects and the ability to enter data in associated Enrichment fields
* User Login and Registration
* Disaster and Project information import via user button that will complete a a full outer join of  the .csv files.  This button will utilize JavaScript
* Cascading dropdown filter. To enable users to quickly filter to their project of interest a cascading dropdown filter will be provided on the main page.

# Data Model

The following databases will be used in the application:
1. Disaster database. This database tracks all declared disasters. This information is 			provided from headquarters daily and should not be edited by users.
2. Project database. This database lists all projects that are associated with a declared disaster
3. Enrichment database. This database provides amplifying information about project workflow and includes fields FEMA personnel will need to enter.
4. User database. The application needs to be secure and will require a login feature.

![models](/models.svg)

# Schedule

* By **1/21/2022**: Complete markdown and project plan
* By **1/28/2022**: Build initial App, Set up environment and Django, Import libraries, Construct Models, Construct URLs, Construct Login View and template
* By **2/4/2022**:  Build Disaster and Project List and Details, Build Disaster List view and template, Build Disaster Detail view and template, Build Project List view and template, Build Project Detail view and template
* By **2/11/2022**:  Build functions: .csv import feature, cascading dropdown feature, workflow status indicator 
* By **2/11/2022**: Complete project