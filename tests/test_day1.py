"""
Day 1 Validation Tests - Environment Setup
Tests that the student has completed all Day 1 tasks.
"""
import os
import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestDay1Environment:
    """Test Day 1: Environment Setup tasks."""

    def test_environment_txt_exists(self):
        """Check that environment.txt was created."""
        filepath = os.path.join(BASE_DIR, "environment.txt")
        assert os.path.exists(filepath), "environment.txt not found - create it with your system info"

    def test_environment_txt_has_content(self):
        """Check that environment.txt has meaningful content."""
        filepath = os.path.join(BASE_DIR, "environment.txt")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read().strip()
            assert len(content) > 10, "environment.txt appears to be empty or too short"

    def test_src_directory_exists(self):
        """Check that src/ directory was created."""
        dirpath = os.path.join(BASE_DIR, "src")
        assert os.path.isdir(dirpath), "src/ directory not found - create it using mkdir"

    def test_calculator_directory_exists(self):
        """Check that src/calculator/ directory was created."""
        dirpath = os.path.join(BASE_DIR, "src", "calculator")
        assert os.path.isdir(dirpath), "src/calculator/ directory not found - create nested directories"

    def test_calculator_init_exists(self):
        """Check that src/calculator/__init__.py was created."""
        filepath = os.path.join(BASE_DIR, "src", "calculator", "__init__.py")
        assert os.path.exists(filepath), "src/calculator/__init__.py not found - create it with touch"

    def test_notes_txt_exists(self):
        """Check that notes.txt was created."""
        filepath = os.path.join(BASE_DIR, "notes.txt")
        assert os.path.exists(filepath), "notes.txt not found"

    def test_notes_txt_has_two_lines(self):
        """Check that notes.txt has at least 2 lines (original + appended)."""
        filepath = os.path.join(BASE_DIR, "notes.txt")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                lines = f.readlines()
            assert len(lines) >= 2, "notes.txt should have at least 2 lines (you need to append to it)"

    def test_notes_backup_exists(self):
        """Check that notes_backup.txt was created."""
        filepath = os.path.join(BASE_DIR, "notes_backup.txt")
        assert os.path.exists(filepath), "notes_backup.txt not found - copy notes.txt to create it"

    def test_notes_backup_has_one_line(self):
        """Check that notes_backup.txt has the original content (1 line)."""
        filepath = os.path.join(BASE_DIR, "notes_backup.txt")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                lines = f.readlines()
            # Backup should have 1 line (created before append)
            assert len(lines) >= 1, "notes_backup.txt should have at least 1 line"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
