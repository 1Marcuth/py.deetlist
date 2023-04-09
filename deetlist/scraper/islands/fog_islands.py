from ..base import BaseScraper

from ...fetcher.islands import FogIslandsFetcher
from ...parser.islands import FogIslandsParser

def scrape_fog_islands():
    html_data = FogIslandsFetcher().get()
    data = FogIslandsParser(html_data).get()

    return data

class FogIslandsScraper(BaseScraper):
    def __init__(self):
        super().__init__(FogIslandsFetcher, FogIslandsParser)

__all__ = [ "FogIslandsScraper", "scrape_fog_islands" ]