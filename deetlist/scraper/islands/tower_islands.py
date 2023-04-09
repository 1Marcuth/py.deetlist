from ..base import BaseScraper

from ...fetcher.islands import TowerIslandsFetcher
from ...parser.islands import TowerIslandsParser

def scrape_tower_islands():
    html_data = TowerIslandsFetcher().get()
    data = TowerIslandsParser(html_data).get()

    return data

class TowerIslandsScraper(BaseScraper):
    def __init__(self):
        super().__init__(TowerIslandsFetcher, TowerIslandsParser)

__all__ = [ "TowerIslandsScraper", "scrape_tower_islands" ]