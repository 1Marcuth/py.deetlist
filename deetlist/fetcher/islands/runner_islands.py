from ..base import BaseFetcher

class RunnerIslandsFetcher(BaseFetcher):
    __url = "https://deetlist.com/dragoncity/events/runner/"

    def __init__(self) -> None:
        super().__init__(self.__url)

__all__ = [ "RunnerIslandsFetcher" ]