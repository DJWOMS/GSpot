from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGODB_URL: str
    MONGODB_TEST_DATABASE: str

    RABBITMQ_DEFAULT_USER: str
    RABBITMQ_DEFAULT_PASS: str
    RABBITMQ_LOCAL_HOST_NAME: str
    RABBITMQ_LOCAL_PORT: int
    RABBITMQ_TEST_QUEUE: str

    class Config:
        env_file = './.env.dev'


settings = Settings()
