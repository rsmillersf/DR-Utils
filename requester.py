# requester.py

import zmq
from PIL import Image
import io
import time

context = zmq.Context()
socket = context.socket(zmq.REQ) # REQ socket type for making requests
socket.connect("tcp://localhost:5555") # Connect to the server

while True:
    # Request image
    socket.send_string("request_image")
    image_data = socket.recv()
    
    # Display the received image
    image_stream = io.BytesIO(image_data)
    image = Image.open(image_stream)
    image.show()
    
    time.sleep(5)  # Wait for 5 seconds before the next request
