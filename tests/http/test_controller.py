from unittest import TestCase

from booksee.http.controller import HttpController

from tests.http.factories import requests_factory


class HttpControllerTestCase(TestCase):
    def test_get_text(self):
        requests = requests_factory(text='my text')
        controller = HttpController(requests)
        text = controller.get_text('http://google.fr/', params={'q': 'query'})
        requests.get.assert_called_once_with(
            'http://google.fr/', params={'q': 'query'})
        self.assertEqual('my text', text)

    def test_get_content(self):
        requests = requests_factory(content=b'my content')
        controller = HttpController(requests)
        content = controller.get_content('http://google.fr/',
                                         referer='http://eps.fr')
        requests.get.assert_called_once_with(
            'http://google.fr/', headers={'Referer': 'http://eps.fr'})
        self.assertEqual(b'my content', content)

    def test_head_location(self):
        requests = requests_factory(location='location')
        controller = HttpController(requests)
        location = controller.head_location('http://google.fr/')
        requests.head.assert_called_once_with('http://google.fr/')
        self.assertEqual('location', location)
