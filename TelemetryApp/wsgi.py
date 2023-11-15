"""
WSGI config for TelemetryApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from typing import Union

import dotenv
from django.core.wsgi import get_wsgi_application

# Load environment variables from `.env` file
dotenv.load_dotenv()

# Collect the current environment (development | production)
environment: Union[str, None] = os.environ.get("ENV")

# Check for specified enviornment and set settings file location
if environment.lower() == "development":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TelemetryApp.settings.development")
elif environment.lower() == "production":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TelemetryApp.settings.production")
else:
    raise EnvironmentError("Could not detect environment from .env file.")


application = get_wsgi_application()
