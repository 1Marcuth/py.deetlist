from pydantic import validate_arguments
from parsel import Selector

from .mission import MissionParser

class MissionSetParser:
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def __init__(self, selector: Selector) -> None:
        self.__selector = selector

    @property
    def missions(self) -> list[dict]:
        missions_selector = self.__selector.css(".mission_id")
        missions = [ MissionParser(mission_selector).get() for mission_selector in missions_selector ]
        return missions

    def get(self) -> list[dict]:
        return self.missions

__all__ = [ "MissionSetParser" ]