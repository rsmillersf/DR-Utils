# capturer.py

import zmq
import picamera2
import io

context = zmq.Context()
socket = context.socket(zmq.REP) # REP socket type for replying to requests
socket.bind("tcp://*:5555") # Bind to a port

with picamera2.PiCamera() as camera:
    while True:
        # Wait for request from client
        message = socket.recv_string()
        
        if message == "request_image":
            # Capture image
            image_stream = io.BytesIO()
            camera.capture(image_stream, format='jpeg')
            image_stream.seek(0)
            
            # Send the image
            socket.send(image_stream.read())
