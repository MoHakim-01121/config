#!/bin/bash

# Print all environment variables for debugging
echo "Environment Variables:"
printenv

# Start the Gunicorn server
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --log-file -