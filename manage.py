#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from typing import Union

import dotenv
from opentelemetry.instrumentation.django import DjangoInstrumentor

# Load environment variables from `.env` file
dotenv.load_dotenv()


def main():
    """Run administrative tasks."""

    # Collect the current environment (development | production)
    environment: Union[str, None] = os.environ.get("ENV")

    # Check for specified enviornment and set settings file location
    if environment.lower() == "development":
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "TelemetryApp.settings.development"
        )
    elif environment.lower() == "production":
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "TelemetryApp.settings.production"
        )
    else:
        raise EnvironmentError("Could not detect environment from .env file.")

    # This call is what makes the Django application to be instrumented
    DjangoInstrumentor().instrument()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
