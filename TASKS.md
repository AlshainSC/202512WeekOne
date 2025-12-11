# Day 4: Docker Fundamentals

## Objective

Demonstrate your understanding of Docker basics: running containers, inspecting them, and managing the container lifecycle.

---

## Prerequisites

Ensure you have completed Days 1 through 3. Your repository should contain:
- All files from previous days
- Working calculator functions in `src/calculator/operations.py`
- `src/hello.py` and `src/test_operations.py`

---

## Tasks

### Task 1: Verify Docker Installation

1. Confirm that Docker is installed and running:
   ```bash
   docker --version
   ```
2. Create a file called `docker_version.txt` containing the output

---

### Task 2: Run Hello World Container

1. Run the Docker hello-world container:
   ```bash
   docker run hello-world
   ```
2. Create a file called `docker/hello_world_output.txt` containing the output from this command

Note: You will need to create the `docker/` directory first.

---

### Task 3: Explore Python Container

1. Run an interactive Python container:
   ```bash
   docker run -it python:3.11-slim python
   ```
2. Inside the container, execute a simple calculation using your knowledge from Day 3
3. Exit the container
4. Create a file `docker/python_container_notes.txt` documenting:
   - The command you used to start the container
   - What you executed inside the container
   - How you exited the container

---

### Task 4: Run and Inspect Nginx

1. Run an nginx container in detached mode on port 8080:
   ```bash
   docker run -d -p 8080:80 --name my-nginx nginx
   ```
2. Verify it is running with `docker ps`
3. View the logs with `docker logs my-nginx`
4. Create a file `docker/nginx_exploration.txt` containing:
   - The output of `docker ps` showing your nginx container
   - The first 10 lines of the nginx logs

---

### Task 5: Container Lifecycle

Practice the container lifecycle commands and document your experience:

1. Stop the nginx container
2. Start it again
3. Stop and remove it
4. Remove the nginx image

Create a file `docker/lifecycle_commands.txt` listing each command you used and describing what it accomplished.

---

### Task 6: Docker Concepts Documentation

Create a file `docker/DOCKER_NOTES.md` explaining the following concepts in your own words:

1. **What is a container?** (2-3 sentences)
2. **What is an image?** (2-3 sentences)
3. **What is the difference between `docker run` and `docker start`?**
4. **What does the `-d` flag do?**
5. **What does `-p 8080:80` mean?**

---

### Task 7: Commit Your Work

1. Stage all changes
2. Commit with the message: "Day 4: Docker fundamentals complete"

---

## Verification Checklist

Before proceeding to Day 5, confirm the following:
- `docker_version.txt` exists
- `docker/hello_world_output.txt` exists
- `docker/python_container_notes.txt` exists
- `docker/nginx_exploration.txt` exists
- `docker/lifecycle_commands.txt` exists
- `docker/DOCKER_NOTES.md` exists with all five explanations
- All changes have been committed

---

## Completion

Once you have finished all tasks:

1. Push this branch:
   ```bash
   git push -u origin day4-docker
   ```

2. Proceed to the next branch:
   ```bash
   git checkout day5-final
   ```

---

## Reference

The following Docker commands may be useful for completing these tasks:

| Command | Purpose |
|---------|---------|
| `docker run image` | Create and start a container |
| `docker run -d` | Run in detached (background) mode |
| `docker run -it` | Run interactively with terminal access |
| `docker run -p host:container` | Map host port to container port |
| `docker run --name name` | Assign a name to the container |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker logs name` | View container logs |
| `docker stop name` | Stop a running container |
| `docker start name` | Start a stopped container |
| `docker rm name` | Remove a container |
| `docker rmi image` | Remove an image |
| `docker images` | List downloaded images |

---

## Extra Credit

Create a `Dockerfile` in the root of the project that:
- Uses `python:3.11-slim` as the base image
- Copies the `src/` directory into the container
- Sets the working directory appropriately
- Runs `python test_operations.py` as the default command

This task is optional but provides valuable practice with Docker image creation.
