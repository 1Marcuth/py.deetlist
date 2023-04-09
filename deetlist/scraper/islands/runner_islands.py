from ..base import BaseScraper

from ...fetcher.islands import RunnerIslandsFetcher
from ...parser.islands import RunnerIslandsParser

def scrape_runner_islands():
    html_data = RunnerIslandsFetcher().get()
    data = RunnerIslandsParser(html_data).get()

    return data

class RunnerIslandsScraper(BaseScraper):
    def __init__(self):
        super().__init__(RunnerIslandsFetcher, RunnerIslandsParser)

__all__ = [ "RunnerIslandsScraper", "scrape_runner_islands" ]