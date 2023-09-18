FROM python:3.11-slim AS builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/* 

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -U app \
    && mkdir -p /home/app/web/static \
    && chown -R app:app /home/app

WORKDIR /home/app/web
COPY --chown=app:app . .

EXPOSE 8000

CMD ["sh", "./scripts/entrypoint.sh"]