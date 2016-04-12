# -*- coding: utf-8 -*-
from httmock import response, urlmatch


DOMAIN = r'example.com'
NETLOC = r'(.*\.)?%s$' % DOMAIN
HEADERS = {'content-type': 'image/jpeg'}
GET = 'get'


class Resource:
    def __init__(self, path):
        self.path = path

    def get(self):
        """ Perform a GET request on the resource.
        :rtype: str
        """
        with open(self.path, 'r') as f:
            content = f.read()
        return content


@urlmatch(netloc=NETLOC, method=GET)
def resource_get(url, request):
    file_path = url.netloc + url.path
    try:
        content = Resource(file_path).get()
    except EnvironmentError:
        # catch any environment errors (i.e. file does not exist) and return a
        # 404.
        return response(404, {}, HEADERS, None, 5, request)

    headers = {
        "Content-Length": len(content),
        'content-type': 'image/jpeg'
    }

    return response(200, content, headers, None, 5, request)


@urlmatch(netloc=NETLOC, method="head")
def resource_head(url, request):
    file_path = url.netloc + url.path
    try:
        content = Resource(file_path).get()
    except EnvironmentError:
        # catch any environment errors (i.e. file does not exist) and return a
        # 404.
        return response(400, {}, HEADERS, None, 5, request)

    headers = {
        "Content-Length": len(content),
        'content-type': 'image/jpeg'
    }

    return response(200, content, headers, None, 5, request)

example_com = [resource_get, resource_head]
