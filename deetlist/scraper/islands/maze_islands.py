from ..base import BaseScraper

from ...fetcher.islands import MazeIslandsFetcher
from ...parser.islands import MazeIslandsParser

class MazeIslandsScraper(BaseScraper):
    def __init__(self):
        super().__init__(MazeIslandsFetcher, MazeIslandsParser)

__all__ = [ MazeIslandsScraper ]