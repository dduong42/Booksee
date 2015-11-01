class RawResult:
    def __init__(self, title, authors, url):
        self.title = title
        self.authors = authors
        self.url = url

    @property
    def can_download(self):
        return bool(self.url)

    def __repr__(self):
        return '{}(title={}, authors={}, url={})'.format(
            self.__class__.__name__,
            repr(self.title),
            repr(self.authors),
            repr(self.url),
        )
