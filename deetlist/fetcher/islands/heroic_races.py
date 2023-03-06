from ..base import BaseFetcher

class HeroicRacesFetcher(BaseFetcher):
    __url = "https://deetlist.com/dragoncity/events/race/"

    def __init__(self) -> None:
        super().__init__(self.__url)

__all__ = [ HeroicRacesFetcher ]