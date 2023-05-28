from config.settings.pydantic_files import rollbar_token

from .base import BASE_DIR, DEBUG

ROLLBAR = {
    'access_token': rollbar_token.r_token,
    'environment': 'development' if DEBUG else 'production',
    'code_version': '1.0',
    'root': BASE_DIR,
}
