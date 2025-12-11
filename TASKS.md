# Day 3: Python Setup & Calculator Functions

## 🎯 Goal
Set up Python development environment and implement the core calculator functions.

---

## 📋 Prerequisites

Make sure you have completed Days 1-2. You should have:
- `environment.txt`, `notes.txt`, `notes_backup.txt`
- `src/calculator/__init__.py`
- `src/calculator/operations.py` with `SUPPORTED_OPERATIONS`
- `src/calculator/README.md`
- `github_verified.txt` and `git_log_output.txt`

---

## 📋 Tasks

### Task 1: Verify Python Installation

1. Check that Python 3 is installed:
   ```bash
   python3 --version
   ```
2. Create a file called `python_version.txt` containing the output of the above command

---

### Task 2: Create a Hello Script

Create a file `src/hello.py` that:
1. Prints "Hello, Calculator!" to the console
2. Prints the current Python version using the `platform` module

Run it to verify it works:
```bash
python3 src/hello.py
```

---

### Task 3: Implement Calculator Functions

Update `src/calculator/operations.py` to include four functions:

1. **add(a, b)** - Returns the sum of a and b
2. **subtract(a, b)** - Returns a minus b
3. **multiply(a, b)** - Returns the product of a and b
4. **divide(a, b)** - Returns a divided by b

Requirements:
- Each function should take two numeric parameters
- Each function should return the result (not print it)
- The `divide` function should handle division by zero by returning `None`

**Hint:** Keep the `SUPPORTED_OPERATIONS` list you created in Day 2.

---

### Task 4: Create a Test Script

Create a file `src/test_operations.py` that:
1. Imports all four functions from `calculator.operations`
2. Tests each function with sample values
3. Prints the results in a readable format

Example output format:
```
Testing Calculator Operations
-----------------------------
add(5, 3) = 8
subtract(10, 4) = 6
multiply(7, 2) = 14
divide(20, 5) = 4.0
divide(10, 0) = None
```

Run your test script:
```bash
python3 src/test_operations.py
```

---

### Task 5: Update the Package Init

Update `src/calculator/__init__.py` to:
1. Import all four operations from the operations module
2. Define a `__version__` variable set to "0.1.0"

This allows users to do:
```python
from calculator import add, subtract, multiply, divide
```

---

### Task 6: Commit Your Work

1. Stage all changes
2. Commit with message: "Day 3: Implement calculator operations"

---

## ✅ Verification Checklist

Before moving on:
- [ ] `python_version.txt` exists
- [ ] `src/hello.py` runs and prints expected output
- [ ] `src/calculator/operations.py` has all four functions
- [ ] `divide(x, 0)` returns `None` (not an error)
- [ ] `src/test_operations.py` runs successfully
- [ ] `src/calculator/__init__.py` exports the functions
- [ ] All changes committed

---

## ✅ Completion

When all tasks are complete:
1. Push this branch:
   ```bash
   git push -u origin day3-python
   ```
2. Move to the next branch:
   ```bash
   git checkout day4-docker
   ```

---

## 💡 Python Concepts You'll Use

| Concept | Example |
|---------|---------|
| Function definition | `def add(a, b):` |
| Return statement | `return a + b` |
| Conditional | `if b == 0:` |
| Import from module | `from calculator.operations import add` |
| Module variable | `__version__ = "0.1.0"` |
| Platform module | `import platform` |
