import requests
from bs4 import BeautifulSoup
import oper
clarcoder = oper.clarcoder


@clarcoder
class get:
    def __init__(self, url) -> None:
        self.url = url

    def get(self, id) -> object:
        @clarcoder
        class lib:
            def __init__(self, url):
                self.text = BeautifulSoup(requests.get(url).text, 'html.parser').find(id=id).get_text()

            def __enter__(self) -> object:
                return self

            def __exit__(self, exc_type, exc_value, traceback) -> None:
                pass
        return lib(self.url)

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        pass