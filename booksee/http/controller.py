import requests


def get_controller():
    return HttpController(requests)


class HttpController:
    def __init__(self, requests_):
        self.requests = requests_

    def get_text(self, url, *, params):
        return self.requests.get(url, params=params).text

    def get_content(self, url, *, referer):
        headers = {'Referer': referer}
        return self.requests.get(url, headers=headers).content

    def head_location(self, url):
        response = self.requests.head(url)
        return response.headers['Location']
