import time

from django.conf import settings 
from django.utils import timezone

from base.token_adapter import BaseTokenAdapter
from base.models import BaseAbstractUser
from common.services.users.get_permissions import get_user_permissions
from common.services.jwt.exceptions import TokenExpired
from common.services.jwt.mixins import JWTMixin


class JWTAdapter(BaseTokenAdapter, JWTMixin):

	def __init__(self, user: BaseAbstractUser, role: str):
		self.user = user
		self.role = role


	def generate_access_token(self, additional_data: dict = {}) -> str:
		iat = timezone.localtime()
		exp = iat + settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"]
		payload = {
			"token_type":"access",
			"iat":int(iat.timestamp()),
			"exp":int(exp.timestamp()),
			"user_id":str(self.user.id),
			"role":self.role,
			"permissions":get_user_permissions(self.user),
			**additional_data
			}
		access_token = self._encode(payload)
		return access_token

	
	def generate_refresh_token(self) -> str:
		iat = timezone.localtime()
		exp = iat + settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"]
		payload = {
			"token_type":"refresh",
			"iat":int(iat.timestamp()),
			"exp":int(exp.timestamp()),
			"user_id":str(self.user.id),
			"role":self.role
			}
		refresh_token = self._encode(payload)
		return refresh_token

	
	def generate_tokens(self) -> dict:
		tokens = {
			"access":self.generate_access_token(),
			"refresh":self.generate_refresh_token()
		}
		return tokens
	
	
	def check_token(self, token: str):
		self.check_exp(token)
		return True


	def check_exp(self, token: str) -> int:
		decoded_token = self._decode(token)
		now = int(time.time())
		exp = decoded_token['exp']
		if exp > now :
			return exp - now 
		else:
			raise TokenExpired(f"Token Expired {now-exp} ago.")
		