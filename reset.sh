#! /bin/bash

python3 $(dirname $0)/manage.py makemigrations translator
python3 $(dirname $0)/manage.py migrate