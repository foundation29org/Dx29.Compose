<div style="margin-bottom: 1%; padding-bottom: 2%;">
	<img align="right" width="100px" src="https://dx29.ai/assets/img/logo-Dx29.png">
</div>

Dx29 Docker Compose
==============================================================================================================================================
[![MIT license](https://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)

### **Overview**

The Dx29.Compose project includes two functionalities:
>1. Obtain the **images** of an environment from the Dx29 application. To do this you must have permissions in Azure in subscription where the environment is deployed. It is in the PullImages folder of the project and is programmed in Python. With its execution, the latest versions of the images of a environment are downloaded locally (with a few code modifications, changing the endpoints, it can be quickly adapted to download those of another environment).
>2. This project also includes the **DockerCompose** file. Once the images are downloaded, this can be used to build the local container with the Docker images and ports that Foundation29 developers work with.

This project therefore accesses the Azure container registry of a selected environment. 

It is used in the [Dx29 application](https://dx29.ai/) and therefore how to integrate it is described in the [Dx29 architecture guide](https://dx29-v2.readthedocs.io/en/latest/index.html).

<p>&nbsp;</p>

### **Getting Started**

####  1. Configuration: Pre-requisites

This project doesn’t need any dependency but it download and mount each needed image (microservice) for the execution of [Dx29 application](https://dx29.ai/). Therefore, in order to run it, the file appsettings.secrets.json must be added to the secrets folder with the following information:

|  Key                 | Value               |		                                                                                |
|----------------------|---------------------|--------------------------------------------------------------------------------------|
| Application          | Host                |URL of the application                                                                |
| ConnectionStrings    | IdentityConnection  |SQL database endpoint and credentials                                                 |
| ConnectionStrings    | BlobStorage         |Blob endpoint and credentials                                                         |
| ConnectionStrings    | OpenDataBlobStorage |OpenDx29 blob endpoint and credentials                                                |
| ServiceBus           | ConnectionString    |Connection string service bus                                                         |
| ServiceBus           | QueueName           |Queue configured name                                                                 |
| SignalR              | ConnectionString    |SignalR connection string & credentials                                               |
| SignalR              | HubName             |SignalR Hub HubName                                                                   |
| AppInsights          | Key                 |Secret key for connecting with AppInsights                                            |
| Account              | Key                 |Secret from SQL database (encrypt)                                                    |
| Account              | Inx                 |Secret from SQL database (encrypt)                                                    |
| Records              | Key                 |Secret from SQL database (encrypt)                                                    |
| Records              | Inx                 |Secret from SQL database (encrypt)                                                    |
| SendGrid             | APIKey              |Secret Key for connect SendGrid                                                       |
| CaseRecords          | AppName             |Appplication name                                                                     |
| CaseRecords          | DatabaseName        |Database Name where case records are saved                                            |
| CaseRecords          | ConnectionString    |Connection string to case records database                                            |
| MedicalCase          | AppName             |Appplication name                                                                     |
| MedicalCase          | DatabaseName        |Database Name where medical cases are saved                                           |
| MedicalCase          | ConnectionString    |Connection string to medical cases database                                           |
| ResourceGroups       | AppName             |Appplication name                                                                     |
| ResourceGroups       | DatabaseName        |Database Name where resource groups are saved                                         |
| ResourceGroups       | ConnectionString    |Connection string to resource groups database                                         |
| CognitiveServices    | Endpoint            |Endpoint Azure cognitive service configured                                           |
| CognitiveServices    | Authorization       |Authorization key                                                                     |
| CognitiveServices    | Region              |Azure cognitive service region configured                                             |
| TAHAnnotation        | Endpoint            |Endpoint Azure cognitive service configured  for Text Analytics                       |
| TAHAnnotation        | Path                |text/analytics/v3.1/entities/health/jobs                                              |
| TAHAnnotation        | Authorization       |Authorization key                                                                     |
| TAHAnnotation        | BlackList           |User ids in black list                                                                |
| IdentityServer       | Clients             |"Dx29.Web.UI": {"Profile": "IdentityServerSPA"}                                       |
| IdentityServer       | Key                 |"Key": {"Type": "File","FilePath": Path certificate,"Password": Password certificate} |


<p>&nbsp;</p>

####  2. Download and installation

Download the repository code with `git clone` or use download button.

We use [Visual Studio 2019](https://visualstudio.microsoft.com/downloads/) or [Visual Studio Code](https://code.visualstudio.com/download) for working with this project.
Having a [Python](https://www.python.org/downloads/) environment installed, for execute "PullImages/Scripts.py"

<p>&nbsp;</p>

### **Contribute**

Please refer to each project's style and contribution guidelines for submitting patches and additions. 

In general, we follow the "fork-and-pull" Git workflow.

>1. Fork the repo on GitHub
>2. Clone the project to your own machine
>3. Commit changes to your own branch
>4. Push your work back up to your fork
>5. Submit a Pull request so that we can review your changes

The project is licenced under the **(TODO: LICENCE & LINK & Brief explanation)**

<p>&nbsp;</p>
<p>&nbsp;</p>

<div style="border-top: 1px solid !important;
	padding-top: 1% !important;
    padding-right: 1% !important;
    padding-bottom: 0.1% !important;">
	<div align="right">
		<img width="150px" src="https://dx29.ai/assets/img/logo-foundation-twentynine-footer.png">
	</div>
	<div align="right" style="padding-top: 0.5% !important">
		<p align="right">	
			Copyright © 2020
			<a style="color:#009DA0" href="https://www.foundation29.org/" target="_blank"> Foundation29</a>
		</p>
	</div>
<div>

	
