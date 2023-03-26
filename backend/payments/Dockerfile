FROM python:3.11-slim 

WORKDIR /payments/apps

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
COPY flake8-requirements.txt /tmp/flake8-requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && pip install --no-cache-dir -r /tmp/flake8-requirements.txt \
    && rm -rf /tmp/requirements.txt \
    && useradd -U app_user \
    && install -d -m 0755 -o app_user -g app_user /home/app/web/static


ENV HOME=/home/app
ENV APP_HOME=/home/app/web
WORKDIR $APP_HOME

COPY ./entrypoint.sh $APP_HOME
USER app_user:app_user
COPY --chown=app_user:app_user . .
RUN chmod +x ./*.sh

ENTRYPOINT ["/home/app/web/entrypoint.sh"]
CMD [ "./start.sh", "server" ]