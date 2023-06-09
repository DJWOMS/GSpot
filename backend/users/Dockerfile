FROM python:3.11-slim-buster

ENV \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
  POETRY_VERSION=1.3.2 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry'

# Cleaning cache:
RUN apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*
# System deps:
RUN apt-get update && \
  apt-get install --no-install-recommends -y \
  build-essential \
  gettext \
  libpq-dev \
  wget

  # Installing `poetry` package manager:
  # https://github.com/python-poetry/poetry
RUN pip install "poetry-core==1.4.0" "poetry==$POETRY_VERSION" && poetry --version

# Copy only requirements, to cache them in docker layer
WORKDIR /app
COPY ./pyproject.toml /app/

# Project initialization:
RUN poetry install --no-root

# Creating folders, and files for a project:
COPY . /app

# Setting up proper permissions:

RUN mkdir -p /app/media /app/static && \
	chmod +x /app/media/ /app/static/

WORKDIR backend

CMD python manage.py migrate && \
    gunicorn -b 0.0.0.0:8000 --log-level info --access-logfile - config.wsgi:application
