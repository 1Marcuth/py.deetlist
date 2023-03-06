from ..base import BaseFetcher

class TowerIslandsFetcher(BaseFetcher):
    __url = "https://deetlist.com/dragoncity/events/tower/"

    def __init__(self) -> None:
        super().__init__(self.__url)

__all__ = [ TowerIslandsFetcher ]