#!/bin/sh

gunicorn -w 4 -b 0.0.0.0:4000 app:app