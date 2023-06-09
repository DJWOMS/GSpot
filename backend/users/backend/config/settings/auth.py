import os

AUTH_USER_MODEL = 'administrator.Admin'

AUTHENTICATION_BACKENDS = [
    "common.auth_backends.AdminBackend",
]


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DJANGO_SUPERUSER_USERNAME = os.environ["DJANGO_SUPERUSER_USERNAME"]
DJANGO_SUPERUSER_PASSWORD = os.environ["DJANGO_SUPERUSER_PASSWORD"]
DJANGO_SUPERUSER_PHONE = os.environ["DJANGO_SUPERUSER_PHONE"]
DJANGO_SUPERUSER_EMAIL = os.environ["DJANGO_SUPERUSER_EMAIL"]
