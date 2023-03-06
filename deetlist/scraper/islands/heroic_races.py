from ..base import BaseScraper

from ...fetcher.islands import HeroicRacesFetcher
from ...parser.islands import HeroicRacesParser

class HeroicRacesScraper(BaseScraper):
    def __init__(self):
        super().__init__(HeroicRacesFetcher, HeroicRacesParser)

__all__ = [ HeroicRacesScraper ]