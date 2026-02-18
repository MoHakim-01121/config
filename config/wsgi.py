"""
WSGI project for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

# Debugging PORT environment variable
port = os.getenv('PORT')
if not port:
    print("Error: PORT environment variable is not set or is empty.")
else:
    print(f"PORT environment variable: {port}")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
