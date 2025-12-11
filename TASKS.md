# Day 2: GitHub Integration and Branching

## Objective

Practice GitHub workflows, branching strategies, and project documentation.

---

## Prerequisites

Ensure you have completed all Day 1 tasks. Your repository should contain:
- `environment.txt` with your system information
- The `src/calculator/__init__.py` directory structure
- `notes.txt` and `notes_backup.txt`

---

## Tasks

### Task 1: Verify GitHub Connection

Confirm that your SSH connection to GitHub is working:
```bash
ssh -T git@github.com
```

Create a file called `github_verified.txt` containing the text "GitHub SSH connection verified" followed by today's date.

---

### Task 2: Create a Feature Branch

In this task, you will practice the feature branch workflow:

1. Create a new branch called `feature-add-operations` from the current branch
2. Switch to that branch
3. Create a file `src/calculator/operations.py` with the following structure:
   - A comment at the top describing the purpose of this file
   - A variable called `SUPPORTED_OPERATIONS` defined as a list containing: "add", "subtract", "multiply", "divide"

The command `git checkout -b` allows you to create and switch to a new branch in one step.

---

### Task 3: Commit on Feature Branch

Complete the following workflow:

1. Stage your new file
2. Commit with the message: "Add operations module with supported operations list"
3. Switch back to the `day2-github` branch
4. Merge your feature branch into `day2-github`

The command `git merge <branch-name>` integrates changes from the specified branch into your current branch.

---

### Task 4: Update Project README

Create a file called `src/calculator/README.md` to document your calculator project. Include the following sections:

- **Project Name**: Choose a name for your calculator
- **Description**: A brief explanation of what the calculator will do (1-2 sentences)
- **Planned Features**: List the four operations it will support
- **Author**: Your name

---

### Task 5: View Git History

1. Use `git log` to examine your commit history
2. Create a file called `git_log_output.txt` containing the output of `git log --oneline`

---

### Task 6: Final Commit

1. Stage all changes
2. Commit with the message: "Day 2: GitHub workflow complete"

---

## Verification Checklist

Before proceeding to Day 3, confirm the following:
- `github_verified.txt` exists
- `src/calculator/operations.py` exists and contains the `SUPPORTED_OPERATIONS` list
- `src/calculator/README.md` exists with all required sections
- `git_log_output.txt` exists
- A feature branch was created, committed to, and merged
- All changes have been committed to `day2-github`

---

## Completion

Once you have finished all tasks:

1. Push this branch:
   ```bash
   git push -u origin day2-github
   ```

2. Proceed to the next branch:
   ```bash
   git checkout day3-python
   ```

---

## Reference

The following commands may be useful for completing these tasks:

| Command | Purpose |
|---------|---------|
| `git checkout -b name` | Create and switch to a new branch |
| `git checkout name` | Switch to an existing branch |
| `git merge branch` | Merge a branch into the current branch |
| `git log` | View commit history |
| `git log --oneline` | View compact commit history |
| `git branch` | List all branches |
| `git branch -d name` | Delete a branch |
| `date` | Display current date |
