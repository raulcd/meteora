import asyncio
import requests


class Requestor(object):
    """
    Main class to generate requests.
    """
    def __init__(self, url, number_of_requests=1, *args, **kwargs):
        """
        """
        self.url = url
        self.number_of_requests = number_of_requests
        self.results = []

    def start_requests(self):
        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(
            self._run_requests(
                self.url, self.number_of_requests
            )
        )
        self.results = Result(results)

    def _do_request(self, url, num_requests):
        responses = []
        for i in range(num_requests):
            responses.append(requests.get(url))
        return responses

    @asyncio.coroutine
    def _run_requests(self, url, num_requests, num_concurrent_users=1):
        loop = asyncio.get_event_loop()
        futures = []
        responses = []
        for i in range(num_concurrent_users):
            futures.append(
                loop.run_in_executor(
                    None, self._do_request, url, num_requests
                )
            )
        for i in range(num_concurrent_users):
            response = yield from futures[i]
            responses.append(response)
        return responses


class Result(object):

    def __init__(self, responses_list):
        """
        """
        self.responses_list = responses_list

    def __len__(self):
        return sum((len(response_per_user)
                    for response_per_user in self.responses_list))
