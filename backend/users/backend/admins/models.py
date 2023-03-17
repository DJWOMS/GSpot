from common.models import BaseUser


class Admin(BaseUser):
    class Meta:
        db_table = "admin"
