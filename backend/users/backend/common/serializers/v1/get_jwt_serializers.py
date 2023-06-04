import os
from rest_framework import serializers
from common.services.jwt.token import Token
from common.services.jwt.exceptions import UnauthorizedUserError, TokenBannedError


class GetJwtSerializers(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, attrs):
        token = Token()
        user = self.context["request"].user
        refresh_token = attrs.pop('refresh_token')
        token_in_black_list = False
        user_data = {'user_id': str(user.id), 'role': str(user._meta.app_label)}
        if token.check_token(refresh_token):
            if not token_in_black_list:
                if user_data.get('role') != 'customer':
                    user_data.update(
                        {'permissions': str(user.permissions_codename), 'avatar': str(user.avatar)}
                    )
                else:
                    user_data.update({'age': user.age})
                if user.is_active and not user.is_banned:
                    exp_left = token.check_exp_left(refresh_token)
                    if exp_left > int(os.environ['REFRESH_TOKEN_ROTATE_MIN_LIFETIME']):
                        dict_token = {
                            'refresh': refresh_token,
                            'access': token.generate_access_token(user_data),
                        }
                        return dict_token
                    # - ban refresh token
                    dict_token = token.generate_tokens(user_data)
                    return dict_token
                raise UnauthorizedUserError
            else:
                raise TokenBannedError
