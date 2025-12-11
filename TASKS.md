# Day 2: GitHub Integration & Branching

## 🎯 Goal
Practice GitHub workflows, branching strategies, and documentation.

---

## 📋 Prerequisites

Make sure you have completed Day 1 tasks. You should have:
- `environment.txt` with your system info
- `src/calculator/__init__.py` directory structure
- `notes.txt` and `notes_backup.txt`

---

## 📋 Tasks

### Task 1: Verify GitHub Connection

Confirm your SSH connection to GitHub works:
```bash
ssh -T git@github.com
```

Create a file called `github_verified.txt` containing the text "GitHub SSH connection verified" followed by today's date.

---

### Task 2: Create a Feature Branch

You will practice the feature branch workflow:

1. Create a new branch called `feature-add-operations` from the current branch
2. Switch to that branch
3. Create a file `src/calculator/operations.py` with the following content structure:
   - A comment at the top describing what this file will contain
   - Define a variable `SUPPORTED_OPERATIONS` that is a list containing: "add", "subtract", "multiply", "divide"

**Hint:** Use `git checkout -b` to create and switch to a new branch.

---

### Task 3: Commit on Feature Branch

1. Stage your new file
2. Commit with message: "Add operations module with supported operations list"
3. Switch back to `day2-github` branch
4. Merge your feature branch into `day2-github`

**Hint:** Use `git merge <branch-name>` to merge.

---

### Task 4: Update Project README

Create a file called `src/calculator/README.md` that documents your calculator project:

Include these sections:
- **Project Name**: Give your calculator a name
- **Description**: What will this calculator do? (1-2 sentences)
- **Planned Features**: List the four operations it will support
- **Author**: Your name

---

### Task 5: View Git History

1. Use `git log` to view your commit history
2. Create a file called `git_log_output.txt` containing the output of `git log --oneline` (just the short version)

---

### Task 6: Final Commit

1. Stage all changes
2. Commit with message: "Day 2: GitHub workflow complete"

---

## ✅ Verification Checklist

Before moving on:
- [ ] `github_verified.txt` exists
- [ ] `src/calculator/operations.py` exists with `SUPPORTED_OPERATIONS` list
- [ ] `src/calculator/README.md` exists with required sections
- [ ] `git_log_output.txt` exists
- [ ] Feature branch was created, committed to, and merged
- [ ] All changes committed to `day2-github`

---

## ✅ Completion

When all tasks are complete:
1. Push this branch:
   ```bash
   git push -u origin day2-github
   ```
2. Move to the next branch:
   ```bash
   git checkout day3-python
   ```

---

## 💡 Commands You Might Need

| Command | Purpose |
|---------|---------|
| `git checkout -b name` | Create and switch to new branch |
| `git checkout name` | Switch to existing branch |
| `git merge branch` | Merge branch into current branch |
| `git log` | View commit history |
| `git log --oneline` | View compact commit history |
| `git branch` | List all branches |
| `git branch -d name` | Delete a branch |
| `date` | Get current date |
