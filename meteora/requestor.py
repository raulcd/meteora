import asyncio
import aiohttp


class Requestor(object):
    """
    Main class to generate requests.
    """

    def __init__(self, url, number_of_requests=1, *args, **kwargs):
        """
        """
        self.url = url
        self.number_of_requests = number_of_requests
        self.results = {}

    def start_requests(self):
        loop = asyncio.get_event_loop()
        tasks = []
        for i in range(self.number_of_requests):
            tasks.append(asyncio.async(self.make_request(self.url, i)))
        loop.run_until_complete(asyncio.wait(tasks))

    @asyncio.coroutine
    def make_request(self, url, request_number):
        response = yield from aiohttp.request('GET', url)
        self.results[request_number] = yield from response.read()
