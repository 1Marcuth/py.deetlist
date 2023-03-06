from ..base import BaseScraper
from ...fetcher.dragons import AllDragonsFetcher
from ...parser.dragons import AllDragonsParser

class AllDragonsScraper(BaseScraper):
    def __init__(self):
        super().__init__(AllDragonsFetcher, AllDragonsParser)

    def get(self) -> list[dict]:
        return super().get()

__all__ = [ AllDragonsScraper ]