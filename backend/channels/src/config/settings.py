from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGODB_URL: str
    MONGODB_TEST_DATABASE: str

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DATABASE: str

    RABBITMQ_DEFAULT_USER: str
    RABBITMQ_DEFAULT_PASS: str
    RABBITMQ_LOCAL_HOST_NAME: str
    RABBITMQ_LOCAL_PORT: int
    RABBITMQ_TEST_QUEUE: str

    EMAIL_HOST: str
    EMAIL_PORT: int
    EMAIL_HOST_USER: str
    EMAIL_HOST_PASSWORD: str

    class Config:
        env_file = './.env.dev'


settings = Settings()
