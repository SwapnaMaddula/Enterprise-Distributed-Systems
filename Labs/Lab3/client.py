import zmq
from threading import Thread
import sys
import time


# ZeroMQ Context
context = zmq.Context()
clientname = sys.argv[1]

sender = context.socket(zmq.PUSH)
sender.connect("tcp://127.0.0.1:5678")

print("User [%s] Connected to the chat server." %(clientname))


def subscriber():

    """Receives messages and prints it."""
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://127.0.0.1:5679")
    socket.setsockopt_string(zmq.SUBSCRIBE, '') 

    while True:
        time.sleep(1)
        data_rec = socket.recv().decode()
        if(data_rec):
            if ("[{}]:".format(clientname) not in data_rec):
                print ("\n{}".format(data_rec)+"\n["+clientname+"] > ", end="")
        
def start():
    thread = Thread(target=subscriber)
    thread.start()

start()
while True:
    msg = input("[{0}] > ".format(clientname))
    msg = "[%s]:  %s" % (clientname, msg)
    sender.send(msg.encode())