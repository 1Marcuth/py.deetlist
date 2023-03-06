from pydantic import validate_arguments
from parsel import Selector

from .mission import MissionParser

class NodeParser:
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def __init__(self, selector: Selector) -> None:
        self.__selector = selector

    @property
    def number(self) -> int:
        number = int(self.__selector
            .css(".nnh::text")
            .get()
            .split("-")[1]
            .strip()
            .removeprefix("Node"))

        return number

    @property
    def missions(self) -> list[dict]:
        missions_selector = self.__selector.css(".ml")
        missions = [ MissionParser(mission_selector).get() for mission_selector in missions_selector ]
        return missions

    def get(self) -> dict:
        return dict(
            number = self.number,
            missions = self.missions
        )

__all__ = [ NodeParser ]