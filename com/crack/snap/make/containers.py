# @author Mohan Sharma
import os
import sys
from dependency_injector import containers, providers

from com.crack.snap.make.config import get_settings
from com.crack.snap.make.services.api_service import ApiService
from com.crack.snap.make.services.file_processing_service import \
	FileProcessingService
from com.crack.snap.make.utils.http_client import HttpClient
from com.crack.snap.make.utils.session_store import SessionStore
from com.crack.snap.make.utils.utility import Utility


class Container(containers.DeclarativeContainer):
	
	@staticmethod
	def get_env():
		return os.environ.get("APP_ENV", "dev")
	
	env = providers.Callable(
		lambda: sys.argv[1] if len(sys.argv) > 1 else "dev"
	)
	
	settings = providers.Factory(get_settings, env=get_env())
	file_processing_service = providers.Factory(FileProcessingService)
	utility = providers.Factory(Utility, settings=settings, file_processing_service=file_processing_service)
	session_store = providers.Factory(SessionStore)
	http_client = providers.Factory(HttpClient, settings=settings)
	api_service = providers.Factory(ApiService, settings=settings, http_client=http_client)

