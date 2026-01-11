#!/usr/bin/env bash
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running migrations..."
python manage.py migrate --noinput

echo "Generating sample data..."
python manage.py generate_sample_data

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "✓ Build complete!"
