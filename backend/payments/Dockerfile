###BUILDER###

FROM python:3.11-alpine AS builder

WORKDIR /payments/apps

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev \
    gcc python3-dev musl-dev

RUN pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip wheel --no-cache-dir --no-deps \
     --wheel-dir /usr/src/app/wheels \
     -r requirements.txt


###FINAL###

FROM python:3.11-alpine 

RUN mkdir -p /home/app

RUN addgroup -S app && adduser -S app -G app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

RUN apk update && apk add libpq
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /payments/apps/requirements.txt .
RUN pip install --no-cache /wheels/*

COPY ./entrypoint.sh $APP_HOME
COPY . $APP_HOME

RUN chmod +x ./entrypoint.sh
RUN chown -R app:app $APP_HOME

USER app

CMD ["sh","/home/app/web/entrypoint.sh"]
