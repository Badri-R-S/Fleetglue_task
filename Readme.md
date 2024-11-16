# ROS2 - REST API 

This repository contains the source code that runs a REST API server, and uses it to communicate with the ROS2 nodes.
It has been used to communicate tasks and print acknowledgement. The entire application has been dockerized to deploy easier.
It includes:

- The ROS2 source code (`src/` directory)
- A `Dockerfile` to build the Docker image
- An `entrypoint.sh` script for initializing the ROS environment and running the nodes
- A Flask-based REST API server to interact with the ROS 2 system

## Prerequisites

Before proceeding, ensure you have the following installed:

1. [Docker](https://docs.docker.com/get-docker/) (Docker Desktop on Windows/Mac or Docker Engine on Linux)
2. (Optional) `git` for cloning the repository

---

## Repository Structure

```plaintext
.
├── Dockerfile             # Docker configuration to build the image
├── entrypoint.sh          # Script to initialize and launch the application
├── src/                   # Source code for ROS packages
│   ├── fg_task/           # ROS2 python package that contains scripts to run the application         
│   ├── custom_msgs/       # ROS@ C++ package that contains custom action and message  

```

## Steps to run the container.
- Clone the github repository using `git clone https://github.com/Badri-R-S/Fleetglue_task.git`
- cd into the cloned repository
- run `docker build -t $IMAGE_NAME $PATH_TO_DOCKER_FILE` to build docker image. Replace the PATH_To_DOCKER_FILE with the path to the Dockerfile in this repository and replace IMAGE_NAME with the name you want to give to the docker image.
- run  `docker run -it --rm $IMAGE_NAME` to run the docker image.
