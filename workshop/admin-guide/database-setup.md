# Admin Guide - Setup and Configure Data Sources

The workshop simulates the real world data connection process by having data reside on one or more data sources which are then added as connection in Cloud Pak for Data. This workshop is using databases as the data sources, loaded with content from a couple of CSV files. Before delivering the workshop, you will need to set up the databases and then load them with data that will be consumed by participants. 

Configure the databases we use in this workshop:

1. [DB2 Warehouse](#create-and-load-db2-warehouse-instance)
1. [DB2 Server](#create-db2-instance)

## Create and Load DB2 Warehouse Instance

You will be creating a DB2 Warehouse instance on IBM Cloud.

#### Provision and Connection Details

* Assuming you are logged in to an IBM Cloud account. Provision an instance of [DB2 Warehouse on IBM Cloud from the catalog.](https://cloud.ibm.com/catalog/services/db2-warehouse).

* Once the service is provisioned, Go to `Service Credentials` and click `New credential +`. Open `View credentials` and copy the credentials (this is your connection details) for use later.

   ![Get DB2 Warehouse credentials](../workshop/.gitbook/assets/images/connections/db2whoc-credentials.png)

#### Load Data

* Now go to `Manage` and click `Open Console`:

   ![DB2 Warehouse Cloud open console](../workshop/.gitbook/assets/images/connections/db2whoc-manage-console.png)

* From the upper-left (☰) hamburger menu click `Load` -> `Load data`:

   ![DB2 Warehouse Cloud load data](../workshop/.gitbook/assets/images/connections/db2whoc-load-data.png)

* Choose `Browse file` and navigate to where you cloned this repository, then to `data/` and choose `medications.csv`, then click `Next`.

* Click `+ New Schema` and name it `CP4DHEALTH`.

* With the new schema selected, click `+ New table`. Under "New Table Name" type "MEDICATIONS" and click `Create`, then `Next`. Accept the defaults and click `Next`. Click `Begin Load`.

* Repeat the data load steps for the `patients.csv` file, naming the table `PATIENTS`.

* Repeat the data load steps for the `conditions.csv` file, naming the table `CONDITIONS`.

#### Get SSL Certificate

* You will need an SSL certificate for Cloud Pak for Data to use the IBM Cloud DB2 Warehouse instance.

* In the DB2 Warehouse console, from the upper-left (☰) hamburger menu click `Connection Info` -> `Connection Information`. Then click `Download SSL Certificate`:

   ![DB2 get SSL certificate](../workshop/.gitbook/assets/images/connections/db2whoc-get-ssl-cert.png)

* You'll need to convert the SSL certificate from `.crt` to a `.pem` file using [openssl](https://www.openssl.org/). Run the following command:

  ```bash
  openssl x509 -in DigiCertGlobalRootCA.crt -out DigiCertGlobalRootCA.pem -outform PEM -inform DER
  ```

* Save this file for later use.

## Create DB2 Instance

If you are running the OpenScale Lab, you will need a DB2 Server instance (DB2 Warehouse is not supported but there are other databases that can be used in place of DB2). 

* Assuming you are logged in to an IBM Cloud account. Provision an instance of [DB2 Server from the catalog.](https://cloud.ibm.com/catalog/services/db2).

* Once the service is provisioned, Go to `Service Credentials` and click `New credential +`. Open `View credentials` and copy the credentials for use later.

  ![Get DB2 Warehouse credentials](../workshop/.gitbook/assets/images/connections/db2-server-credential.png)

__THIS SECTION IS COMPLETE, GO BACK AND CONTINUE WITH THE [ADMIN GUIDE](./README.md)__
