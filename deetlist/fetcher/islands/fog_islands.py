from ..base import BaseFetcher

class FogIslandsFetcher(BaseFetcher):
    __url = "https://deetlist.com/dragoncity/events/fog/"

    def __init__(self) -> None:
        super().__init__(self.__url)

__all__ = [ "FogIslandsFetcher" ]