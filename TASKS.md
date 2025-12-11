# Day 5: Final Integration and Documentation

## Objective

Complete the command-line calculator application and document your learning throughout this week.

---

## Prerequisites

Ensure you have completed Days 1 through 4. Your repository should contain:
- Environment files from Day 1
- GitHub workflow files from Day 2
- Calculator functions from Day 3
- Docker documentation from Day 4

---

## Tasks

### Task 1: Create the CLI Calculator

Create a file `src/calculator/cli.py` that provides an interactive command-line calculator.

Requirements:
- Import the operations from your operations module
- Display a welcome message when the program starts
- Show available operations to the user
- Prompt the user for:
  1. First number
  2. Operation (add, subtract, multiply, divide)
  3. Second number
- Display the result
- Handle invalid input gracefully (non-numeric input, invalid operations)
- Allow the user to perform multiple calculations or quit the program

The calculator should be executable with:
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

Create a file `src/system_info.py` that displays the following information:
- Operating system name
- OS release/version
- Python version
- Current working directory
- Current user

Use the `platform` and `os` modules to retrieve this information.

---

### Task 3: Update Package Version

Modify `src/calculator/__init__.py` to:
- Change `__version__` to "1.0.0"
- Add a docstring at the top of the file describing the package

---

### Task 4: Create LEARNING_LOG.md

Create a file `LEARNING_LOG.md` in the root directory containing the following sections:

1. **Environment Setup** - What tools did you install? Were there any challenges?
2. **Git Skills Learned** - List at least five Git commands you now understand
3. **Linux Commands Learned** - List at least five Linux commands you practiced
4. **Python Skills** - What Python concepts did you apply in this project?
5. **Docker Knowledge** - Summarize what you learned about containers
6. **Challenges Faced** - What difficulties did you encounter? How did you resolve them?
7. **Next Steps** - What topics do you want to explore next?

Write honestly and reflectively. This document serves as your personal learning record.

---

### Task 5: Final Project Structure Verification

Your final project structure should resemble the following:

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

Execute the following commands and verify that each produces the expected output:

1. `python3 src/hello.py`
2. `python3 src/test_operations.py`
3. `python3 src/system_info.py`
4. `python3 src/calculator/cli.py` (perform several test calculations)

---

### Task 7: Final Commit and Push

1. Stage all changes
2. Commit with the message: "Day 5: Calculator complete - Week 1 finished!"
3. Push this branch:
   ```bash
   git push -u origin day5-final
   ```

---

## Final Verification Checklist

Before submitting, confirm the following:
- `src/calculator/cli.py` exists and runs interactively
- The CLI handles invalid input without crashing
- `src/system_info.py` displays system information correctly
- `__version__` in `__init__.py` is set to "1.0.0"
- `LEARNING_LOG.md` exists and contains all seven sections
- `project_structure.txt` exists
- All Python scripts execute without errors
- All changes have been committed and pushed

---

## Summary

Upon completing this final day, you will have demonstrated competency in:

- Configuring a development environment
- Using Git and GitHub for version control
- Working with the Linux command line
- Writing Python functions and applications
- Understanding Docker container fundamentals
- Documenting your work and learning process

Your final deliverable is this repository with all five branches completed and pushed to your GitHub account.

---

## Extra Credit

The following extensions are optional but encouraged:

1. **Dockerize the calculator** - Create a Dockerfile that runs your CLI application
2. **Add more operations** - Implement power, square root, or modulo functions
3. **Add calculation history** - Store and display previous calculations
4. **Input validation** - Implement more robust error handling
5. **Unit tests** - Write pytest tests for your calculator operations
