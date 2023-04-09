from pydantic import validate_arguments
import asyncio
import httpx

class BaseFetcher:
    @validate_arguments
    def __init__(self, url: str, params: dict = {}) -> None:
        self.__url = url
        self.__params = params

    def get(self):
        response = httpx.get(url=self.__url, params=self.__params)
        data = response.text
        return data

class BaseAsyncFetcher:
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    async def get(self, url_params: tuple[str, dict | None], client: httpx.AsyncClient):
        url, params = url_params
        response = await client.get(url=url, params=params)
        html = response.text
        return html

    @validate_arguments
    async def fetch(self, urls_params: list[tuple[str, dict | None]]):
        async with httpx.AsyncClient(http2=True) as client:
            tasks = [
                self.get(url_params, client)
                for url_params in urls_params
            ]

            responses = await asyncio.gather(*tasks)
            return responses

    @validate_arguments
    def run(self, urls_params: list[tuple[str, dict | None]]):
        return asyncio.run(self.fetch(urls_params))

__all__ = [ "BaseFetcher"," BaseAsyncFetcher" ]