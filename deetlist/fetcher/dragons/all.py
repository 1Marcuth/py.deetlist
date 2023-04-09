from ..base import BaseFetcher

class AllDragonsFetcher(BaseFetcher):
    __url = "https://deetlist.com/dragoncity/all-dragons/"

    def __init__(self) -> None:
        super().__init__(self.__url)

__all__ = [ "AllDragonsFetcher" ]