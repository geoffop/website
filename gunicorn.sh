#!/bin/sh
gunicorn run:app -w 1 --threads 4 -b 0.0.0.0:8080