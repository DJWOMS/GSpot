import os
import logging
from datetime import timedelta

logger = logging.getLogger(__name__)

ACCESS_TOKEN_LIFETIME = timedelta(seconds=int(os.environ["ACCESS_TOKEN_LIFETIME"]))
REFRESH_TOKEN_LIFETIME = timedelta(seconds=int(os.environ["REFRESH_TOKEN_LIFETIME"]))
REFRESH_TOKEN_ROTATE_MIN_LIFETIME = timedelta(
    seconds=int(os.environ['REFRESH_TOKEN_ROTATE_MIN_LIFETIME'])
)
ALGORITHM = "HS256"

GET_TOKEN_FROM = "header"

if os.environ["GET_TOKEN_FROM"] not in ["header", "cookies"]:
    logging.warning(f"GET_TOKEN_FROM settled with default value {GET_TOKEN_FROM}")
else:
    GET_TOKEN_FROM = os.environ["GET_TOKEN_FROM"]
