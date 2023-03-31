#Build
FROM python:3.11-slim AS builder

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/* \
  curl -fsSL https://deb.nodesource.com/setup_19.x | bash - && \
  apt-get install -y nodejs && \
  apt-get install -y npm && \
  npm install -g localtunnel

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
COPY --from=builder /usr/local/lib/node_modules /usr/local/lib/node_modules
COPY --from=builder /usr/bin/nodejs /usr/bin/node
COPY --from=builder /usr/lib /usr/lib

WORKDIR /home/app/web
COPY --chown=app:app . .

RUN chmod +x ./*.sh
USER app:app

ENTRYPOINT ["sh", "/home/app/web/entrypoint.sh"]