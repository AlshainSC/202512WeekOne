"""
Day 4 Validation Tests - Docker Fundamentals
Tests that the student has completed all Day 4 tasks.
"""
import os
import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestDay4Docker:
    """Test Day 4: Docker Fundamentals tasks."""

    def test_docker_version_txt_exists(self):
        """Check that docker_version.txt was created."""
        filepath = os.path.join(BASE_DIR, "docker_version.txt")
        assert os.path.exists(filepath), "docker_version.txt not found"

    def test_docker_version_has_content(self):
        """Check that docker_version.txt contains Docker version info."""
        filepath = os.path.join(BASE_DIR, "docker_version.txt")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read().lower()
            assert "docker" in content or "version" in content, \
                "docker_version.txt should contain Docker version information"

    def test_docker_directory_exists(self):
        """Check that docker/ directory was created."""
        dirpath = os.path.join(BASE_DIR, "docker")
        assert os.path.isdir(dirpath), "docker/ directory not found"

    def test_hello_world_output_exists(self):
        """Check that docker/hello_world_output.txt was created."""
        filepath = os.path.join(BASE_DIR, "docker", "hello_world_output.txt")
        assert os.path.exists(filepath), "docker/hello_world_output.txt not found"

    def test_hello_world_has_content(self):
        """Check that hello_world_output.txt has Docker hello-world output."""
        filepath = os.path.join(BASE_DIR, "docker", "hello_world_output.txt")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read().lower()
            assert "hello" in content or "docker" in content, \
                "hello_world_output.txt should contain hello-world output"

    def test_python_container_notes_exists(self):
        """Check that docker/python_container_notes.txt was created."""
        filepath = os.path.join(BASE_DIR, "docker", "python_container_notes.txt")
        assert os.path.exists(filepath), "docker/python_container_notes.txt not found"

    def test_python_container_notes_has_content(self):
        """Check that python_container_notes.txt documents the experience."""
        filepath = os.path.join(BASE_DIR, "docker", "python_container_notes.txt")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read()
            assert len(content) > 20, "python_container_notes.txt should document your experience"

    def test_nginx_exploration_exists(self):
        """Check that docker/nginx_exploration.txt was created."""
        filepath = os.path.join(BASE_DIR, "docker", "nginx_exploration.txt")
        assert os.path.exists(filepath), "docker/nginx_exploration.txt not found"

    def test_lifecycle_commands_exists(self):
        """Check that docker/lifecycle_commands.txt was created."""
        filepath = os.path.join(BASE_DIR, "docker", "lifecycle_commands.txt")
        assert os.path.exists(filepath), "docker/lifecycle_commands.txt not found"

    def test_lifecycle_commands_has_content(self):
        """Check that lifecycle_commands.txt documents Docker commands."""
        filepath = os.path.join(BASE_DIR, "docker", "lifecycle_commands.txt")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read().lower()
            # Should mention at least some Docker commands
            docker_keywords = ["stop", "start", "rm", "remove", "docker"]
            has_keywords = any(kw in content for kw in docker_keywords)
            assert has_keywords, "lifecycle_commands.txt should document Docker lifecycle commands"

    def test_docker_notes_md_exists(self):
        """Check that docker/DOCKER_NOTES.md was created."""
        filepath = os.path.join(BASE_DIR, "docker", "DOCKER_NOTES.md")
        assert os.path.exists(filepath), "docker/DOCKER_NOTES.md not found"

    def test_docker_notes_has_explanations(self):
        """Check that DOCKER_NOTES.md has required explanations."""
        filepath = os.path.join(BASE_DIR, "docker", "DOCKER_NOTES.md")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read().lower()
            # Check for key concepts
            concepts = ["container", "image"]
            for concept in concepts:
                assert concept in content, f"DOCKER_NOTES.md should explain what a {concept} is"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
