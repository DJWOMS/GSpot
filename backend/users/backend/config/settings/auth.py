AUTH_USER_MODEL = 'admins.Admin'

AUTHENTICATION_BACKENDS = [
    "common.auth_backends.AdminBackend",
    "common.auth_backends.DeveloperBackend",
    "common.auth_backends.CustomerBackend",
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
