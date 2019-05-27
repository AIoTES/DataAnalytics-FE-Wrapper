# Data analytics - feature selection - wrapper method

## Introduction
This repository contains the code for the development of the wrapper method of the activage analysis tools. 
In this documentation you will find information on how to build, launch and deploy the project.

## Architecture
The project provides an HTTP REST server with a single endpoint for the execution of the analysis method.
## Build and deployment

### Prerequisites:
- Install Docker

````
sudo apt-get install docker-ce
````
- Install Docker Compose

````
sudo curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
````

### Build

#### Build docker image
Assuming you are in the project root folder, the docker image of the methods can be built executing:

#### Select features - wrapper method
```bash
$ docker build -f docker/Dockerfile -t feature-selection-wrapper-method:develop .
```

### Deployment
The project rely on docker for development and production deployments. The following subsections explains in detail how to 
deploy the tool using docker technology and how to configure the tool with the required environmental variables or configuration files.

```bash
$ docker run -it -p 5000:8000 -e "ANALYTICS_SERVER=http://<ip:port or domain>" --name select_features-wrapper_method feature-selection-wrapper-method:develop
```

- **ANALYTICS_SERVER** → URL where methods to be wrapped can be found.  


## API Documentation

* [Wrapper method](src/controllers/README.md#wrapper-method)
