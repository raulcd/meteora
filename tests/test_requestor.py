import unittest

from meteora import requestor


class TestRequestor(unittest.TestCase):

    def setUp(self):
        self.url = 'http://echo.jsontest.com/'

    def test_generate_one_request(self):
        my_requestor = requestor.Requestor(number_of_requests=10, url=self.url)
        my_requestor.start_requests()
        #my_requestor.wait_to_finish(timeout=3)
        self.assertIsNotNone(my_requestor.results)
