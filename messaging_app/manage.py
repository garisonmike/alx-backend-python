#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path

def main():
    """Run administrative tasks."""
    # Make sure /app is added to the import path inside Docker
    BASE_DIR = Path(__file__).resolve().parent
    ROOT_DIR = BASE_DIR.parent
    if str(ROOT_DIR) not in sys.path:
        sys.path.append(str(ROOT_DIR))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messaging_app.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? "
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
