from ..base import BaseScraper

from ...fetcher.islands import GridIslandsFetcher
from ...parser.islands import GridIslandsParser

class GridIslandsScraper(BaseScraper):
    def __init__(self):
        super().__init__(GridIslandsFetcher, GridIslandsParser)

__all__ = [ GridIslandsScraper ]