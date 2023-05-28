import dj_database_url
from config.settings.pydantic_files import db_datas_config

DATABASES = {'default': dj_database_url.config(default=db_datas_config.url)}
# DATABASES = {'default': dj_database_url.config(default='postgres://postgres:postgres@
# localhost:5433/payment')}
#
#
