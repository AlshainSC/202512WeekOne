"""
Day 5 Validation Tests - Final Integration
Tests that the student has completed all Day 5 tasks.
"""
import os
import sys
import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, "src")

# Add src to path for imports
sys.path.insert(0, SRC_DIR)


class TestDay5Final:
    """Test Day 5: Final Integration tasks."""

    def test_cli_py_exists(self):
        """Check that src/calculator/cli.py was created."""
        filepath = os.path.join(SRC_DIR, "calculator", "cli.py")
        assert os.path.exists(filepath), "src/calculator/cli.py not found"

    def test_cli_imports_operations(self):
        """Check that cli.py imports from operations module."""
        filepath = os.path.join(SRC_DIR, "calculator", "cli.py")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read()
            has_import = "import" in content and "operations" in content.lower()
            has_from = "from" in content and ("add" in content or "operations" in content)
            assert has_import or has_from, "cli.py should import from operations module"

    def test_cli_has_input_handling(self):
        """Check that cli.py handles user input."""
        filepath = os.path.join(SRC_DIR, "calculator", "cli.py")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read()
            assert "input" in content, "cli.py should use input() for user interaction"

    def test_cli_has_loop_or_quit(self):
        """Check that cli.py allows multiple calculations or quitting."""
        filepath = os.path.join(SRC_DIR, "calculator", "cli.py")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read().lower()
            has_loop = "while" in content
            has_quit = "quit" in content or "exit" in content or "break" in content
            assert has_loop or has_quit, "cli.py should allow multiple calculations or quitting"

    def test_system_info_py_exists(self):
        """Check that src/system_info.py was created."""
        filepath = os.path.join(SRC_DIR, "system_info.py")
        assert os.path.exists(filepath), "src/system_info.py not found"

    def test_system_info_uses_platform(self):
        """Check that system_info.py uses platform module."""
        filepath = os.path.join(SRC_DIR, "system_info.py")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read()
            assert "platform" in content, "system_info.py should use the platform module"

    def test_init_version_is_1_0_0(self):
        """Check that __init__.py has version 1.0.0."""
        filepath = os.path.join(SRC_DIR, "calculator", "__init__.py")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read()
            assert "1.0.0" in content, "__version__ should be '1.0.0' in __init__.py"

    def test_init_has_docstring(self):
        """Check that __init__.py has a docstring."""
        filepath = os.path.join(SRC_DIR, "calculator", "__init__.py")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read().strip()
            has_docstring = content.startswith('"""') or content.startswith("'''")
            assert has_docstring, "__init__.py should have a docstring at the top"

    def test_learning_log_exists(self):
        """Check that LEARNING_LOG.md was created."""
        filepath = os.path.join(BASE_DIR, "LEARNING_LOG.md")
        assert os.path.exists(filepath), "LEARNING_LOG.md not found"

    def test_learning_log_has_sections(self):
        """Check that LEARNING_LOG.md has required sections."""
        filepath = os.path.join(BASE_DIR, "LEARNING_LOG.md")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read().lower()
            
            # Check for key sections (flexible matching)
            sections = [
                ("environment", "setup"),
                ("git",),
                ("linux", "command"),
                ("python",),
                ("docker",),
            ]
            
            for keywords in sections:
                found = any(kw in content for kw in keywords)
                assert found, f"LEARNING_LOG.md should have a section about {keywords[0]}"

    def test_learning_log_has_substance(self):
        """Check that LEARNING_LOG.md has meaningful content."""
        filepath = os.path.join(BASE_DIR, "LEARNING_LOG.md")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read()
            # Should have substantial content
            assert len(content) > 500, "LEARNING_LOG.md should have detailed reflections (at least 500 characters)"

    def test_project_structure_txt_exists(self):
        """Check that project_structure.txt was created."""
        filepath = os.path.join(BASE_DIR, "project_structure.txt")
        assert os.path.exists(filepath), "project_structure.txt not found"

    def test_calculator_functions_still_work(self):
        """Verify all calculator functions still work correctly."""
        try:
            from calculator.operations import add, subtract, multiply, divide
            
            assert add(10, 5) == 15, "add(10, 5) should equal 15"
            assert subtract(10, 5) == 5, "subtract(10, 5) should equal 5"
            assert multiply(10, 5) == 50, "multiply(10, 5) should equal 50"
            assert divide(10, 5) == 2, "divide(10, 5) should equal 2"
            assert divide(10, 0) is None, "divide(10, 0) should return None"
        except ImportError as e:
            pytest.fail(f"Could not import calculator functions: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
