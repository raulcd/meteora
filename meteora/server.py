"""
server.py - AsyncIO Server using StreamReader and StreamWriter

example in another terminal:

    $ nc localhost 2991
    HELLO
    WORLD
    READY
    one
    ECHO 1: one
    two
    ECHO 2: two
    three
    ECHO 3: three
    four
    ECHO 4: four
    five
    ECHO 5: five
    six
    ECHO 6: six
    seven
    ECHO 7: seven
    eight
    ECHO 8: eight
    nine
    ECHO 9: nine
    ten
    ECHO 10: ten
    bye
    BYE

    $
"""
 
import asyncio
import logging
import time
import random

log = logging.getLogger(__name__)
 
clients = {}  # task -> (reader, writer)
 
num_requests = 0
max_requests = 5

def accept_client(client_reader, client_writer):
    task = asyncio.Task(handle_client(client_reader, client_writer))
    clients[task] = (client_reader, client_writer)
 
    def client_done(task):
        del clients[task]
        client_writer.close()
        log.info("End Connection")
 
    log.info("New Connection")
    task.add_done_callback(client_done)
 
def generate_requests(max_requests):
    for i in range(max_requests):
        if i == 1:
            yield "GET /"
        else:
            yield "POST /"

@asyncio.coroutine
def handle_client(client_reader, client_writer):
    # send a hello to let the client know they are connected
    response_body = "{ 'a' : 1, 'b' : 2 }"
    content_length = len(response_body)
    response_header_ok = "\n".join(["HTTP/1.1 200 OK",
                            "Access-Control-Allow-Origin: *",
                            "Content-Type: application/json; charset=ISO-8859-",
                            "Content-Encoding: text/plain",
                            "Vary: Accept-Encoding",
                            "Date: Sat, 07 Feb 2015 15:02:29 GMT",
                            "Server: Google Frontend",
                            "Cache-Control: private",
                            "Content-Length: %d" % content_length,
                            "Alternate-Protocol: 80:quic,p=0.02,80:quic,p=0.02"])
    response_header_err = "\n".join(["HTTP/1.1 500 OK",])
    resp = random.randint(1,2)
    if resp == 1:
        client_writer.write(response_header_err.encode())
    else:
        client_writer.write(response_header_ok.encode())
        client_writer.write("\n".encode())
        client_writer.write(response_body.encode())
 
def main():
    loop = asyncio.get_event_loop()
    f = asyncio.start_server(accept_client, host=None, port=2991)
    loop.run_until_complete(f)
    loop.run_forever()
 
if __name__ == '__main__':
    log = logging.getLogger("")
    formatter = logging.Formatter("%(asctime)s %(levelname)s " +
                                  "[%(module)s:%(lineno)d] %(message)s")
    # setup console logging
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
 
    ch.setFormatter(formatter)
    log.addHandler(ch)
    main()