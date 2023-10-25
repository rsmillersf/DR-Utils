import picamera2
import time

camera = picamera2.Picamera2()
picam2.start_and_capture_files("test{:d}.jpg", show_preview=True, initial_delay=5, delay=5, num_files=10)
