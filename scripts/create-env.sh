#!/usr/bin/env bash

# Get the app path
env_path=$(dirname $(dirname "$0"))/.env

# create .env file
{
  echo "LOG_LEVEL=DEBUG"
  echo "ENVIRONMENT=local"
  echo "APPLICATION_PORT=8011"
  echo "BASE_PATH=/cinefy"
  echo "CORS_ORIGINS=*"
  echo "GUNICORN_WORKERS=3"
  echo "DB_HOST=localhost"
  echo "DB_PORT=5432"
  echo "DB_NAME=test_db"
  echo "DB_USERNAME=postgres"
  echo "DB_PASSWORD=cantguessthis"
  echo "SENTRY_DSN="
} > $env_path

echo "Local $env_path file created."
