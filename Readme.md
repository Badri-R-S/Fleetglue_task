# ROS2 - REST API 

This repository contains the source code that runs a REST API server and uses it to communicate with the ROS2 nodes.
It has been used to communicate tasks and print acknowledgment. The entire application has been dockerized to deploy more easily.
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
├── Dockerfile                     # Docker configuration to build the image
├── entrypoint.sh                  # Script to initialize and launch the application
├── src/                           # Source code for ROS packages
│   ├── fg_task/                   # ROS2 python package that contains scripts to run the application
        ├── fg_task/
            ├── app.py             # Script to host the API server
            ├── task_publisher.py  # Script to get task and send a POST request to the endpoint in the server
            ├── rn1.py             # Client script to send a GET request to the server to retrieve the task and send it to the Action Server.
            ├── rn2.py             # Action Server script that accepts the task and prints it.           
│   ├── custom_msgs/               # ROS2 C++ package that contains custom action and message
        ├── action/
            ├── Task.action        # Custom action
        ├── msg/
            ├── Task.msg           # Custom message  
```

## Steps to run the container.
- Clone the github repository using `git clone https://github.com/Badri-R-S/Fleetglue_task.git`
- If using Windows, text files might have CRLF  line endings instead of LF. This can cause the script to be unrecognized inside the container (especially if the container runs a Linux-based OS). Convert the line endings of entrypoint.sh to LF before building the Docker image. This can be done by changing the line ending option in the bottom-right corner of vs code.
- cd into the cloned repository
- run `docker build -t $IMAGE_NAME $PATH_TO_DOCKER_FILE` to build docker image. Replace the PATH_TO_DOCKER_FILE with the path to the Dockerfile in this repository and replace IMAGE_NAME with the name you want to give to the docker image.
- run  `docker run -p 5000:5000 -it --rm $IMAGE_NAME` to run the docker image.

## Result
Please refer to this link to view a video of the result, when running this docker image: [Result](https://drive.google.com/file/d/1uNYPyOWoAyobI_RcExVaUeY6i8kz_sAH/view?usp=sharing)
