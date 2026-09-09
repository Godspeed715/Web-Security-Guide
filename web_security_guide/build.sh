#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

# migrate and loaddata no longer needed - app uses content.py for all data
# python manage.py migrate
# python manage.py loaddata data.json || true
