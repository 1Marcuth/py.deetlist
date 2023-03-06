from pydantic import validate_arguments
from parsel import Selector

class DragonParser:
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def __init__(self, selector: Selector) -> None:
        self.__selector = selector

    @property
    def name(self) -> str:
        name = self.__selector.css(".rn::text").get()
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
    def image_url(self) -> str:
        image_url = (self.__selector.css(".newi::attr(src)")
            .get()
            .replace("../", "https://deetlist.com/dragoncity/")
            .replace(" ", "%20"))

        return image_url
    
    @property
    def page_url(self) -> str:
        page_url = (self.__selector
            .css("::attr(href)")
            .get()
            .replace("../", "https://deetlist.com/dragoncity/")
            .replace(" ", "%20"))

        return page_url

    @property
    def launched_in(self) -> int:
        launched_in = int(int(self.__selector.css(".rt::text").get()) / 1000)
        return launched_in

    def get(self) -> dict:
        return dict(
            name = self.name,
            rarity = self.rarity,
            image_url = self.image_url,
            page_url = self.page_url,
            launched_in = self.launched_in
        )

class NewDragonsParser:
    def __init__(self, html: str) -> None:
        self.__selector = Selector(html)

    def get(self):
        dragons_selector = self.__selector.css(".drag_link")
        dragons = [ DragonParser(dragon_selector).get() for dragon_selector in dragons_selector ]
        return dragons

__all__ = [ NewDragonsParser ]