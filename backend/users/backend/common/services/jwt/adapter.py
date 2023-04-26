from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenVerifySerializer
from rest_framework_simplejwt.settings import api_settings

from base.token_adapter import BaseTokenAdapter
from base.models import BaseAbstractUser
from common.services.users.get_permissions import get_dict_of_user_permissions


class SimpleJWTAdapter(BaseTokenAdapter):

	def __init__(self, user:BaseAbstractUser, role:str):
		self.user = user
		self.role = role

	def generate_access_token(self) -> str:
		tokens = self.__generate_tokens__()
		return str(tokens.access_token)

	
	def generate_refresh_token(self) -> str:
		tokens = self.__generate_tokens__()
		return str(tokens.refresh_token)

	
	def __generate_tokens__(self) -> dict:
		token = RefreshToken.for_user(self.user)
		token['user_id'] = str(self.user.id)
		token['role'] = self.role
		token['permissions'] = get_dict_of_user_permissions(self.user)
		if api_settings.UPDATE_LAST_LOGIN:
			update_last_login(None, self.user)
		return token
	
	
	def check_token(self):
		pass
	

	def check_if_token_in_blacklist(self, token:str):
		return TokenVerifySerializer().validate({'token':token})
	