import unittest

from meteora import requestor
from meteora import utils


class TestRequestor(unittest.TestCase):

    def setUp(self):
        self.url = 'http://echo.jsontest.com/'

    def test_generate_one_get_request(self):
        my_requestor = requestor.Requestor(number_of_requests=1, url=self.url)
        my_requestor.start_requests()
        self.assertIsNotNone(my_requestor.results)
        self.assertEquals(len(my_requestor.results), 1)

    def test_generate_three_get_requests(self):
        my_requestor = requestor.Requestor(number_of_requests=3, url=self.url)
        my_requestor.start_requests()
        results = my_requestor.results
        self.assertIsNotNone(results)
        self.assertEquals(len(results), 3)
        self.assertEquals(results.responses[0].request.method, 'GET')

    def test_generate_one_post_request(self):
        my_requestor = requestor.Requestor(
            number_of_requests=1, url=self.url, method=utils.POST
        )
        my_requestor.start_requests()
        results = my_requestor.results
        self.assertIsNotNone(results)
        self.assertEquals(len(results), 1)
        self.assertEquals(results.responses[0].request.method, 'POST')

    def test_post_one_request_with_data(self):
        data = {'key': 'value'}
        my_requestor = requestor.Requestor(
            number_of_requests=1, url=self.url, method=utils.POST,
            data=data
        )
        my_requestor.start_requests()
        results = my_requestor.results
        self.assertEquals(results.responses[0].request.body, 'key=value')
        self.assertEquals(results.responses[0].request.method, 'POST')
