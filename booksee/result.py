from .book import Book
from .download import get_downloader


def get_result(raw_result):
    return Result(
        raw_result.title,
        raw_result.authors,
        raw_result.url,
        get_downloader(),
        Book,
    )


class Result:
    def __init__(self, title, authors, url, downloader, book_factory):
        self.title = title
        self.authors = authors
        self.url = url
        self.downloader = downloader
        self.book_factory = book_factory

    def download(self):
        downloaded_file = self.downloader.download(self.url)
        return self.book_factory(self.title, self.authors, downloaded_file)

    def __repr__(self):
        return '{}(title={}, authors={})'.format(
            self.__class__.__name__, repr(self.title), repr(self.authors))
