from pydantic import validate_arguments

from ..base import BaseFetcher, BaseAsyncFetcher

class DragonPageFetcher(BaseFetcher):
    @validate_arguments
    def __init__(self, url_or_dragon_name: str) -> None:
        if not url_or_dragon_name.startswith("http://") and not url_or_dragon_name.startswith("https://"):
            url = f"https://deetlist.com/dragoncity/dragon/{url_or_dragon_name.title().replace(' ', '%20')}"

        else:
            url = url_or_dragon_name

        super().__init__(url)

class DragonPageAsyncFetcher(BaseAsyncFetcher):
    __urls_params = []

    @validate_arguments
    def __init__(self, urls: list[str]) -> None:
        for url in urls:
            if not url.startswith("http://") and not url.startswith("https://"):
                url = f"https://deetlist.com/dragoncity/dragon/{url.title().replace(' ', '%20')}"

            self.__urls_params.append((url, None))

    @validate_arguments
    def run(self) -> list[dict]:
        return super().run(self.__urls_params)

__all__ = [ DragonPageFetcher, DragonPageAsyncFetcher ]