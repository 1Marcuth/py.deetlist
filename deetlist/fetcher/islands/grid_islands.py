from ..base import BaseFetcher

class GridIslandsFetcher(BaseFetcher):
    __url = "https://deetlist.com/dragoncity/events/grid/"

    def __init__(self) -> None:
        super().__init__(self.__url)

__all__ = [ GridIslandsFetcher ]