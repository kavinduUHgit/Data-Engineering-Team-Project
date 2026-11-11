"""A first, simple test that proves pytest is set up correctly.

Real tests for the ETL functions are added once those functions are written.
"""

from src import config


def test_project_root_exists() -> None:
    """Check that config.PROJECT_ROOT points to a real folder on this laptop.

    If this passes, Python can import our src package and pytest is working.
    """
    assert config.PROJECT_ROOT.exists(), f"PROJECT_ROOT not found: {config.PROJECT_ROOT}"
    assert config.PROJECT_ROOT.is_dir(), f"PROJECT_ROOT is not a folder: {config.PROJECT_ROOT}"
