from pydantic import validate_arguments
from parsel import Selector

class DragonParser:
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def __init__(self, dragon_selector: Selector) -> None:
        self.__dragon_selector = dragon_selector

    @property
    def name(self) -> str:
        dragon_name = self.__dragon_selector.css(".drag::text").get()
        return dragon_name

    @property
    def page_url(self) -> str:
        dragon_page_url = (
            self.__dragon_selector.css("::attr(href)")
                .get()
                .replace("../", "https://deetlist.com/dragoncity/")
                .replace(" ", "%20"))

        return dragon_page_url

    @property
    def image_url(self) -> str:
        dragon_page_url = (
            self.__dragon_selector.css("::attr(href)")
                .get()
                .replace("../", "https://deetlist.com/dragoncity/img/")
                .lower()
                .replace(" ", "%20")) + ".png"
                
        return dragon_page_url

    def get(self):
        return dict(
            name = self.name,
            page_url = self.page_url,
            image_url = self.image_url
        )

class AllDragonsParser:
    @validate_arguments
    def __init__(self, html: str) -> None:
        self.__selector = Selector(html)

    def get(self):
        dragons_selector = self.__selector.css("a:has(.drag)")
        dragons = [ DragonParser(dragon_selector).get() for dragon_selector in dragons_selector ]
        return dragons

__all__ = [ AllDragonsParser ]