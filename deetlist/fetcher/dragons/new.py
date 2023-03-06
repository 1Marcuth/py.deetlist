from ..base import BaseFetcher

class NewDragonsFetcher(BaseFetcher):
    __url = "https://deetlist.com/dragoncity/new-dragons/"

    def __init__(self) -> None:
        super().__init__(self.__url)

__all__ = [ NewDragonsFetcher ]