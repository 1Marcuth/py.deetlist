from ..base import BaseScraper

from ...fetcher.islands import RunnerIslandsFetcher
from ...parser.islands import RunnerIslandsParser

class RunnerIslandsScraper(BaseScraper):
    def __init__(self):
        super().__init__(RunnerIslandsFetcher, RunnerIslandsParser)

__all__ = [ RunnerIslandsScraper ]