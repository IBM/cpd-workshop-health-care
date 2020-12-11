# Pre-work

This section is broken up into the following steps:

1. [Download or Clone the Repository](#1-download-or-clone-the-repository)
1. [Create an Analytics Project and Deployment Space](#2-create-a-project-and-deployment-space)

## 1. Download or Clone the Repository

Various parts of this workshop will require the attendee to upload files or run scripts that we've stored in the repository. So let's get that done early on, you'll need [`git`](https://git-scm.com) on your laptop to clone the repository directly, or access to [GitHub.com](https://github.com/) to download the zip file.

* To Download, go to the [GitHub repo for this workshop](https://github.com/IBM/cpd-workshop-health-care) and download the archived version of the workshop and extract it on your laptop.

![download workshop zip](../.gitbook/assets/images/pre-work/cpd-git-zip-download.png)

* Once Downloaded, you will need to unzip to extract the files in the repository.

* Alternately, run the following command:

```bash
git clone https://github.com/IBM/cpd-workshop-health-care
cd cpd-workshop-health-care
```

## 2. Create a Project and Deployment Space

At this point of the workshop we will be using Cloud Pak for Data for the remaining steps.

### Log into Cloud Pak for Data

Launch a browser and navigate to your Cloud Pak for Data deployment

> **NOTE:** Your instructor will provide a URL and credentials to log into Cloud Pak for Data!

![Cloud Pak for Data login](../.gitbook/assets/images/pre-work/cpd-login.png)

### Create a New project

In Cloud Pak for Data, we use the concept of a project to collect / organize the resources used to achieve a particular goal (resources to build a solution to a problem). Your project resources can include data, collaborators, and analytic assets like notebooks and models, etc.

* Go the (☰) menu and click *Projects* -> *All projects*.

![(☰) Menu -> Projects -> All projects](../.gitbook/assets/images/pre-work/cpd-projects-menu.png)

* Click on *New project +*.

![Start a new project](../.gitbook/assets/images/pre-work/cpd-new-project.png)

* Select *Analytics project* for the project type and click on *Next*.

![Select project type](../.gitbook/assets/images/pre-work/cpd-project-type.png)

* We are going to create a project from an existing file (which contains assets we will use throughout this workshop), as opposed to creating an empty project. Select the _*Create a project from a file*_ option.

![Create project from file](../.gitbook/assets/images/pre-work/cpd-create-project-from-sample.png)

* Navigate to where you cloned this repository, then to `projects/` and choose `HealthCareProject.zip`. Give the project a name and click `Create`.

![Browse for project files](../.gitbook/assets/images/pre-work/cpd-import-project.png)

* After succesful creation, click on *View new project*. You will see the new project with the imported assets.

![Import project success](../.gitbook/assets/images/pre-work/cpd-import-project-success.png)

### Create a Deployment Space

Cloud Pak for Data uses the concept of `Deployment Spaces` to configure and manage the deployment of a set of related deployable assets. These assets can be data files, machine learning models, etc.

* Go the (☰) menu and click `Deployments`.

![(☰) Menu -> Deployments](../.gitbook/assets/images/pre-work/cpd-choose-deployments.png)

* Click on `New deployment space +`.

![Add New deployment space](../.gitbook/assets/images/pre-work/cpd-add-new-deployment-space.png)

* Select the _*Create an empty space*_ option.

![Create empty deployment space](../.gitbook/assets/images/pre-work/cpd-create-empty-deployment-space.png)

* Give your deployment space a unique name, optional description, then click `Create`. You will use this space later when you deploy a machine learning model.

![Create deployment space](../.gitbook/assets/images/pre-work/cpd-create-deployment-space.png)

* Next, we will add a collaborator to the new deployment space, so that assets we deploy can be monitored in the OpenScale model monitoring lab.

* Click on the `Access control` tab and then click on `Add collaborators +` on the right.

![Deployment space access control](../.gitbook/assets/images/pre-work/cpd-deployment-space-access-control.png)

* Search for the *Admin* user, and then click on the `Admin` choice when it comes up. Click `Add to list +` and then the `Add` button.

![Deployment space access search Admin](../.gitbook/assets/images/pre-work/cpd-access-search-admin.png)

* The *Admin* user will show up under *Collaborators*.

![Deployment space Admin successfully added](../.gitbook/assets/images/pre-work/cpd-collaborator-added.png)

# Summary

In this pre-work module we have imported the projet for the worshop and created a Deployment Space. We can now move on to the next module.
