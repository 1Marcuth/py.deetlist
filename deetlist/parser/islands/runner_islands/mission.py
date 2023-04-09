from pydantic import validate_arguments
from parsel import Selector

class MissionParser:
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def __init__(self, selector: Selector) -> None:
        self.__selector = selector

    @property
    def title(self) -> str:
        title = (self.__selector
            .css(".p2::text")
            .get())

        return title

    @property
    def quantity_of_times(self) -> int:
        quantity_of_times = int(self.__selector
            .css(".p3::text")
            .get())

        return quantity_of_times

    @property
    def quantity_of_coins(self) -> int:
        quantity_of_coins = int(self.__selector.
            css(".p1::text")
            .get()
            .removeprefix("+"))
        
        return quantity_of_coins

    @property
    def icon_url(self) -> str:
        icon_url = (self.__selector
            .css(".rii2 .rimg::attr(src)")
            .get()
            .replace("../../", "https://deetlist.com/dragoncity/"))

        return icon_url

    def get(self) -> dict:
        return dict(
            title = self.title,
            quantity_of_times = self.quantity_of_times,
            quantity_of_coins = self.quantity_of_coins,
            icon_url = self.icon_url
        )

__all__ = [ "MissionParser" ]