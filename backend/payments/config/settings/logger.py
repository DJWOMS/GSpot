from environs import Env

from .base import BASE_DIR, DEBUG

env = Env()
env.read_env()

ROLLBAR = {
    'access_token': env.str('ROLLBAR_ACCESS_TOKEN'),
    'environment': 'development' if DEBUG else 'production',
    'code_version': '1.0',
    'root': BASE_DIR,
}
