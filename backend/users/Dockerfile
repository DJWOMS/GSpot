FROM python:3.11-slim-buster

ENV \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

# System deps:
RUN apt-get update && \
  apt-get install --no-install-recommends -y \
  build-essential \
  gettext \
  libpq-dev \
  wget && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Copy only requirements, to cache them in docker layer
WORKDIR /app
COPY ./requirements.txt /app/

# Project initialization:
RUN pip install -r requirements.txt

# Creating folders, and files for a project:
COPY . /app

# Setting up proper permissions:

RUN mkdir -p /app/media /app/static

WORKDIR backend

CMD python manage.py collectstatic --noinput && python manage.py migrate && \
    gunicorn -b 0.0.0.0:8000 --log-level info --access-logfile - config.wsgi:application
