import sys


def test_python_version_matches_project_requirement():
    """The environment must run the Python version required by pyproject.toml."""
    assert sys.version_info >= (3, 13)
