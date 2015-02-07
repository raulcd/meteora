import unittest

from meteora import requestor


class TestRequestor(unittest.TestCase):

    def setUp(self):
        self.url = 'http://echo.jsontest.com/'

    def test_generate_one_request(self):
        my_requestor = requestor.Requestor(number_of_requests=1, url=self.url)
        my_requestor.start_requests()
        self.assertIsNotNone(my_requestor.results)
        self.assertEquals(len(my_requestor.results), 1)

    def test_generate_two_requests(self):
        my_requestor = requestor.Requestor(number_of_requests=3, url=self.url)
        my_requestor.start_requests()
        self.assertIsNotNone(my_requestor.results)
        self.assertEquals(len(my_requestor.results), 3)

    def test_generate_one_thousand_requests(self):
        my_requestor = requestor.Requestor(number_of_requests=1000, url=self.url)
        my_requestor.start_requests()
        self.assertIsNotNone(my_requestor.results)
        self.assertEquals(len(my_requestor.results), 1000) 




