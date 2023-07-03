import os

AUTH_USER_MODEL = "administrator.Admin"


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

DJANGO_SUPERUSER_USERNAME = 'username'
DJANGO_SUPERUSER_PASSWORD = 'password'
DJANGO_SUPERUSER_PHONE = '88005553535'
DJANGO_SUPERUSER_EMAIL = 'admin@gmail.com'
