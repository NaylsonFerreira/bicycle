#!/bin/bash
export TERM=dumb
export SHELL=/bin/bash

python manage.py migrate
# python manage.py loaddata fixtures/*
python bicycle/manage.py runserver 0.0.0.0:8000
