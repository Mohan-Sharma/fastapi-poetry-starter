# @author Mohan Sharma

from dependency_injector.wiring import inject


class SessionStore:
	
	@inject
	def __init__(self):
		self.store = {}
	
	def set(self, key, value):
		self.store[key] = value
	
	def get(self, key):
		return self.store.get(key)
