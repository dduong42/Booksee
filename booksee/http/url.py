import posixpath
from urllib.parse import urlparse


class URL:
    def __init__(self, url):
        self.url = url

    def head_location(self, http_controller):
        return http_controller.head_location(self.url)

    def get_content(self, http_controller, *, referer):
        return http_controller.get_content(self.url, referer=referer)

    def get_filename(self):
        path = urlparse(self.url).path
        return posixpath.basename(path)

    def __repr__(self):
        return '{}(url={})'.format(self.__class__.__name__, repr(self.url))
