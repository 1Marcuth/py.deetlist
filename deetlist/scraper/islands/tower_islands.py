from ..base import BaseScraper

from ...fetcher.islands import TowerIslandsFetcher
from ...parser.islands import TowerIslandsParser

class TowerIslandsScraper(BaseScraper):
    def __init__(self):
        super().__init__(TowerIslandsFetcher, TowerIslandsParser)

__all__ = [ TowerIslandsScraper ]