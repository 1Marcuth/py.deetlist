from pydantic import validate_arguments

from ...fetcher.dragons import DragonPageFetcher, DragonPageAsyncFetcher 
from ...parser.dragons import DragonPageParser

class DragonPageScraper:
    @validate_arguments
    def __init__(self, url_or_dragon_name: str):
        self.__url_or_dragon_name = url_or_dragon_name

    def get(self) -> dict:
        html_data = DragonPageFetcher(self.__url_or_dragon_name).get()
        data = DragonPageParser(html_data).get()
        return data

class DragonPageAsyncScraper:
    @validate_arguments
    def __init__(self, urls_or_dragon_names: list[str]):
        self.__urls_or_dragon_names = urls_or_dragon_names

    def run(self) -> list[dict]:
        html_data_of_dragons = DragonPageAsyncFetcher(self.__urls_or_dragon_names).run()
        data_of_dragons = [ DragonPageParser(html_data).get() for html_data in html_data_of_dragons ]
        return data_of_dragons

__all__ = [ DragonPageScraper, DragonPageAsyncScraper ]