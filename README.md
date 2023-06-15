# Azure Functions

To get started with Azure, create a free trail account here: https://azure.microsoft.com/en-us/free/?cdn=disable

### Prerequisites
```text
Python 3.8.17
NodeJS v20.2.0
Serverless framework: npm install -g serverless
Azure CLI: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
```

## Azure set-up
Login into azure
```
az login
```

Get Trail subscription Id from account list
```
az account list
```

Replace with subscription id
```
az account set -s [Subscription ID]
```

Create role and permission
```
az ad sp create-for-rbac
az role assignment create --assignee [App id from previous step] --role Contributor
```

## Set-up
Install the project requirements:
```shell
npm install
```
```shell
pip install -r requirements.txt
```
```shell
sls offline build
```

To run a local version of the Azure Function to test with, use:
```shell
sls offline
```
You can try sending a POST request to the given endpoint with postman with a body like:
```json
{
	"name": "Copaco"
}
```
To deploy the function to your Azure account use:
```shell
sls deploy
```


Refer to [Serverless docs](https://serverless.com/framework/docs/providers/azure/guide/intro/) for more information.
