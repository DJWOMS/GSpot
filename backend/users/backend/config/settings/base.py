import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../../../.env"))


def reduce_path(file_name, times):
    result = os.path.realpath(file_name)
    for _ in range(times):
        result = os.path.dirname(result)
    return result


ROOT_DIR = reduce_path(__file__, 4)
APPS_DIR = reduce_path(__file__, 3)

DEBUG = os.getenv("DEBUG", False)
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
ALLOWED_HOSTS = os.environ["DJANGO_ALLOWED_HOSTS"].split(",")

ROOT_URLCONF = "config.urls"

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(ROOT_DIR, "static/")
# STATICFILES_DIRS = [os.path.join(APPS_DIR, "static/")]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(ROOT_DIR, "media/")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third party apps
    "drf_yasg",
    "django_filters",
    "rest_framework",
    # Local apps
    "administrator.apps.AdministratorAppConfig",
    "developer.apps.DeveloperAppConfig",
    "customer.apps.CustomerAppConfig",
    "common.apps.CommonAppConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

FIXTURE_DIRS = [
    'fixtures',
]
CSRF_TRUSTED_ORIGINS = os.environ["DJANGO_CORS_ALLOWED_ORIGINS"].split(",")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
