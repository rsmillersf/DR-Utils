import picamera2
import time

# Setup
num_images = 20
interval_seconds = 5.5  # Account for the 0.5s freeze effect

# Capture images
camera = picamera2.Picamera2()

for i in range(num_images):
    image_name = f"image_{i+1}.jpg"
    capture_config = picam2.create_still_configuration()
    picam2.start(show_preview=True)
    
    time.sleep(5)

    picam2.switch_mode_and_capture_file(capture_config, "image.jpg")

    print(f"Captured {image_name}")
    
print("finished")
