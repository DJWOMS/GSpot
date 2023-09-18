FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /games

COPY /requirements.txt .
RUN pip install -r requirements.txt

RUN pip install --upgrade pip

COPY . .
