# Day 1: Environment Setup

## Objective

Validate your development environment and demonstrate basic proficiency with Git and Linux commands.

---

## Tasks

### Task 1: Create Environment Info File

Create a file called `environment.txt` in the root of this repository containing the following information:
- Your operating system name
- Your Git version (the output of `git --version`)
- Your current username

You should use Linux commands to gather this information and redirect the output to a file.

---

### Task 2: Create Project Structure

Using only the command line, create the following directory structure:

```
src/
  calculator/
    __init__.py
```

The `__init__.py` file should be empty for now. Consider which flags you need for `mkdir` to create nested directories, and how `touch` can create empty files.

---

### Task 3: Practice File Operations

Complete the following sequence of operations:

1. Create a file called `notes.txt` containing the text "Day 1 started"
2. Copy `notes.txt` to a new file called `notes_backup.txt`
3. Append the text "Environment validated" to `notes.txt` (the original file should now contain 2 lines)

You will need to use `echo`, `cp`, and the append operator `>>` to complete this task.

---

### Task 4: Git Fundamentals

Perform the following Git operations:

1. Check the status of your repository
2. Add all new files to the staging area
3. Create a commit with the message: "Day 1: Environment setup complete"

---

### Task 5: Verify Your Work

Before proceeding to Day 2, confirm the following:
- `environment.txt` exists and contains your system information
- `src/calculator/__init__.py` exists
- `notes.txt` exists and contains 2 lines
- `notes_backup.txt` exists and contains 1 line
- All changes have been committed

---

## Completion

Once you have finished all tasks:

1. Push this branch to your repository:
   ```bash
   git push -u origin day1-environment
   ```

2. Proceed to the next branch:
   ```bash
   git checkout day2-github
   ```

---

## Reference

The following commands may be useful for completing these tasks:

| Command | Purpose |
|---------|---------|
| `uname -s` | Display operating system name |
| `git --version` | Display Git version |
| `whoami` | Display current username |
| `mkdir -p` | Create nested directories |
| `touch` | Create an empty file |
| `echo "text" > file` | Write text to a file (overwrites) |
| `echo "text" >> file` | Append text to a file |
| `cp source dest` | Copy a file |
| `git status` | Display repository status |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Create a commit with a message |
