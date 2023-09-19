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

# create .env file
colored_echo "$GREEN" "Creating .env file"
./scripts/create-env.sh

# Install pre-commit hooks
colored_echo "$GREEN" "Installing pre-commit hooks"
pre-commit run --all-files

# Check unused steps
colored_echo "$GREEN" "Checking unused steps"
output=$(behave -f steps.usage --dry-run features/)
unused_steps=$(echo "$output" | grep -A 1000 "UNUSED STEP DEFINITIONS")
if [ -n "$unused_steps" ]; then
  colored_echo "$RED" "There are some unused step definitions:"
  echo "$unused_steps"
  exit 1
fi

# Run Unit Tests
colored_echo "$GREEN" "Running Unit Tests"
pytest_output=$(pytest)

# Check if the output contains any test failures
if echo "$pytest_output" | grep -q "ERROR\|FAILED"; then
  colored_echo "$RED" "One or more unit tests failed"
  echo "$pytest_output"
  exit 1
else
  colored_echo "$GREEN" "All unit tests passed"
fi

# Build Database
colored_echo "$GREEN" "Building Database"
python create_db.py
check_command_result "Database build completed successfully" "Failed to build the database"

# Run System Tests
colored_echo "$GREEN" "Running System Tests"
behave --logging-clear-handlers --format progress
check_command_result "All system tests passed" "One or more system tests failed"

# Build Done
colored_echo "$GREEN" "Build Done!"
