#!/bin/bash

set -e

# Go to the root
cd "${0%/*}" || exit 1

# Read options
migrate=  # apply migrations after rebuild
git_add=  # add migrations to git index for following commit
delete=   # whether to delete old migrations
for arg in "$@"
do
    if [ "$arg" == "--migrate" ] || [ "$arg" == "-m" ]
    then
        migrate="true"
    fi
    if [ "$arg" == "--git-add" ] || [ "$arg" == "-a" ]
    then
        git_add="true"
    fi
    if [ "$arg" == "--delete" ] || [ "$arg" == "-d" ]
    then
        delete="true"
    fi
done

# Check if there is something to update.
# If migrations already up to date, then just exit
python manage.py makemigrations --check --dry-run && exit 0

# If "delete" flag is used, then delete old migrations
if [ "$delete" ]; then
    find . -path "*/migrations/000*_auto.py" -not -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc"  -delete
fi

# Rebuild migrations
python manage.py makemigrations --no-header --name auto

# Reformat and remove empty dependencies.
find . -path "*/migrations/*.py" | while read fname; do
    # Reformat before changes
    black "$fname"
    sed -i.bak '/dependencies = \[\]/d' "$fname"
    rm "${fname}.bak"
    # Reformat after changes once again
    black "$fname"
done

# Reformat after changes
pre-commit run -a

# If "migrate" flag is used, then apply migrations
if [ "$migrate" ]; then
    python manage.py migrate
fi

# If "--git-add" then add generated migrations to git index
if [ "$git_add" ]; then
    cd .. && git add website/*/migrations/*.py
fi
