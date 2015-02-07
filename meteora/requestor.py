import asyncio
import requests

def do_request(url, num_connections):
	responses = []
	for i in range(num_connections):
		responses.append(requests.get(url))
	return responses

@asyncio.coroutine
def run_requests(url, num_requests):
	loop = asyncio.get_event_loop()
	futures = []
	responses = []
	for i in range(num_requests):
		futures.append(loop.run_in_executor(None, do_request, url, num_requests))
	for i in range(num_requests):
		response = yield from futures[i]
		responses.append(response)
	return responses



import aiohttp

@asyncio.coroutine
def run_requests_async(url, num_requests):
	response = yield from aiohttp.request('GET', url)
	assert response.status == 200
	return (yield from response.read())

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
		results = loop.run_until_complete(run_requests(self.url, self.number_of_requests))
		#content = asyncio.get_event_loop().run_until_complete(
		#run_requests_async(self.url, self.num_requests))
		#print(content)
		print(results)
