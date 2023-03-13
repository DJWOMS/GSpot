from pydantic import BaseSettings


class Settings(BaseSettings):
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    MONGODB_URL: str
    MONGODB_TEST_DATABASE: str

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_TEST_DATABASE_INDEX: int

    RABBITMQ_DEFAULT_USER: str
    RABBITMQ_DEFAULT_PASS: str
    RABBITMQ_LOCAL_HOST_NAME: str
    RABBITMQ_LOCAL_PORT: int
    RABBITMQ_TEST_QUEUE: str

    class Config:
        env_file = './.env'


settings = Settings()
