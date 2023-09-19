#!/usr/bin/env bash

# ANSI escape codes for text formatting
GREEN='\033[0;32m'
RED='\033[0;31m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Function to display colored message
colored_echo() {
  local color="$1"
  local message="$2"
  shift 2
  echo -e "${color}${BOLD}${message}${NC} $@"
}

# Function to check if a command succeeded and display colored result
check_command_result() {
  local result=$?
  local success_message="$1"
  local failure_message="$2"

  if [ $result -eq 0 ]; then
    colored_echo "$GREEN" "Success: $success_message"
  else
    colored_echo "$RED" "Failure: $failure_message"
    exit $result
  fi
}

# install latest dependencies
colored_echo "$GREEN" "Installing dependencies"
poetry install

# run migrations
colored_echo "$GREEN" "Syncronize migrations"
alembic upgrade head

# Build Done
colored_echo "$GREEN" "Build Done!"
