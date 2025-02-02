#!/usr/bin/env bash

# exit when any command fails
set -o errexit

## Install dependencies via pip
pip install -r requirements.txt

## Run migration just in case
python manage.py migrate

# Run this comand after creating this file:
# chmod a+x setup.sh