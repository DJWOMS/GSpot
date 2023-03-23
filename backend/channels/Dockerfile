FROM python:3.11.2

# Set work directory
WORKDIR /channels

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update

RUN pip install --upgrade pip
RUN pip install poetry

COPY ./pyproject.toml /channels
RUN poetry install

COPY . /channels
