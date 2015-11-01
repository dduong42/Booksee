from . import http
from .parser import get_parser
from .result import get_result


def search(query):
    searcher = Searcher(
        http.get_controller(),
        get_parser(),
        get_result,
    )
    return searcher.search(query)


class Searcher:
    search_url = 'http://en.booksee.org/s/'

    def __init__(self, http_controller, parser, result_factory):
        self.http_controller = http_controller
        self.parser = parser
        self.result_factory = result_factory

    def get_result_page(self, query):
        return self.http_controller.get_text(self.search_url, params={'q': query})

    def search(self, query):
        result_page = self.get_result_page(query)
        results = self.parser.get_results(result_page)
        return [self.result_factory(result) for result in results
                if result.can_download]
