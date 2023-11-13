# Hello World Testing Python application
Sample App Python with Flask service to service communication and Monitoring with Prometheus

## Web App
This is a simple flask web app that will return the string, you can se in [here](https://github.com/andreeko28/rukita-test/blob/main/app/app.py)

## Pipeline CI/CD
This app will build and deploy using this Azure DevOps pipeline with multibranch pipeline for each environment with conditional following/trigger from branch that trigger in repository, you can see the pipeline in [here](https://github.com/andreeko28/rukita-test/blob/main/pipelines.yml)

In this pipeline Define 2 Stage for Development from branch 'develop' and Production from branch 'main'
And in this pipeline is have seperate with different stage for each jobs have several step :
1. Build and Test the app
2. Build and Push container Image to registry with dynamic version image
3. Change tag environment
4. Deploy to Kubernetes

## Docker image
This is for the Image that will be build in pipeline and use for deploy in kubernetes, you can see in [here](https://github.com/andreeko28/rukita-test/blob/main/Dockerfile)

## Manifest Kubernetes
In this part for manifest that will be use for deploy the web app into Kubernetes, you can see in [here](https://github.com/andreeko28/rukita-test/blob/main/manifest/deployment.yml)