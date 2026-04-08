"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Set up Django environment and execute management commands."""

    # Set the default settings module for the project
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sticky_notes.settings')

    try:
        # Import Django's command-line execution utility
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raised if Django isn't installed or environment isn't set up properly
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute the command passed in (e.g., runserver, migrate)
    execute_from_command_line(sys.argv)


# Ensure this script runs only when executed directly
if __name__ == '__main__':
    main()
