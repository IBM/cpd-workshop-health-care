# Admin Guide

This section covers the setup and configuration of Cloud Pak for Data as a Service as well as supporting services necessary for the workshop. This involves the following steps:

1. [Create/Load Database(s)](#database-setup)
1. [Configure Database Connections](#database-connection-configuration)
1. [Configure Watson OpenScale](#watson-openscale-configuration)

## Database Setup

The workshop uses data stored in various data sources, these databases need to be installed / provisioned and setup prior to the workshop. This involves:

* Provisioning databases.
* Loading data.
* Gathering connection information.

Run through the instructions in the [Database Setup Readme](./database-setup.md)

## Database Connection Configuration

For Cloud Pak for Data to access the databases we setup above, we need to add *Data Connections* to connect to them via JDBC. (_Note: You must complete the *Database Setup* section before this section._)

* Adding global connection.

Run through the instructions in the [Database Connection Configuration Readme](./database-connection-configuration.md)

## Watson OpenScale Configuration

We setup the a sample model and content in Watson OpenScale. (_Note: You must complete the *Database Setup* section before this section._).

* Run fastpath configuration.

Run through the instructions in the [OpenScale Configuration Readme](./wos-configuration.md)
