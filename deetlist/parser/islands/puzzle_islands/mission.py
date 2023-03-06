from pydantic import validate_arguments
from parsel import Selector

class MissionParser:
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def __init__(self, selector: Selector) -> None:
        self.__selector = selector

    @property
    def title(self) -> str:
        title = (self.__selector
            .css(".miss_con::text")
            .get()
            .split(".")[1]
            .strip())

        return title

    @property
    def quantity_of_pieces(self) -> int:
        quantity_of_pieces = int(self.__selector
            .css(".moves_h::text")
            .get()
            .removeprefix("+"))

        return quantity_of_pieces

    def get(self) -> dict:
        return dict(
            title = self.title,
            quantity_of_pieces = self.quantity_of_pieces
        )

__all__ = [ MissionParser ]