from unittest import TestCase

from booksee.http.url import URL

from tests.http.factories import http_controller_factory


class URLTestCase(TestCase):
    def test_head_location(self):
        controller = http_controller_factory(location='Paris')

        url = URL('http://goog.le')
        location = url.head_location(controller)
        controller.head_location.assert_called_once_with(
            'http://goog.le')
        self.assertEqual('Paris', location)

    def test_get_content(self):
        controller = http_controller_factory(content=b'my content')

        url = URL('http://google.fr')
        content = url.get_content(controller, referer='http://epf.fr')
        controller.get_content.assert_called_once_with(
            'http://google.fr', referer='http://epf.fr')
        self.assertEqual(b'my content', content)

    def test_get_filename(self):
        url = URL('http://google.fr/blabla/toto.pdf')
        filename = url.get_filename()
        self.assertEqual('toto.pdf', filename)
