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

    def test_generate_request_method(self):
        my_requestor = requestor.Requestor(number_of_requests=utils.generate_request, url=self.url)
        my_requestor.start_requests()
        self.assertIsNotNone(my_requestor.results)
        self.assertEquals(len(my_requestor.results), 1)
