import os


REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
REDIS_ACCESS_DB = os.getenv('REDIS_ACCESS_DB', 0)
REDIS_REFRESH_DB = os.getenv('REDIS_REFRESH_DB', 1)
REDIS_TOTP_DB = os.getenv('REDIS_TOTP_DB', 2)
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', 'Qwe123!@#')
REDIS_ACCESS_KEY = os.getenv('REDIS_ACCESS_KEY', 'good_key')
REDIS_REFRESH_KEY = os.getenv('REDIS_REFRESH_KEY', 'refresh_key')
REDIS_BLACK_LIST_KEY = os.getenv('REDIS_BLACK_LIST_KEY', 'wrong_key')