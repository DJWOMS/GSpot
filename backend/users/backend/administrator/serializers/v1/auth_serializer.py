from administrator.models import Admin
from base.serializers import BaseAuthSerializer


class AdminAuthSerializer(BaseAuthSerializer):
    class Meta:
        model = Admin
        fields = ("email", "password")
