# Import necessary libraries
import zmq
from picamera2 import PiCamera2

# Set up ZMQ REP socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

# Create a PiCamera2 object
camera = PiCamera2()

# Continuously capture and send images to the host
while True:
    # Wait for a request from the host
    message = socket.recv()

    # Capture an image from the camera
    camera.capture('/tmp/image.jpg')

    # Send the image to the host
    with open('/tmp/image.jpg', 'rb') as f:
        image_data = f.read()
        socket.send(image_data)

