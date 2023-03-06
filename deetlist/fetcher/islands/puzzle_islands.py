from ..base import BaseFetcher

class PuzzleIslandsFetcher(BaseFetcher):
    __url = "https://deetlist.com/dragoncity/events/puzzle/"

    def __init__(self) -> None:
        super().__init__(self.__url)

__all__ = [ PuzzleIslandsFetcher ]