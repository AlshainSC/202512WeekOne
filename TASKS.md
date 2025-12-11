# Day 5: Final Integration & Documentation

## 🎯 Goal
Complete the command-line calculator application and document your learning journey.

---

## 📋 Prerequisites

Make sure you have completed Days 1-4. You should have:
- Environment files from Day 1
- GitHub workflow files from Day 2
- Calculator functions from Day 3
- Docker documentation from Day 4

---

## 📋 Tasks

### Task 1: Create the CLI Calculator

Create a file `src/calculator/cli.py` that provides an interactive command-line calculator.

Requirements:
- Import the operations from your operations module
- Display a welcome message when started
- Show available operations to the user
- Prompt the user for:
  1. First number
  2. Operation (add, subtract, multiply, divide)
  3. Second number
- Display the result
- Handle invalid input gracefully (non-numbers, invalid operations)
- Allow the user to perform multiple calculations or quit

The calculator should be runnable with:
```bash
python3 src/calculator/cli.py
```

Example interaction:
```
=================================
  Welcome to Python Calculator!
=================================
Available operations: add, subtract, multiply, divide
Type 'quit' to exit.

Enter first number: 10
Enter operation: add
Enter second number: 5
Result: 10 + 5 = 15

Enter first number: quit
Goodbye!
```

---

### Task 2: Create System Info Script

Create a file `src/system_info.py` that displays:
- Operating system name
- OS release/version
- Python version
- Current working directory
- Current user

Use the `platform` and `os` modules.

---

### Task 3: Update Package Version

Update `src/calculator/__init__.py`:
- Change `__version__` to "1.0.0"
- Add a docstring at the top describing the package

---

### Task 4: Create LEARNING_LOG.md

Create a file `LEARNING_LOG.md` in the root directory with the following sections:

1. **Environment Setup** - What tools did you install? Any challenges?
2. **Git Skills Learned** - List 5+ Git commands you now understand
3. **Linux Commands Learned** - List 5+ Linux commands you practiced
4. **Python Skills** - What Python concepts did you use in this project?
5. **Docker Knowledge** - Summarize what you learned about containers
6. **Challenges Faced** - What was difficult? How did you solve it?
7. **Next Steps** - What do you want to learn next?

Be genuine - this is YOUR learning journal!

---

### Task 5: Final Project Structure Verification

Your final project structure should look similar to this:

```
202512WeekOne/
├── README.md
├── TASKS.md
├── LEARNING_LOG.md
├── .gitignore
├── environment.txt
├── notes.txt
├── notes_backup.txt
├── github_verified.txt
├── git_log_output.txt
├── python_version.txt
├── docker_version.txt
├── docker/
│   ├── hello_world_output.txt
│   ├── python_container_notes.txt
│   ├── nginx_exploration.txt
│   ├── lifecycle_commands.txt
│   └── DOCKER_NOTES.md
└── src/
    ├── hello.py
    ├── test_operations.py
    ├── system_info.py
    └── calculator/
        ├── __init__.py
        ├── operations.py
        ├── cli.py
        └── README.md
```

Create a file called `project_structure.txt` containing the output of:
```bash
find . -type f -name "*.py" -o -name "*.md" -o -name "*.txt" | grep -v __pycache__ | sort
```

---

### Task 6: Final Testing

Run these commands and verify they all work:

1. `python3 src/hello.py`
2. `python3 src/test_operations.py`
3. `python3 src/system_info.py`
4. `python3 src/calculator/cli.py` (test a few calculations)

---

### Task 7: Final Commit and Push

1. Stage all changes
2. Commit with message: "Day 5: Calculator complete - Week 1 finished!"
3. Push this branch:
   ```bash
   git push -u origin day5-final
   ```

---

## ✅ Final Verification Checklist

- [ ] `src/calculator/cli.py` exists and runs interactively
- [ ] CLI handles invalid input without crashing
- [ ] `src/system_info.py` displays system information
- [ ] `__version__` in `__init__.py` is "1.0.0"
- [ ] `LEARNING_LOG.md` exists with all 7 sections
- [ ] `project_structure.txt` exists
- [ ] All Python scripts run without errors
- [ ] All changes committed and pushed

---

## 🎉 Congratulations!

You have completed Week 1! You now have:

- ✅ A working development environment
- ✅ Git and GitHub proficiency
- ✅ Linux command line skills
- ✅ Python programming fundamentals
- ✅ Docker basics understanding
- ✅ A working CLI calculator application
- ✅ Documentation of your learning journey

**Your final deliverable is this repository with all 5 branches completed and pushed.**

---

## 🏆 Extra Credit Ideas

1. **Dockerize the calculator** - Create a Dockerfile that runs your CLI
2. **Add more operations** - Power, square root, modulo
3. **Add calculation history** - Store and display previous calculations
4. **Input validation** - More robust error handling
5. **Unit tests** - Write pytest tests for your operations
