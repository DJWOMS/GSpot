import os


REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_ACCESS_DB = int(os.getenv('REDIS_ACCESS_DB', 0))
REDIS_REFRESH_DB = int(os.getenv('REDIS_REFRESH_DB', 1))
REDIS_TOTP_DB = int(os.getenv('REDIS_TOTP_DB', 2))
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)
REDIS_ACCESS_PREFIX = os.getenv('REDIS_ACCESS_PREFIX', 'access')
REDIS_REFRESH_PREFIX = os.getenv('REDIS_REFRESH_PREFIX', 'refresh')
REDIS_TOTP_PREFIX = os.getenv('REDIS_TOTP_PREFIX', 'totp')
