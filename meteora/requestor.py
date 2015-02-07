import asyncio
import requests
import functools

from meteora import utils
import time
import datetime


class Backoff():
    """
    Implements exponential backoff.
    """
    def __init__(self, maxretries=8):
        self.retry = 0
        self.maxretries = maxretries
        self.first = True

    def loop(self):
        if self.first:
            self.first = False
            return True
        else:
            return self.retry < self.maxretries

    def fail(self):
        self.retry += 1
        delay = 2 ** self.retry
        time.sleep(delay)


class Requestor(object):
    """
    Main class to generate requests.
    """
    def __init__(self, url, method=utils.GET, number_of_requests=None,
                 *args, **kwargs):
        """
        """
        self.method = method
        self.url = url
        self.number_of_requests = number_of_requests
        self.results = []
        self.args = args
        self.kwargs = kwargs

    def start_requests(self):
        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(
            self._run_requests(
                self.url, self.number_of_requests,
            )
        )
        self.results = Result(results)

    def _do_request(self, url, num_requests):
        responses = []
        backoff = Backoff()
        for i in range(num_requests):
            while backoff.loop():
                start_time = datetime.datetime.now().microsecond
                if self.method == utils.GET:
                    response = requests.get(url, *self.args, **self.kwargs)
                elif self.method == utils.POST:
                    response = requests.post(url, *self.args, **self.kwargs)
                    # TODO add other methods
                end_time = datetime.datetime.now().microsecond
                response.execution_time = end_time - start_time
                if response.status_code in [402, 403, 408, 503, 504]:
                    print ("Backing off due to status code: %d" % response[i])
                    backoff.fail()
                else:
                    responses.append(response)
                    break

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

    @property
    def responses(self):
        return functools.reduce(lambda x, y: x.extend(y), self.responses_list)
