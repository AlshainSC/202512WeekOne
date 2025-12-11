# Day 4: Docker Fundamentals

## 🎯 Goal
Demonstrate understanding of Docker basics: running containers, inspecting them, and managing container lifecycle.

---

## 📋 Prerequisites

Make sure you have completed Days 1-3. You should have:
- All files from previous days
- Working calculator functions in `src/calculator/operations.py`
- `src/hello.py` and `src/test_operations.py`

---

## 📋 Tasks

### Task 1: Verify Docker Installation

1. Check that Docker is installed and running:
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

**Note:** Create the `docker/` directory first.

---

### Task 3: Explore Python Container

1. Run an interactive Python container:
   ```bash
   docker run -it python:3.11-slim python
   ```
2. Inside the container, run a simple calculation using your knowledge from Day 3
3. Exit the container
4. Create a file `docker/python_container_notes.txt` documenting:
   - The command you used to start the container
   - What you ran inside the container
   - How you exited

---

### Task 4: Run and Inspect Nginx

1. Run an nginx container in detached mode on port 8080:
   ```bash
   docker run -d -p 8080:80 --name my-nginx nginx
   ```
2. Verify it's running with `docker ps`
3. View the logs with `docker logs my-nginx`
4. Create a file `docker/nginx_exploration.txt` containing:
   - Output of `docker ps` (showing your nginx container)
   - First 10 lines of the nginx logs

---

### Task 5: Container Lifecycle

Practice the container lifecycle commands and document your experience:

1. Stop the nginx container
2. Start it again
3. Stop and remove it
4. Remove the nginx image

Create a file `docker/lifecycle_commands.txt` that lists each command you used and what it did.

---

### Task 6: Docker Concepts Documentation

Create a file `docker/DOCKER_NOTES.md` that explains in your own words:

1. **What is a container?** (2-3 sentences)
2. **What is an image?** (2-3 sentences)
3. **Difference between `docker run` and `docker start`**
4. **What does the `-d` flag do?**
5. **What does `-p 8080:80` mean?**

---

### Task 7: Commit Your Work

1. Stage all changes
2. Commit with message: "Day 4: Docker fundamentals complete"

---

## ✅ Verification Checklist

Before moving on:
- [ ] `docker_version.txt` exists
- [ ] `docker/hello_world_output.txt` exists
- [ ] `docker/python_container_notes.txt` exists
- [ ] `docker/nginx_exploration.txt` exists
- [ ] `docker/lifecycle_commands.txt` exists
- [ ] `docker/DOCKER_NOTES.md` exists with all 5 explanations
- [ ] All changes committed

---

## ✅ Completion

When all tasks are complete:
1. Push this branch:
   ```bash
   git push -u origin day4-docker
   ```
2. Move to the next branch:
   ```bash
   git checkout day5-final
   ```

---

## 💡 Docker Commands Reference

| Command | Purpose |
|---------|---------|
| `docker run image` | Create and start a container |
| `docker run -d` | Run in detached (background) mode |
| `docker run -it` | Run interactively with terminal |
| `docker run -p host:container` | Map ports |
| `docker run --name name` | Give container a name |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker logs name` | View container logs |
| `docker stop name` | Stop a container |
| `docker start name` | Start a stopped container |
| `docker rm name` | Remove a container |
| `docker rmi image` | Remove an image |
| `docker images` | List images |

---

## 🏆 Extra Credit

Create a `Dockerfile` in the root of the project that:
- Uses `python:3.11-slim` as base image
- Copies the `src/` directory into the container
- Sets the working directory
- Runs `python test_operations.py` as the default command

This is optional but great practice!
