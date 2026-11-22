from importlib.metadata import version


def test_package_is_importable():
    """CompAI must be importable from the installed environment."""
    import compai

    assert compai.__doc__


def test_version_comes_from_project_metadata():
    """The installed version must match the one declared in pyproject.toml."""
    assert version("compai") == "0.1.0"
