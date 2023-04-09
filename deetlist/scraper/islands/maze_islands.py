from ..base import BaseScraper

from ...fetcher.islands import MazeIslandsFetcher
from ...parser.islands import MazeIslandsParser

def scrape_maze_islands():
    html_data = MazeIslandsFetcher().get()
    data = MazeIslandsParser(html_data).get()

    return data

class MazeIslandsScraper(BaseScraper):
    def __init__(self):
        super().__init__(MazeIslandsFetcher, MazeIslandsParser)

__all__ = [ "MazeIslandsScraper", "scrape_maze_islands" ]