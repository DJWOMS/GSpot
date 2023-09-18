from base.serializers import BaseAuthSerializer
from developer.models import CompanyUser


class DeveloperAuthSerializer(BaseAuthSerializer):
    class Meta:
        model = CompanyUser
        fields = ("email", "password")
