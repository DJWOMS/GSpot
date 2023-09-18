from rest_framework.pagination import LimitOffsetPagination
from rest_framework.settings import api_settings


class BasePagination(LimitOffsetPagination):
    default_limit = api_settings.user_settings["MAX_LIMIT"]
    max_limit = api_settings.user_settings["DEFAULT_LIMIT"]
