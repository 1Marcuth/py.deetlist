from pydantic import validate_arguments
from parsel import Selector

from .dragon import DragonParser
from .node import NodeParser

class PathParser:
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def __init__(self, selector: Selector) -> None:
        self.__selector = selector

    @property
    def dragon(self) -> int:
        dragon_selector = self.__selector.css(".ev_ds")[0]
        dragon_name_selector = self.__selector.css("h3")[0]
        dragon = DragonParser(dragon_selector, dragon_name_selector).get()
        return dragon

    @property
    def nodes(self) -> list[dict]:
        node_selectors = self.__selector.css(".miihold")
        cost_selectors = [None] + self.__selector.css(".mii_cost")

        nodes = [
            NodeParser(node_selector, cost_selector).get()
            for node_selector, cost_selector in zip(node_selectors, cost_selectors)
        ]

        return nodes

    def get(self) -> dict:
        return dict(
            dragon = self.dragon,
            nodes = self.nodes
        )

__all__ = [ PathParser ]