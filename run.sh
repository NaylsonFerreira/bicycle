#!/bin/bash
export TERM=dumb
export SHELL=/bin/bash

python bicycle/manage.py migrate
python bicycle/manage.py loaddata bicycle/fixtures/*
python bicycle/manage.py runserver 0.0.0.0:8000
