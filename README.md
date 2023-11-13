# Hello World Testing Python application
Sample App Python with Flask service to service communication and Monitoring with Prometheus

## Web App
This is a simple Flask web app that will return the string, you can see service-a in [here](https://github.com/andreeko28/kumparan-test/blob/main/service-a/app.py) and service-b in [here](https://github.com/andreeko28/kumparan-test/blob/main/service-b/service_b.py)

## Docker image
This is for the Image that will be built and used for deployment in Kubernetes, you can see for service-a in [here](https://github.com/andreeko28/kumparan-test/blob/main/service-a/Dockerfile) and service-b in [here](https://github.com/andreeko28/kumparan-test/blob/main/service-b/Dockerfile)

## Manifest Kubernetes
In this part of manifest that will be used to deploy the web app into Kubernetes, you can see for service-a in [here](https://github.com/andreeko28/kumparan-test/blob/main/service-a/deployment.yml) and service-b in [here](https://github.com/andreeko28/kumparan-test/blob/main/service-b/deployment.yml)

## Monitoring
This part is for monitoring with Prometheus using Helm Chart and specifying Prometheus configuration, you can see for Prometheus config in [here](https://github.com/andreeko28/kumparan-test/blob/main/prometheus-config.yaml)
and this is a command for running Prometheus using Helm Chart : 
- helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
- helm install prometheus prometheus-community/prometheus -f prometheus-config.yaml -n <namespace>
