# @author Mohan Sharma
from dependency_injector.wiring import inject
from httpx import AsyncClient, BasicAuth, Limits, Timeout

from com.crack.snap.make.config import CommonSettings


class HttpClient:
	
	@inject
	def __init__(self, settings: CommonSettings):
		self.client = AsyncClient(
			verify=False,
			timeout=Timeout(settings.http_timeout),
			limits=Limits(max_keepalive_connections=settings.http_max_keepalive_connections, max_connections=settings.http_max_connections)
		)
	
	async def get(self, url: str, auth: BasicAuth, headers: dict):
		response = await self.client.get(url, auth=auth, headers=headers)
		response.raise_for_status()
		return response.text
	
	async def post(self, url: str, auth: BasicAuth, headers: dict, data: dict):
		response = await self.client.post(url, auth=auth, headers=headers, data=data)
		response.raise_for_status()
		return response.text
	
	async def close(self):
		await self.client.aclose()
