from .downloadedfile import get_downloaded_file
from .. import http


def get_downloader():
    return Downloader(
        http.controller.get_controller(),
        get_downloaded_file,
        http.URL,
    )


class Downloader:
    def __init__(self, http_controller, downloaded_file_factory, url_factory):
        self.http_controller = http_controller
        self.downloaded_file_factory = downloaded_file_factory
        self.url_factory = url_factory

    def download(self, url):
        location = self.http_controller.head_location(url)
        content = self.http_controller.get_content(url, referer=location)
        return self.downloaded_file_factory(
            content,
            self.url_factory(location).get_filename(),
        )
