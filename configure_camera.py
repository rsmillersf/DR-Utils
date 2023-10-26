# Importing the necessary libraries
import cv2 as cv
import glob
import numpy as np

# Defining the termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Preparing object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

# Reading all the images in the current directory
images = glob.glob('*.jpg')

# Looping through all the images
for fname in images:
    # Reading the image
    img = cv.imread(fname)
    # Converting the image to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Finding the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (7,6), None)
    # If the corners are found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)
        # Drawing and displaying the corners
        cv.drawChessboardCorners(img, (7,6), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(500)

# Calibrating the camera
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# Saving the parameters to a file
np.savez('camera_params.npz', mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs)

# Destroying all the windows
cv.destroyAllWindows()
