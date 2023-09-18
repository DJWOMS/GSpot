import os

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        # 'file': {
        #     'level': 'ERROR',
        #     'class': 'logging.FileHandler',
        #     'filename': LOG_FILE,
        #     'formatter': 'verbose'
        # },
        "console": {"class": "logging.StreamHandler", "formatter": "verbose"},
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "propagate": True,
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
        },
    },
}
