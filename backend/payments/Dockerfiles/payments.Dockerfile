#Build
FROM python:3.11-slim AS builder

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/* 

WORKDIR /payments/apps
  
COPY requirements.txt flake8-requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir -r flake8-requirements.txt

# Final
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN useradd -U app \
    && mkdir -p /home/app/web/static \
    && chown -R app:app /home/app

COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

WORKDIR /home/app/web
COPY --chown=app:app . .

EXPOSE 8000

CMD ["sh", "./Dockerfiles/scripts/entrypoint.sh"]