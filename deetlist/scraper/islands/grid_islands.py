from ..base import BaseScraper

from ...fetcher.islands import GridIslandsFetcher
from ...parser.islands import GridIslandsParser

def scrape_grid_islands():
    html_data = GridIslandsFetcher().get()
    data = GridIslandsParser(html_data).get()

    return data

class GridIslandsScraper(BaseScraper):
    def __init__(self):
        super().__init__(GridIslandsFetcher, GridIslandsParser)

__all__ = [ "GridIslandsScraper", "scrape_grid_islands" ]