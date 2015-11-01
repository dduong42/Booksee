from bs4 import BeautifulSoup

from .model import RawResult


def get_parser():
    return Parser(BeautifulSoup, RawResult)


class Parser:
    def __init__(self, soup_factory, raw_result_factory):
        self.soup_factory = soup_factory
        self.raw_result_factory = raw_result_factory

    def extract_results(self, result_page):
        soup = self.soup_factory(result_page, 'html.parser')
        return soup.select('div.resItemBox.exactMatch')

    def get_title(self, result):
        return result.find('h3').text

    def get_authors(self, result):
        authors = result.find_all('a', itemprop="author")
        return [author.text for author in authors]

    def extract_url(self, url_tag):
        return url_tag.attrs['href']

    def get_url(self, result):
        url_tag = result.find('a', class_='ddownload')
        return self.extract_url(url_tag) if url_tag else ''

    def create_raw_result(self, result):
        title = self.get_title(result)
        authors = self.get_authors(result)
        url = self.get_url(result)
        return self.raw_result_factory(title, authors, url)

    def get_results(self, result_page):
        results = self.extract_results(result_page)
        return [self.create_raw_result(result)
                for result in results]
