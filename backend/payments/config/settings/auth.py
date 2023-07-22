from environs import Env

env = Env()
env.read_env()


REDIS_ACCESS_PREFIX = env.str('REDIS_ACCESS_PREFIX', '')
REDIS_ACCESS_DB = env.int('REDIS_ACCESS_DB', 0)
REDIS_HOST = env.str('REDIS_HOST', 'localhost')
REDIS_PORT = env.int('REDIS_PORT', 6379)
REDIS_PASSWORD = env.str('REDIS_PASSWORD', '')
GET_TOKEN_FROM = env.str('REDIS_GET_TOKEN_FROM', 'headers')  # 'headers' or 'cookies'
