#!/bin/bash
# Script untuk jalankan Django server tanpa HTTPS error spam

cd /home/hakim/Desktop/config

# Run server dan filter error HTTPS
/home/hakim/Desktop/config/env/bin/python manage.py runserver 127.0.0.1:8000 2>&1 | \
  grep -v "You're accessing the development server over HTTPS" | \
  grep -v "Bad request version" | \
  grep -v "Bad request syntax" | \
  grep -v "Bad HTTP/0.9 request"
