import zmq

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
responder = context.socket(zmq.PULL)
responder.bind("tcp://127.0.0.1:5678")
broadcaster = context.socket(zmq.PUB)
broadcaster.bind("tcp://127.0.0.1:5679")

# Run server
while True:
    message = responder.recv()
    broadcaster.send(message)
    print("[Server] Echo: " + message.decode())