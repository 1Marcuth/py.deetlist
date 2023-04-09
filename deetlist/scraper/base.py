class BaseScraper:
    def __init__(self, fetcher, parser):
        self.__fetcher = fetcher
        self.__parser = parser

    def get(self):
        html_data = self.__fetcher().get()
        data = self.__parser(html_data).get()

        return data

__all__ = [ "BaseScraper" ]