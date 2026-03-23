#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python web_security_guide/manage.py collectstatic --no-input
python web_security_guide/manage.py migrate
