FROM python:3.11.2-slim-buster

RUN apt-get update && apt-get install --no-install-recommends -y \
    netcat \
    gcc

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry

WORKDIR /chat

COPY pyproject.toml .

RUN poetry config virtualenvs.create false
RUN poetry install --no-root

EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
