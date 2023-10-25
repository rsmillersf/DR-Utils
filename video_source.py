# Import necessary libraries
#import zmq
#import io
from picamera2 import PiCamera2
import time

# Set up ZMQ REP socket
# context = zmq.Context()
# socket = context.socket(zmq.REP)
# socket.bind("tcp://*:5555")

# Create a PiCamera2 object
camera = PiCamera2()
counter = 1

# Continuously capture and send images to the host
while counter < 21:
    # Wait for a request from the host
    #message = socket.recv()
    camera.capture(image_stream, format='jpeg')
    

    # Check if the message is a request for an image
    # if message == b"request image":
    #     # Capture an image from the camera
    #     image_stream = io.BytesIO()
    #     camera.capture(image_stream, format='jpeg')

    #     # Serialize the image and send it to the host
    #     socket.send(image_stream.getvalue())
    # else:
    #     # If the message is not a request for an image, send an error message
    #     socket.send(b"Invalid request")

