from ..base import BaseScraper

from ...fetcher.islands import HeroicRacesFetcher
from ...parser.islands import HeroicRacesParser

def scrape_heroic_races():
    html_data = HeroicRacesFetcher().get()
    data = HeroicRacesParser(html_data).get()

    return data

class HeroicRacesScraper(BaseScraper):
    def __init__(self):
        super().__init__(HeroicRacesFetcher, HeroicRacesParser)

__all__ = [ "HeroicRacesScraper", "scrape_heroic_races" ]