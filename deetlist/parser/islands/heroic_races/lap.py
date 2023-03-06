from pydantic import validate_arguments
from parsel import Selector

from .node import NodeParser

class LapParser:
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def __init__(self, selector: Selector) -> None:
        self.__selector = selector

    @property
    def number(self) -> int:
        number = int(self.__selector
            .css(".nnh::text")
            .get()
            .strip()
            .split("-")[0]
            .removeprefix("Lap"))

        return number

    @property
    def nodes(self) -> list[dict]:
        nodes_selector = self.__selector.css(".nn")
        nodes = [ NodeParser(node_selector).get() for node_selector in nodes_selector ]
        return nodes

    def get(self) -> dict:
        return dict(
            number = self.number,
            nodes = self.nodes
        )

__all__ = [ LapParser ]