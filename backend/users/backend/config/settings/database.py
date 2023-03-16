import os

from .base import ROOT_DIR

DB_ENGINE = os.environ["DB_ENGINE"]

if DB_ENGINE == "postgres":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ["DB_NAME"],
            "USER": os.environ["DB_USER"],
            "PASSWORD": os.environ["DB_PASSWORD"],
            "HOST": os.environ["DB_HOST"],
            "PORT": os.environ["DB_PORT"],
        }
    }
else:
    DATABASE_FILE_NAME = os.path.join(ROOT_DIR, "db.sqlite3")  # noqa: F405
    DATABASES = {
        "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": DATABASE_FILE_NAME}
    }
