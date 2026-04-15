#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate --no-input

# Optional: create superuser if env vars are set
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser --no-input || echo "Superuser already exists."
fi

# Optional: seed the database with sample packages
if [ "$SEED_DB" = "True" ]; then
  python manage.py shell < seed_data.py
fi
