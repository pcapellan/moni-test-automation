# Moni - Test Automation

This project is based on a technical automation test using Python and Selenium.
The project consists of the creation of 3 scenarios:
  - Creation of User Account
  - Login
  - Purchase process a product

## QA Framework Documentation
### Installing the Testing Framework
##### Setup your machine for running Python based applications
In order to setup your machine to run Python based applications, the following actions should be performed:

 * Enable PowerShell for executing remote commands

 * Install Python framework

 * Install Python pip

 * Install Python virtualenv

 * Add Python binaries to the "PATH" environment variable


### How to manually setup your machine

**In case you need to install all components manually, please execute the following tasks**

#### Install Python

Download and install Python 2.7 from https://www.python.org/download/
Add python dir (C:\Python27) and python scripts dir (c:\Python27\Scripts) to the PATH environment variable.

#### Install pip
Ensure python 2.7 was properly installed, then install pip using instructions from https://pip.pypa.io/en/latest/installing.html
```
python get-pip.py
```
#### Install virtualenv

```
pip install virtualenv
```

#### Create virtualenv
Run **./create_virtualenv.sh** to create a virtualenv environment in an env directory with the correct dependencies.


### Running the tests
To run the tests you must do it by running  **run_scenarios.py**
If you want to run specific scenarios you can do it using the respective Tags of each scenario