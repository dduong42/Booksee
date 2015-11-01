from unittest import TestCase
from unittest.mock import Mock

from booksee.download.downloader import Downloader
from booksee.http.url import URL

from tests.http.factories import http_controller_factory


class DownloaderTestCase(TestCase):
    def test_download(self):
        downloaded_file_factory = Mock()
        controller = http_controller_factory(
            location='http://google.fr/plouf.doc',
            content=b'my content',
        )
        downloader = Downloader(controller, downloaded_file_factory, URL)
        downloader.download('http://yoman.com/plouf')

        controller.get_content.assert_called_once_with(
            'http://yoman.com/plouf',
            referer='http://google.fr/plouf.doc',
        )

        downloaded_file_factory.assert_called_once_with(
            b'my content',
            'plouf.doc',
        )
