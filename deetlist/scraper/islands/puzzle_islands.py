from ..base import BaseScraper

from ...fetcher.islands import PuzzleIslandsFetcher
from ...parser.islands import PuzzleIslandsParser

def scrape_puzzle_islands():
    html_data = PuzzleIslandsFetcher().get()
    data = PuzzleIslandsParser(html_data).get()

    return data

class PuzzleIslandsScraper(BaseScraper):
    def __init__(self):
        super().__init__(PuzzleIslandsFetcher, PuzzleIslandsParser)

__all__ = [ "PuzzleIslandsScraper", "scrape_puzzle_islands" ]