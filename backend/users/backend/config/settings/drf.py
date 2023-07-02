import os

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "common.services.jwt.authentication.CustomJWTAuthentication",
    ],
    "PAGE_SIZE": 10,
    "MAX_LIMIT": 10,
    "DEFAULT_LIMIT": 100,
    # 'DEFAULT_RENDERER_CLASSES': [
    #     'rest_framework.renderers.JSONRenderer',
    # ]
}
