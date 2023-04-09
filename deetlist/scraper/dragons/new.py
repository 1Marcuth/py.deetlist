from ..base import BaseScraper
from ...fetcher.dragons import NewDragonsFetcher
from ...parser.dragons import NewDragonsParser

def scrape_new_dragons():
    html_data = NewDragonsFetcher().get()
    data = NewDragonsParser(html_data).get()

    return data

class NewDragonsScraper(BaseScraper):
    def __init__(self):
        super().__init__(NewDragonsFetcher, NewDragonsParser)

    def get(self) -> list[dict]:
        return super().get()

__all__ = [ "NewDragonsScraper", "scrape_new_dragons" ]