from pydantic import validate_arguments
from parsel import Selector

from .path import PathParser

from ....settings import SECONDS_PER_DAY

class MazeIslandsParser:
    @validate_arguments
    def __init__(self, html: str) -> None:
        self.__selector = Selector(html)

    @property
    def name(self) -> str:
        name = (self.__selector
            .css("h1::text")
            .get()
            .strip()
            .removesuffix(" Maze Guide"))

        return name

    @property
    def max_points_per_collection(self) -> int:
        max_points_per_collection = int(self.__selector.css(".tkn_hold div b::text").get())
        return max_points_per_collection

    @property
    def duration(self) -> int:
        duration = int(self.__selector
            .css(".dur_text::text")
            .get()
            .strip()
            .removeprefix("This event lasts ")
            .removesuffix(" days")) * SECONDS_PER_DAY

        return duration
    @property
    def paths(self) -> list[dict]:
        paths_selector = self.__selector.css(".ee")
        paths = [ PathParser(path_selector).get() for path_selector in paths_selector ]
        return paths

    def get(self) -> dict:
        return dict(
            name = self.name,
            max_points_per_collection = self.max_points_per_collection,
            duration = self.duration,
            paths = self.paths
        )

__all__ = [ MazeIslandsParser ]