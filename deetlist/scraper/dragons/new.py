from ..base import BaseScraper
from ...fetcher.dragons import NewDragonsFetcher
from ...parser.dragons import NewDragonsParser

class NewDragonsScraper(BaseScraper):
    def __init__(self):
        super().__init__(NewDragonsFetcher, NewDragonsParser)

    def get(self) -> list[dict]:
        return super().get()

__all__ = [ NewDragonsScraper ]