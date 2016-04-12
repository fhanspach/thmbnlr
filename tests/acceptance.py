import unittest
from httmock import with_httmock
import main
from urllib import parse
from tests import mock


class ThmbnlrTestCase(unittest.TestCase):
    def setUp(self):
        main.app.config['TESTING'] = True
        self.app = main.app.test_client()

    def tearDown(self):
        pass

    @with_httmock(*mock.example_com)
    def test_missing_url_parameter(self):
        response = self.app.get('/')
        self.assertEquals(400, response.status_code)

    @with_httmock(*mock.example_com)
    def test_url_without_parameters(self):
        path = "{}/600x200.jpg".format(mock.DOMAIN)
        query_dict = {
            "url": ("http://%s" % path)
        }
        query = parse.urlencode(query_dict)

        response = self.app.get('/?{}'.format(query))

        self.assertEquals(302, response.status_code)
        # TODO check if the content contains the correct image
        # self.assertEquals(mock.Resource(path).get(), response.content)


if __name__ == '__main__':
    unittest.main()
