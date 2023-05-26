FROM python:3.11.2-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#TODO сначало копировать requirements.txt , потом остальной код
#TODO убрать команд из докер-композ файла и добавить сюда