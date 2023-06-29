from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from developer.models import CompanyUser


class ChangePasswordSerializers(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])
    confirmation_new_password = serializers.CharField(required=True)

    class Meta:
        ref_name = "developer_account_change_pass"
        model = CompanyUser
        fields = ("old_password", "new_password", "confirmation_new_password")

    def validate(self, attrs):
        user: CompanyUser = self.context["request"].user
        if not user.check_password(attrs["old_password"]):
            raise serializers.ValidationError("Invalid old password")

        if attrs["new_password"] != attrs["confirmation_new_password"]:
            raise serializers.ValidationError(
                "New password and confirmation do not match"
            )
        return attrs

    def create(self, validated_data) -> None:
        instance: CompanyUser = self.context["request"].user
        instance.set_password(validated_data["new_password"])
        instance.save()
