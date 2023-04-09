from pydantic import validate_arguments
from parsel import Selector

from ....settings import DRAGON_ELEMENTS

class DragonParser:
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def __init__(
        self,
        selector: Selector,
        name_selector: Selector
    ) -> None:
        self.__selector = selector
        self.__name_selector = name_selector

    @property
    def name(self) -> str:
        name = (self.__name_selector
            .css("::text")
            .get()
            .removesuffix("Path")
            .strip())

        return name

    @property
    def rarity(self) -> str:
        rarity = (self.__selector
            .css(".img_rar::attr(class)")
            .get()
            .split()[0]
            .removeprefix("img_rp_")
            .upper())

        return rarity

    @property
    def elements(self) -> list[str]:
        elements_selector = self.__selector.css(".typ_i")
        elements = [
            DRAGON_ELEMENTS[element_selector
                .css("::attr(class)")
                .get()
                .split()[1]
                .removeprefix("tb_")]
            for element_selector in elements_selector
        ]

        return elements

    @property
    def category(self) -> str:
        category = int(self.__selector
            .css("p::text")
            .get()
            .strip()
            .removeprefix("Category:"))

        return category

    @property
    def image_url(self) -> str:
        image_url = (self.__selector
            .css(".mi_i_hld::attr(src)")
            .get()
            .replace("../../", "https://deetlist.com/dragoncity/"))

        return image_url

    @property
    def page_url(self) -> str:
        page_url = (self.__selector
            .css("a::attr(href)")
            .get()
            .replace("../../", "https://deetlist.com/dragoncity/"))

        return page_url

    def get(self) -> dict:
        return dict(
            name = self.name,
            rarity = self.rarity,
            elements = self.elements,
            category = self.category,
            image_url = self.image_url,
            page_url = self.page_url
        )

__all__ = [ "DragonParser" ]