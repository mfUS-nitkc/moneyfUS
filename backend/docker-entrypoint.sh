#!/bin/bash
set -e

if [ $# -eq 0 ]; then
    set -- --settings=config.settings.develop
fi

/venv/bin/python3 manage.py makemigrations $1
/venv/bin/python3 manage.py migrate $1
/venv/bin/python3 manage.py runserver 0.0.0.0:8000 $1
