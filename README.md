# NMvW4DataScience
PIpeline to dump the SQL dataset frfom the NMvW's servers (not public), transorm it into a unified CSV dataset representation and clean and process it for data science. The outcome of this pipeline is also used by the bias exploration tool's backend.




## Overview

The NMvW's digital collection managers have created SQL dumps of their databases on a Microsoft Azure.  For use within our own project, we have created scripts to download, reorganise and clean the tables that make up the NMvW's digital collection into a CSV representation fit for data science and machine learning applications.  
Since the collection itself is not private and data protection restrictions apply, we cannot publish the CSV data set itself. Instead, if given permission by the NMvW (i.e. a username and password to connect to the Azure server), our scripts enable users to create the data set by yourself in just a few lines of code. Publishing this way has the added benefit of allowing users to choose certain parameters (such as subsets, filters and join operations) in the creation of the dataset

## Contents

We have created a Python package that contains the following functions:

 - establish a connection to the Azure Server
 - list, inspect and dump the SQL tables available on the server (including options for specifying specific columns and numbers of rows to be downloaded)
 - joining the SQL tables containing different aspects of information about objects into one table
 - cleaning and filtering based on a variety of aspects and levels of aggressiveness
 - saving and parsing the collection to and from CSV representation
 - basic descriptive statistics
 - basics for machine learning, such as n-gram modelling and vectorisation 

 
## Installation Instructions

0. Preliminaries

 - unzip src.zip 
 
 - this package uses the `pip` package manager for Python (non-`pip` based solutions may exist)
 - tested and developed on a Linux environment (Manjaro 21.2.5)

 - the Microsoft Azure server is configured to block any requests UNLESS the IP address is whitelisted;  
   please make sure that your current IP address has been whitelisted;  
   to test this, you can run: {TODO}

#### 1. Install Required Programs

_for Arch Linux:_
 - (optional) `tqsl`: establishes connections between a Linux system and a Microsoft SQL Server)  
   -> only needed to check connections and manually list tables on the server
 - `unixodbc`
 - `msodbcsql` from https://aur.archlinux.org/packages/msodbcsql/
 - `pyodbc` with `pip`

_required Python packages_:

installable via `pip`
 - `pyodbc`(see [installation manual](https://github.com/mkleehammer/pyodbc/wiki/Install) for OS-specific
   pre-requisites
 - `tqdm`
 - `numpy`
 - `pandas`
 - (optional: `matplotlib` & `seaborn`)

#### 2. Install Package

 - `git clone https://github.com/valevo/NMvW4DataScience/`
 - `cd NMvW4DataScience`
 - `pip install .`

 - `pip uninstall NMvW4DataScience`
 - `scikit-learn`

