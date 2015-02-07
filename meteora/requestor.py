import asyncio
import requests

@asyncio.coroutine
def run_requests(url, num_requests):
    loop = asyncio.get_event_loop()
    future = []
    for (i in range(num_requests)):
    	future[i] = loop.run_in_executor(None, requests.get, url)
    
    for (i in range(num_requests)):
    	response[i] = yield from future[i]
    	print(response[i].text)




class Requestor(object):
    """
    Main class to generate requests.
    """

    def __init__(self, url, number_of_requests=1, *args, **kwargs):
        """
        """
        self.url= url
        self.number_of_requests = number_of_requests

    def start_requests(self):
        loop = asyncio.get_event_loop()
		loop.run_until_complete(run_requests(self.url, self.number_of_requests))

