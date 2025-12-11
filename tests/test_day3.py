"""
Day 3 Validation Tests - Python Setup
Tests that the student has completed all Day 3 tasks.
"""
import os
import sys
import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, "src")

# Add src to path for imports
sys.path.insert(0, SRC_DIR)


class TestDay3Python:
    """Test Day 3: Python Setup tasks."""

    def test_python_version_txt_exists(self):
        """Check that python_version.txt was created."""
        filepath = os.path.join(BASE_DIR, "python_version.txt")
        assert os.path.exists(filepath), "python_version.txt not found"

    def test_python_version_has_content(self):
        """Check that python_version.txt contains Python version info."""
        filepath = os.path.join(BASE_DIR, "python_version.txt")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read().lower()
            assert "python" in content or "3." in content, \
                "python_version.txt should contain Python version information"

    def test_hello_py_exists(self):
        """Check that src/hello.py was created."""
        filepath = os.path.join(SRC_DIR, "hello.py")
        assert os.path.exists(filepath), "src/hello.py not found"

    def test_hello_py_has_print(self):
        """Check that hello.py prints something."""
        filepath = os.path.join(SRC_DIR, "hello.py")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read()
            assert "print" in content, "hello.py should use print()"

    def test_operations_has_add_function(self):
        """Check that operations.py has an add function."""
        try:
            from calculator.operations import add
            result = add(5, 3)
            assert result == 8, f"add(5, 3) should return 8, got {result}"
        except ImportError:
            pytest.fail("Could not import add from calculator.operations")

    def test_operations_has_subtract_function(self):
        """Check that operations.py has a subtract function."""
        try:
            from calculator.operations import subtract
            result = subtract(10, 4)
            assert result == 6, f"subtract(10, 4) should return 6, got {result}"
        except ImportError:
            pytest.fail("Could not import subtract from calculator.operations")

    def test_operations_has_multiply_function(self):
        """Check that operations.py has a multiply function."""
        try:
            from calculator.operations import multiply
            result = multiply(7, 2)
            assert result == 14, f"multiply(7, 2) should return 14, got {result}"
        except ImportError:
            pytest.fail("Could not import multiply from calculator.operations")

    def test_operations_has_divide_function(self):
        """Check that operations.py has a divide function."""
        try:
            from calculator.operations import divide
            result = divide(20, 5)
            assert result == 4.0 or result == 4, f"divide(20, 5) should return 4, got {result}"
        except ImportError:
            pytest.fail("Could not import divide from calculator.operations")

    def test_divide_handles_zero(self):
        """Check that divide handles division by zero gracefully."""
        try:
            from calculator.operations import divide
            result = divide(10, 0)
            assert result is None, f"divide(10, 0) should return None, got {result}"
        except ImportError:
            pytest.fail("Could not import divide from calculator.operations")
        except ZeroDivisionError:
            pytest.fail("divide(10, 0) should return None, not raise ZeroDivisionError")

    def test_test_operations_py_exists(self):
        """Check that src/test_operations.py was created."""
        filepath = os.path.join(SRC_DIR, "test_operations.py")
        assert os.path.exists(filepath), "src/test_operations.py not found"

    def test_init_has_version(self):
        """Check that __init__.py defines __version__."""
        filepath = os.path.join(SRC_DIR, "calculator", "__init__.py")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read()
            assert "__version__" in content, "__init__.py should define __version__"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
