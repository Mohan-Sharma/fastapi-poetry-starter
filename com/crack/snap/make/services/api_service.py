# @author Mohan Sharma

import requests
from dependency_injector.wiring import inject
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from com.crack.snap.make.config import CommonSettings
from com.crack.snap.make.utils.http_client import HttpClient


class ApiService:
	
	@inject
	def __init__(self, settings: CommonSettings, http_client: HttpClient):
		self.settings = settings
		self.http_client = http_client
		requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	
	@staticmethod
	def get(url, username, password, headers):
		response = requests.get(url, auth=HTTPBasicAuth(username, password), headers=headers, verify=False)
		response.raise_for_status()
		return response.text
	
	@staticmethod
	def post(url, username, password, headers, data):
		response = requests.post(url, data=data, auth=HTTPBasicAuth(username, password), headers=headers, verify=False)
		response.raise_for_status()
		return response.text
