#!/bin/sh
gunicorn3 -b 0.0.0.0:5002 'app:create_app()' --log-level debug -w 1 --threads 12
