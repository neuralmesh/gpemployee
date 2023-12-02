# Running the gpemployee Docker Container

This document provides instructions on how to build and run the Docker container for the gpemployee project.

## justrun.sh

```bash
bash ./scripts/justrun.sh
```

## Prerequisites

Before proceeding, ensure you have Docker installed on your machine. If Docker is not installed, please follow the [official Docker installation guide](https://docs.docker.com/get-docker/).

## Building the Docker Image

1. **Open a Terminal**: Navigate to your terminal or command prompt.

2. **Navigate to the Project Directory**: Change to the directory where your gpemployee project is located.
    ```bash
    cd path/to/gpemployee
    ```

3. **Build the Docker Image**: Use the Docker CLI to build the image. This process reads the `Dockerfile` in the `docker` directory and constructs the Docker image.
    ```bash
    docker build -t gpemployee -f docker/Dockerfile .
    ```
    This command builds the Docker image with the tag `gpemployee`.

## Running the Docker Container

Once the image is built, you can run it as a container.

1. **Run the Container**: Execute the following command to start the container. This command maps the container's port 8000 to port 8000 on your host machine.
    ```bash
    docker run -p 8000:8000 gpemployee
    ```

2. **Verify the Application is Running**: Open your web browser and navigate to `http://localhost:8000`. You should see the gpemployee application's greeting message.

## Stopping the Container

To stop the running Docker container:

1. **Find the Container ID**: Open another terminal window and list all running containers.
    ```bash
    docker ps
    ```

2. **Stop the Container**: Use the container ID obtained from the previous step to stop the container.
    ```bash
    docker stop [CONTAINER_ID]
    ```

## Conclusion

Following these steps, you should be able to build and run the Docker container for the gpemployee project successfully. This setup enables a consistent and isolated environment for development and testing.

