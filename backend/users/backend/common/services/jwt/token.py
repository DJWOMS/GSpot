import time

from django.conf import settings 
from django.utils import timezone

from base.token import BaseToken
from common.services.jwt.exceptions import TokenExpired
from common.services.jwt.mixins import JWTMixin


class Token(BaseToken, JWTMixin):


	def generate_access_token(self, data: dict = {}) -> str:
		iat = timezone.localtime()
		exp = iat + settings.ACCESS_TOKEN_LIFETIME
		payload = {
			"token_type":"access",
			"iat":int(iat.timestamp()),
			"exp":int(exp.timestamp()),
			**data
			}
		access_token = self._encode(payload)
		return access_token

	
	def generate_refresh_token(self) -> str:
		iat = timezone.localtime()
		exp = iat + settings.REFRESH_TOKEN_LIFETIME
		payload = {
			"token_type":"refresh",
			"iat":int(iat.timestamp()),
			"exp":int(exp.timestamp()),
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
		self.check_signature(token)
		return True


	def check_exp(self, token: str) -> int:
		exp_left = self.check_exp_left(token)
		if exp_left == 0:
			raise TokenExpired()
		else:
			return exp_left
			
	
	def check_exp_left(self, token: str) -> int:
		decoded_token = self._decode(token)
		now = int(time.time())
		exp = decoded_token['exp']

		if exp > now:
			return exp - now
		else:
			return 0
	

	def check_signature(self, token: str):
		self._decode(token)