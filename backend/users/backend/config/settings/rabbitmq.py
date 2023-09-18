import os

RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = int(os.environ.get("RABBITMQ_PORT", 5672))
RABBITMQ_USERNAME = os.environ.get("RABBITMQ_USERNAME", "guest")
RABBITMQ_PASSWORD = os.environ.get("RABBITMQ_PASSWORD", "guest")
RABBITMQ_VIRTUAL_HOST = os.environ.get("RABBITMQ_VIRTUAL_HOST", "/")
EMAIL_EXCHANGE_NAME = os.environ.get("EMAIL_EXCHANGE_NAME", "email_exchange")
EMAIL_ROUTING_KEY = os.environ.get("EMAIL_ROUTING_KEY", "email_queue")
NOTIFY_EXCHANGE_NAME = os.environ.get("NOTIFY_EXCHANGE_NAME", "notify_exchange")
NOTIFY_ROUTING_KEY = os.environ.get("NOTIFY_ROUTING_KEY", "notify_queue")
TOTP_EXCHANGE_NAME = os.environ.get("TOTP_EXCHANGE_NAME", "totp_exchange")
TOTP_ROUTING_KEY = os.environ.get("TOTP_ROUTING_KEY", "totp_queue")
