import os

RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = int(os.environ.get("RABBITMQ_PORT", 5672))
RABBITMQ_USERNAME = os.environ.get("RABBITMQ_USERNAME", "guest")
RABBITMQ_PASSWORD = os.environ.get("RABBITMQ_PASSWORD", "guest")
RABBITMQ_VIRTUAL_HOST = os.environ.get("RABBITMQ_VIRTUAL_HOST", "/")

TOTP_EXCHANGE_NAME = os.environ.get("TOTP_EXCHANGE_NAME", "totp_exchange")
TOTP_ROUTING_KEY = os.environ.get("TOTP_ROUTING_KEY", "totp_queue")
