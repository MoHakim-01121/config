"""
WSGI project for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

# Debugging PORT environment variable with fallback
port = os.getenv('PORT', '8000')  # Default to 8000 if PORT is not set
if not port.isdigit():
    print(f"Error: PORT environment variable is not a valid number: {port}")
else:
    print(f"PORT environment variable: {port}")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
