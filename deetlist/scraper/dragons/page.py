from pydantic import validate_arguments

from ...fetcher.dragons import DragonPageFetcher, DragonPagesAsyncFetcher 
from ...parser.dragons import DragonPageParser

@validate_arguments
def scrape_dragon_page(url_or_dragon_name: str):
    html_data = DragonPageFetcher(url_or_dragon_name).get()
    data = DragonPageParser(html_data).get()

    return data

@validate_arguments
def scrape_async_dragon_pages(urls_or_dragon_names: list[str]):
    html_data_of_dragons = DragonPagesAsyncFetcher(urls_or_dragon_names).run()
    data_of_dragons = [ DragonPageParser(html_data).get() for html_data in html_data_of_dragons ]
    return data_of_dragons

class DragonPageScraper:
    @validate_arguments
    def __init__(self, url_or_dragon_name: str):
        self.__url_or_dragon_name = url_or_dragon_name

    def get(self) -> dict:
        html_data = DragonPageFetcher(self.__url_or_dragon_name).get()
        data = DragonPageParser(html_data).get()
        return data

class DragonPagesAsyncScraper:
    @validate_arguments
    def __init__(self, urls_or_dragon_names: list[str]):
        self.__urls_or_dragon_names = urls_or_dragon_names

    def run(self) -> list[dict]:
        html_data_of_dragons = DragonPagesAsyncFetcher(self.__urls_or_dragon_names).run()
        data_of_dragons = [ DragonPageParser(html_data).get() for html_data in html_data_of_dragons ]
        return data_of_dragons

__all__ = [
    "DragonPageScraper",
    "DragonPagesAsyncScraper",
    "scrape_dragon_page",
    "scrape_async_dragon_pages"
]