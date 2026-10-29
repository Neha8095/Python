"""Convenience entry point for the example Django project.

Run this file from the repository root to use Django's management commands::

    python Django.py runserver

If no command is supplied, the development server is started automatically.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent / "mysite"


def main() -> None:
    """Run a Django management command for the example project."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    os.chdir(PROJECT_DIR)
    sys.path.insert(0, str(PROJECT_DIR))

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise SystemExit(
            "Django is not installed. Activate the project virtual environment "
            "and install the requirements before running this program."
        ) from exc

    command = sys.argv[1:] or ["runserver"]
    execute_from_command_line([str(Path(__file__))] + command)


if __name__ == "__main__":
    main()
