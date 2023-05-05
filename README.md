# jaeger
Jaeger setup

1. You have an existing Azure Subscription, if not create one.
2. Install Azure CLI if not already installed using the below documentation.
    [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
3. Open your command prompt or terminal and login to your Azure account by running the following command:
```bash
az login
```
4. Create a resource group where all the resources will be grouped.
```bash
az group create --name <resource-group-name> --location <location>
```
5. Create an AKS cluster (preferably with v1.25.5) by running the following command:
```bash
az aks create --resource-group <resource-group-name> --name <cluster-name> --node-count <node-count> --kubernetes-version 1.25.5 --generate-ssh-keys
```
6. Once the AKS cluster is created, you can connect to it by running the following command:
```bash
az aks get-credentials --resource-group <resource-group-name> --name <cluster-name>
```

7. Clone the repository to your local machine
8. Navigate to the project directory
9. Create the Deployment using kubectl apply:
-------
    kubectl apply -f jaeger-deployment.yaml
    
10. Create the Service using kubectl apply:
-------
    kubectl apply -f jaeger-service.yaml
    
11. Now Goto Loadbalancer and check whether service comes Inservice or not, If it comes Inservice copy DNS Name of Loadbalancer and check in web UI:
-------
    kubectl get svc
    
12. After that we will get similar dashboard:
![Screenshot from 2023-05-05 19-28-42](https://user-images.githubusercontent.com/109966978/236481208-4958dbe9-6a96-4ca1-b944-3ca6bc3f995e.png)

