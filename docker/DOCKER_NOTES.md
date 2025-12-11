# Docker Concepts

## What is a container?

A container is a lightweight, standalone, executable package that includes everything needed to run a piece of software. Containers isolate applications from each other and from the underlying system, ensuring consistent behavior across different environments. They share the host operating system's kernel, making them more efficient than traditional virtual machines.

## What is an image?

An image is a read-only template used to create containers. It contains the application code, runtime, libraries, and dependencies needed to run the application. Images are built in layers, where each layer represents a set of changes, making them efficient to store and transfer.

## Difference between `docker run` and `docker start`

`docker run` creates a new container from an image and starts it. It is used when you want to create a fresh container instance. `docker start` is used to start an existing container that was previously stopped. The container retains its state and configuration from when it was created.

## What does the `-d` flag do?

The `-d` flag runs the container in detached mode, meaning it runs in the background. Without this flag, the container runs in the foreground and occupies the terminal. Detached mode is useful for long-running services like web servers.

## What does `-p 8080:80` mean?

This flag maps port 8080 on the host machine to port 80 inside the container. The format is `host_port:container_port`. This allows you to access services running inside the container through the host's network interface.
