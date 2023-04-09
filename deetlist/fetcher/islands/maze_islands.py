from ..base import BaseFetcher

class MazeIslandsFetcher(BaseFetcher):
    __url = "https://deetlist.com/dragoncity/events/maze/"

    def __init__(self) -> None:
        super().__init__(self.__url)

__all__ = [ "MazeIslandsFetcher" ]