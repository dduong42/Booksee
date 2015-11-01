from unittest.mock import Mock


def requests_factory(text='some text',
                     location='some location',
                     content=b'some content'):
    requests = Mock()

    get_response = Mock()
    get_response.text = text
    get_response.content = content

    head_response = Mock()
    head_response.headers = {'Location': location}

    requests.get = Mock(return_value=get_response)
    requests.head = Mock(return_value=head_response)

    return requests


def http_controller_factory(location='some location',
                            content=b'some content'):
    controller = Mock()
    controller.head_location = Mock(return_value=location)
    controller.get_content = Mock(return_value=content)
    return controller
