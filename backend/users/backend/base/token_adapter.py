from abc import ABC, abstractmethod


class BaseTokenAdapter(ABC):
	
	@abstractmethod
	def generate_access_token():
		pass

	@abstractmethod
	def generate_refresh_token():
		pass

	@abstractmethod
	def check_token():
		pass