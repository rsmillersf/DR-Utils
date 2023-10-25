import picamera2 as PiCamera2
import time

# Setup
num_images = 20
interval_seconds = 5.5  # Account for the 0.5s freeze effect

with PiCamera2() as camera:
    camera.start_preview()
    time.sleep(2)  # Give the camera some time to warm up
    
    for i in range(num_images):
        image_name = f"image_{i+1}.jpg"
        
        # Capture the image and save it in the current directory
        camera.capture(image_name)
        print(f"Captured {image_name}")
        
        # Freeze effect: Show the captured image for 0.5 seconds
        camera.show(image_name)
        time.sleep(0.5)
        
        # Continue with live preview
        camera.start_preview()
        
        if i < num_images - 1:
            time.sleep(interval_seconds - 0.5)  # Minus the freeze effect duration
    
    camera.stop_preview()

print("Finished capturing images.")
