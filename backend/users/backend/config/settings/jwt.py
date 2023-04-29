import os
from datetime import timedelta


GET_TOKEN_FROM = os.environ["GET_TOKEN_FROM"]
ACCESS_TOKEN_LIFETIME = timedelta(
    seconds=int(os.environ["ACCESS_TOKEN_LIFETIME"])
    )
REFRESH_TOKEN_LIFETIME = timedelta(
    seconds=int(os.environ["REFRESH_TOKEN_LIFETIME"])
    )
ALGORITHM = "HS256"
