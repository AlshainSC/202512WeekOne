# Day 1: Environment Setup

## 🎯 Goal
Validate your development environment and demonstrate basic Git and Linux proficiency.

---

## 📋 Tasks

### Task 1: Create Environment Info File

Create a file called `environment.txt` in the root of this repository that contains:
- Your operating system name
- Your Git version (output of `git --version`)
- Your current username

**Hint:** You can use Linux commands to gather this information and redirect output to a file.

---

### Task 2: Create Project Structure

Using **only the command line**, create the following folder structure:

```
src/
  calculator/
    __init__.py
```

The `__init__.py` file should be empty for now.

**Hint:** Use `mkdir` with appropriate flags and `touch` to create empty files.

---

### Task 3: Practice File Operations

1. Create a file called `notes.txt` with the text "Day 1 started"
2. Copy `notes.txt` to `notes_backup.txt`
3. Append the text "Environment validated" to `notes.txt` (original file should now have 2 lines)

**Hint:** Use `echo`, `cp`, and the append operator `>>`.

---

### Task 4: Git Fundamentals

1. Check the status of your repository
2. Add all new files to staging
3. Create a commit with the message: "Day 1: Environment setup complete"

---

### Task 5: Verify Your Work

Before moving on, make sure:
- [ ] `environment.txt` exists and contains system info
- [ ] `src/calculator/__init__.py` exists
- [ ] `notes.txt` exists with 2 lines
- [ ] `notes_backup.txt` exists with 1 line
- [ ] All changes are committed

---

## ✅ Completion

When all tasks are complete:
1. Push this branch to your repository:
   ```bash
   git push -u origin day1-environment
   ```
2. Move to the next branch:
   ```bash
   git checkout day2-github
   ```

---

## 💡 Commands You Might Need

| Command | Purpose |
|---------|---------|
| `uname -s` | Get OS name |
| `git --version` | Get Git version |
| `whoami` | Get current username |
| `mkdir -p` | Create nested directories |
| `touch` | Create empty file |
| `echo "text" > file` | Write text to file |
| `echo "text" >> file` | Append text to file |
| `cp source dest` | Copy file |
| `git status` | Check repo status |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Commit with message |
