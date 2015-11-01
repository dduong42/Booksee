class Book:
    def __init__(self, title, authors, downloaded_file):
        self.title = title
        self.authors = authors
        self.downloaded_file = downloaded_file

    def write(self, f):
        self.downloaded_file.write(f)

    def save(self, path=None):
        self.downloaded_file.save(path)

    def __repr__(self):
        return '{}(title={}, authors={})'.format(
            self.__class__.__name__, repr(self.title), repr(self.authors))
