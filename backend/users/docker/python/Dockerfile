FROM python:3.11-slim-buster

ENV DJANGO_ENV=${DJANGO_ENV} \
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

# System deps:
RUN apt-get update && \
  apt-get install --no-install-recommends -y \
  build-essential \
  gettext \
  libpq-dev \
  wget \
  # Cleaning cache:
  && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
  # Installing `poetry` package manager:
  # https://github.com/python-poetry/poetry
  && pip install "poetry-core==1.4.0" "poetry==$POETRY_VERSION" && poetry --version

# Copy only requirements, to cache them in docker layer
WORKDIR /code
COPY ./poetry.lock ./pyproject.toml /code/

# Project initialization:
RUN poetry install --no-root

# Creating folders, and files for a project:
COPY . /code

COPY ./docker/python/start-web.sh /start-web.sh

# Setting up proper permissions:
RUN chmod +x /start-web.sh \
  && mkdir -p /code/media /code/static \
  && chmod +x /code/media/ /code/static/

WORKDIR backend