GET = 'GET'
POST = 'POST'
DELETE = 'DELETE'
PUT = 'PUT'
PATCH = 'PATCH'
HEAD = 'HEAD'

import math

def generate_request( threadNum, numberOfThreads ):
    x = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "10" ]
    numberToSend = math.ceil( len(x)/numberOfThreads )
    start = threadNum * numberToSend
    end = start + numberToSend
    for i in x[ start:end ]:
        yield "request%s" % str( i )