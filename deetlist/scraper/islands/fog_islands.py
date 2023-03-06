from ..base import BaseScraper

from ...fetcher.islands import FogIslandsFetcher
from ...parser.islands import FogIslandsParser

class FogIslandsScraper(BaseScraper):
    def __init__(self):
        super().__init__(FogIslandsFetcher, FogIslandsParser)

__all__ = [ FogIslandsScraper ]