#!/bin/bash

# Fail on first error
set -e

# Go to the root
cd "${0%/*}" || exit 1

# 1. Check that no duplicate migrations exist
# Loop through all migration directories
find -type d -name 'migrations' -print0 | while read -d $'\0' migrations_dir; do
  # Find all *.py files except __init__.py in the migration folder,
  # get only their names and cut each name from 5th character to the end.
  # Sort this obtained result and count duplicates.
  # If any duplicate file exists then end it with failure and the message will be printed.
  if [[ $(find $migrations_dir -type f -name '*.py' ! -name '__init__.py' \
    -printf "%f\n" | cut -c -4 | sort | uniq -cd) ]]
  then
    echo "There are some duplicate migrations in the $migrations_dir folder." \
         "Please, rebuild the last one or rename and change dependencies in it."
    exit 1
  fi
done

# 2. Check that migrations were applied
if ! python manage.py makemigrations --check --dry-run
then
    echo "New migrations need to be applied!"
    exit 1
fi

# 3. Check that no one imported Django user model directly
if grep "from django.contrib.auth.models import.* User.*" -r ./ \
    --include=\*.py
then
    echo "Usage of Admin from django.contrib.auth.models is not allowed. " \
         "Use Admin from main.models!"
    exit 1
fi
