from ..base import BaseScraper

from ...fetcher.islands import PuzzleIslandsFetcher
from ...parser.islands import PuzzleIslandsParser

class PuzzleIslandsScraper(BaseScraper):
    def __init__(self):
        super().__init__(PuzzleIslandsFetcher, PuzzleIslandsParser)

__all__ = [ PuzzleIslandsScraper ]