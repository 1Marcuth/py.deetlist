from pydantic import validate_arguments
from parsel import Selector

class NodeParser:
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def __init__(self, selector: Selector, cost_selector: Selector | None = None) -> None:
        self.__selector = selector
        self.__cost_selector = cost_selector

    @property
    def number(self) -> int:
        number = int(self.__selector.css(".nummi::text").get())
        return number
    
    @property
    def title(self) -> str | None:
        title = self.__selector.css(".mi_con::text").get()

        if title != "":
            return title

    @property
    def cost(self) -> dict:
        if self.__cost_selector:
            current = int(self.__cost_selector
                .css("::text")
                .get()
                .removeprefix("↓"))

            accumulated = int(self.__selector
                .css(".mii_tota b::text")
                .get())

            return dict(
                current = current,
                accumulated = accumulated
            )

        return dict(
            current = 0,
            accumulated = 0
        )

    def get(self) -> dict:
        return dict(
            number = self.number,
            title = self.title,
            cost = self.cost
        )

__all__ = [ "NodeParser" ]