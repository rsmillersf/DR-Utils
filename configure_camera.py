"""
This script captures images from a remote camera and uses them to calibrate the camera.
The calibration parameters are saved to a file named 'calibration.npz'.

Instructions:
1. Replace the server address in line 8 with the address of your server.
2. Set the number of images to capture for calibration by changing the value of 'num_images' in line 14.
3. Set the size of the calibration pattern by changing the values of 'pattern_size' in line 17.
4. Run the script and wait for it to capture the required number of good images.
5. The calibration parameters will be saved to a file named 'calibration.npz' in the current directory.
"""

import zmq
import time
import cv2
import numpy as np

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")  # Replace with your server address

# Define the calibration pattern
pattern_size = (9, 6)  # Number of inner corners in the calibration pattern
obj_points = []  # 3D points in real world space
img_points = []  # 2D points in image plane

num_images = 20  # Number of images to capture for calibration
counter = 0  # Counter for number of good images detected

while counter < num_images:
    # Send a message to the server requesting an image
    socket.send(b"request image")

    # Receive the image from the server
    message = socket.recv()
    nparr = np.frombuffer(message, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the corners of the calibration pattern
    ret, corners = cv2.findChessboardCorners(gray, pattern_size, None)

    # If the corners are detected successfully, add them to the lists
    if ret:
        obj_points.append(np.zeros((pattern_size[0] * pattern_size[1], 3), np.float32))
        obj_points[-1][:, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2)
        img_points.append(corners)
        counter += 1

        # Draw the corners on the image and display it
        img = cv2.drawChessboardCorners(img, pattern_size, corners, ret)
        cv2.imshow('img', img)
        cv2.waitKey(5000) #Wait 5 senconds before requesting the next image

    # Break out of the loop if 20 good images are detected
    if counter == num_images:
        break

# Calibrate the camera using the collected object points and image points
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)

# Save the calibration parameters to a file
np.savez('calibration.npz', mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs)
