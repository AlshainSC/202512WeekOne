"""
Day 2 Validation Tests - GitHub Integration
Tests that the student has completed all Day 2 tasks.
"""
import os
import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestDay2GitHub:
    """Test Day 2: GitHub Integration tasks."""

    def test_github_verified_exists(self):
        """Check that github_verified.txt was created."""
        filepath = os.path.join(BASE_DIR, "github_verified.txt")
        assert os.path.exists(filepath), "github_verified.txt not found - verify your GitHub SSH connection"

    def test_github_verified_has_content(self):
        """Check that github_verified.txt has content about verification."""
        filepath = os.path.join(BASE_DIR, "github_verified.txt")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read().lower()
            assert "verified" in content or "github" in content or "ssh" in content, \
                "github_verified.txt should mention verification status"

    def test_operations_py_exists(self):
        """Check that src/calculator/operations.py was created."""
        filepath = os.path.join(BASE_DIR, "src", "calculator", "operations.py")
        assert os.path.exists(filepath), "src/calculator/operations.py not found"

    def test_operations_has_supported_operations(self):
        """Check that operations.py defines SUPPORTED_OPERATIONS list."""
        filepath = os.path.join(BASE_DIR, "src", "calculator", "operations.py")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read()
            assert "SUPPORTED_OPERATIONS" in content, \
                "operations.py should define SUPPORTED_OPERATIONS variable"

    def test_supported_operations_is_list(self):
        """Check that SUPPORTED_OPERATIONS contains the four operations."""
        filepath = os.path.join(BASE_DIR, "src", "calculator", "operations.py")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read().lower()
            required_ops = ["add", "subtract", "multiply", "divide"]
            for op in required_ops:
                assert op in content, f"SUPPORTED_OPERATIONS should include '{op}'"

    def test_calculator_readme_exists(self):
        """Check that src/calculator/README.md was created."""
        filepath = os.path.join(BASE_DIR, "src", "calculator", "README.md")
        assert os.path.exists(filepath), "src/calculator/README.md not found"

    def test_calculator_readme_has_sections(self):
        """Check that calculator README has required sections."""
        filepath = os.path.join(BASE_DIR, "src", "calculator", "README.md")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read().lower()
            # Check for key content (flexible matching)
            has_name = any(word in content for word in ["calculator", "calc", "project", "name"])
            has_description = len(content) > 50  # Should have some description
            assert has_name and has_description, \
                "README.md should have project name and description"

    def test_git_log_output_exists(self):
        """Check that git_log_output.txt was created."""
        filepath = os.path.join(BASE_DIR, "git_log_output.txt")
        assert os.path.exists(filepath), "git_log_output.txt not found - run git log --oneline"

    def test_git_log_has_commits(self):
        """Check that git_log_output.txt shows commit history."""
        filepath = os.path.join(BASE_DIR, "git_log_output.txt")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                lines = f.readlines()
            assert len(lines) >= 1, "git_log_output.txt should show at least one commit"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
