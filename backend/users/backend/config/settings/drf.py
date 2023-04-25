import os


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
    	'rest_framework.permissions.IsAuthenticated'
        ],
    'DEFAULT_AUTHENTICATION_CLASSES': 
    	os.environ["DEFAULT_AUTHENTICATION_CLASSES"].split(","),
    'PAGE_SIZE': 10,
    # 'DEFAULT_RENDERER_CLASSES': [
    #     'rest_framework.renderers.JSONRenderer',
    # ]
}
